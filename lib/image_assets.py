"""
Image assets for Natro Macro
Provides access to all game UI element bitmaps for image recognition
"""

import base64
from PIL import Image
import io
from typing import Dict, Any

# Import all bitmap modules
from nm_image_assets.beemenu.bitmaps import bitmaps as beemenu_bitmaps
from nm_image_assets.boost.bitmaps import bitmaps as boost_bitmaps
from nm_image_assets.buffs.bitmaps import bitmaps as buffs_bitmaps
from nm_image_assets.collect.bitmaps import bitmaps as collect_bitmaps
from nm_image_assets.convert.bitmaps import bitmaps as convert_bitmaps
from nm_image_assets.fdc.bitmaps import bitmaps as fdc_bitmaps
from nm_image_assets.general.bitmaps import bitmaps as general_bitmaps
from nm_image_assets.gui.bitmaps import bitmaps as gui_bitmaps
from nm_image_assets.inventory.bitmaps import bitmaps as inventory_bitmaps
from nm_image_assets.kill.bitmaps import bitmaps as kill_bitmaps
from nm_image_assets.memorymatch.bitmaps import bitmaps as memorymatch_bitmaps
from nm_image_assets.mutator.bitmaps import bitmaps as mutator_bitmaps
from nm_image_assets.mutatorgui.bitmaps import bitmaps as mutatorgui_bitmaps
from nm_image_assets.night.bitmaps import bitmaps as night_bitmaps
from nm_image_assets.offset.bitmaps import bitmaps as offset_bitmaps
from nm_image_assets.perfstats.bitmaps import bitmaps as perfstats_bitmaps
from nm_image_assets.quests.bitmaps import bitmaps as quests_bitmaps
from nm_image_assets.reconnect.bitmaps import bitmaps as reconnect_bitmaps
from nm_image_assets.reset.bitmaps import bitmaps as reset_bitmaps
from nm_image_assets.sprinkler.bitmaps import bitmaps as sprinkler_bitmaps
from nm_image_assets.stickerprinter.bitmaps import bitmaps as stickerprinter_bitmaps
from nm_image_assets.stickerstack.bitmaps import bitmaps as stickerstack_bitmaps
from nm_image_assets.webhook_gui.bitmaps import bitmaps as webhook_gui_bitmaps

# Combine all bitmaps into a single dictionary
BITMAPS = {
    **beemenu_bitmaps,
    **boost_bitmaps,
    **buffs_bitmaps,
    **collect_bitmaps,
    **convert_bitmaps,
    **fdc_bitmaps,
    **general_bitmaps,
    **gui_bitmaps,
    **inventory_bitmaps,
    **kill_bitmaps,
    **memorymatch_bitmaps,
    **mutator_bitmaps,
    **mutatorgui_bitmaps,
    **night_bitmaps,
    **offset_bitmaps,
    **perfstats_bitmaps,
    **quests_bitmaps,
    **reconnect_bitmaps,
    **reset_bitmaps,
    **sprinkler_bitmaps,
    **stickerprinter_bitmaps,
    **stickerstack_bitmaps,
    **webhook_gui_bitmaps,
}

def get_bitmap_base64(key: str) -> str:
    """
    Get base64 encoded bitmap data for a given key

    Args:
        key: Bitmap key (e.g., 'e_button', 'redcannon')

    Returns:
        Base64 encoded image data

    Raises:
        KeyError: If bitmap key not found
    """
    return BITMAPS[key]

def get_bitmap_image(key: str) -> Image.Image:
    """
    Get PIL Image object for a given bitmap key

    Args:
        key: Bitmap key (e.g., 'e_button', 'redcannon')

    Returns:
        PIL Image object

    Raises:
        KeyError: If bitmap key not found
    """
    base64_data = get_bitmap_base64(key)
    image_data = base64.b64decode(base64_data)
    return Image.open(io.BytesIO(image_data))

def bitmap_exists(key: str) -> bool:
    """
    Check if a bitmap key exists

    Args:
        key: Bitmap key to check

    Returns:
        True if bitmap exists, False otherwise
    """
    return key in BITMAPS

def list_bitmaps() -> list:
    """
    Get a list of all available bitmap keys

    Returns:
        List of bitmap keys
    """
    return list(BITMAPS.keys())

def get_category_bitmaps(category: str) -> Dict[str, str]:
    """
    Get all bitmaps for a specific category

    Args:
        category: Category name (e.g., 'general', 'boost', 'inventory')

    Returns:
        Dictionary of bitmaps for the category

    Raises:
        ValueError: If category not found
    """
    categories = {
        'beemenu': beemenu_bitmaps,
        'boost': boost_bitmaps,
        'buffs': buffs_bitmaps,
        'collect': collect_bitmaps,
        'convert': convert_bitmaps,
        'fdc': fdc_bitmaps,
        'general': general_bitmaps,
        'gui': gui_bitmaps,
        'inventory': inventory_bitmaps,
        'kill': kill_bitmaps,
        'memorymatch': memorymatch_bitmaps,
        'mutator': mutator_bitmaps,
        'mutatorgui': mutatorgui_bitmaps,
        'night': night_bitmaps,
        'offset': offset_bitmaps,
        'perfstats': perfstats_bitmaps,
        'quests': quests_bitmaps,
        'reconnect': reconnect_bitmaps,
        'reset': reset_bitmaps,
        'sprinkler': sprinkler_bitmaps,
        'stickerprinter': stickerprinter_bitmaps,
        'stickerstack': stickerstack_bitmaps,
        'webhook_gui': webhook_gui_bitmaps,
    }

    if category not in categories:
        raise ValueError(f"Unknown category: {category}. Available categories: {list(categories.keys())}")

    return categories[category].copy()
