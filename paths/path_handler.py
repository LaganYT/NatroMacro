"""
Path handling system for Natro Macro
Converts AHK path files to Python executable movement sequences
"""

import logging
import time
from typing import List, Dict, Any, Optional

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
            *keys: Keys to hold during movement
            haste_cap: Haste cap for movement calculation
        """
        try:
            # Convert key names to actual keys
            actual_keys = []
            for key in keys:
                if key in self.key_mappings:
                    actual_keys.append(self.key_mappings[key])
                else:
                    actual_keys.append(key.lower())

            # Press keys
            for key in actual_keys:
                self.macro.send_keys(f"{{{key} down}}")

            # Calculate movement time based on distance and current speed
            # This is a simplified calculation - actual implementation would
            # use the Walk() function from lib/Walk.ahk for precise timing
            base_speed = 16  # studs per second (approximate)
            move_time = (distance / base_speed) * 1000  # milliseconds

            # Sleep for movement duration
            time.sleep(move_time / 1000)

            # Release keys
            for key in reversed(actual_keys):
                self.macro.send_keys(f"{{{key} up}}")

        except Exception as e:
            logger.error(f"Error in nm_walk: {e}")

    def nm_gotoramp(self):
        """Go to the ramp position"""
        # This would be a specific movement sequence
        # Implementation depends on current position
        logger.debug("Going to ramp")
        # TODO: Implement actual ramp navigation

    def nm_gotocannon(self):
        """Go to the cannon position"""
        # This would be a specific movement sequence
        logger.debug("Going to cannon")
        # TODO: Implement actual cannon navigation

    def send_key_sequence(self, sequence: str):
        """
        Send a sequence of key presses
        Equivalent to AHK send command

        Args:
            sequence: Key sequence string (e.g., "{e down}", "{space 2}")
        """
        try:
            self.macro.send_keys(sequence)
        except Exception as e:
            logger.error(f"Error sending key sequence: {e}")

    def hyper_sleep(self, ms: float):
        """High-precision sleep"""
        from lib.hyper_sleep import hyper_sleep
        hyper_sleep(ms)


# Path execution functions for different field types

def gtb_blue(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gather treasure bee - blue field path
    Converted from paths/gtb-blue.ahk
    """
    if move_method == "walk":
        path_handler.nm_gotoramp()
        path_handler.nm_walk(88.875, "BackKey", "LeftKey")
        path_handler.nm_walk(27, "LeftKey")
        path_handler.hyper_sleep(50)
        path_handler.send_key_sequence("{q 2}")
        # inside
        path_handler.nm_walk(50, "FwdKey")
    else:
        path_handler.nm_gotoramp()
        path_handler.nm_gotocannon()
        path_handler.send_key_sequence("{e down}")
        path_handler.hyper_sleep(100)
        path_handler.send_key_sequence("{e up}{a down}")
        path_handler.hyper_sleep(700)
        path_handler.send_key_sequence("{space 2}")
        path_handler.hyper_sleep(4450)
        path_handler.send_key_sequence("{a up}{space}")
        path_handler.hyper_sleep(1000)
        path_handler.send_key_sequence("{q 2}")
        path_handler.nm_walk(4, "BackKey", "LeftKey")
        path_handler.nm_walk(8, "FwdKey", "LeftKey")
        path_handler.nm_walk(6, "FwdKey")
        path_handler.nm_walk(5, "BackKey")
        path_handler.nm_walk(8, "RightKey")
        # inside
        path_handler.nm_walk(30, "FwdKey")

    path_handler.send_key_sequence("{space down}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{space up}")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(9, "RightKey", "BackKey")
    path_handler.nm_walk(4, "RightKey")
    path_handler.nm_walk(2, "LeftKey")
    path_handler.nm_walk(21, "BackKey")
    path_handler.nm_walk(3.4, "FwdKey", "LeftKey")
    path_handler.nm_walk(16, "LeftKey")
    # path 230630 noobyguy


