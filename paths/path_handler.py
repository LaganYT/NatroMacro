"""
Path handling for Natro Macro
Converted from paths/*.ahk
"""

import logging
import time
from typing import Optional

logger = logging.getLogger(__name__)


class PathHandler:
    """Handles movement paths and sequences"""

    def __init__(self, macro_instance):
        self.macro = macro_instance

        # Key mappings (these would be defined in the main macro)
        self.key_mappings = {
            'FwdKey': 'w',
            'BackKey': 's',
            'LeftKey': 'a',
            'RightKey': 'd',
            'RotLeft': 'q',
            'RotRight': 'e',
            'Space': 'space'
        }

    def execute_path(self, path_name: str, move_method: str = "walk"):
        """
        Execute a movement path by name

        Args:
            path_name: Name of the path to execute
            move_method: Movement method ("walk" or "cannon")
        """
        try:
            # Import the specific path module
            path_module = __import__(f'paths.{path_name}', fromlist=[path_name])
            path_function = getattr(path_module, path_name.replace('-', '_'))

            # Execute the path
            path_function(self, move_method)

        except ImportError:
            logger.error(f"Path {path_name} not found")
        except AttributeError:
            logger.error(f"Path function {path_name} not found in path module")
        except Exception as e:
            logger.error(f"Error executing path {path_name}: {e}")

    def nm_walk(self, distance: float, *keys: str, haste_cap: int = 0):
        """
        Walk a specific distance while holding keys
        Equivalent to nm_Walk()

        Args:
            distance: Distance to walk (in studs/tiles)
            *keys: Keys to hold while walking
            haste_cap: Haste cap limit (0 = no limit)
        """
        logger.info(f"Walking {distance} units with keys: {keys}")

        # Calculate walk time based on distance (this is a simplified calculation)
        # In the real implementation, this would be more complex
        walk_time = distance * 0.1  # 100ms per unit (simplified)

        # Send key down events
        for key in keys:
            actual_key = self.key_mappings.get(key, key)
            self.macro.send_keys(f"{{{actual_key} down}}")

        # Wait for walk duration
        time.sleep(walk_time)

        # Send key up events
        for key in keys:
            actual_key = self.key_mappings.get(key, key)
            self.macro.send_keys(f"{{{actual_key} up}}")

    def nm_gotoramp(self):
        """Go to the ramp location"""
        logger.info("Going to ramp")
        # Simplified implementation - would contain actual movement logic
        pass

    def nm_gotocannon(self):
        """Go to the cannon location"""
        logger.info("Going to cannon")
        # Simplified implementation - would contain actual movement logic
        pass

    def send_key_sequence(self, sequence: str):
        """
        Send a sequence of key presses
        Equivalent to Send in AHK

        Args:
            sequence: Key sequence to send (AHK format)
        """
        logger.info(f"Sending key sequence: {sequence}")
        # Convert AHK-style sequences to pyautogui format
        # This is a simplified conversion
        self.macro.send_keys(sequence)

    def hyper_sleep(self, milliseconds: int):
        """
        Sleep for specified milliseconds
        Equivalent to Sleep in AHK

        Args:
            milliseconds: Time to sleep in milliseconds
        """
        from lib.hyper_sleep import hyper_sleep
        hyper_sleep(milliseconds)

    def nm_resetwindow(self):
        """Reset the game window position"""
        logger.info("Resetting window")
        # Simplified implementation
        pass

    def nm_center(self):
        """Center the character"""
        logger.info("Centering character")
        # Simplified implementation
        pass
