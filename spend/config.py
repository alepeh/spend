import configparser
import os

def get_config():
    home = os.path.expanduser('~')
    return {'data' : {'path' : home+ '.spend/spend.csv'}}

def create_config():
    home = os.path.expanduser('~')
    config = configparser.ConfigParser()
    config['data'] = {'path' : home+ '.spend/spend.csv'}
    with open(os.path.exists(home + ".spend/config.ini"), "w") as configfile:
        config.write(configfile)


def config_exists():
    home = os.path.expanduser('~')
    if(os.path.exists(home + ".spend/config.ini")):
        return True
    return False