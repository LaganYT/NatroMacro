"""
Movement and walking system for Natro Macro
Equivalent to lib/Walk.ahk (simplified version)
"""

import time
import logging
from typing import Optional, Tuple

logger = logging.getLogger(__name__)


class WalkSystem:
    """Handles player movement with buff detection"""

    def __init__(self, macro_instance):
        self.macro = macro_instance
        self.image_search = macro_instance.image_search
        self.roblox = macro_instance.roblox

        # Movement speed modifiers (simplified)
        self.base_movespeed = 16.0  # studs per second
        self.hasty_guard = False
        self.gifted_hasty = False

        # Buff detection cache
        self.last_buff_check = 0
        self.cached_buffs = {}

    def walk(self, tiles: float, haste_cap: int = 0):
        """
        Walk a specified number of tiles with haste compensation
        Equivalent to Walk()

        Args:
            tiles: Number of tiles to walk
            haste_cap: Haste cap value
        """
        try:
            # Calculate target distance in studs (4 studs per tile)
            target_distance = tiles * 4

            # Get current movement speed
            start_time = time.perf_counter()
            current_speed = self.detect_movespeed(haste_cap)

            # Calculate movement time
            if current_speed > 0:
                move_time = target_distance / current_speed
            else:
                move_time = target_distance / self.base_movespeed  # fallback

            logger.debug(f"Walking {tiles} tiles ({target_distance} studs) at {current_speed} studs/sec for {move_time:.2f}s")

            # Continue monitoring speed during movement
            elapsed = 0
            while elapsed < move_time:
                remaining_time = move_time - elapsed
                remaining_distance = remaining_time * current_speed

                # Update speed every 0.5 seconds
                if elapsed % 0.5 < 0.1:
                    new_speed = self.detect_movespeed(haste_cap)
                    if new_speed > 0:
                        current_speed = new_speed
                        # Recalculate remaining time with new speed
                        move_time = elapsed + (remaining_distance / current_speed)

                time.sleep(0.1)
                elapsed = time.perf_counter() - start_time

        except Exception as e:
            logger.error(f"Error in walk: {e}")

    def detect_movespeed(self, haste_cap: int = 0) -> float:
        """
        Detect current movement speed based on active buffs
        Equivalent to DetectMovespeed()

        Args:
            haste_cap: Haste cap value

        Returns:
            Current movement speed in studs per second
        """
        try:
            # Check Roblox window
            if not self.roblox.get_roblox_client_pos():
                logger.warning("Cannot detect movement speed - Roblox window not found")
                return 0

            # Throttle buff checks to avoid excessive CPU usage
            current_time = time.time()
            if current_time - self.last_buff_check < 0.5:  # Check every 500ms
                return self.cached_buffs.get('speed', self.base_movespeed)

            self.last_buff_check = current_time

            # Detect active buffs
            buffs = self._detect_active_buffs()

            # Calculate movement speed
            speed = self._calculate_movespeed_from_buffs(buffs, haste_cap)

            # Cache result
            self.cached_buffs = buffs
            self.cached_buffs['speed'] = speed

            return speed

        except Exception as e:
            logger.error(f"Error detecting movement speed: {e}")
            return self.base_movespeed

    def _detect_active_buffs(self) -> dict:
        """
        Detect currently active movement buffs
        This is a simplified version - full implementation would use image search
        """
        buffs = {
            'haste': 0,  # Number of haste stacks
            'coconut_haste': False,
            'haste_plus': False,
            'oil': False,
            'smoothie': False,
            'bear': False
        }

        try:
            # This would be the full image search implementation
            # For now, return default values (no buffs active)
            # TODO: Implement full buff detection using image search

            # Example of what the full implementation would do:
            # - Take screenshot of buff area
            # - Search for haste icons
            # - Detect haste stacks by analyzing numbers
            # - Check for other buff icons

            return buffs

        except Exception as e:
            logger.error(f"Error detecting buffs: {e}")
            return buffs

    def _calculate_movespeed_from_buffs(self, buffs: dict, haste_cap: int) -> float:
        """
        Calculate movement speed based on detected buffs
        Equivalent to the formula in DetectMovespeed()
        """
        try:
            base_speed = self.base_movespeed

            # Apply buff modifiers
            coconut_bonus = 10 if buffs.get('coconut_haste', False) else 0
            bear_bonus = 4 if buffs.get('bear', False) else 0

            # Hasty Guard and Gifted Hasty modifiers
            hasty_guard_mult = 1.1 if self.hasty_guard else 1.0
            gifted_hasty_mult = 1.15 if self.gifted_hasty else 1.0

            # Haste stacks (with cap consideration)
            haste_stacks = buffs.get('haste', 0)
            if haste_cap > 0:
                # No haste compensation up to cap, then 100% after
                haste_mult = 1.0 + max(0, haste_stacks - haste_cap) * 0.1
            else:
                haste_mult = 1.0 + haste_stacks * 0.1

            # Special buffs
            haste_plus_mult = 2.0 if buffs.get('haste_plus', False) else 1.0
            oil_mult = 1.2 if buffs.get('oil', False) else 1.0
            smoothie_mult = 1.25 if buffs.get('smoothie', False) else 1.0

            # Calculate final speed
            final_speed = ((base_speed + coconut_bonus + bear_bonus) *
                         hasty_guard_mult * gifted_hasty_mult * haste_mult *
                         haste_plus_mult * oil_mult * smoothie_mult)

            return final_speed

        except Exception as e:
            logger.error(f"Error calculating movement speed: {e}")
            return self.base_movespeed

    def set_buff_modifiers(self, hasty_guard: bool = None, gifted_hasty: bool = None,
                          base_movespeed: float = None):
        """
        Set buff modifier values

        Args:
            hasty_guard: Whether Hasty Guard buff is active
            gifted_hasty: Whether Gifted Hasty buff is active
            base_movespeed: Base movement speed
        """
        if hasty_guard is not None:
            self.hasty_guard = hasty_guard
        if gifted_hasty is not None:
            self.gifted_hasty = gifted_hasty
        if base_movespeed is not None:
            self.base_movespeed = base_movespeed

    def get_current_buffs(self) -> dict:
        """
        Get currently cached buff information

        Returns:
            Dictionary of active buffs
        """
        return self.cached_buffs.copy()

    def reset_buff_cache(self):
        """Reset the buff detection cache"""
        self.cached_buffs = {}
        self.last_buff_check = 0
