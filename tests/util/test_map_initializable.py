from pywatson.util.map_initializable import MapInitializable


class TestMapInitializable(object):
    def test(self):
        class Foo(MapInitializable):
            attribute_name_mapping = {
                'Bar': 'bar',
                'BAZ': 'baz'
            }

            def __init__(self, bar, baz):
                self.bar = bar
                self.baz = baz

        f = Foo.from_mapping({
            'Bar': 123,
            'BAZ': 456
        })
        assert f.bar == 123
        assert f.baz == 456
