import collections


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

        You can also specify a MapInitializable subclass for an attribute,
        which will be used to initialize the attribute from a mapping:

        >>> class Qux(MapInitializable):
        ...     attribute_name_mapping = {
        ...         'norf': 'norf',
        ...         'foo': ('foo', Foo)
        ...     }
        ...
        ...     def __init__(self, norf, foo):
        ...         self.norf = norf
        ...         self.foo = foo

        >>> q = Qux.from_mapping({
        ...     'norf': 321,
        ...     'foo': {
        ...         'Bar': 123,
        ...         'BAZ': 456
        ...     }
        ... })
        >>> q.foo.norf
        321
        >>> q.foo.bar
        123
    """

    #: Mapping of ``(k: v)`` where
    #:
    #: * ``k``: The attribute name passed as a key to :py:meth:`from_mapping`
    #: * ``v``: Either:
    #:   1. ``attr_name``: The attribute name to assign to the new instance, or
    #:   2. A tuple of ``(attr_name, cls)`` where ``cls`` inherits from ``MapInitializable``
    attribute_name_mapping = {}

    @classmethod
    def from_mapping(cls, mapping):
        """Initialize a new instance of ``cls`` from the given ``mapping``.

        :param mapping: A Mapping (e.g. dict) of attributes to assign to the new instance
        :return: A new instance of ``cls``
        """
        name_mapping = cls.attribute_name_mapping

        renamed_mapping = {}
        for k, v in mapping.items():
            if k in name_mapping:
                r = name_mapping[k]
                # r is either ``attr_name`` or ``(attr_name, cls)``
                if isinstance(r, tuple) and isinstance(r[1], MapInitializable):
                    # r is a tuple of ``(attr_name, cls)``; use ``cls.from_mapping`` to initialize v
                    renamed_mapping[name_mapping[k][0]] = r[1].from_mapping(v)
                else:
                    renamed_mapping[name_mapping[k]] = v

        return cls(**renamed_mapping)
