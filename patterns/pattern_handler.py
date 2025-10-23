"""
Pattern handling system for Natro Macro
Converts AHK pattern files to Python executable movement patterns
"""

import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class PatternHandler:
    """Handles movement patterns for different gathering strategies"""

    def __init__(self, macro_instance):
        self.macro = macro_instance
        self.path_handler = macro_instance.path_handler

        # Pattern key mappings (these correspond to AHK variables)
        self.key_mappings = {
            'TCFBKey': 'w',      # Top-Close Forward-Back
            'TCLRKey': 'a',      # Top-Close Left-Right
            'AFCFBKey': 's',     # Away-From-Center Forward-Back
            'AFCLRKey': 'd',     # Away-From-Center Left-Right
            'FwdKey': 'w',
            'BackKey': 's',
            'LeftKey': 'a',
            'RightKey': 'd',
        }

    def execute_pattern(self, pattern_name: str, reps: int, size: float = 1.0,
                       **kwargs) -> bool:
        """
        Execute a movement pattern by name

        Args:
            pattern_name: Name of the pattern to execute
            reps: Number of repetitions
            size: Size multiplier for movements
            **kwargs: Additional pattern-specific parameters

        Returns:
            True if successful, False otherwise
        """
        try:
            # Import the specific pattern module
            pattern_module = __import__(f'patterns.{pattern_name}', fromlist=[pattern_name])
            pattern_function = getattr(pattern_module, pattern_name.replace('-', '_'))

            # Execute the pattern
            pattern_function(self, reps, size, **kwargs)
            return True

        except ImportError:
            logger.error(f"Pattern {pattern_name} not found")
            return False
        except AttributeError:
            logger.error(f"Pattern function {pattern_name} not found in pattern module")
            return False
        except Exception as e:
            logger.error(f"Error executing pattern {pattern_name}: {e}")
            return False

    def nm_walk(self, distance: float, *keys: str):
        """Walk with pattern-specific key mapping"""
        actual_keys = []
        for key in keys:
            if key in self.key_mappings:
                actual_keys.append(self.key_mappings[key])
            else:
                actual_keys.append(key.lower())

        return self.path_handler.nm_walk(distance, *actual_keys)

    def send_key_sequence(self, sequence: str):
        """Send key sequence with pattern key mapping"""
        # Replace pattern keys in the sequence
        for pattern_key, actual_key in self.key_mappings.items():
            sequence = sequence.replace(f"{{{pattern_key}", f"{{{actual_key}")

        return self.path_handler.send_key_sequence(sequence)


# Individual pattern implementations

