from pywatson.watson import Watson


class TestWatson:
    def test_init(self, config):
        watson = Watson(url=config['url'], username=config['username'], password=config['password'])
