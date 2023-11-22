from unittest import mock
from spend.config import Config


class TestSpend():

    def test_get_config(self):
        config = Config()
        read_data = "{'data' : {'path' : '.spend/spend.csv'}}"
        mock_open = mock.mock_open(read_data=read_data)

        with mock.patch('builtins.open', mock_open):
            result = config.get_config()
            assert result == "{'data' : {'path' : '.spend/spend.csv'}}"