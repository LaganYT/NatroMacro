"""
Memory Match game data for Natro Macro
Equivalent to lib/data/memorymatch.ahk
"""

from typing import Dict, Any


# Memory Match game configurations
# Games in decreasing binary order: Winter, Extreme, Night, Mega, Normal
MEMORY_MATCH_GAMES: Dict[str, Dict[str, Any]] = {
    "Winter": {"bit": 16, "cooldown": 14400},      # 4 hours
    "Extreme": {"bit": 8, "cooldown": 28800},      # 8 hours
    "Night": {"bit": 4, "cooldown": 28800},        # 8 hours
    "Mega": {"bit": 2, "cooldown": 14400},         # 4 hours
    "Normal": {"bit": 1, "cooldown": 7200}         # 2 hours
}

# Memory match items with their display names and available games
# games: decimal value representing which games the item appears in
# Binary format: Winter Extreme Night Mega Normal
MEMORY_MATCH_ITEMS: Dict[str, Dict[str, Any]] = {
    "Treat": {"name": "Treats", "games": 31},                      # 11111 - All games
    "SunflowerSeed": {"name": "Sunflower Seeds", "games": 11},      # 01011 - Normal, Mega
    "Blueberry": {"name": "Blueberries", "games": 11},              # 01011 - Normal, Mega
    "Strawberry": {"name": "Strawberries", "games": 11},            # 01011 - Normal, Mega
    "Pineapple": {"name": "Pineapples", "games": 11},               # 01011 - Normal, Mega
    "RoyalJelly": {"name": "Royal Jellies", "games": 11},           # 01011 - Normal, Mega
    "Gumdrop": {"name": "Gumdrops", "games": 27},                   # 11011 - Normal, Mega, Night
    "MoonCharm": {"name": "Moon Charms", "games": 7},               # 00111 - Normal, Mega, Extreme
    "Ticket": {"name": "Tickets", "games": 31},                     # 11111 - All games
    "JellyBean": {"name": "Jelly Beans", "games": 27},              # 11011 - Normal, Mega, Night
    "MicroConverter": {"name": "Micro-Converters", "games": 31},    # 11111 - All games
    "FieldDice": {"name": "Field Dice", "games": 23},               # 10111 - Normal, Mega, Extreme, Winter
    "MagicBean": {"name": "Magic Beans", "games": 31},              # 11111 - All games
    "Oil": {"name": "Oils", "games": 15},                           # 01111 - Normal, Mega, Extreme, Night
    "Enzyme": {"name": "Enzymes", "games": 15},                     # 01111 - Normal, Mega, Extreme, Night
    "Glitter": {"name": "Glitter", "games": 31},                    # 11111 - All games
    "NightBell": {"name": "Night Bells", "games": 21},              # 10101 - Normal, Extreme, Winter
    "Glue": {"name": "Glue", "games": 22},                          # 10110 - Mega, Extreme, Winter
    "RedExtract": {"name": "Red Extracts", "games": 10},            # 01010 - Mega, Winter
    "BlueExtract": {"name": "Blue Extracts", "games": 10},          # 01010 - Mega, Winter
    "Stinger": {"name": "Stingers", "games": 14},                   # 01110 - Mega, Extreme, Night
    "Coconut": {"name": "Coconuts", "games": 10},                   # 01010 - Mega, Winter
    "StarJelly": {"name": "Star Jellies", "games": 30},             # 11110 - Mega, Extreme, Night, Winter
    "TropicalDrink": {"name": "Tropical Drinks", "games": 26},      # 11010 - Mega, Night, Winter
    "CyanTrim": {"name": "Cyan Sticker", "games": 2},               # 00010 - Mega only
    "CloudVial": {"name": "Cloud Vials", "games": 8},                # 01000 - Extreme only
    "SoftWax": {"name": "Soft Wax", "games": 16},                   # 10000 - Winter only
    "HardWax": {"name": "Hard Wax", "games": 16},                   # 10000 - Winter only
    "SwirledWax": {"name": "Swirled Wax", "games": 16},             # 10000 - Winter only
    "Honeysuckle": {"name": "Honeysuckles", "games": 16},           # 10000 - Winter only
    "SuperSmoothie": {"name": "Super Smoothies", "games": 16},      # 10000 - Winter only
    "SmoothDice": {"name": "Smooth Dice", "games": 16},             # 10000 - Winter only
    "Neonberry": {"name": "Neonberries", "games": 16},              # 10000 - Winter only
    "Gingerbread": {"name": "Gingerbread Bears", "games": 16},      # 10000 - Winter only
    "SilverEgg": {"name": "Silver Eggs", "games": 16},              # 10000 - Winter only
    "GoldEgg": {"name": "Gold Eggs", "games": 24},                  # 11000 - Night, Winter
    "DiamondEgg": {"name": "Diamond Eggs", "games": 25}             # 11001 - Normal, Night, Winter
}


class MemoryMatchData:
    """Manages memory match game data and item availability"""

    def __init__(self):
        self.games = MEMORY_MATCH_GAMES
        self.items = MEMORY_MATCH_ITEMS

    def get_game_info(self, game_name: str) -> Dict[str, Any]:
        """
        Get information about a specific memory match game

        Args:
            game_name: Name of the game ("Winter", "Extreme", etc.)

        Returns:
            Dict with 'bit' and 'cooldown' information
        """
        return self.games.get(game_name, {})

    def get_item_info(self, item_key: str) -> Dict[str, Any]:
        """
        Get information about a specific memory match item

        Args:
            item_key: Item key (e.g., "Treat", "SunflowerSeed")

        Returns:
            Dict with 'name' and 'games' information
        """
        return self.items.get(item_key, {})

    def is_item_in_game(self, item_key: str, game_name: str) -> bool:
        """
        Check if an item appears in a specific game

        Args:
            item_key: Item key
            game_name: Game name

        Returns:
            True if item appears in the game, False otherwise
        """
        item_info = self.get_item_info(item_key)
        game_info = self.get_game_info(game_name)

        if not item_info or not game_info:
            return False

        # Check if the game's bit is set in the item's games value
        return (item_info['games'] & game_info['bit']) != 0

    def get_games_for_item(self, item_key: str) -> list[str]:
        """
        Get list of games where an item appears

        Args:
            item_key: Item key

        Returns:
            List of game names where the item appears
        """
        item_info = self.get_item_info(item_key)
        if not item_info:
            return []

        games = []
        for game_name, game_info in self.games.items():
            if (item_info['games'] & game_info['bit']) != 0:
                games.append(game_name)

        return games

    def get_items_for_game(self, game_name: str) -> list[str]:
        """
        Get list of items that appear in a specific game

        Args:
            game_name: Game name

        Returns:
            List of item keys that appear in the game
        """
        game_info = self.get_game_info(game_name)
        if not game_info:
            return []

        items = []
        for item_key, item_info in self.items.items():
            if (item_info['games'] & game_info['bit']) != 0:
                items.append(item_key)

        return items

    def get_game_cooldown(self, game_name: str) -> int:
        """
        Get the cooldown time for a game in seconds

        Args:
            game_name: Game name

        Returns:
            Cooldown in seconds, or 0 if game not found
        """
        game_info = self.get_game_info(game_name)
        return game_info.get('cooldown', 0)

    def get_item_display_name(self, item_key: str) -> str:
        """
        Get the display name for an item

        Args:
            item_key: Item key

        Returns:
            Display name, or the key if not found
        """
        item_info = self.get_item_info(item_key)
        return item_info.get('name', item_key)
