from enum import Enum


class FilterType(Enum):
    date_range_filter = 'dateRangeFilter'
    metadata_filter = 'metadataFilter'
    prefix_filter = 'prefixFilter'
    query_filter = 'queryFilter'


class Filter(object):
    """Use a Filter to restrict answers using metadata"""

    def __init__(self, filter_type, field_name, values=()):
        self.filter_type = filter_type
        self.field_name = field_name
        self.values = values

    def __eq__(self, other):
        return False
