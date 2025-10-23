"""
Inventory search functionality for Natro Macro
Equivalent to lib/nm_InventorySearch.ahk
"""

import logging
from pathlib import Path
from .image_search import ImageSearch
from .roblox import RobloxController

logger = logging.getLogger(__name__)


class InventorySearch:
    def __init__(self, macro_instance):
        self.macro = macro_instance
        self.image_search = macro_instance.image_search
        self.roblox = macro_instance.roblox

        # Cache for window-specific data
        self.hwnd_cache = {}
        self.offset_cache = {}

    def nm_inventory_search(self, item: str, direction: str = "down", prescroll: int = 0,
                          prescrolldir: str = "", scrolltoend: int = 1, max_scrolls: int = 70):
        """
        Search for item in inventory
        Equivalent to nm_InventorySearch()

        Args:
            item: Item name to search for
            direction: Scroll direction ("down" or "up")
            prescroll: Number of scrolls before direction switch
            prescrolldir: Prescroll direction (blank for same as direction)
            scrolltoend: Whether to scroll to end after prescrolls
            max_scrolls: Maximum number of scrolls

        Returns:
            True if item found, False otherwise
        """
        try:
            # Open item menu
            self._open_item_menu()

            # Get current Roblox window
            hwnd = self.roblox.get_roblox_hwnd()
            if not hwnd:
                logger.warning("No Roblox window found")
                return False

            # Check if we need to recalculate inventory bounds
            if hwnd['pid'] not in self.hwnd_cache:
                self._detect_inventory_bounds(hwnd)

            # Search inventory
            return self._search_inventory(item, direction, prescroll, prescrolldir,
                                        scrolltoend, max_scrolls)

        except Exception as e:
            logger.error(f"Inventory search error: {e}")
            return False

    def _open_item_menu(self):
        """Open the item menu"""
        # This would use image search or keyboard shortcuts to open inventory
        # Simplified implementation
        logger.debug("Opening item menu")
        # TODO: Implement actual menu opening logic

    def _detect_inventory_bounds(self, hwnd):
        """Detect inventory boundaries for the current window"""
        try:
            # Get window bounds
            if not self.roblox.get_roblox_client_pos(hwnd):
                return False

            # Calculate inventory area
            # This is a simplified calculation - actual implementation would
            # use image search to find inventory boundaries
            inventory_top = self.macro.window_y + 150
            inventory_left = self.macro.window_x
            inventory_width = 306
            inventory_height = self.macro.window_height - 150

            self.hwnd_cache[hwnd['pid']] = {
                'inventory_bounds': (inventory_left, inventory_top, inventory_width, inventory_height),
                'item_height': 80,
                'scroll_offset': 60
            }

            return True

        except Exception as e:
            logger.error(f"Error detecting inventory bounds: {e}")
            return False

    def _search_inventory(self, item: str, direction: str, prescroll: int,
                        prescrolldir: str, scrolltoend: int, max_scrolls: int):
        """Perform the actual inventory search"""
        try:
            hwnd = self.roblox.get_roblox_hwnd()
            if not hwnd or hwnd['pid'] not in self.hwnd_cache:
                return False

            cache = self.hwnd_cache[hwnd['pid']]
            bounds = cache['inventory_bounds']

            # Scroll to beginning/end if needed
            if scrolltoend:
                self._scroll_inventory(direction == "up" and "down" or "up", 20)

            # Perform prescrolls
            if prescroll > 0:
                pre_dir = prescrolldir or direction
                self._scroll_inventory(pre_dir, prescroll)

            # Search for item
            for scroll_count in range(max_scrolls):
                # Take screenshot of inventory area
                result = self.image_search.imagesearch_in_region(
                    f"items/{item}.png", bounds[0], bounds[1], bounds[2], bounds[3]
                )

                if result:
                    logger.info(f"Item {item} found at scroll {scroll_count}")
                    return True

                # Scroll and continue searching
                if not self._scroll_inventory(direction, 1):
                    break

            logger.info(f"Item {item} not found after {max_scrolls} scrolls")
            return False

        except Exception as e:
            logger.error(f"Error during inventory search: {e}")
            return False

    def _scroll_inventory(self, direction: str, scrolls: int):
        """Scroll the inventory"""
        try:
            # Calculate scroll wheel movement
            scroll_amount = scrolls * (direction == "down" and -1 or 1)

            # Move mouse to inventory area and scroll
            cache = self.hwnd_cache.get(self.roblox.get_roblox_hwnd()['pid'])
            if cache:
                center_x = cache['inventory_bounds'][0] + cache['inventory_bounds'][2] // 2
                center_y = cache['inventory_bounds'][1] + cache['inventory_bounds'][3] // 2

                import pyautogui
                pyautogui.moveTo(center_x, center_y)
                pyautogui.scroll(scroll_amount)

            return True

        except Exception as e:
            logger.error(f"Error scrolling inventory: {e}")
            return False