def squares(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Squares gathering pattern
    Converted from patterns/Squares.ahk
    """
    for _ in range(reps):
        pattern_handler.send_key_sequence("{w down}")
        pattern_handler.nm_walk(5 * size + 1)  # A_Index starts from 1
        pattern_handler.send_key_sequence("{w up}{a down}")
        pattern_handler.nm_walk(5 * size + 1)
        pattern_handler.send_key_sequence("{a up}{s down}")
        pattern_handler.nm_walk(5 * size + 1)
        pattern_handler.send_key_sequence("{s up}{d down}")
        pattern_handler.nm_walk(5 * size + 1)
        pattern_handler.send_key_sequence("{d up}")


def snake(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Snake gathering pattern
    Converted from patterns/Snake.ahk
    """
    # Towards center
    for _ in range(reps):
        pattern_handler.send_key_sequence("{a down}")
        pattern_handler.nm_walk(11 * size)
        pattern_handler.send_key_sequence("{a up}{w down}")
        pattern_handler.nm_walk(1)
        pattern_handler.send_key_sequence("{w up}{d down}")
        pattern_handler.nm_walk(11 * size)
        pattern_handler.send_key_sequence("{d up}{w down}")
        pattern_handler.nm_walk(1)
        pattern_handler.send_key_sequence("{w up}")

    # Away from center
    for _ in range(reps):
        pattern_handler.send_key_sequence("{a down}")
        pattern_handler.nm_walk(11 * size)
        pattern_handler.send_key_sequence("{a up}{s down}")
        pattern_handler.nm_walk(1)
        pattern_handler.send_key_sequence("{s up}{d down}")
        pattern_handler.nm_walk(11 * size)
        pattern_handler.send_key_sequence("{d up}{s down}")
        pattern_handler.nm_walk(1)
        pattern_handler.send_key_sequence("{s up}")


def lines(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Lines gathering pattern
    Placeholder implementation
    """
    logger.info(f"Executing lines pattern with {reps} reps, size {size}")
    # TODO: Implement actual lines pattern from patterns/Lines.ahk


def diamonds(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Diamonds gathering pattern
    Placeholder implementation
    """
    logger.info(f"Executing diamonds pattern with {reps} reps, size {size}")
    # TODO: Implement actual diamonds pattern from patterns/Diamonds.ahk


def fork(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Fork gathering pattern
    Placeholder implementation
    """
    logger.info(f"Executing fork pattern with {reps} reps, size {size}")
    # TODO: Implement actual fork pattern from patterns/Fork.ahk


def stationary(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Stationary gathering pattern
    Placeholder implementation
    """
    logger.info(f"Executing stationary pattern with {reps} reps, size {size}")
    # TODO: Implement actual stationary pattern from patterns/Stationary.ahk


def auryn(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Auryn gathering pattern
    Placeholder implementation
    """
    logger.info(f"Executing auryn pattern with {reps} reps, size {size}")
    # TODO: Implement actual auryn pattern from patterns/Auryn.ahk


def corner_x_snake(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Corner X Snake gathering pattern
    Placeholder implementation
    """
    logger.info(f"Executing corner x snake pattern with {reps} reps, size {size}")
    # TODO: Implement actual corner x snake pattern from patterns/CornerXSnake.ahk


def e_lol(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    E LOL gathering pattern
    Placeholder implementation
    """
    logger.info(f"Executing e_lol pattern with {reps} reps, size {size}")
    # TODO: Implement actual e_lol pattern from patterns/e_lol.ahk


def slimline(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Slimline gathering pattern
    Placeholder implementation
    """
    logger.info(f"Executing slimline pattern with {reps} reps, size {size}")
    # TODO: Implement actual slimline pattern from patterns/Slimline.ahk


def super_cat(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Super Cat gathering pattern
    Placeholder implementation
    """
    logger.info(f"Executing super cat pattern with {reps} reps, size {size}")
    # TODO: Implement actual super cat pattern from patterns/SuperCat.ahk


def x_snake(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    X Snake gathering pattern
    Placeholder implementation
    """
    logger.info(f"Executing x snake pattern with {reps} reps, size {size}")
    # TODO: Implement actual x snake pattern from patterns/XSnake.ahk


def Auryn(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Auryn gathering pattern
    Converted from patterns/Auryn.ahk
    """
    ﻿;Auryn Gathering Path
    AurynDelay:=175
    for _ in range(reps):
        # infinity
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*3*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*3*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*1.4)
        pattern_handler.send_key_sequence("{{")
        # big circle
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2*1.4)
        pattern_handler.send_key_sequence("{{")
        # FLIP!!
        # move to other side (half circle)
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2*1.4)
        pattern_handler.send_key_sequence("{{")
        pattern_handler.send_key_sequence("{{")
        # pause here
        HyperSleep(50)
        # reverse infinity
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*3*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*1.4)
        pattern_handler.send_key_sequence("{{")
        # big circle
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2*1.4)
        pattern_handler.send_key_sequence("{{")
        # FLIP!!
        # move to other side (half circle)
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2*1.4)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2)
        pattern_handler.send_key_sequence("{{")
        Walk(AurynDelay*9/2000*size*A_Index*1.1*2*1.4)
        pattern_handler.send_key_sequence("{{")
        pattern_handler.send_key_sequence("{{")


def CornerXSnake(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Cornerxsnake gathering pattern
    Converted from patterns/CornerXSnake.ahk
    """
    ﻿send "{" TCLRKey " down}"
    pattern_handler.nm_walk(4 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(2 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(2 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    Walk( Sqrt( ( ( 8 * size ) ** 2 ) + ( ( 8 * size ) ** 2 ) ) )
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(2 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    Walk(6.7 * size + 10)
    pattern_handler.send_key_sequence("{{")
    Walk(6 + reps)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(3)
    pattern_handler.send_key_sequence("{{")
    Walk(2 + reps)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(5)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(2 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(2 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(2 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(3 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    Walk( Sqrt( ( ( 4 * size ) ** 2 ) + ( ( 4 * size ) ** 2 ) ) )
    pattern_handler.send_key_sequence("{{")


def Diamonds(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Diamonds gathering pattern
    Converted from patterns/Diamonds.ahk
    """
    ﻿loop reps {
    pattern_handler.send_key_sequence("{{")
    Walk(5 * size + A_Index)
    pattern_handler.send_key_sequence("{{")
    Walk(5 * size + A_Index)
    pattern_handler.send_key_sequence("{{")
    Walk(5 * size + A_Index)
    pattern_handler.send_key_sequence("{{")
    Walk(5 * size + A_Index)
    pattern_handler.send_key_sequence("{{")


def e_lol(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    E Lol gathering pattern
    Converted from patterns/e-lol.ahk
    """
    ﻿spacingDelay:=274 ;183
    pattern_handler.send_key_sequence("{{")
    Walk(spacingDelay*9/2000*(reps*2+1))
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(5 * size)
    pattern_handler.send_key_sequence("{{")
    for _ in range(reps):
        pattern_handler.send_key_sequence("{{")
        Walk(spacingDelay*9/2000)
        pattern_handler.send_key_sequence("{{")
        pattern_handler.nm_walk(5 * size)
        pattern_handler.send_key_sequence("{{")
        Walk(spacingDelay*9/2000)
        pattern_handler.send_key_sequence("{{")
        Walk((1094+25*facingcorner)*9/2000*size)
        pattern_handler.send_key_sequence("{{")
    pattern_handler.send_key_sequence("{{")
    Walk(spacingDelay*9/2000*(reps*2+0.5))
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(5 * size)
    pattern_handler.send_key_sequence("{{")
    for _ in range(reps):
        pattern_handler.send_key_sequence("{{")
        Walk(spacingDelay*9/2000)
        pattern_handler.send_key_sequence("{{")
        Walk((1094+25*facingcorner)*9/2000*size)
        pattern_handler.send_key_sequence("{{")
        Walk(spacingDelay*9/2000*1.5)
        pattern_handler.send_key_sequence("{{")
        pattern_handler.nm_walk(5 * size)
        pattern_handler.send_key_sequence("{{")


def Fork(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Fork gathering pattern
    Converted from patterns/Fork.ahk
    """
    ﻿CForkGap:=0.75 ;flowers between lines
    CForkDiagonal := CForkGap*sqrt(2)
    CForkLength := (40-CForkGap*16-CForkDiagonal*4)/6
    if(facingcorner) {
    pattern_handler.send_key_sequence("{{")
    Walk(1.5, 10)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.send_key_sequence("{{")
    Walk(CForkDiagonal*2)
    pattern_handler.send_key_sequence("{{")
    Walk(((reps-1)*4+2)*CForkGap)
    pattern_handler.send_key_sequence("{{")
    Walk(CForkDiagonal*2)
    pattern_handler.send_key_sequence("{{")
    for _ in range(reps):
        Walk(CForkLength * size, 99)
        pattern_handler.send_key_sequence("{{")
        Walk(CForkGap*2)
        pattern_handler.send_key_sequence("{{")
        Walk(CForkLength * size, 99)
        pattern_handler.send_key_sequence("{{")
        Walk(CForkGap*2)
        pattern_handler.send_key_sequence("{{")
    Walk(CForkLength * size, 99)
    pattern_handler.send_key_sequence("{{")
    Walk(CForkGap*2)
    pattern_handler.send_key_sequence("{{")
    Walk(CForkLength * size, 99)
    pattern_handler.send_key_sequence("{{")


def Lines(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Lines gathering pattern
    Converted from patterns/Lines.ahk
    """
    ﻿loop reps {
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(11 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(1)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(11 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(1)
    pattern_handler.send_key_sequence("{{")
    # away from center
    for _ in range(reps):
        pattern_handler.send_key_sequence("{{")
        pattern_handler.nm_walk(11 * size)
        pattern_handler.send_key_sequence("{{")
        pattern_handler.nm_walk(1)
        pattern_handler.send_key_sequence("{{")
        pattern_handler.nm_walk(11 * size)
        pattern_handler.send_key_sequence("{{")
        pattern_handler.nm_walk(1)
        pattern_handler.send_key_sequence("{{")


def Slimline(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Slimline gathering pattern
    Converted from patterns/Slimline.ahk
    """
    ﻿send "{" TCLRKey " down}"
    Walk(( 4 * size ) + ( reps * 0.1 ) - 0.1)
    pattern_handler.send_key_sequence("{{")
    Walk( 8 * size )
    pattern_handler.send_key_sequence("{{")
    Walk( 4 * size )
    pattern_handler.send_key_sequence("{{")


def Snake(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Snake gathering pattern
    Converted from patterns/Snake.ahk
    """
    ﻿loop reps {
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(11 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(1)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(11 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(1)
    pattern_handler.send_key_sequence("{{")
    # away from center
    for _ in range(reps):
        pattern_handler.send_key_sequence("{{")
        pattern_handler.nm_walk(11 * size)
        pattern_handler.send_key_sequence("{{")
        pattern_handler.nm_walk(1)
        pattern_handler.send_key_sequence("{{")
        pattern_handler.nm_walk(11 * size)
        pattern_handler.send_key_sequence("{{")
        pattern_handler.nm_walk(1)
        pattern_handler.send_key_sequence("{{")


def Squares(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Squares gathering pattern
    Converted from patterns/Squares.ahk
    """
    ﻿loop reps {
    pattern_handler.send_key_sequence("{{")
    Walk(5 * size + A_Index)
    pattern_handler.send_key_sequence("{{")
    Walk(5 * size + A_Index)
    pattern_handler.send_key_sequence("{{")
    Walk(5 * size + A_Index)
    pattern_handler.send_key_sequence("{{")
    Walk(5 * size + A_Index)
    pattern_handler.send_key_sequence("{{")


def Stationary(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Stationary gathering pattern
    Converted from patterns/Stationary.ahk
    """
    ﻿Sleep 10000


def SuperCat(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Supercat gathering pattern
    Converted from patterns/SuperCat.ahk
    """
    ﻿loop reps {
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(1.25 * size)
    pattern_handler.send_key_sequence("{{")
    Walk(7 * size, 10)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(1.25 * size)
    pattern_handler.send_key_sequence("{{")
    Walk(6.66 * size, 10)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(1.25 * size)
    pattern_handler.send_key_sequence("{{")
    Walk(7 * size, 10)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(2 * size)
    pattern_handler.send_key_sequence("{{")
    Walk(6.5 * size, 10)
    pattern_handler.send_key_sequence("{{")
    for _ in range(reps):
        pattern_handler.send_key_sequence("{{")
        pattern_handler.nm_walk(1.25 * size)
        pattern_handler.send_key_sequence("{{")
        Walk(7 * size, 10)
        pattern_handler.send_key_sequence("{{")
        pattern_handler.nm_walk(1 * size)
        pattern_handler.send_key_sequence("{{")
        Walk(6.66 * size, 10)
        pattern_handler.send_key_sequence("{{")
        pattern_handler.nm_walk(1.25 * size)
        pattern_handler.send_key_sequence("{{")
        Walk(7 * size, 10)
        pattern_handler.send_key_sequence("{{")
        pattern_handler.nm_walk(1.25 * size)
        pattern_handler.send_key_sequence("{{")
        Walk(6.5 * size, 10)
        pattern_handler.send_key_sequence("{{")


def XSnake(pattern_handler: PatternHandler, reps: int, size: float = 1.0):
    """
    Xsnake gathering pattern
    Converted from patterns/XSnake.ahk
    """
    ﻿loop reps {
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(4 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(2 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(2 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    Walk(Sqrt( ( ( 8 * size ) ** 2 ) + ( ( 8 * size ) ** 2 )))
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(2 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(6.7 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(2 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(2 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(2 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(3 * size)
    pattern_handler.send_key_sequence("{{")
    pattern_handler.nm_walk(8 * size)
    pattern_handler.send_key_sequence("{{")
    Walk(Sqrt( ( ( 4 * size ) ** 2 ) + ( ( 4 * size ) ** 2 )))
    pattern_handler.send_key_sequence("{{")
