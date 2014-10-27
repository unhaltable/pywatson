import os
import pytest
from pywatson.watson import Watson


@pytest.fixture
def config():
    """Get Watson configuration from the environment

    :return: dict with keys 'url', 'username', and 'password'
    """
    try:
        return {
            'url': os.environ['WATSON_URL'],
            'username': os.environ['WATSON_USERNAME'],
            'password': os.environ['WATSON_PASSWORD']
        }
    except KeyError as err:
        raise Exception('You must set the environment variable {}'.format(err.args[0]))


@pytest.fixture
def watson(config):
    return Watson(url=config['url'], username=config['username'], password=config['password'])
