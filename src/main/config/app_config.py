from configparser import ConfigParser


class AppConfig(object):

    config: ConfigParser

    def __new__(cls):
        cls._instance = object.__new__(cls)
        cls._instance.config = ConfigParser()
        cls._instance.config.read("./config/config.ini", "UTF-8")
        return cls._instance
