from configparser import ConfigParser
from pathlib import Path


class ConfigFileReader:
    def __init__(self, config_file: str = 'configs/configuration.ini'):
        self.config = ConfigParser()
        config_path = (Path(__file__).parent.parent / config_file).resolve()

        if not config_path.is_file():
            raise FileNotFoundError(f'Config file not found at {config_path}')

        try:
            self.config.read(config_path, encoding='utf-8')
        except UnicodeDecodeError as e:
            raise ValueError(f'Invalid config file encoding: {config_path}') from e
