import configparser
import os
from enum import Enum


class Config():

    ConfigValue = Enum('ConfigValue', ['DATA_PATH'])

    def get_config(self):
        home = os.path.expanduser('~')
        return open(home + ".spend/config.ini", "r").read()
        # return {'data' : {'path' : home+ '.spend/spend.csv'}}


    def create_config(self):
        home = os.path.expanduser('~')
        config = configparser.ConfigParser()
        config['data'] = {'path' : home+ '.spend/spend.csv'}
        with open(os.path.exists(home + ".spend/config.ini"), "w") as configfile:
            config.write(configfile)


    def config_exists(self):
        home = os.path.expanduser('~')
        if(os.path.exists(home + ".spend/config.ini")):
            return True
        return False