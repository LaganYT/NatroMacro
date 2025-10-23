"""
Menu management for Natro Macro
Equivalent to lib/nm_OpenMenu.ahk
"""

import logging
import time
from typing import Optional

logger = logging.getLogger(__name__)


class MenuManager:
    """Handles opening and closing various game menus"""

    def __init__(self, macro_instance):
        self.macro = macro_instance
        self.image_search = macro_instance.image_search
        self.roblox = macro_instance.roblox

        # Menu tab positions (x-coordinates from left edge of window)
        self.menu_positions = {
            "itemmenu": 30,
            "questlog": 85,
            "beemenu": 140,
            "badgelist": 195,
            "settingsmenu": 250,
            "shopmenu": 305
        }

        # Currently open menu
        self.open_menu: Optional[str] = None

    def nm_open_menu(self, tab: str = "", refresh: int = 0) -> bool:
        """
        Open or close game menus
        Equivalent to nm_OpenMenu()

        Args:
            tab: Menu tab to open ("itemmenu", "questlog", etc.) or "" to close
            refresh: If 1, force close current menu

        Returns:
            True if successful, False otherwise
        """
        try:
            # Get Roblox window
            hwnd = self.roblox.get_roblox_hwnd()
            if not hwnd:
                logger.warning("No Roblox window found")
                return False

            # Activate Roblox window
            if not self.roblox.activate_roblox_window():
                logger.warning("Could not activate Roblox window")
                return False

            # Get Y offset for UI elements
            y_offset = self.roblox.get_y_offset(hwnd, [0])

            if tab == "" or refresh == 1:
                # Close menu
                return self._close_menu(hwnd, y_offset, refresh == 1)
            else:
                # Open specific menu
                return self._open_specific_menu(tab, hwnd, y_offset)

        except Exception as e:
            logger.error(f"Error in nm_open_menu: {e}")
            return False

    def _close_menu(self, hwnd, y_offset: int, refresh: bool) -> bool:
        """Close the currently open menu or all menus"""
        try:
            if self.open_menu:
                # Close the specific open menu
                return self._close_specific_menu(self.open_menu, hwnd, y_offset)
            else:
                # Close any open menu
                return self._close_any_menu(hwnd, y_offset)

        except Exception as e:
            logger.error(f"Error closing menu: {e}")
            return False

    def _close_specific_menu(self, menu_name: str, hwnd, y_offset: int) -> bool:
        """Close a specific menu"""
        try:
            for attempt in range(10):
                # Update window position
                if not self.roblox.get_roblox_client_pos(hwnd):
                    return False

                # Take screenshot of menu area
                menu_region = (
                    self.macro.window_x,
                    self.macro.window_y + y_offset + 72,
                    350,
                    80
                )

                # Check if menu is still open
                menu_image = f"menus/{menu_name}.png"
                if not self.image_search.imagesearch_in_region(menu_image, *menu_region):
                    # Menu is closed
                    self.open_menu = ""
                    return True

                # Click to close menu
                close_x = self.macro.window_x + self.menu_positions[menu_name]
                close_y = self.macro.window_y + y_offset + 120

                self.macro.click_at(close_x, close_y)

                # Also click in empty area to ensure closure
                empty_x = self.macro.window_x + 350
                empty_y = self.macro.window_y + y_offset + 100
                self.macro.click_at(empty_x, empty_y)

                time.sleep(0.5)

            logger.warning(f"Could not close menu {menu_name} after 10 attempts")
            return False

        except Exception as e:
            logger.error(f"Error closing specific menu: {e}")
            return False

    def _close_any_menu(self, hwnd, y_offset: int) -> bool:
        """Close any open menu"""
        try:
            for menu_name, pos in self.menu_positions.items():
                for attempt in range(10):
                    # Update window position
                    if not self.roblox.get_roblox_client_pos(hwnd):
                        continue

                    # Take screenshot of menu area
                    menu_region = (
                        self.macro.window_x,
                        self.macro.window_y + y_offset + 72,
                        350,
                        80
                    )

                    # Check if this menu is open
                    menu_image = f"menus/{menu_name}.png"
                    if not self.image_search.imagesearch_in_region(menu_image, *menu_region):
                        # This menu is not open, continue to next
                        break

                    # Click to close this menu
                    close_x = self.macro.window_x + pos
                    close_y = self.macro.window_y + y_offset + 120

                    self.macro.click_at(close_x, close_y)

                    # Also click in empty area
                    empty_x = self.macro.window_x + 350
                    empty_y = self.macro.window_y + y_offset + 100
                    self.macro.click_at(empty_x, empty_y)

                    time.sleep(0.5)

            self.open_menu = ""
            return True

        except Exception as e:
            logger.error(f"Error closing any menu: {e}")
            return False

    def _open_specific_menu(self, tab: str, hwnd, y_offset: int) -> bool:
        """Open a specific menu tab"""
        try:
            if tab not in self.menu_positions:
                logger.error(f"Unknown menu tab: {tab}")
                return False

            # Close current menu if different
            if self.open_menu and self.open_menu != tab:
                if not self._close_specific_menu(self.open_menu, hwnd, y_offset):
                    logger.warning(f"Could not close current menu {self.open_menu}")

            # Open the desired menu
            for attempt in range(10):
                # Update window position
                if not self.roblox.get_roblox_client_pos(hwnd):
                    return False

                # Take screenshot of menu area
                menu_region = (
                    self.macro.window_x,
                    self.macro.window_y + y_offset + 72,
                    350,
                    80
                )

                # Check if menu is already open
                menu_image = f"menus/{tab}.png"
                if self.image_search.imagesearch_in_region(menu_image, *menu_region):
                    # Menu is open
                    self.open_menu = tab
                    return True

                # Click to open menu
                menu_x = self.macro.window_x + self.menu_positions[tab]
                menu_y = self.macro.window_y + y_offset + 120

                self.macro.click_at(menu_x, menu_y)

                # Also click in empty area (sometimes needed)
                empty_x = self.macro.window_x + 350
                empty_y = self.macro.window_y + y_offset + 100
                self.macro.click_at(empty_x, empty_y)

                time.sleep(0.5)

            logger.warning(f"Could not open menu {tab} after 10 attempts")
            return False

        except Exception as e:
            logger.error(f"Error opening specific menu: {e}")
            return False

    def is_menu_open(self, menu_name: str) -> bool:
        """
        Check if a specific menu is currently open

        Args:
            menu_name: Name of the menu to check

        Returns:
            True if menu is open, False otherwise
        """
        try:
            hwnd = self.roblox.get_roblox_hwnd()
            if not hwnd:
                return False

            y_offset = self.roblox.get_y_offset(hwnd, [0])

            if not self.roblox.get_roblox_client_pos(hwnd):
                return False

            menu_region = (
                self.macro.window_x,
                self.macro.window_y + y_offset + 72,
                350,
                80
            )

            menu_image = f"menus/{menu_name}.png"
            return self.image_search.imagesearch_in_region(menu_image, *menu_region) is not None

        except Exception as e:
            logger.error(f"Error checking if menu is open: {e}")
            return False