def gtb_mountain(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gather treasure bee - mountain field path
    Placeholder implementation
    """
    logger.info("Executing mountain path (placeholder)")
    # TODO: Implement actual mountain path from gtb-mountain.ahk


def gtb_mountain(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gather treasure bee - mountain field path
    Converted from paths/gtb-mountain.ahk
    """
    if move_method == "walk":
        path_handler.nm_gotoramp()
        path_handler.nm_walk(67.5, "BackKey", "LeftKey")
        path_handler.send_key_sequence("{e 4}")
        path_handler.nm_walk(31.5, "FwdKey")
        path_handler.nm_walk(9, "LeftKey")
        path_handler.nm_walk(9, "BackKey")
        path_handler.nm_walk(58.5, "LeftKey")
        path_handler.nm_walk(49.5, "FwdKey")
        path_handler.nm_walk(3.375, "LeftKey")
        path_handler.nm_walk(36, "FwdKey")
        path_handler.nm_walk(54, "RightKey")
        path_handler.nm_walk(54, "BackKey")
        path_handler.nm_walk(58.5, "RightKey")
        path_handler.nm_walk(15.75, "FwdKey", "LeftKey")
        path_handler.nm_walk(13.5, "FwdKey")
        path_handler.send_key_sequence("{e 4}")
        path_handler.nm_walk(27, "RightKey")
        path_handler.nm_walk(18, "BackKey")
        path_handler.nm_walk(27, "RightKey")
    else:
        path_handler.nm_gotoramp()
        path_handler.nm_gotocannon()
        path_handler.send_key_sequence("{e down}")
        path_handler.hyper_sleep(100)
        path_handler.send_key_sequence("{e up}")
        path_handler.hyper_sleep(3000)
        path_handler.nm_walk(40.5, "RightKey")


def gtb_red(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gather treasure bee - red field path
    Converted from paths/gtb-red.ahk
    """
    if move_method == "walk":
        path_handler.nm_gotoramp()
        path_handler.nm_walk(67.5, "BackKey", "LeftKey")
        path_handler.send_key_sequence("{e 4}")
        path_handler.nm_walk(31.5, "FwdKey")
        path_handler.nm_walk(9, "LeftKey")
        path_handler.nm_walk(9, "BackKey")
        path_handler.nm_walk(58.5, "LeftKey")
        path_handler.nm_walk(49.5, "FwdKey")
        path_handler.nm_walk(20.25, "LeftKey")
        path_handler.send_key_sequence("{e 4}")
        path_handler.nm_walk(60.75, "FwdKey")
        path_handler.send_key_sequence("{e 2}")
        path_handler.nm_walk(9, "BackKey")
        path_handler.nm_walk(15.75, "BackKey", "RightKey")
        path_handler.nm_walk(29.7, "LeftKey")
        path_handler.nm_walk(11.25, "FwdKey")
        path_handler.nm_walk(13.5, "LeftKey")
    else:
        path_handler.nm_gotoramp()
        path_handler.send_key_sequence("{space down}{d down}")
        path_handler.hyper_sleep(100)
        path_handler.send_key_sequence("{space up}")
        path_handler.walk_system.walk(2)
        path_handler.send_key_sequence("{w down}")
        path_handler.walk_system.walk(1.8)
        path_handler.send_key_sequence("{w up}")
        path_handler.walk_system.walk(30)
        path_handler.send_key_sequence("{space down}")
        path_handler.hyper_sleep(300)
        path_handler.send_key_sequence("{space up}{w down}")
        path_handler.walk_system.walk(4)
        path_handler.send_key_sequence("{w up}")
        path_handler.walk_system.walk(3)
        path_handler.send_key_sequence("{d up}{e 2}{space down}")
        path_handler.hyper_sleep(100)
        path_handler.send_key_sequence("{space up}")
        path_handler.nm_walk(3, "FwdKey")
        path_handler.hyper_sleep(1000)
        path_handler.send_key_sequence("{space down}{d down}")
        path_handler.hyper_sleep(100)
        path_handler.send_key_sequence("{space up}")
        path_handler.hyper_sleep(300)
        path_handler.send_key_sequence("{space}{d up}")
        path_handler.hyper_sleep(1000)
        path_handler.nm_walk(8, "FwdKey", "RightKey")
        path_handler.nm_walk(1, "FwdKey")


# Go To Collection (gtc-*) paths

def gtc_blender(path_handler: PathHandler, move_method: str = "walk"):
    """
    Go to blender - badge shop path
    Converted from paths/gtc-blender.ahk
    """
    if move_method == "walk":
        path_handler.nm_gotoramp()
        path_handler.nm_walk(67.5, "BackKey", "LeftKey")
        path_handler.send_key_sequence("{e 4}")
        path_handler.nm_walk(31, "FwdKey")
        path_handler.nm_walk(7.8, "LeftKey")
        path_handler.nm_walk(10, "BackKey")
        path_handler.nm_walk(5, "RightKey")
        path_handler.nm_walk(1.5, "FwdKey")
        path_handler.nm_walk(60, "LeftKey")
        path_handler.nm_walk(3.75, "RightKey")
        path_handler.nm_walk(38, "FwdKey")
        path_handler.send_key_sequence("{q 4}")
        path_handler.nm_walk(14, "RightKey")
        path_handler.nm_walk(15, "FwdKey", "LeftKey")
        path_handler.nm_walk(1, "BackKey")
        path_handler.hyper_sleep(200)
        path_handler.nm_walk(25, "RightKey")
        path_handler.hyper_sleep(200)
        path_handler.send_key_sequence("{e 2}")
        path_handler.hyper_sleep(200)
        # inside badge shop
        path_handler.nm_walk(15, "FwdKey")
        path_handler.nm_walk(1, "FwdKey", "RightKey")
        # align with corner
        path_handler.nm_walk(7, "FwdKey")
        path_handler.nm_walk(3, "BackKey")
        path_handler.nm_walk(26, "LeftKey")
        path_handler.nm_walk(1, "FwdKey", "LeftKey")


def gtc_antpass(path_handler: PathHandler, move_method: str = "walk"):
    """
    Go to ant pass
    Converted from paths/gtc-antpass.ahk
    """
    if move_method == "walk":
        path_handler.nm_gotoramp()
        path_handler.nm_walk(67.5, "BackKey", "LeftKey")
        path_handler.send_key_sequence("{e 4}")
        path_handler.nm_walk(31.5, "FwdKey")
        path_handler.nm_walk(9, "LeftKey")
        path_handler.nm_walk(9, "BackKey")
        path_handler.nm_walk(58.5, "LeftKey")
        path_handler.nm_walk(49.5, "FwdKey")
        path_handler.nm_walk(3.375, "LeftKey")
        path_handler.nm_walk(36, "FwdKey")
        path_handler.nm_walk(54, "RightKey")
        path_handler.nm_walk(54, "BackKey")
        path_handler.nm_walk(58.5, "RightKey")
        path_handler.nm_walk(15.75, "FwdKey", "LeftKey")
        path_handler.nm_walk(13.5, "FwdKey")
        path_handler.send_key_sequence("{e 4}")
        path_handler.nm_walk(27, "RightKey")
        path_handler.nm_walk(18, "BackKey")
        path_handler.nm_walk(27, "RightKey")


# Go To Field (gtf-*) paths

def gtf_sunflower(path_handler: PathHandler, move_method: str = "walk"):
    """
    Go to sunflower field
    Converted from paths/gtf-sunflower.ahk
    """
    path_handler.nm_gotoramp()
    path_handler.nm_walk(9, "BackKey")
    path_handler.nm_walk(6.75, "BackKey", "RightKey")
    path_handler.send_key_sequence("{e 2}")
    path_handler.nm_walk(29, "RightKey")
    # path 230212 zaappiix


def gtf_blueflower(path_handler: PathHandler, move_method: str = "walk"):
    """
    Go to blue flower field
    Placeholder implementation
    """
    logger.info("Executing blue flower field path (placeholder)")
    # TODO: Implement actual blue flower field path


# Go To Planter (gtp-*) paths

def gtp_sunflower(path_handler: PathHandler, move_method: str = "walk"):
    """
    Go to sunflower planter
    Converted from paths/gtp-sunflower.ahk
    """
    path_handler.nm_gotoramp()
    path_handler.nm_walk(14, "BackKey")
    path_handler.send_key_sequence("{e 1}")
    path_handler.nm_walk(25, "RightKey")
    path_handler.nm_walk(15, "FwdKey")
    path_handler.nm_walk(9, "BackKey")
    path_handler.send_key_sequence("{e 1}")


# Go To Quest (gtq-*) paths

def gtq_honey(path_handler: PathHandler, move_method: str = "walk"):
    """
    Go to honey quest
    Placeholder implementation
    """
    logger.info("Executing honey quest path (placeholder)")
    # TODO: Implement actual honey quest path


# World Farming (wf-*) paths

def wf_sunflower(path_handler: PathHandler, move_method: str = "walk"):
    """
    World farming - sunflower field path
    Converted from paths/wf-sunflower.ahk
    """
    path_handler.send_key_sequence("{q 2}")
    path_handler.nm_walk(13.5, "RightKey")  # walk to edge of field
    path_handler.nm_walk(45, "FwdKey")      # walk to corner (special sprout)
    path_handler.nm_walk(2.25, "BackKey")   # back out of corner
    path_handler.nm_walk(25, "FwdKey", "LeftKey")  # move diagonally towards hives
    path_handler.nm_walk(13.5, "FwdKey")    # walk towards hives
    path_handler.nm_walk(1.5, "BackKey")    # walk backwards to avoid thicker hives
    path_handler.nm_walk(10, "RightKey")    # walk to ramp
    path_handler.nm_walk(2.7, "BackKey")    # center with hive pads
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update


def gtc_antpass(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Antpass path
    Converted from paths/gtc-antpass.ahk
    """
    path_handler.nm_walk(3, "FwdKey")
    path_handler.nm_walk(52, "LeftKey")
    path_handler.nm_walk(3, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(5, "RightKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}{{")
    path_handler.hyper_sleep(500)
    path_handler.nm_walk(2, "FwdKey")
    path_handler.nm_walk(15, "RightKey")
    path_handler.nm_walk(6, "FwdKey", "RightKey")
    path_handler.nm_walk(7, "FwdKey")
    path_handler.nm_walk(5, "BackKey", "LeftKey")
    path_handler.nm_walk(23, "FwdKey")
    path_handler.nm_walk(12, "LeftKey")
    path_handler.nm_walk(8, "LeftKey", "FwdKey")
    path_handler.nm_walk(10, "FwdKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(25, "FwdKey", "RightKey")
    path_handler.nm_walk(25, "LeftKey")
    path_handler.nm_walk(17, "BackKey")


def gtc_blender(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Blender path
    Converted from paths/gtc-blender.ahk
    """
    if move_method == "walk":
        path_handler.nm_gotoramp()
        path_handler.nm_walk(67.5, "BackKey", "LeftKey")
        path_handler.send_key_sequence("{{")
        path_handler.nm_walk(31, "FwdKey")
        path_handler.nm_walk(7.8, "LeftKey")
        path_handler.nm_walk(10, "BackKey")
        path_handler.nm_walk(5, "RightKey")
        path_handler.nm_walk(1.5, "FwdKey")
        path_handler.nm_walk(60, "LeftKey")
        path_handler.nm_walk(3.75, "RightKey")
        path_handler.nm_walk(38, "FwdKey")
        path_handler.send_key_sequence("{{")
        path_handler.nm_walk(14, "RightKey")
        path_handler.nm_walk(15, "FwdKey", "LeftKey")
        path_handler.nm_walk(1, "BackKey")
        path_handler.hyper_sleep(200)
        path_handler.nm_walk(25, "RightKey")
        path_handler.hyper_sleep(200)
        path_handler.send_key_sequence("{{")
        path_handler.hyper_sleep(200)
        # inside badge shop
        path_handler.nm_walk(15, "FwdKey")
        path_handler.nm_walk(1, "FwdKey", "RightKey")
        # align with corner
        path_handler.nm_walk(7, "FwdKey")
        path_handler.nm_walk(3, "BackKey")
        path_handler.nm_walk(26, "LeftKey")
        path_handler.nm_walk(1, "FwdKey", "LeftKey")
        path_handler.hyper_sleep(300)
    else:
        path_handler.nm_gotoramp()
        path_handler.nm_gotocannon()
        path_handler.send_key_sequence("{{e down}}")
        path_handler.hyper_sleep(100)
        path_handler.send_key_sequence("{{e up}}{{")
        path_handler.hyper_sleep(925)
        path_handler.send_key_sequence("{{space 2}}")
        path_handler.hyper_sleep(2850)
        path_handler.send_key_sequence("{{")
        path_handler.hyper_sleep(1450)
        path_handler.send_key_sequence("{{space}}{{")
        path_handler.hyper_sleep(600)
        # corner align
        path_handler.nm_walk(10, "FwdKey", "LeftKey")
        path_handler.nm_walk(10, "LeftKey", "FwdKey")
        path_handler.nm_walk(1, "BackKey")
        path_handler.hyper_sleep(200)
        path_handler.nm_walk(25, "RightKey")
        path_handler.hyper_sleep(200)
        path_handler.send_key_sequence("{{")
        path_handler.hyper_sleep(200)
        # inside badge shop
        path_handler.nm_walk(15, "FwdKey")
        path_handler.nm_walk(1, "FwdKey", "RightKey")
        # align with corner
        path_handler.nm_walk(7, "FwdKey")
        path_handler.nm_walk(3, "BackKey")
        path_handler.nm_walk(26, "LeftKey")
        path_handler.nm_walk(1, "FwdKey", "LeftKey")
        path_handler.hyper_sleep(300)


def gtc_blueberrydis(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Blueberrydis path
    Converted from paths/gtc-blueberrydis.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(88.875, "BackKey", "LeftKey")
    path_handler.nm_walk(27, "LeftKey")
    path_handler.hyper_sleep(50)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(50)
    path_handler.nm_walk(30, "FwdKey")
    path_handler.nm_walk(11.5, "FwdKey", "RightKey")
    path_handler.nm_walk(2, "RightKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(700)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(4450)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(10, "LeftKey")
    path_handler.nm_walk(8, "RightKey")
    # inside
    path_handler.nm_walk(10, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(100)
    path_handler.nm_walk(1.6, "FwdKey")
    path_handler.send_key_sequence("{{FwdKey down}}{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.send_key_sequence("{{space}}")
    path_handler.hyper_sleep(1300)
    # path 230629 noobyguy


def gtc_candles(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Candles path
    Converted from paths/gtc-candles.ahk
    """
    nm_gotoramp()
    Send "{space down}{" RightKey " down}"
    Sleep 100
    Send "{space up}"
    Walk(2)
    Send "{" FwdKey " down}"
    Walk(1.8)
    Send "{" FwdKey " up}"
    Walk(30)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}{{")
    Walk(4)
    path_handler.send_key_sequence("{{")
    Walk(3)
    path_handler.send_key_sequence("{{")
    Sleep 200
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(3, "FwdKey")
    Sleep 1000
    path_handler.send_key_sequence("{{space down}}{{")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space}}{{")
    path_handler.hyper_sleep(1000)
    path_handler.nm_walk(4, "RightKey")
    path_handler.nm_walk(14, "FwdKey")
    path_handler.nm_walk(8, "RightKey")
    path_handler.nm_walk(5, "LeftKey")


def gtc_clock(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Clock path
    Converted from paths/gtc-clock.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(44.75, "BackKey", "LeftKey")
    path_handler.nm_walk(28, "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(6, "LeftKey")
    path_handler.nm_walk(12, "BackKey", "LeftKey")
    sleep 500
    path_handler.nm_walk(1.5, "RightKey")
    path_handler.nm_walk(12.2, "FwdKey")
    path_handler.nm_walk(14, "LeftKey")
    path_handler.nm_walk(1.5, "RightKey", "BackKey")
    path_handler.nm_walk(15, "BackKey")
    path_handler.nm_walk(7.5, "LeftKey")
    sleep 500
    path_handler.nm_walk(1.75, "RightKey")
    path_handler.nm_walk(4, "FwdKey")
    path_handler.nm_walk(22.5, "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(40, "FwdKey")
    path_handler.nm_walk(1, "BackKey")
    path_handler.nm_walk(20, "RightKey")
    path_handler.nm_walk(5, "FwdKey")
    path_handler.nm_walk(16, "LeftKey")
    path_handler.nm_walk(15, "FwdKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    Send "{e down}"
    path_handler.hyper_sleep(100)
    Send "{e up}{" FwdKey " down}{" LeftKey " down}"
    path_handler.hyper_sleep(1500)
    path_handler.send_key_sequence("{{space 2}}")
    Sleep 8000
    Send "{" FwdKey " up}{" LeftKey " up}"
    path_handler.nm_walk(15, "BackKey")
    path_handler.nm_walk(3.5, "RightKey")
    path_handler.nm_walk(2, "RightKey", "BackKey")
    path_handler.nm_walk(1, "BackKey")


def gtc_coconutdis(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Coconutdis path
    Converted from paths/gtc-coconutdis.ahk
    """
    nm_gotoramp()
    Send "{space down}{" RightKey " down}"
    Sleep 100
    Send "{space up}"
    Walk(2)
    Send "{" FwdKey " down}"
    Walk(1.8)
    Send "{" FwdKey " up}"
    Walk(30)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(4, "RightKey")
    path_handler.nm_walk(5, "FwdKey")
    path_handler.nm_walk(3, "RightKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.nm_walk(2, "LeftKey", "FwdKey")
    path_handler.nm_walk(8, "FwdKey")
    Send "{" FwdKey " down}{" RightKey " down}"
    Walk(11)
    path_handler.send_key_sequence("{{space down}}{{")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(4, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(30, "FwdKey")
    sleep 100
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(15.7, "LeftKey")
    path_handler.nm_walk(8, "FwdKey")
    # paths 230629 noobyguy


def gtc_extrememm(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Extrememm path
    Converted from paths/gtc-extrememm.ahk
    """
    path_handler.nm_gotoramp()
    Send "{space down}{" RightKey " down}"
    Sleep 100
    Send "{space up}"
    Walk(2)
    Send "{" FwdKey " down}"
    Walk(1.8)
    Send "{" FwdKey " up}"
    Walk(30)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(4, "RightKey")
    path_handler.nm_walk(5, "FwdKey")
    path_handler.nm_walk(3, "RightKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.nm_walk(2, "LeftKey", "FwdKey")
    path_handler.nm_walk(8, "FwdKey")
    Send "{" FwdKey " down}{" RightKey " down}"
    Walk(11)
    path_handler.send_key_sequence("{{space down}}{{")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    Walk(18)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    Walk(26)
    Send "{" FwdKey " up}"
    Send "{" RightKey " down}"
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    Walk(15)
    Send "{" RightKey " up}"
    path_handler.nm_walk(2, "FwdKey")
    Sleep 1000


def gtc_feast(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Feast path
    Converted from paths/gtc-feast.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31.5, "FwdKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(9, "BackKey")
    path_handler.nm_walk(58.5, "LeftKey")
    path_handler.nm_walk(49.5, "FwdKey")
    path_handler.nm_walk(3.375, "LeftKey")
    path_handler.nm_walk(36, "FwdKey")
    path_handler.nm_walk(60, "RightKey")
    path_handler.nm_walk(60, "BackKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(3.5, "FwdKey", "RightKey")
    path_handler.nm_walk(8.5, "FwdKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(760)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2100)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space}}{{")
    path_handler.nm_walk(10, "LeftKey")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.nm_walk(2.2, "RightKey")
    path_handler.nm_walk(2, "FwdKey")
    Send "{space down}"
    path_handler.hyper_sleep(100)
    Send "{space up}"
    path_handler.nm_walk(5, "FwdKey")
    Sleep 1000


def gtc_gingerbread(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Gingerbread path
    Converted from paths/gtc-gingerbread.ahk
    """
    nm_gotoramp()
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(4.7, "RightKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(600)
    path_handler.nm_walk(6, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(25, "FwdKey")
    path_handler.nm_walk(3, "FwdKey", "RightKey")
    path_handler.nm_walk(15, "FwdKey")
    path_handler.nm_walk(2, "FwdKey", "RightKey")
    path_handler.nm_walk(12.5, "FwdKey")


def gtc_gluedis(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Gluedis path
    Converted from paths/gtc-gluedis.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_walk(3, "FwdKey")
    path_handler.nm_walk(52, "LeftKey")
    path_handler.nm_walk(3, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(5, "RightKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}{{")
    path_handler.hyper_sleep(500)
    path_handler.nm_walk(2, "FwdKey")
    path_handler.nm_walk(15, "RightKey")
    path_handler.nm_walk(6, "FwdKey", "RightKey")
    path_handler.nm_walk(7, "FwdKey")
    path_handler.nm_walk(5, "BackKey", "LeftKey")
    path_handler.nm_walk(23, "FwdKey")
    path_handler.nm_walk(12, "LeftKey")
    path_handler.nm_walk(8, "LeftKey", "FwdKey")
    path_handler.nm_walk(10, "FwdKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(25, "FwdKey", "RightKey")
    path_handler.nm_walk(50, "LeftKey")
    path_handler.nm_walk(2, "RightKey")
    path_handler.nm_walk(40, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(55, "FwdKey")
    path_handler.nm_walk(10, "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(5.79, "FwdKey", "RightKey")
    path_handler.nm_walk(50, "FwdKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(4, "FwdKey", "RightKey")
    path_handler.send_key_sequence("{{")
    Sleep 1500
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1170)
    path_handler.send_key_sequence("{{space 2}}{{")
    path_handler.hyper_sleep(6750)
    path_handler.nm_walk(18, "FwdKey")
    path_handler.nm_walk(8.5, "LeftKey")
    path_handler.nm_walk(3, "LeftKey", "FwdKey")
    Sleep 1500
    # path 230630 noobyguy - walk updated


def gtc_gummybeacon(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Gummybeacon path
    Converted from paths/gtc-gummybeacon.ahk
    """
    nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1070)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2200)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(2200)
    path_handler.send_key_sequence("{{space}}{{")
    Sleep 1200


def gtc_honeydis(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Honeydis path
    Converted from paths/gtc-honeydis.ahk
    """
    nm_Walk(1, FwdKey)
    nm_Walk(9.2*(7-HiveSlot) + 10, LeftKey)
    path_handler.nm_walk(2, "BackKey", "RightKey")
    path_handler.nm_walk(2, "BackKey")


def gtc_honeylb(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Honeylb path
    Converted from paths/gtc-honeylb.ahk
    """
    nm_gotoramp()
    path_handler.nm_walk(18, "LeftKey", "BackKey")
    path_handler.nm_walk(8, "BackKey")
    path_handler.send_key_sequence("{{")
    Sleep 2000


def gtc_honeystorm(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Honeystorm path
    Converted from paths/gtc-honeystorm.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(44.75, "BackKey", "LeftKey")
    path_handler.nm_walk(52.5, "LeftKey")
    path_handler.nm_walk(2.8, "BackKey", "RightKey")
    path_handler.nm_walk(6.7, "BackKey")
    path_handler.nm_walk(40.5, "LeftKey")
    path_handler.nm_walk(5, "BackKey")
    path_handler.send_key_sequence("{{")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1180)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(5000)
    path_handler.send_key_sequence("{{")
    Sleep 1500
    path_handler.nm_walk(10, "FwdKey", "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(7, "BackKey", "RightKey")
    path_handler.nm_walk(9, "BackKey")
    path_handler.send_key_sequence("{{")
    Sleep 250
    # path 230630 noobyguy


def gtc_lidart(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Lidart path
    Converted from paths/gtc-lidart.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31.5, "FwdKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(9, "BackKey")
    path_handler.nm_walk(58.5, "LeftKey")
    path_handler.nm_walk(49.5, "FwdKey")
    path_handler.nm_walk(3.375, "LeftKey")
    path_handler.nm_walk(36, "FwdKey")
    path_handler.nm_walk(54, "RightKey")
    path_handler.nm_walk(54, "BackKey")
    path_handler.nm_walk(58.5, "RightKey")
    path_handler.nm_walk(3, "LeftKey")
    path_handler.nm_walk(57, "FwdKey")
    path_handler.nm_walk(16, "LeftKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1400)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(650)
    path_handler.send_key_sequence("{{")
    Sleep 1500
    path_handler.nm_walk(4, "RightKey", "FwdKey")
    path_handler.nm_walk(23, "FwdKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(3, "FwdKey")
    path_handler.nm_walk(8, "LeftKey")
    path_handler.nm_walk(3.6, "RightKey")
    path_handler.nm_walk(41, "FwdKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(21, "FwdKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(3, "FwdKey")
    Sleep 1000
    # path 230212 zaappiix


def gtc_megamm(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Megamm path
    Converted from paths/gtc-megamm.ahk
    """
    if move_method == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(7.8, "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.nm_walk(60, "LeftKey")
    path_handler.nm_walk(3.75, "RightKey")
    path_handler.nm_walk(38, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(14, "RightKey")
    path_handler.nm_walk(15, "FwdKey", "LeftKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(925)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2850)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1450)
    path_handler.send_key_sequence("{{space}}{{")
    path_handler.hyper_sleep(600)
    # corner align
    path_handler.nm_walk(10, "FwdKey", "LeftKey")
    path_handler.nm_walk(10, "LeftKey", "FwdKey")
    path_handler.nm_walk(1, "BackKey")
    path_handler.hyper_sleep(200)
    path_handler.nm_walk(25, "RightKey")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(200)
    # inside badge shop
    path_handler.nm_walk(15, "FwdKey")
    path_handler.nm_walk(1, "FwdKey", "RightKey")
    # align with corner
    path_handler.nm_walk(7, "FwdKey")
    path_handler.nm_walk(4, "BackKey")
    path_handler.nm_walk(3, "LeftKey")
    Sleep 1000
    # path 230630 noobyguy - walk updated
    # adjusted for memory match OAC


def gtc_nightmm(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Nightmm path
    Converted from paths/gtc-nightmm.ahk
    """
    if move_method == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31.5, "FwdKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(9, "BackKey")
    path_handler.nm_walk(58.5, "LeftKey")
    path_handler.nm_walk(49.5, "FwdKey")
    path_handler.nm_walk(3.375, "LeftKey")
    path_handler.nm_walk(36, "FwdKey")
    path_handler.nm_walk(54, "RightKey")
    path_handler.nm_walk(54, "BackKey")
    path_handler.nm_walk(58.5, "RightKey")
    path_handler.nm_walk(3, "LeftKey")
    path_handler.nm_walk(57, "FwdKey")
    path_handler.nm_walk(16, "LeftKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1400)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(650)
    path_handler.send_key_sequence("{{")
    Sleep 1500
    path_handler.nm_walk(4, "RightKey", "FwdKey")
    path_handler.nm_walk(23, "FwdKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(3, "FwdKey")
    path_handler.nm_walk(8, "LeftKey")
    path_handler.nm_walk(3.6, "RightKey")
    path_handler.nm_walk(41, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(8.8, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(25.6, "FwdKey")
    # moon jumps
    Jump([5, FwdKey])
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(2, "FwdKey")
    Jump([5, FwdKey])
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(1.5, "FwdKey", "LeftKey")
    path_handler.nm_walk(2, "FwdKey")
    Jump([2.5, FwdKey], [2.5, FwdKey, LeftKey])
    path_handler.nm_walk(2, "FwdKey")
    Jump([5, FwdKey])
    path_handler.nm_walk(2, "FwdKey")
    Jump([2, FwdKey, RightKey], [3, FwdKey])
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(2, "FwdKey")
    Jump([2.5, FwdKey, LeftKey], [2, FwdKey])
    path_handler.nm_walk(2, "FwdKey")
    Jump([5, FwdKey])
    path_handler.nm_walk(2, "FwdKey")
    Jump([4, FwdKey])
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(2, "FwdKey")
    Jump([8, FwdKey])
    path_handler.nm_walk(4, "FwdKey")
    path_handler.nm_walk(8, "FwdKey", "LeftKey")
    path_handler.nm_walk(7, "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(3, "BackKey", "RightKey")
    path_handler.nm_walk(10, "RightKey")
    path_handler.nm_walk(6, "FwdKey", "RightKey")
    Jump([3, FwdKey, RightKey], [1, RightKey])
    Sleep 500
    # jump function
    Jump(movements*) {
    DllCall("GetSystemTimeAsFileTime", "int64p", &jumped:=0)
    path_handler.send_key_sequence("{{")
    Sleep 100
    path_handler.send_key_sequence("{{")
    for params in movements
    nm_Walk(params*)
    DllCall("GetSystemTimeAsFileTime", "int64p", &current:=0)
    Sleep Max(1400-(current-jumped)//10000, -1)
    # [3 Mar 2024 / SP] First version of gtc-nightmm, first half from gtc-lidart zaappiix


def gtc_normalmm(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Normalmm path
    Converted from paths/gtc-normalmm.ahk
    """
    if move_method == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(69, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(30, "FwdKey")
    path_handler.nm_walk(20, "FwdKey", "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(43.5, "FwdKey")
    path_handler.nm_walk(16, "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(800)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(29.25, "FwdKey")
    path_handler.nm_walk(15, "FwdKey", "LeftKey")
    path_handler.nm_walk(8, "LeftKey")
    path_handler.nm_walk(15, "FwdKey", "LeftKey")
    path_handler.nm_walk(3.5, "RightKey")
    path_handler.nm_walk(11, "BackKey")
    path_handler.send_key_sequence("{{")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}")
    path_handler.hyper_sleep(2500)
    path_handler.nm_walk(30, "FwdKey")
    path_handler.nm_walk(2, "BackKey")
    path_handler.nm_walk(22, "LeftKey")
    path_handler.nm_walk(12, "RightKey")
    path_handler.nm_walk(3, "LeftKey")
    path_handler.nm_walk(5, "FwdKey")
    path_handler.send_key_sequence("{{")
    Sleep 1000
    # path 230630 noobyguy - walk updated
    # adjusted for memory match OAC


def gtc_rbpdelevel(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Rbpdelevel path
    Converted from paths/gtc-rbpdelevel.ahk
    """
    nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(530)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(3500)
    path_handler.send_key_sequence("{{space}}")
    Sleep 1200
    path_handler.nm_walk(20, "RightKey", "FwdKey")
    path_handler.nm_walk(8.5, "BackKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}{{")
    path_handler.hyper_sleep(250)
    path_handler.send_key_sequence("{{")
    Sleep 1000


def gtc_robopass(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Robopass path
    Converted from paths/gtc-robopass.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31.5, "FwdKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(9, "BackKey")
    path_handler.nm_walk(58.5, "LeftKey")
    path_handler.nm_walk(49.5, "FwdKey")
    path_handler.nm_walk(3.375, "LeftKey")
    path_handler.nm_walk(36, "FwdKey")
    path_handler.nm_walk(54, "RightKey")
    path_handler.nm_walk(54, "BackKey")
    path_handler.nm_walk(58.5, "RightKey")
    path_handler.nm_walk(3, "LeftKey")
    path_handler.nm_walk(57, "FwdKey")
    path_handler.nm_walk(16, "LeftKey")
    path_handler.nm_walk(3, "FwdKey")
    path_handler.nm_walk(8, "LeftKey")
    path_handler.nm_walk(2, "RightKey")
    path_handler.nm_walk(13, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(8.5, "FwdKey")
    path_handler.nm_walk(3, "LeftKey")
    path_handler.nm_walk(20, "FwdKey")
    Sleep 500
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1400)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(650)
    path_handler.send_key_sequence("{{")
    Sleep 1500
    path_handler.nm_walk(4, "RightKey", "FwdKey")
    path_handler.nm_walk(23, "FwdKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(3, "FwdKey")
    path_handler.nm_walk(8, "LeftKey")
    path_handler.nm_walk(2, "RightKey")
    path_handler.nm_walk(13, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(8.5, "FwdKey")
    path_handler.nm_walk(3, "LeftKey")
    path_handler.nm_walk(20, "FwdKey")
    Sleep 500
    # path 230629 noobyguy | 230909 reverted cannon path -noobyguy


def gtc_royaljellydis(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Royaljellydis path
    Converted from paths/gtc-royaljellydis.ahk
    """
    nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(750)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2250)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{")
    Sleep 1000
    path_handler.send_key_sequence("{{")
    Sleep 2000
    path_handler.nm_walk(13, "FwdKey")


def gtc_samovar(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Samovar path
    Converted from paths/gtc-samovar.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(45, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(58.5, "FwdKey")
    path_handler.nm_walk(18, "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(800)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(63, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(45, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(27, "FwdKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(3, "FwdKey")
    path_handler.nm_walk(10, "FwdKey", "RightKey")
    path_handler.nm_walk(8, "FwdKey", "LeftKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(3.5, "FwdKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(3, "FwdKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(6, "FwdKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(2000)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2800)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(900)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(650)
    path_handler.send_key_sequence("{{space}}")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(36, "FwdKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(3, "FwdKey")
    path_handler.nm_walk(10, "FwdKey", "RightKey")
    path_handler.nm_walk(8, "FwdKey", "LeftKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(3.5, "FwdKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(3, "FwdKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(6, "FwdKey")


def gtc_snowmachine(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Snowmachine path
    Converted from paths/gtc-snowmachine.ahk
    """
    if MoveMethod == "walk":
    {
    switch HiveSlot
    {
    case 2:
    path_handler.nm_gotoramp()
    path_handler.nm_walk(41, "BackKey", "LeftKey")
    path_handler.nm_walk(48, "LeftKey")
    path_handler.nm_walk(10, "FwdKey")
    path_handler.nm_walk(1, "RightKey")
    path_handler.nm_walk(6, "BackKey")
    case 3:
    path_handler.nm_walk(36, "BackKey", "LeftKey")
    path_handler.nm_walk(22, "LeftKey")
    path_handler.nm_walk(10, "FwdKey")
    path_handler.nm_walk(1, "RightKey")
    path_handler.nm_walk(6, "BackKey")
    case 4:
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(23, "BackKey")
    path_handler.nm_walk(30, "LeftKey")
    path_handler.nm_walk(10, "FwdKey")
    path_handler.nm_walk(1, "RightKey")
    path_handler.nm_walk(6, "BackKey")
    case 5:
    path_handler.nm_walk(23, "BackKey")
    path_handler.nm_walk(30, "LeftKey")
    path_handler.nm_walk(10, "FwdKey")
    path_handler.nm_walk(1, "RightKey")
    path_handler.nm_walk(6, "BackKey")
    case 6:
    path_handler.nm_walk(8, "RightKey")
    path_handler.nm_walk(23, "BackKey")
    path_handler.nm_walk(30, "LeftKey")
    path_handler.nm_walk(10, "FwdKey")
    path_handler.nm_walk(1, "RightKey")
    path_handler.nm_walk(6, "BackKey")
    default:
    path_handler.nm_gotoramp()
    path_handler.nm_walk(41, "LeftKey", "BackKey")
    path_handler.nm_walk(48, "LeftKey")
    path_handler.nm_walk(10, "FwdKey")
    path_handler.nm_walk(1, "RightKey")
    path_handler.nm_walk(6, "BackKey")
    path_handler.hyper_sleep(800)
    path_handler.send_key_sequence("{{space down}}{{")
    path_handler.hyper_sleep(250)
    path_handler.send_key_sequence("{{space up}}")
    Walk(17)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(800)
    path_handler.send_key_sequence("{{space down}}{{")
    path_handler.hyper_sleep(250)
    path_handler.send_key_sequence("{{space up}}")
    Walk(40)
    Send "{" LeftKey " up}"
    path_handler.nm_walk(8, "FwdKey")
    path_handler.hyper_sleep(250)
    path_handler.send_key_sequence("{{space down}}{{")
    path_handler.hyper_sleep(150)
    path_handler.send_key_sequence("{{space up}}")
    Walk(15)
    Send "{" LeftKey " up}"
    path_handler.nm_walk(16.5, "BackKey")
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(150)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(500)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(500)
    Walk(9)
    Send "{" FwdKey " up}{" RotLeft " 2}"
    path_handler.nm_walk(3, "FwdKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1250)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2200)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(2650)
    path_handler.send_key_sequence("{{space}}{{")
    Sleep 1500


def gtc_stickerPrinter(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Stickerprinter path
    Converted from paths/gtc-stickerPrinter.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(7.8, "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.nm_walk(60, "LeftKey")
    path_handler.nm_walk(3.75, "RightKey")
    path_handler.nm_walk(85, "FwdKey")
    path_handler.nm_walk(45, "RightKey")
    path_handler.nm_walk(50, "BackKey")
    path_handler.nm_walk(60, "RightKey")
    path_handler.nm_walk(15.75, "FwdKey", "LeftKey")
    path_handler.nm_walk(18, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "LeftKey")
    path_handler.nm_walk(3, "BackKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}")
    Sleep 4000
    path_handler.nm_walk(31, "LeftKey")
    path_handler.nm_walk(3, "BackKey")
    # path idkwhatimdoing money_mountain


def gtc_stickerstack(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Stickerstack path
    Converted from paths/gtc-stickerstack.ahk
    """
    if MoveMethod == "cannon":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1200)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(6000)
    path_handler.nm_walk(7, "RightKey")
    path_handler.nm_walk(11, "BackKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(2, "BackKey")
    path_handler.hyper_sleep(2000)
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31.5, "FwdKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(9, "BackKey")
    path_handler.nm_walk(58.5, "LeftKey")
    path_handler.nm_walk(49.5, "FwdKey")
    path_handler.nm_walk(2.25, "BackKey", "LeftKey")
    path_handler.nm_walk(36, "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.send_key_sequence("{{")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(500)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    Walk(6)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(6, "RightKey")
    path_handler.nm_walk(7, "FwdKey")
    path_handler.nm_walk(6, "LeftKey")
    path_handler.nm_walk(3, "RightKey")
    path_handler.nm_walk(32, "FwdKey")
    path_handler.nm_walk(4, "BackKey")
    path_handler.nm_walk(8, "LeftKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(4, "LeftKey")
    Sleep 500
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(6, "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(12, "FwdKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(14, "FwdKey", "LeftKey")
    path_handler.nm_walk(3, "FwdKey")


def gtc_stockings(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Stockings path
    Converted from paths/gtc-stockings.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(47.25, "BackKey", "LeftKey")
    path_handler.nm_walk(40.5, "LeftKey")
    path_handler.nm_walk(8.5, "BackKey")
    path_handler.nm_walk(43, "LeftKey")
    path_handler.nm_walk(13, "FwdKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1180)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(4950)
    path_handler.send_key_sequence("{{")
    Sleep 1500


def gtc_strawberrydis(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Strawberrydis path
    Converted from paths/gtc-strawberrydis.ahk
    """
    if HiveBees > 25) {
    path_handler.nm_gotoramp()
    Send "{space down}{" RightKey " down}"
    Sleep 100
    Send "{space up}"
    Walk(2)
    Send "{" FwdKey " down}"
    Walk(1.8)
    Send "{" FwdKey " up}"
    Walk(30)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(6, "RightKey")
    path_handler.hyper_sleep(500)
    path_handler.send_key_sequence("{{")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(3, "FwdKey")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{space down}}{{")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space}}{{")
    path_handler.hyper_sleep(1000)
    path_handler.nm_walk(7.5, Backkey, "RightKey")
    else {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31.5, "FwdKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(9, "BackKey")
    path_handler.nm_walk(58.5, "LeftKey")
    path_handler.nm_walk(49.5, "FwdKey")
    path_handler.nm_walk(20.25, "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(60.75, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(9, "BackKey")
    path_handler.nm_walk(15.75, "BackKey", "RightKey")
    path_handler.nm_walk(30, "LeftKey")
    path_handler.nm_walk(36, "FwdKey")
    path_handler.nm_walk(28, "LeftKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(3.5, "BackKey")
    path_handler.nm_walk(23.5, "LeftKey")
    path_handler.nm_walk(3, "BackKey")
    path_handler.nm_walk(10, "RightKey")
    path_handler.nm_walk(3, "LeftKey")
    path_handler.nm_walk(8, "BackKey")
    # dual path 230629 noobyguy


def gtc_treatdis(path_handler: PathHandler, move_method: str == "walk"::
    """
    Gtc-Treatdis path
    Converted from paths/gtc-treatdis.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(30, "FwdKey")
    path_handler.nm_walk(20, "FwdKey", "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(43.5, "FwdKey")
    path_handler.nm_walk(16, "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(800)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(29.25, "FwdKey")
    path_handler.nm_walk(17, "FwdKey", "LeftKey")
    path_handler.nm_walk(3, "FwdKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1810)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(1925)
    path_handler.send_key_sequence("{{")
    Sleep 1500
    # path 230630 noobyguy - walk updated


def gtc_WindShrine(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Windshrine path
    Converted from paths/gtc-WindShrine.ahk
    """
    path_handler.nm_gotoramp()
    Send "{space down}{" RightKey " down}"
    Sleep 100
    Send "{space up}"
    Walk(2)
    Send "{" FwdKey " down}"
    Walk(1.8)
    Send "{" FwdKey " up}"
    Walk(30)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(4, "RightKey")
    path_handler.nm_walk(5, "FwdKey")
    path_handler.nm_walk(3, "RightKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.nm_walk(2, "LeftKey", "FwdKey")
    path_handler.nm_walk(8, "FwdKey")
    Send "{" FwdKey " down}{" RightKey " down}"
    Walk(11)
    path_handler.send_key_sequence("{{space down}}{{")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    Walk(18)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(200)
    path_handler.nm_walk(21, "FwdKey", "RightKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(3, "FwdKey")
    path_handler.nm_walk(19.5, "RightKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(3, "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(200)
    # pepper
    path_handler.nm_walk(13, "FwdKey","RightKey")
    path_handler.nm_walk(10, "RightKey")
    path_handler.nm_walk(1, "LeftKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(120)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(130)
    path_handler.send_key_sequence("{{space up}}{{")
    path_handler.nm_walk(15, "RightKey")
    path_handler.hyper_sleep(300)


def gtc_wintermm(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Wintermm path
    Converted from paths/gtc-wintermm.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31.5, "FwdKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(9, "BackKey")
    path_handler.nm_walk(58.5, "LeftKey")
    path_handler.nm_walk(49.5, "FwdKey")
    path_handler.nm_walk(2.25, "BackKey", "LeftKey")
    path_handler.nm_walk(36, "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.send_key_sequence("{{")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(500)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    Walk(6)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(6, "RightKey")
    path_handler.nm_walk(42, "FwdKey")
    path_handler.send_key_sequence("{{")
    Walk(7)
    path_handler.send_key_sequence("{{space down}}")
    Sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    Walk(7)
    path_handler.send_key_sequence("{{space down}}")
    Sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    Walk(10)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(3.75, "RightKey")
    path_handler.nm_walk(6, "BackKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1150)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(4050)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{")
    Sleep 2200
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(14, "LeftKey")
    path_handler.nm_walk(4, "FwdKey", "LeftKey")
    path_handler.send_key_sequence("{{space down}}")
    Sleep 500
    path_handler.send_key_sequence("{{space up}}{{")
    Walk(8.5)
    path_handler.send_key_sequence("{{")


def gtc_wreath(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtc-Wreath path
    Converted from paths/gtc-wreath.ahk
    """
    nm_gotoramp()
    Send "{space down}{" RightKey " down}"
    Sleep 100
    Send "{space up}"
    Walk(2)
    Send "{" FwdKey " down}"
    Walk(1.8)
    Send "{" FwdKey " up}"
    path_handler.nm_walk(19, "RightKey")
    path_handler.nm_walk(2.5, "BackKey", "LeftKey")


def gtf_bamboo(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Bamboo path
    Converted from paths/gtf-bamboo.ahk
    """
    if MoveMethod == "Cannon": {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1250)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1200)
    path_handler.send_key_sequence("{{space}}{{")
    Sleep 2000
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(23.5, "FwdKey")
    path_handler.nm_walk(31.5, "FwdKey", "RightKey")
    path_handler.nm_walk(10, "RightKey")
    path_handler.send_key_sequence("{{")
    # walk path 230212 zaappiix - adjusted line 9 and line 13 delays
    # cannon path 230630 nooby - updated line 7 and 8


def gtf_blueflower(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Blueflower path
    Converted from paths/gtf-blueflower.ahk
    """
    if MoveMethod == "Cannon": {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(675)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2000)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1250)
    path_handler.send_key_sequence("{{space}}{{")
    Sleep 1000
    path_handler.nm_gotoramp()
    path_handler.nm_walk(86.875, "BackKey", "LeftKey")
    path_handler.nm_walk(28, "LeftKey")
    path_handler.send_key_sequence("{{")


def gtf_cactus(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Cactus path
    Converted from paths/gtf-cactus.ahk
    """
    if MoveMethod == "Cannon": {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(950)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(1700)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{space}}")
    Sleep 2000
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(7.8, "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.nm_walk(60, "LeftKey")
    path_handler.nm_walk(49.5, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(13.5, "LeftKey")
    # path 230630 noobyguy


def gtf_clover(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Clover path
    Converted from paths/gtf-clover.ahk
    """
    if MoveMethod == "Cannon": {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(525)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(1250)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1850)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{space}}")
    Sleep 1000
    path_handler.nm_gotoramp()
    path_handler.nm_walk(44.75, "BackKey", "LeftKey")
    path_handler.nm_walk(52.5, "LeftKey")
    path_handler.nm_walk(2.8, "BackKey", "RightKey")
    path_handler.nm_walk(6.7, "BackKey")
    path_handler.nm_walk(20.5, "LeftKey")
    path_handler.nm_walk(4.5, "FwdKey")
    # path 230212 zaappiix
    # path 230630 noobyguy - changed line 6, 7, 8


def gtf_coconut(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Coconut path
    Converted from paths/gtf-coconut.ahk
    """
    nm_gotoramp()
    Send "{space down}{" RightKey " down}"
    Sleep 100
    Send "{space up}"
    Walk(2)
    Send "{" FwdKey " down}"
    Walk(1.8)
    Send "{" FwdKey " up}"
    Walk(30)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(4, "RightKey")
    path_handler.nm_walk(5, "FwdKey")
    path_handler.nm_walk(3, "RightKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.nm_walk(2, "LeftKey", "FwdKey")
    path_handler.nm_walk(8, "FwdKey")
    Send "{" FwdKey " down}{" RightKey " down}"
    Walk(11)
    path_handler.send_key_sequence("{{space down}}{{")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    Walk(18)
    Send "{" FwdKey " up}"
    path_handler.nm_walk(13.5, "LeftKey")
    # path 230212 zaappiix


def gtf_dandelion(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Dandelion path
    Converted from paths/gtf-dandelion.ahk
    """
    nm_gotoramp()
    path_handler.nm_walk(39, "BackKey", "LeftKey")
    path_handler.nm_walk(14, "LeftKey")
    path_handler.send_key_sequence("{{")


def gtf_mountaintop(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Mountaintop path
    Converted from paths/gtf-mountaintop.ahk
    """
    if MoveMethod == "Cannon": {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1525)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(350)
    path_handler.send_key_sequence("{{")
    Sleep 1500
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(7.8, "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.nm_walk(60, "LeftKey")
    path_handler.nm_walk(3.75, "RightKey")
    path_handler.nm_walk(85, "FwdKey")
    path_handler.nm_walk(45, "RightKey")
    path_handler.nm_walk(50, "BackKey")
    path_handler.nm_walk(60, "RightKey")
    path_handler.nm_walk(15.75, "FwdKey", "LeftKey")
    path_handler.nm_walk(13.5, "FwdKey")
    path_handler.send_key_sequence("{{")
    # path 230630 noobyguy -added corneralign and tweaked slightly


def gtf_mushroom(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Mushroom path
    Converted from paths/gtf-mushroom.ahk
    """
    nm_gotoramp()
    path_handler.nm_walk(36, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31.5, "FwdKey")


def gtf_pepper(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Pepper path
    Converted from paths/gtf-pepper.ahk
    """
    nm_gotoramp()
    Send "{space down}{" RightKey " down}"
    Sleep 100
    Send "{space up}"
    Walk(2)
    Send "{" FwdKey " down}"
    Walk(1.8)
    Send "{" FwdKey " up}"
    Walk(30)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(4, "RightKey")
    path_handler.nm_walk(5, "FwdKey")
    path_handler.nm_walk(3, "RightKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.nm_walk(2, "LeftKey", "FwdKey")
    path_handler.nm_walk(8, "FwdKey")
    Send "{" FwdKey " down}{" RightKey " down}"
    Walk(11)
    path_handler.send_key_sequence("{{space down}}{{")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    Walk(18)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    Walk(20)
    Send "{" RightKey " down}"
    Walk(9)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    Walk(1)
    Send "{" FwdKey " up}"
    Walk(33)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    Walk(4)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(9, "FwdKey")
    path_handler.nm_walk(1.5, "RightKey")
    # path 230212 zaappiix


def gtf_pineapple(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Pineapple path
    Converted from paths/gtf-pineapple.ahk
    """
    if MoveMethod == "Cannon": {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1850)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2750)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1150)
    path_handler.send_key_sequence("{{")
    Sleep 2000
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(30, "FwdKey")
    path_handler.nm_walk(20, "FwdKey", "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(43.5, "FwdKey")
    path_handler.nm_walk(18, "RightKey")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(65.5, "FwdKey")
    path_handler.nm_walk(1.5, "RightKey")
    # path 230630 noobyguy


def gtf_pinetree(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Pinetree path
    Converted from paths/gtf-pinetree.ahk
    """
    if MoveMethod == "Cannon": {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(925)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(4500)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(500)
    path_handler.send_key_sequence("{{")
    Sleep 2000
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(7.8, "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.nm_walk(60, "LeftKey")
    path_handler.nm_walk(3.75, "RightKey")
    path_handler.nm_walk(38, "FwdKey")
    path_handler.nm_walk(33, "LeftKey", "FwdKey")
    # path 230630 noobyguy


def gtf_pumpkin(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Pumpkin path
    Converted from paths/gtf-pumpkin.ahk
    """
    if MoveMethod == "Cannon": {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(950)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2700)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(500)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(600)
    path_handler.send_key_sequence("{{space}}{{")
    Sleep 1500
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(7.8, "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.nm_walk(60, "LeftKey")
    path_handler.nm_walk(3.75, "RightKey")
    path_handler.nm_walk(38, "FwdKey")
    path_handler.nm_walk(18, "RightKey", "FwdKey")
    path_handler.nm_walk(10, "FwdKey")
    # path 230630 noobyguy


def gtf_rose(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Rose path
    Converted from paths/gtf-rose.ahk
    """
    if MoveMethod == "Cannon": {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(550)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2000)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{space}}{{")
    Sleep 1000
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(7.8, "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.nm_walk(60, "LeftKey")
    path_handler.nm_walk(3.75, "RightKey")
    path_handler.nm_walk(38, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(14, "RightKey")
    path_handler.nm_walk(15, "FwdKey", "LeftKey")
    path_handler.nm_walk(1, "BackKey")
    path_handler.hyper_sleep(200)
    path_handler.nm_walk(16, "RightKey")
    path_handler.nm_walk(49, "FwdKey")
    path_handler.send_key_sequence("{{")
    # path 230630 noobyguy


def gtf_spider(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Spider path
    Converted from paths/gtf-spider.ahk
    """
    if MoveMethod == "Cannon": {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1050)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{")
    Sleep 1500
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31.5, "FwdKey")
    path_handler.nm_walk(13, "LeftKey", "FwdKey")
    # path 230630 noobyguy adjusted line 7


def gtf_strawberry(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Strawberry path
    Converted from paths/gtf-strawberry.ahk
    """
    if MoveMethod == "Cannon": {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(700)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(1700)
    path_handler.send_key_sequence("{{")
    Sleep 2000
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(7, "FwdKey", "LeftKey")
    path_handler.nm_walk(33.25, "LeftKey")
    path_handler.nm_walk(6.75, "FwdKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    # path 230630 noobyguy adjusted line 7


def gtf_stump(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Stump path
    Converted from paths/gtf-stump.ahk
    """
    if MoveMethod == "Cannon": {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1850)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2750)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(900)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1650)
    path_handler.send_key_sequence("{{")
    Sleep 1000
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(30, "FwdKey")
    path_handler.nm_walk(20, "FwdKey", "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(43.5, "FwdKey")
    path_handler.nm_walk(18, "RightKey")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(43, "FwdKey")
    path_handler.nm_walk(30, "FwdKey", "RightKey")
    path_handler.nm_walk(24, "RightKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.send_key_sequence("{{")
    # path 230630 noobyguy


def gtf_sunflower(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtf-Sunflower path
    Converted from paths/gtf-sunflower.ahk
    """
    nm_gotoramp()
    path_handler.nm_walk(9, "BackKey")
    path_handler.nm_walk(6.75, "BackKey", "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(29, "RightKey")
    # path 230212 zaappiix


def gtp_bamboo(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Bamboo path
    Converted from paths/gtp-bamboo.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(23.5, "FwdKey")
    path_handler.nm_walk(31.5, "FwdKey", "RightKey")
    path_handler.nm_walk(10, "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(20, "FwdKey")
    path_handler.nm_walk(5, "FwdKey", "LeftKey")
    path_handler.nm_walk(7, "LeftKey")
    path_handler.nm_walk(1, "FwdKey")
    path_handler.nm_walk(8, "RightKey")
    path_handler.nm_walk(14, "BackKey")
    else {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(800)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(3000)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{")
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.nm_walk(20, "LeftKey")
    path_handler.nm_walk(30, "FwdKey")
    path_handler.nm_walk(8, "RightKey")
    path_handler.nm_walk(14, "BackKey")
    # path 230729 noobyguy


def gtp_blueflower(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Blueflower path
    Converted from paths/gtp-blueflower.ahk
    """
    if MoveMethod == "walk" : {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(88.875, "BackKey", "LeftKey")
    path_handler.nm_walk(27, "LeftKey")
    path_handler.hyper_sleep(50)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(17, "FwdKey")
    path_handler.nm_walk(17, "LeftKey")
    path_handler.nm_walk(18, "FwdKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(7, "BackKey", "RightKey")
    else {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(700)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(4450)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(19, "LeftKey")
    path_handler.nm_walk(18, "FwdKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(7, "BackKey", "RightKey")
    # path 230729 noobyguy


def gtp_cactus(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Cactus path
    Converted from paths/gtp-cactus.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(7.8, "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.nm_walk(60, "LeftKey")
    path_handler.nm_walk(49.5, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(35.5, "FwdKey")
    path_handler.nm_walk(3, "RightKey")
    path_handler.nm_walk(7, "BackKey")
    path_handler.send_key_sequence("{{")
    else {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(890)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2500)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(600)
    path_handler.nm_walk(15, "FwdKey", "RightKey")
    path_handler.nm_walk(22, "RightKey")
    path_handler.nm_walk(30, "BackKey")
    path_handler.nm_walk(7, "LeftKey")
    path_handler.send_key_sequence("{{")
    # path 230729 noobyguy


def gtp_clover(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Clover path
    Converted from paths/gtp-clover.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(44.75, "BackKey", "LeftKey")
    path_handler.nm_walk(52.5, "LeftKey")
    path_handler.nm_walk(2.8, "BackKey", "RightKey")
    path_handler.nm_walk(6.7, "BackKey")
    path_handler.nm_walk(25.5, "LeftKey")
    path_handler.nm_walk(35, "FwdKey", "LeftKey")
    path_handler.nm_walk(7, "BackKey", "RightKey")
    path_handler.nm_walk(12, "RightKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(525)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(1250)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(3850)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.nm_walk(10, "FwdKey", "LeftKey")
    path_handler.nm_walk(15, "LeftKey")
    path_handler.nm_walk(7, "FwdKey")
    path_handler.nm_walk(7, "BackKey", "RightKey")
    path_handler.nm_walk(12, "RightKey")
    # path 230729 noobyguy


def gtp_coconut(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Coconut path
    Converted from paths/gtp-coconut.ahk
    """
    nm_gotoramp()
    Send "{space down}{" RightKey " down}"
    Sleep 100
    Send "{space up}"
    Walk(2)
    Send "{" FwdKey " down}"
    Walk(1.8)
    Send "{" FwdKey " up}"
    Walk(30)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(4, "RightKey")
    path_handler.nm_walk(5, "FwdKey")
    path_handler.nm_walk(3, "RightKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(5, "FwdKey")
    path_handler.nm_walk(2, "LeftKey", "FwdKey")
    path_handler.nm_walk(8, "FwdKey")
    Send "{" FwdKey " down}{" RightKey " down}"
    Walk(11)
    path_handler.send_key_sequence("{{space down}}{{")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    Walk(18)
    Send "{" FwdKey " up}"
    path_handler.nm_walk(7, "LeftKey")
    # path 230212 zaappiix


def gtp_dandelion(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Dandelion path
    Converted from paths/gtp-dandelion.ahk
    """
    nm_gotoramp()
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(39, "BackKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(51, "FwdKey")
    path_handler.nm_walk(15, "BackKey")


def gtp_mountaintop(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Mountaintop path
    Converted from paths/gtp-mountaintop.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(7.8, "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.nm_walk(60, "LeftKey")
    path_handler.nm_walk(3.75, "RightKey")
    path_handler.nm_walk(85, "FwdKey")
    path_handler.nm_walk(45, "RightKey")
    path_handler.nm_walk(50, "BackKey")
    path_handler.nm_walk(60, "RightKey")
    path_handler.nm_walk(5, "LeftKey")
    path_handler.nm_walk(7, "FwdKey")
    path_handler.nm_walk(9, "FwdKey", "LeftKey")
    path_handler.nm_walk(16.5, "FwdKey")
    path_handler.send_key_sequence("{{")
    else {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}")
    Sleep 2750
    # path 230729 noobyguy


def gtp_mushroom(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Mushroom path
    Converted from paths/gtp-mushroom.ahk
    """
    nm_gotoramp()
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(200)
    path_handler.nm_walk(55.75, "FwdKey", "RightKey")
    path_handler.nm_walk(26.5, "FwdKey")
    path_handler.nm_walk(10, "FwdKey", "RightKey")
    path_handler.nm_walk(5, "LeftKey")
    # path 230729 noobyguy


def gtp_pepper(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Pepper path
    Converted from paths/gtp-pepper.ahk
    """
    nm_gotoramp()
    Send "{space down}{" RightKey " down}"
    Sleep 100
    Send "{space up}"
    Walk(2)
    Send "{" FwdKey " down}"
    Walk(1.8)
    Send "{" FwdKey " up}"
    Walk(30)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(4, "RightKey")
    path_handler.nm_walk(5, "FwdKey")
    path_handler.nm_walk(3, "RightKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.nm_walk(2, "LeftKey", "FwdKey")
    path_handler.nm_walk(8, "FwdKey")
    Send "{" FwdKey " down}{" RightKey " down}"
    Walk(11)
    path_handler.send_key_sequence("{{space down}}{{")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    Walk(18)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    Walk(20)
    Send "{" RightKey " down}"
    Walk(9)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    Walk(1)
    Send "{" FwdKey " up}"
    Walk(33)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    Walk(6)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(30, "FwdKey")
    Send "{" RightKey " up}"
    path_handler.nm_walk(10, "FwdKey")
    path_handler.nm_walk(10, "BackKey", "LeftKey")
    path_handler.nm_walk(4, "BackKey")
    # path 230212 zaappiix


def gtp_pineapple(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Pineapple path
    Converted from paths/gtp-pineapple.ahk
    """
    If (HiveBees >= 25) && (MoveMethod = "cannon")
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}")
    path_handler.hyper_sleep(500)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{space}}")
    path_handler.hyper_sleep(500)
    path_handler.send_key_sequence("{{space}}")
    path_handler.hyper_sleep(2900)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1600)
    path_handler.send_key_sequence("{{space}}")
    path_handler.hyper_sleep(1000)
    path_handler.nm_walk(14, "FwdKey", "LeftKey")
    path_handler.nm_walk(10, "FwdKey")
    path_handler.nm_walk(7, "BackKey", "RightKey")
    else {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(30, "FwdKey")
    path_handler.nm_walk(20, "FwdKey", "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(43.5, "FwdKey")
    path_handler.nm_walk(18, "RightKey")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(66, "FwdKey")
    path_handler.nm_walk(19, "FwdKey", "LeftKey")
    path_handler.nm_walk(7, "BackKey", "RightKey")
    # path 230212 zaappiix
    # path 230729 noobyguy: If (HiveBees < 25) && (MoveMethod = "cannon") & walk path
    # path ferox7274: cannon path


def gtp_pinetree(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Pinetree path
    Converted from paths/gtp-pinetree.ahk
    """
    If (MoveMethod = "walk")
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(7.8, "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.nm_walk(60, "LeftKey")
    path_handler.nm_walk(3.75, "RightKey")
    path_handler.nm_walk(45, "FwdKey")
    path_handler.nm_walk(47, "LeftKey", "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(9, "RightKey")
    path_handler.nm_walk(9, "FwdKey")
    nm_walk(16, LeftKey)
    nm_walk(5, BackKey)
    path_handler.send_key_sequence("{{")
    else {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(925)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(5000)
    path_handler.send_key_sequence("{{")
    Sleep 1000
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.send_key_sequence("{{space}}")
    path_handler.hyper_sleep(2000)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(15, "RightKey")
    path_handler.nm_walk(15, "FwdKey")
    nm_walk(16, LeftKey)
    nm_walk(5, BackKey)
    path_handler.send_key_sequence("{{")
    # path 230212 zaappiix
    # path 230729 noobyguy


def gtp_pumpkin(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Pumpkin path
    Converted from paths/gtp-pumpkin.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(7.8, "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.nm_walk(60, "LeftKey")
    path_handler.nm_walk(3.75, "RightKey")
    path_handler.nm_walk(45, "FwdKey")
    path_handler.nm_walk(34, "RightKey", "FwdKey")
    path_handler.nm_walk(10, "RightKey")
    path_handler.nm_walk(12, "LeftKey")
    path_handler.nm_walk(3, "BackKey")
    else {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(890)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2500)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(600)
    path_handler.nm_walk(15, "FwdKey")
    path_handler.nm_walk(24, "RightKey")
    path_handler.nm_walk(12, "LeftKey")
    path_handler.nm_walk(3, "BackKey")
    # path 230729 noobyguy


def gtp_rose(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Rose path
    Converted from paths/gtp-rose.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(7.8, "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(1.5, "FwdKey")
    path_handler.nm_walk(60, "LeftKey")
    path_handler.nm_walk(3.75, "RightKey")
    path_handler.nm_walk(38, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(14, "RightKey")
    path_handler.nm_walk(15, "FwdKey", "LeftKey")
    path_handler.nm_walk(1, "BackKey")
    path_handler.hyper_sleep(200)
    path_handler.nm_walk(16, "RightKey")
    path_handler.nm_walk(49, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(10, "RightKey")
    path_handler.nm_walk(12, "RightKey", "FwdKey")
    path_handler.nm_walk(7, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    else {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(550)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2500)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.nm_walk(17, "FwdKey")
    path_handler.nm_walk(10, "RightKey")
    path_handler.nm_walk(8, "FwdKey", "RightKey")
    path_handler.nm_walk(8, "FwdKey")
    path_handler.nm_walk(7, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    # path 230729 noobyguy


def gtp_spider(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Spider path
    Converted from paths/gtp-spider.ahk
    """
    if MoveMethod == "walk": {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(37.5, "FwdKey")
    path_handler.nm_walk(38, "LeftKey", "FwdKey")
    path_handler.nm_walk(9, "BackKey", "RightKey")
    else {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1050)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{")
    Sleep 1500
    path_handler.nm_walk(20, "FwdKey")
    path_handler.nm_walk(10, "FwdKey", "LeftKey")
    path_handler.nm_walk(10, "LeftKey")
    path_handler.nm_walk(9, "BackKey", "RightKey")
    # path 230729 noobyguy


def gtp_strawberry(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Strawberry path
    Converted from paths/gtp-strawberry.ahk
    """
    if MoveMethod == "walk": {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(7, "FwdKey", "LeftKey")
    path_handler.nm_walk(30.25, "LeftKey")
    path_handler.nm_walk(30, "FwdKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(10, "BackKey", "LeftKey")
    else {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(750)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(800)
    path_handler.send_key_sequence("{{space}}{{")
    Sleep 2000
    path_handler.nm_walk(10, "FwdKey", "RightKey")
    path_handler.nm_walk(15, "RightKey")
    path_handler.nm_walk(15, "FwdKey")
    path_handler.nm_walk(10, "BackKey", "LeftKey")
    # path 230729 noobyguy


def gtp_stump(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Stump path
    Converted from paths/gtp-stump.ahk
    """
    If (HiveBees >= 25) && (MoveMethod = "cannon") {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1800)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(2750)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(900)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1500)
    path_handler.send_key_sequence("{{")
    Sleep 1000
    else {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(30, "FwdKey")
    path_handler.nm_walk(20, "FwdKey", "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(43.5, "FwdKey")
    path_handler.nm_walk(18, "RightKey")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(43, "FwdKey")
    path_handler.nm_walk(30, "FwdKey", "RightKey")
    path_handler.nm_walk(50, "RightKey")
    path_handler.nm_walk(14, Backkey, "LeftKey")
    path_handler.nm_walk(10, "LeftKey")
    path_handler.send_key_sequence("{{")


def gtp_sunflower(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtp-Sunflower path
    Converted from paths/gtp-sunflower.ahk
    """
    nm_gotoramp()
    path_handler.nm_walk(14, "BackKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(25, "RightKey")
    path_handler.nm_walk(15, "FwdKey")
    path_handler.nm_walk(9, "BackKey")
    path_handler.send_key_sequence("{{")


def gtq_black(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtq-Black path
    Converted from paths/gtq-black.ahk
    """
    nm_gotoramp()
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(13.5, "RightKey")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.nm_walk(6, "BackKey")


def gtq_brown(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtq-Brown path
    Converted from paths/gtq-brown.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(44.75, "BackKey", "LeftKey")
    path_handler.nm_walk(42.5, "LeftKey")
    path_handler.nm_walk(8.5, "BackKey")
    path_handler.nm_walk(22.5, "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(40, "FwdKey")
    path_handler.nm_walk(1.2, "BackKey")
    path_handler.nm_walk(15, "RightKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    Send "{e down}"
    path_handler.hyper_sleep(100)
    Send "{e up}{" FwdKey " down}{" LeftKey " down}"
    path_handler.hyper_sleep(1500)
    path_handler.send_key_sequence("{{space 2}}")
    Sleep 8000
    Send "{" FwdKey " up}{" LeftKey " up}"
    path_handler.nm_walk(20, "RightKey")
    path_handler.nm_walk(8, "LeftKey")
    path_handler.nm_walk(3, "RightKey", "BackKey")
    path_handler.nm_walk(2, "BackKey")


def gtq_bucko(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtq-Bucko path
    Converted from paths/gtq-bucko.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(88.875, "BackKey", "LeftKey")
    path_handler.nm_walk(27, "LeftKey")
    path_handler.hyper_sleep(50)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(50)
    path_handler.nm_walk(50, "FwdKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(700)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(4450)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(4, "BackKey", "LeftKey")
    path_handler.nm_walk(8, "FwdKey", "LeftKey")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.nm_walk(5, "BackKey")
    path_handler.nm_walk(8, "RightKey")
    # inside
    path_handler.nm_walk(30, "FwdKey")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.nm_walk(5, "RightKey")
    path_handler.nm_walk(9, "RightKey", "BackKey")
    path_handler.nm_walk(4, "RightKey")
    path_handler.nm_walk(2, "LeftKey")
    path_handler.nm_walk(28, "BackKey")
    path_handler.nm_walk(1.75, "FwdKey")
    path_handler.nm_walk(9.5, "LeftKey")
    path_handler.nm_walk(6.5, "FwdKey")
    sleep 100
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.nm_walk(5, "FwdKey")
    # path 230630 noobyguy


def gtq_honey(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtq-Honey path
    Converted from paths/gtq-honey.ahk
    """
    if MoveMethod == "walk":
    {
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31.5, "FwdKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(9, "BackKey")
    path_handler.nm_walk(58.5, "LeftKey")
    path_handler.nm_walk(49.5, "FwdKey")
    path_handler.nm_walk(2.25, "BackKey", "LeftKey")
    path_handler.nm_walk(36, "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.send_key_sequence("{{")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(500)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(300)
    path_handler.send_key_sequence("{{space up}}")
    Walk(6)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(6, "RightKey")
    path_handler.nm_walk(7, "FwdKey")
    path_handler.nm_walk(6, "LeftKey")
    path_handler.nm_walk(3, "RightKey")
    path_handler.nm_walk(32, "FwdKey")
    path_handler.nm_walk(8.5, "BackKey")
    else:
    {
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(1150)
    path_handler.send_key_sequence("{{space 2}}")
    path_handler.hyper_sleep(4050)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(1000)
    path_handler.send_key_sequence("{{")
    Sleep 2200
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(14, "LeftKey")
    path_handler.nm_walk(4, "FwdKey")
    path_handler.nm_walk(3, "BackKey")
    path_handler.nm_walk(11, "RightKey")


def gtq_polar(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtq-Polar path
    Converted from paths/gtq-polar.ahk
    """
    if MoveMethod == "walk":{
    path_handler.nm_gotoramp()
    path_handler.nm_walk(67.5, "BackKey", "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(31.5, "FwdKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(9, "BackKey")
    path_handler.nm_walk(58.5, "LeftKey")
    path_handler.nm_walk(49.5, "FwdKey")
    path_handler.nm_walk(3.375, "LeftKey")
    path_handler.nm_walk(36, "FwdKey")
    path_handler.nm_walk(60, "RightKey")
    path_handler.nm_walk(60, "BackKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(9, "FwdKey")
    path_handler.nm_gotoramp()
    path_handler.nm_gotocannon()
    path_handler.send_key_sequence("{{")
    sleep 100
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}{{")
    path_handler.hyper_sleep(800)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(2100)
    path_handler.send_key_sequence("{{space}}")
    sleep 1000
    path_handler.nm_walk(7, "BackKey", "LeftKey")
    path_handler.nm_walk(9, "LeftKey", "FwdKey")
    path_handler.nm_walk(5, "FwdKey")
    path_handler.nm_walk(5, "BackKey")
    path_handler.nm_walk(2, "RightKey")


def gtq_riley(path_handler: PathHandler, move_method: str = "walk"):
    """
    Gtq-Riley path
    Converted from paths/gtq-riley.ahk
    """
    nm_gotoramp()
    send("{" SC_Space " down}"), sleep(100)
    send("{" SC_Space " up}")
    path_handler.nm_walk(2, "RightKey")
    path_handler.nm_walk(1.8, "FwdKey", "RightKey")
    path_handler.nm_walk(32, "RightKey")
    send("{" SC_Space " down}"), HyperSleep(300)
    send("{" SC_Space " up}")
    path_handler.nm_walk(2, "RightKey")
    path_handler.nm_walk(6, "RightKey", "FwdKey")
    path_handler.nm_walk(3, "RightKey")
    send("{" RotRight " 2}"), Sleep(100)
    path_handler.send_key_sequence("{{")
    send("{" SC_Space " down}"), HyperSleep(300)
    path_handler.send_key_sequence("{{")
    send("{" SC_Space " up}")
    path_handler.nm_walk(2, "FwdKey")
    send("{" SC_Space " down}{" Rightkey " down}"), HyperSleep(100)
    send("{" SC_Space " up}"), HyperSleep(100)
    send("{" SC_Space " down}"),HyperSleep(100), send("{" SC_Space " up}"), HyperSleep(100)
    path_handler.send_key_sequence("{{space}}{{")
    sleep 100
    path_handler.send_key_sequence("{{space up}}")
    sleep 1000
    path_handler.nm_walk(1, "FwdKey", "RightKey")
    path_handler.nm_walk(20, "RightKey")
    path_handler.nm_walk(2, "FwdKey")
    path_handler.nm_walk(12, "FwdKey", "RightKey")
    path_handler.nm_walk(10, "FwdKey")
    path_handler.nm_walk(6, "BackKey")
    send("{" RotRight " 2}"), Sleep(100)
    path_handler.nm_walk(5, "FwdKey")
    sleep 100
    send("{" SC_Space " down}"), HyperSleep(300)
    send("{" SC_Space " up}"), nm_Walk(6, FwdKey)
    sleep 300
    # 12/23/2024 - dully176 - Reworked Path.


def wf_bamboo(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Bamboo path
    Converted from paths/wf-bamboo.ahk
    """
    nm_Walk(16, LeftKey)
    path_handler.nm_walk(5, "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(75, "RightKey")
    path_handler.nm_walk(64, "FwdKey")
    path_handler.nm_walk(5.5, "FwdKey", "RightKey")
    path_handler.nm_walk(36, "FwdKey")
    switch HiveSlot
    {
    case 3:
    path_handler.nm_walk(2.7, "BackKey")
    default:
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # path 230212 zaappiix
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
    # [2024-01-15/rpertusio] Aligns with default SpawnLocation, saves walking if player chose Hive 3


def wf_blueflower(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Blueflower path
    Converted from paths/wf-blueflower.ahk
    """
    send "{" RotRight " 2}"
    path_handler.nm_walk(13.5, "FwdKey")
    path_handler.nm_walk(4.5, "BackKey")
    path_handler.nm_walk(46, "RightKey")
    path_handler.nm_walk(40.5, "FwdKey")
    path_handler.nm_walk(33.5, "RightKey")
    path_handler.nm_walk(27, "FwdKey")
    switch HiveSlot
    {
    case 3:
    path_handler.nm_walk(2.7, "BackKey")
    default:
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
    # [2024-01-15/rpertusio] Aligns with default SpawnLocation, saves walking if player chose Hive 3


def wf_cactus(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Cactus path
    Converted from paths/wf-cactus.ahk
    """
    nm_Walk(8, BackKey)
    path_handler.nm_walk(10, "LeftKey", "BackKey")
    path_handler.nm_walk(14.5, "BackKey")
    path_handler.nm_walk(28, "LeftKey")
    path_handler.nm_walk(36, "FwdKey")
    path_handler.nm_walk(3, "RightKey")
    path_handler.nm_walk(4, "FwdKey")
    path_handler.nm_walk(4, "LeftKey")
    path_handler.nm_walk(27, "FwdKey")
    path_handler.nm_walk(2.75, "FwdKey", "LeftKey")
    path_handler.nm_walk(90, "FwdKey")
    switch HiveSlot
    {
    case 3:
    path_handler.nm_walk(2.7, "BackKey")
    default:
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
    # [2024-01-15/rpertusio] Aligns with default SpawnLocation, saves walking if player chose Hive 3


def wf_clover(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Clover path
    Converted from paths/wf-clover.ahk
    """
    nm_Walk(18, FwdKey)
    path_handler.nm_walk(36, "RightKey")
    path_handler.nm_walk(4.5, "BackKey")
    path_handler.nm_walk(50.5, "RightKey")
    path_handler.nm_walk(36, "FwdKey")
    switch HiveSlot
    {
    case 3:
    path_handler.nm_walk(2.7, "BackKey")
    default:
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
    # [2024-01-15/rpertusio] Aligns with default SpawnLocation, saves walking if player chose Hive 3


def wf_coconut(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Coconut path
    Converted from paths/wf-coconut.ahk
    """
    nm_Walk(20.25, RightKey)
    path_handler.send_key_sequence("{{")
    Walk(22.5)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(50)
    path_handler.send_key_sequence("{{space up}}")
    Walk(31.5)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(33.75, "LeftKey")
    path_handler.nm_walk(13.5, "FwdKey")
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(10, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update


def wf_dandelion(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Dandelion path
    Converted from paths/wf-dandelion.ahk
    """
    send "{" RotRight " 2}"
    path_handler.nm_walk(13.5, "FwdKey")
    path_handler.nm_walk(42, "RightKey")
    path_handler.nm_walk(28, "FwdKey")
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
    # [2024-01-15/rpertusio] Aligns with default SpawnLocation, saves walking if player chose Hive 3
    # [2024-02-08/misc] Modified to improve compatibility with variable return path start locations, e.g. planter


def wf_mountaintop(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Mountaintop path
    Converted from paths/wf-mountaintop.ahk
    """
    Loop 15
    {
    path_handler.nm_walk(3, "BackKey")
    path_handler.nm_walk(1, "LeftKey")
    path_handler.nm_walk(36, "FwdKey", "RightKey")
    path_handler.nm_walk(100, "FwdKey")
    path_handler.nm_walk(32, "RightKey")
    path_handler.nm_walk(37, "FwdKey")
    switch HiveSlot
    {
    case 3:
    path_handler.nm_walk(2.7, "BackKey")
    default:
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
    # [2024-01-15/rpertusio] Aligns with default SpawnLocation, saves walking if player chose Hive 3


def wf_mushroom(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Mushroom path
    Converted from paths/wf-mushroom.ahk
    """
    nm_Walk(13.5, FwdKey)   ;move to rear of mushroom field
    path_handler.nm_walk(27, "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(11.5, "LeftKey")
    path_handler.nm_walk(72, "FwdKey")
    switch HiveSlot
    {
    case 3:
    path_handler.nm_walk(2.7, "BackKey")
    default:
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
    # [2024-01-15/rpertusio] Aligns with default SpawnLocation, saves walking if player chose Hive 3


def wf_pepper(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Pepper path
    Converted from paths/wf-pepper.ahk
    """
    nm_Walk(42, RightKey)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(45, "FwdKey")
    path_handler.nm_walk(50, "LeftKey")
    path_handler.nm_walk(49, "FwdKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(13.5, "FwdKey")
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(10, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
    # [2024-01-15/rpertusio] Updated camera angle to 'follow' user to hive, less disorienting


def wf_pineapple(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Pineapple path
    Converted from paths/wf-pineapple.ahk
    """
    nm_Walk(18, FwdKey)
    path_handler.nm_walk(31.5, "RightKey")
    path_handler.nm_walk(4, "LeftKey")
    path_handler.nm_walk(10, "BackKey")
    path_handler.nm_walk(4, "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(60, "FwdKey")
    path_handler.nm_walk(5.5, "BackKey")
    path_handler.nm_walk(10, "RightKey")
    if HiveBees < 12) {
    path_handler.nm_walk(12, "FwdKey")
    path_handler.nm_walk(8, "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.send_key_sequence("{{")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.send_key_sequence("{{")
    nm_walk(30, FwdKey)
    nm_walk(3, BackKey)
    path_handler.send_key_sequence("{{")
    nm_walk(30, FwdKey)
    path_handler.nm_walk(4.5, "BackKey")
    path_handler.nm_walk(40.5, "RightKey")
    path_handler.nm_walk(40.5, "FwdKey")
    path_handler.nm_walk(34.5, "RightKey")
    path_handler.nm_walk(27, "FwdKey")
    else {
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(50)
    path_handler.send_key_sequence("{{space up}}")
    nm_walk(4, rightkey)
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}")
    path_handler.hyper_sleep(3000)
    path_handler.nm_walk(34, "FwdKey")
    switch HiveSlot
    {
    case 3:
    path_handler.nm_walk(2.7, "BackKey")
    default:
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # added walk path if <12 bees, misc 17/11/23
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
    # [2024-01-15/rpertusio] Aligns with default SpawnLocation, saves walking if player chose Hive 3


def wf_pinetree(path_handler: PathHandler, move_method: str == "walk"::
    """
    Wf-Pinetree path
    Converted from paths/wf-pinetree.ahk
    """
    If ((HiveBees < 25) || (MoveMethod = "Walk")) {
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(75, "RightKey")
    path_handler.send_key_sequence("{{")
    Sleep(50)
    path_handler.nm_walk(20, "FwdKey")
    path_handler.nm_walk(3, "FwdKey", "LeftKey")
    path_handler.nm_walk(18, "FwdKey")
    path_handler.nm_walk(6, "FwdKey", "RightKey")
    path_handler.nm_walk(10, "RightKey")
    path_handler.nm_walk(2, "LeftKey")
    path_handler.send_key_sequence("{{")
    Walk(6)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{")
    Walk(108)
    path_handler.send_key_sequence("{{")
    switch HiveSlot
    {
    case 3:
    path_handler.nm_walk(2.7, "BackKey")
    default:
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    else {
    path_handler.nm_walk(31, "FwdKey")
    path_handler.nm_walk(75, "RightKey")
    path_handler.send_key_sequence("{{")
    Sleep(50)
    path_handler.nm_walk(20, "FwdKey")
    path_handler.nm_walk(3, "FwdKey", "LeftKey")
    path_handler.nm_walk(18, "FwdKey")
    path_handler.nm_walk(6, "FwdKey", "RightKey")
    path_handler.nm_walk(10, "RightKey")
    path_handler.nm_walk(2, "LeftKey")
    path_handler.send_key_sequence("{{")
    Walk(6)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(3000)
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(2600)
    path_handler.nm_walk(15, "FwdKey")
    switch HiveSlot
    {
    case 3:
    path_handler.nm_walk(2.7, "BackKey")
    default:
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # added MoveMethod condition to no-glider option misc 181123
    # slightly altered tile measurements and optimised glider deployment SP 230405
    # path with and without glider zaappiix 230212
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
    # [2024-01-15/rpertusio] Aligns with default SpawnLocation, saves walking if player chose Hive 3


def wf_pumpkin(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Pumpkin path
    Converted from paths/wf-pumpkin.ahk
    """
    nm_Walk(9, RightKey)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(9, "BackKey")
    path_handler.send_key_sequence("{{")
    path_handler.send_key_sequence("{{")
    path_handler.hyper_sleep(2000)
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.hyper_sleep(2000)
    path_handler.send_key_sequence("{{")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(36, "FwdKey")
    path_handler.nm_walk(4.5, "FwdKey", "RightKey")
    path_handler.nm_walk(4.5, "FwdKey", "LeftKey")
    path_handler.nm_walk(27, "FwdKey")
    path_handler.nm_walk(3, "FwdKey", "LeftKey")
    path_handler.nm_walk(85.5, "FwdKey")
    switch HiveSlot
    {
    case 3:
    path_handler.nm_walk(2.7, "BackKey")
    default:
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
    # [2024-01-15/rpertusio] Aligns with default SpawnLocation, saves walking if player chose Hive 3


def wf_rose(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Rose path
    Converted from paths/wf-rose.ahk
    """
    nm_Walk(12, FwdKey)
    path_handler.nm_walk(20, "LeftKey")
    path_handler.nm_walk(8, "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(35, "LeftKey")
    path_handler.nm_walk(41, "FwdKey")
    path_handler.nm_walk(9, "LeftKey")
    path_handler.nm_walk(28, "FwdKey")
    path_handler.nm_walk(8, "LeftKey")
    path_handler.nm_walk(6, "FwdKey", "LeftKey")
    path_handler.nm_walk(6, "FwdKey")
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # path 230212 zaappiix
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update


def wf_spider(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Spider path
    Converted from paths/wf-spider.ahk
    """
    nm_Walk(22.5, FwdKey)
    path_handler.nm_walk(27, "LeftKey")
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(64, "FwdKey")
    path_handler.nm_walk(5.5, "FwdKey", "RightKey")
    path_handler.nm_walk(36, "FwdKey")
    switch HiveSlot
    {
    case 3:
    path_handler.nm_walk(2.7, "BackKey")
    default:
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
    # [2024-01-15/rpertusio] Aligns with default SpawnLocation, saves walking if player chose Hive 3


def wf_strawberry(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Strawberry path
    Converted from paths/wf-strawberry.ahk
    """
    Send "{" RotLeft " 2}"
    path_handler.nm_walk(12, "BackKey")
    path_handler.nm_walk(15, "BackKey", "LeftKey")
    path_handler.nm_walk(18, "LeftKey")
    path_handler.nm_walk(15, "FwdKey")
    path_handler.nm_walk(6, "LeftKey")
    path_handler.nm_walk(95, "FwdKey")
    switch HiveSlot
    {
    case 3:
    path_handler.nm_walk(2.7, "BackKey")
    default:
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # zaappiix 230203
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
    # [2024-01-15/rpertusio] No longer uses the Instant Converter corner to align
    # [2024-01-15/rpertusio] Aligns with default SpawnLocation, saves walking if player chose Hive 3


def wf_stump(path_handler: PathHandler, move_method: str = "walk"):
    """
    Wf-Stump path
    Converted from paths/wf-stump.ahk
    """
    nm_Walk(40.5, RightKey)
    path_handler.send_key_sequence("{{")
    path_handler.nm_walk(22.5, "RightKey")
    path_handler.nm_walk(22.5, "BackKey")
    path_handler.nm_walk(13, "RightKey")
    path_handler.nm_walk(40.5, "FwdKey")
    path_handler.nm_walk(5.5, "BackKey")
    path_handler.nm_walk(10, "RightKey")
    if HiveBees < 12) { ;walk
    path_handler.nm_walk(12, "FwdKey")
    path_handler.nm_walk(8, "RightKey")
    path_handler.send_key_sequence("{{")
    path_handler.send_key_sequence("{{")
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(200)
    path_handler.send_key_sequence("{{space up}}")
    path_handler.send_key_sequence("{{")
    nm_walk(30, FwdKey)
    nm_walk(3, BackKey)
    path_handler.send_key_sequence("{{")
    nm_walk(30, FwdKey)
    path_handler.nm_walk(4.5, "BackKey")
    path_handler.nm_walk(40.5, "RightKey")
    path_handler.nm_walk(40.5, "FwdKey")
    path_handler.nm_walk(34.5, "RightKey")
    path_handler.nm_walk(27, "FwdKey")
    else { ;use yellow cannon
    path_handler.send_key_sequence("{{space down}}")
    path_handler.hyper_sleep(50)
    path_handler.send_key_sequence("{{space up}}")
    nm_walk(4, rightkey)
    path_handler.hyper_sleep(1100)
    path_handler.send_key_sequence("{{e down}}")
    path_handler.hyper_sleep(100)
    path_handler.send_key_sequence("{{e up}}")
    path_handler.hyper_sleep(3000)
    path_handler.nm_walk(34, "FwdKey")
    switch HiveSlot
    {
    case 3:
    path_handler.nm_walk(2.7, "BackKey")
    default:
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(35, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
    # [2024-01-15/rpertusio] Now can walk without yellow cannon if < 12 bees
    # [2024-01-15/rpertusio] Aligns with default SpawnLocation, saves walking if player chose Hive 3


def wf_sunflower(path_handler: PathHandler, move_method: str == "walk"::
    """
    Wf-Sunflower path
    Converted from paths/wf-sunflower.ahk
    """
    send "{" RotLeft " 2}"
    path_handler.nm_walk(13.5, "RightKey")
    path_handler.nm_walk(45, "FwdKey")
    path_handler.nm_walk(2.25, "BackKey")
    path_handler.nm_walk(25, "FwdKey", "LeftKey")
    path_handler.nm_walk(13.5, "FwdKey")
    path_handler.nm_walk(1.5, "BackKey")
    path_handler.nm_walk(10, "RightKey")
    path_handler.nm_walk(2.7, "BackKey")
    # [2024-01-15/rpertusio] Avoid using corner (Hive 1 and ramp) where character gets stuck after 2024-01-12 BSS update
