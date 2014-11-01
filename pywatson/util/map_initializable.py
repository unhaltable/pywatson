class MapInitializable(object):
    """Inherit from this abstract class to be able to initialize from a mapping (e.g. dict).

    Usage:
        You must define an :py:attr:`attribute_name_mapping` class variable
        which defines the instance attributes that can be initialized from a mapping
        and renames attributes from key -> value.

        >>> class Foo(MapInitializable):
        ...     attribute_name_mapping = {
        ...         'Bar': 'bar',
        ...         'BAZ': 'baz'
        ...     }
        ...
        ...     def __init__(self, bar, baz):
        ...         self.bar = bar
        ...         self.baz = baz

        >>> f = Foo.from_mapping({
        ...     'Bar': 123,
        ...     'BAZ': 456
        ... })
        >>> f.bar
        123
        >>> f.baz
        456
    """

    #: Mapping of ``(k: v)`` where
    #:
    #: * ``k``: the attribute name passed as a key to :py:meth:`from_mapping`
    #: * ``v``: the attribute name to assign to the new instance
    attribute_name_mapping = {}

    @classmethod
    def from_mapping(cls, mapping):
        """Initialize a new instance of ``cls`` from the given ``mapping``.

        :param mapping: A Mapping (e.g. dict) of attributes to assign to the new instance
        :return: A new instance of ``cls``
        """
        name_mapping = cls.attribute_name_mapping
        renamed_mapping = {name_mapping[k]: v for k, v in mapping.items() if k in name_mapping}
        return cls(**renamed_mapping)
