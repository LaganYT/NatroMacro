"""
JSON utilities for Natro Macro
Equivalent to lib/JSON.ahk (simplified version using Python's built-in json module)
"""

import json
from typing import Any, Union


class JSON:
    """JSON parsing and serialization utilities"""

    # Constants for compatibility
    null = None
    true = True
    false = False

    @staticmethod
    def parse(text: str, keepbooltype: bool = False, as_map: bool = True) -> Any:
        """
        Parse JSON string into Python object
        Equivalent to JSON.parse()

        Args:
            text: JSON string to parse
            keepbooltype: If True, keeps boolean types as is (not relevant in Python)
            as_map: If True, object literals become dicts, otherwise custom objects

        Returns:
            Parsed Python object (dict, list, str, int, float, bool, None)
        """
        try:
            return json.loads(text.strip())
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")

    @staticmethod
    def stringify(obj: Any, indent: Union[int, str] = None, sort_keys: bool = False) -> str:
        """
        Convert Python object to JSON string
        Equivalent to JSON.stringify()

        Args:
            obj: Python object to serialize
            indent: Indentation level (int) or string
            sort_keys: Whether to sort dictionary keys

        Returns:
            JSON string
        """
        try:
            return json.dumps(obj, indent=indent, sort_keys=sort_keys, ensure_ascii=False)
        except (TypeError, ValueError) as e:
            raise ValueError(f"Cannot serialize object: {e}")

    @staticmethod
    def load(file_path: str, encoding: str = 'utf-8') -> Any:
        """
        Load JSON from file

        Args:
            file_path: Path to JSON file
            encoding: File encoding

        Returns:
            Parsed Python object
        """
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError, IOError) as e:
            raise ValueError(f"Cannot load JSON from file {file_path}: {e}")

    @staticmethod
    def dump(obj: Any, file_path: str, indent: Union[int, str] = None,
             sort_keys: bool = False, encoding: str = 'utf-8'):
        """
        Save Python object as JSON to file

        Args:
            obj: Python object to serialize
            file_path: Path to save JSON file
            indent: Indentation level
            sort_keys: Whether to sort dictionary keys
            encoding: File encoding
        """
        try:
            with open(file_path, 'w', encoding=encoding) as f:
                json.dump(obj, f, indent=indent, sort_keys=sort_keys, ensure_ascii=False)
        except (TypeError, ValueError, IOError) as e:
            raise ValueError(f"Cannot save JSON to file {file_path}: {e}")

    @staticmethod
    def is_valid(text: str) -> bool:
        """
        Check if string is valid JSON

        Args:
            text: String to validate

        Returns:
            True if valid JSON, False otherwise
        """
        try:
            json.loads(text)
            return True
        except json.JSONDecodeError:
            return False
