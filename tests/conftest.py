import json
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


@pytest.fixture
def questions():
    qs = []

    for root, dirs, files in os.walk('tests/json/questions'):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                qs.append(json.load(open(filepath)))
            except ValueError:
                raise ValueError('Expected {} to contain valid JSON'.format(filepath))

    return qs
