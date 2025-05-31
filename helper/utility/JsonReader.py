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

        # Create parent directory if it doesn't exist
        path.parent.mkdir(parents=True, exist_ok=True)

        # Create an empty JSON file with [] if it doesn't exist
        if not path.exists():
            raise FileNotFoundError(f"JSON file not found at configured path: {path}")
        if path.suffix.lower() != '.json':
            raise ValueError(f"Configured path is not a JSON file: {path}")

        return path

    def read(self) -> Dict[str, Any]:
        """Read and parse JSON file with full validation"""
        try:
            with open(self._json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if not isinstance(data, dict):
                    raise ValueError(f"JSON file {self._json_path} must contain a dictionary")
                return data
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {self._json_path}: {str(e)}")
        except UnicodeDecodeError:
            raise ValueError(f"Encoding error in {self._json_path} (use UTF-8)")

    def save_credentials_if_empty(self, email:str, password:str, first_name:str, last_name:str) -> bool:
        """Save email and password only if JSON is empty; return True if saved, False if skipped"""
        data = self.read()

        # Skip if JSON is not empty
        if data:
            print("Credentials already exists. Skipping save.")
            return False
        # Save new credentials
        data = {'first_name': first_name,
               'last_name': last_name,
               'email': email,
               'password': password
        }
        try:
            with open(self._json_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            print('Credentials saved to json')
            return True
        except Exception as e:
            raise IOError(f"Failed to save to {self._json_path}: {str(e)}")

    def get_credentials(self) -> Dict[str, str]:
        """Get email and password from JSON"""
        data = self.read()
        if not data:
            raise ValueError(f"No credentials found in {self._json_path}")
        required_keys = ["first_name", "last_name", "email", "password"]
        missing_keys = [key for key in required_keys if key not in data]
        if missing_keys:
            raise KeyError(f"JSON file {self._json_path} missing keys: {', '.join(missing_keys)}")
        return {"first_name": data["first_name"],
                "last_name": data["last_name"],
                "email": data["email"],
                "password": data["password"]
        }

