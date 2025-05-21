import json
from pathlib import Path
from typing import Optional, Dict, Any

from helper.dataProvider.ConfigFileReader import ConfigFileReader


class JSONFileManager:
    def __init__(self, config_reader: Optional[ConfigFileReader] = None):
        self._config = config_reader or ConfigFileReader()
        self._json_path = self._resolve_json_path()

    def _resolve_json_path(self) -> Path:
        """Get and validate JSON path from config"""
        raw_path = self._config.get_json_path()
        path = Path(raw_path)

        if not path.exists():
            raise FileNotFoundError(f"JSON file not found at configured path: {path}")
        if path.suffix.lower() != '.json':
            raise ValueError(f"Configured path is not a JSON file: {path}")

        return path

    def read(self) -> Dict[str, Any]:
        """Read and parse JSON file with full validation"""
        try:
            with open(self._json_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {self._json_path}: {str(e)}")
        except UnicodeDecodeError:
            raise ValueError(f"Encoding error in {self._json_path} (use UTF-8)")

    def get_value(self, key: str, default: Any = None) -> Any:
        """Get specific value from JSON with optional default"""
        data = self.read()
        if key not in data and default is None:
            raise KeyError(f"Key '{key}' not found in {self._json_path} and no default provided")
        return data.get(key, default)