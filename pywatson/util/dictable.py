import inflection


class Dictable(object):
    """Inherit from this abstract class to add to_dict functionality"""

    def to_dict(self):
        """
        Return a dict of all instance variables with truthy values,
        with key names camelized
        """
        return {
            inflection.camelize(k, False): v
            for k, v in self.__dict__.items()
            if v
        }
