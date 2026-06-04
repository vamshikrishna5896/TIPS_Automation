import configparser
from pathlib import Path

config = configparser.ConfigParser()

config_path = (
    Path(__file__).parent.parent
    / "Config"
    / "config.ini"
)

config.read(config_path)


class ReadConfig:

    @staticmethod
    def get_base_url():
        return config.get("ENV", "base_url")

    @staticmethod
    def get_username():
        return config.get("ENV", "username")

    @staticmethod
    def get_password():
        return config.get("ENV", "password")

    @staticmethod
    def get_browser():
        return config.get("ENV", "browser")

    @staticmethod
    def get_headless():
        return config.getboolean("ENV", "headless")