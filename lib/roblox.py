"""
Roblox automation functions for macOS
Equivalent to lib/Roblox.ahk
"""

import logging
import Quartz
from Quartz import CoreGraphics
from AppKit import NSWorkspace
import time

logger = logging.getLogger(__name__)

class RobloxController:
    def __init__(self, macro_instance):
        self.macro = macro_instance
        self.roblox_app = None
        self.window_bounds = None
        self.last_bounds_update = 0
        self.bounds_cache_duration = 2.0  # Cache bounds for 2 seconds

    def get_roblox_hwnd(self):
        """
        Find Roblox window handle equivalent for macOS
        Returns: dict with window info or None
        """
        try:
            workspace = NSWorkspace.sharedWorkspace()
            running_apps = workspace.runningApplications()

            for app in running_apps:
                app_name = app.localizedName()
                if app_name and "Roblox" in app_name:
                    self.roblox_app = app
                    return {
                        'pid': app.processIdentifier(),
                        'name': app_name,
                        'bundle_id': app.bundleIdentifier(),
                        'app': app
                    }

            # Try alternative method for Roblox Player
            # Check for processes containing "RobloxPlayer"
            import psutil
            for proc in psutil.process_iter(['pid', 'name']):
                if 'RobloxPlayer' in proc.info['name'] or 'Roblox' in proc.info['name']:
                    return {
                        'pid': proc.info['pid'],
                        'name': proc.info['name'],
                        'bundle_id': None,
                        'app': None
                    }

        except Exception as e:
            logger.error(f"Error finding Roblox window: {e}")

        return None

    def get_roblox_client_pos(self, hwnd=None, force_update=False):
        """
        Update global window coordinates for Roblox client
        Equivalent to GetRobloxClientPos()
        Returns: True if successful, False otherwise
        """
        current_time = time.time()

        # Use cached bounds if recent enough and not forcing update
        if (not force_update and
            self.window_bounds and
            current_time - self.last_bounds_update < self.bounds_cache_duration):
            return True

        if not hwnd:
            hwnd = self.get_roblox_hwnd()

        if not hwnd:
            logger.warning("Roblox window not found")
            self.macro.window_x = self.macro.window_y = self.macro.window_width = self.macro.window_height = 0
            return False

        try:
            # Get window bounds using Quartz
            window_list = Quartz.CGWindowListCopyWindowInfo(
                Quartz.kCGWindowListOptionOnScreenOnly | Quartz.kCGWindowListExcludeDesktopElements,
                Quartz.kCGNullWindowID
            )

            for window in window_list:
                owner_pid = window.get('kCGWindowOwnerPID')
                window_name = window.get('kCGWindowName', '')
                owner_name = window.get('kCGWindowOwnerName', '')

                if owner_pid == hwnd['pid'] and ('Roblox' in owner_name or 'Roblox' in window_name):
                    bounds = window.get('kCGWindowBounds')
                    if bounds:
                        self.window_bounds = bounds
                        self.last_bounds_update = current_time
                        self.macro.window_x = int(bounds['X'])
                        self.macro.window_y = int(bounds['Y'])
                        self.macro.window_width = int(bounds['Width'])
                        self.macro.window_height = int(bounds['Height'])
                        return True

            # Fallback: assume full screen if no window found
            # Only warn if we haven't warned recently or if this is the first time
            if not hasattr(self, '_last_fallback_warning') or current_time - self._last_fallback_warning > 30:
                logger.warning("Could not get exact window bounds, using fallback")
                self._last_fallback_warning = current_time

            screen_size = Quartz.CGDisplayBounds(Quartz.CGMainDisplayID())
            self.macro.window_x = 0
            self.macro.window_y = 0
            self.macro.window_width = int(screen_size.size.width)
            self.macro.window_height = int(screen_size.size.height)
            self.last_bounds_update = current_time
            return True

        except Exception as e:
            logger.error(f"Error getting window position: {e}")
            self.macro.window_x = self.macro.window_y = self.macro.window_width = self.macro.window_height = 0
            return False

    def get_y_offset(self, hwnd=None, fail_ref=None):
        """
        Find the y-offset of GUI elements in the current Roblox window
        Equivalent to GetYOffset()
        Returns: offset (int), sets fail_ref[0] to 1 on error
        """
        static_cache = {}

        if not hwnd:
            hwnd = self.get_roblox_hwnd()

        if not hwnd:
            if fail_ref:
                fail_ref[0] = 1
            return 0

        cache_key = hwnd['pid']
        if cache_key in static_cache:
            return static_cache[cache_key]

        try:
            # This function would search for specific UI elements in BSS
            # to determine the Y offset caused by different GUI layouts
            # Simplified implementation for now
            offset = 0

            # In the full implementation, this would:
            # 1. Take screenshots of specific areas
            # 2. Use image search to find UI elements
            # 3. Calculate offset based on their positions

            static_cache[cache_key] = offset
            if fail_ref:
                fail_ref[0] = 0
            return offset

        except Exception as e:
            logger.error(f"Error calculating Y offset: {e}")
            if fail_ref:
                fail_ref[0] = 1
            return 0

    def activate_roblox_window(self):
        """
        Bring Roblox window to front
        Returns: True if successful
        """
        try:
            if self.roblox_app:
                self.roblox_app.activateWithOptions_(1)  # NSApplicationActivateIgnoringOtherApps
                time.sleep(0.5)  # Wait for window to activate
                return True
            else:
                # Fallback method using AppleScript
                import subprocess
                script = '''
                tell application "RobloxPlayer"
                    activate
                end tell
                '''
                result = subprocess.run(['osascript', '-e', script],
                                      capture_output=True, text=True)
                return result.returncode == 0
        except Exception as e:
            logger.error(f"Error activating Roblox window: {e}")
            return False

    def is_roblox_focused(self):
        """
        Check if Roblox window is currently focused
        Returns: True if focused
        """
        try:
            frontmost_app = NSWorkspace.sharedWorkspace().frontmostApplication()
            if frontmost_app and self.roblox_app:
                return frontmost_app.processIdentifier() == self.roblox_app.processIdentifier()
            return False
        except Exception as e:
            logger.error(f"Error checking focus: {e}")
            return False

    def get_roblox_window_region(self):
        """
        Get the screen region occupied by Roblox window
        Returns: (x, y, width, height) or None
        """
        if self.get_roblox_client_pos():
            return (self.macro.window_x, self.macro.window_y,
                   self.macro.window_width, self.macro.window_height)
        return None
