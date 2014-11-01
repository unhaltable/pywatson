class MapInitializable(object):
    """Inherit from this abstract class to be able to initialize from a mapping (e.g. dict).

    Usage:
        >>> class Foo(MapInitializable):
        ...     def __init__(self, bar, baz):
        ...         self.bar = bar
        ...         self.baz = baz
        ...
        ...     @classmethod
        ...     def from_mapping(cls, mapping):
        ...         return cls(bar=mapping['Bar'],
        ...                    baz=mapping['BAZ'])

        >>> f = Foo.from_mapping({
        ...     'Bar': 123,
        ...     'BAZ': 456
        ... })
        >>> f.bar
        123
        >>> f.baz
        456
    """

    @classmethod
    def from_mapping(cls, mapping):
        """Initialize a new instance of ``cls`` from the given ``mapping``.

        :param mapping: A Mapping (e.g. dict) of attributes to assign to the new instance
        :return: A new instance of ``cls``
        """
        raise NotImplementedError('Subclasses of MapInitializable must implement from_mapping.')
