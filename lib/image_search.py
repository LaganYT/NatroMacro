"""
Image search functions for macOS
Equivalent to lib/Gdip_ImageSearch.ahk
"""

import cv2
import numpy as np
import pyautogui
from PIL import Image
import logging
from pathlib import Path
import time

logger = logging.getLogger(__name__)

class ImageSearch:
    def __init__(self, macro_instance):
        self.macro = macro_instance

    def image_search(self, needle_path, output_list=None, outer_x1=0, outer_y1=0,
                    outer_x2=0, outer_y2=0, variation=0, trans_color=None,
                    search_direction=1, center_results=False):
        """
        Search for pBitmapNeedle within the screen
        Equivalent to Gdip_ImageSearch()

        Args:
            needle_path: Path to needle image file
            output_list: List to store found coordinates (x, y)
            outer_x1, outer_y1, outer_x2, outer_y2: Search region bounds
            variation: Color variation tolerance (0-255)
            trans_color: Transparent color (RGB)
            search_direction: Search direction (1-8)
            center_results: Whether to return center coordinates

        Returns:
            Number of matches found (negative = error)
        """
        try:
            needle_path = Path(needle_path)
            if not needle_path.exists():
                logger.error(f"Needle image not found: {needle_path}")
                return -1

            # Load needle image
            needle = cv2.imread(str(needle_path))
            if needle is None:
                logger.error(f"Could not load needle image: {needle_path}")
                return -2

            needle_height, needle_width = needle.shape[:2]

            # Handle transparent color
            if trans_color is not None:
                # Convert RGB to BGR for OpenCV
                trans_bgr = (trans_color & 0xFF, (trans_color >> 8) & 0xFF, (trans_color >> 16) & 0xFF)
                # Create mask for transparent pixels
                mask = cv2.inRange(needle, trans_bgr, trans_bgr)
                needle = cv2.bitwise_and(needle, needle, mask=cv2.bitwise_not(mask))

            # Take screenshot of search area
            if outer_x2 > outer_x1 and outer_y2 > outer_y1:
                # Specific region
                region = (outer_x1, outer_y1, outer_x2 - outer_x1, outer_y2 - outer_y1)
                haystack_img = pyautogui.screenshot(region=region)
            else:
                # Full screen
                haystack_img = pyautogui.screenshot()

            # Convert PIL to OpenCV format
            haystack = cv2.cvtColor(np.array(haystack_img), cv2.COLOR_RGB2BGR)

            # Perform template matching
            result = cv2.matchTemplate(haystack, needle, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            # Apply variation threshold (convert to similarity threshold)
            threshold = (100 - variation) / 100.0

            # Find all matches above threshold
            locations = np.where(result >= threshold)
            matches = list(zip(*locations[::-1]))  # Reverse to get (x, y) tuples

            if not matches:
                return 0

            # Filter matches based on search direction and avoid overlapping
            filtered_matches = self._filter_matches(matches, needle_width, needle_height,
                                                  search_direction, haystack.shape)

            # Store results
            if output_list is not None:
                output_list.clear()
                for x, y in filtered_matches:
                    # Adjust coordinates if searching in a region
                    if outer_x2 > outer_x1 and outer_y2 > outer_y1:
                        x += outer_x1
                        y += outer_y1

                    # Return center coordinates if requested
                    if center_results:
                        x += needle_width // 2
                        y += needle_height // 2

                    output_list.append((x, y))

            return len(filtered_matches)

        except Exception as e:
            logger.error(f"Image search error: {e}")
            return -3

    def _filter_matches(self, matches, needle_width, needle_height, search_direction, haystack_shape):
        """
        Filter matches to avoid overlapping and respect search direction
        """
        if not matches:
            return []

        filtered = []
        haystack_height, haystack_width = haystack_shape[:2]

        # Sort matches based on search direction
        if search_direction == 1:  # Top-left to bottom-right
            matches.sort(key=lambda m: (m[1], m[0]))  # Sort by y, then x
        elif search_direction == 2:  # Bottom-left to top-right
            matches.sort(key=lambda m: (-m[1], m[0]))  # Sort by -y, then x
        elif search_direction == 3:  # Bottom-right to top-left
            matches.sort(key=lambda m: (-m[1], -m[0]))  # Sort by -y, then -x
        elif search_direction == 4:  # Top-right to bottom-left
            matches.sort(key=lambda m: (m[1], -m[0]))  # Sort by y, then -x
        # Add more directions as needed...

        for match in matches:
            x, y = match

            # Check if this match overlaps with any previously found match
            overlaps = False
            for existing_x, existing_y in filtered:
                if (abs(x - existing_x) < needle_width and
                    abs(y - existing_y) < needle_height):
                    overlaps = True
                    break

            if not overlaps:
                # Ensure match is within bounds
                if (0 <= x < haystack_width - needle_width and
                    0 <= y < haystack_height - needle_height):
                    filtered.append((x, y))

        return filtered

    def imagesearch_in_region(self, needle_path, x1, y1, x2, y2, variation=0):
        """
        Simple image search in a specific region
        Returns: (x, y) of first match or None
        """
        output_list = []
        result = self.image_search(needle_path, output_list, x1, y1, x2, y2, variation)

        if result > 0 and output_list:
            return output_list[0]
        return None

    def imagesearch_on_screen(self, needle_path, variation=0):
        """
        Simple image search on entire screen
        Returns: (x, y) of first match or None
        """
        output_list = []
        result = self.image_search(needle_path, output_list, variation=variation)

        if result > 0 and output_list:
            return output_list[0]
        return None

    def wait_for_image(self, needle_path, timeout=30, region=None, variation=0):
        """
        Wait for an image to appear on screen
        Returns: (x, y) of match or None if timeout
        """
        start_time = time.time()

        while time.time() - start_time < timeout:
            if region:
                x1, y1, x2, y2 = region
                result = self.imagesearch_in_region(needle_path, x1, y1, x2, y2, variation)
            else:
                result = self.imagesearch_on_screen(needle_path, variation)

            if result:
                return result

            time.sleep(0.5)  # Check every 500ms

        return None

    def multi_image_search(self, needle_paths, region=None, variation=0):
        """
        Search for the first matching image from a list
        Returns: (index, x, y) or None
        """
        for i, needle_path in enumerate(needle_paths):
            if region:
                x1, y1, x2, y2 = region
                result = self.imagesearch_in_region(needle_path, x1, y1, x2, y2, variation)
            else:
                result = self.imagesearch_on_screen(needle_path, variation)

            if result:
                return (i, result[0], result[1])

        return None
