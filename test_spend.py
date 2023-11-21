from spend.config import get_config
import os

class TestSpend():

    def test_get_config(self):
        home = os.path.expanduser('~')
        assert get_config() == {'data' : {'path' : home+ '.spend/spend.csv'}}
