from configparser import ConfigParser
from pathlib import Path

from helper.enums.DriverType import BrowserType


class ConfigFileReader:
    def __init__(self, config_file: str = 'resources/configs/configuration.ini'):
        self.config = ConfigParser()
        project_root = Path(__file__).resolve().parent.parent.parent
        config_path = (project_root / config_file).resolve()
        print(config_path)

        if not config_path.is_file():
            raise FileNotFoundError(f'Config file not found at {config_path}')

        try:
            self.config.read(config_path, encoding='utf-8')
        except UnicodeDecodeError as e:
            raise ValueError(f'Invalid config file encoding: {config_path}') from e

    def get_excel_path(self) -> str:
        return self._get_property("excelFilePath", "Paths")

    def get_application_url(self) -> str:
        return self._get_property("url", "Application")

    def get_browser(self) -> BrowserType:
        browser_name = self._get_property("browser", "Browser").lower()
        try:
            return BrowserType[browser_name.upper()]
        except KeyError:
            valid_browsers = [e.value for e in BrowserType]
            raise ValueError(
                f"Unsupported browser: '{browser_name}'. "
                f"Must be one of: {valid_browsers}"
            )

    def get_implicit_wait(self) -> float:
        wait = self._get_property("implicitlyWait", "Timeouts")
        try:
            return float(wait)
        except ValueError:
            raise ValueError(f"Invalid wait time: {wait}")

    def _get_property(self, key: str, section: str) -> str:
        try:
            value = self.config.get(section, key)
            if not value:
                raise ValueError(f"Empty value for {key} in config")
            return value
        except Exception as e:
            raise KeyError(f"Missing or invalid config key: {section}.{key}") from e