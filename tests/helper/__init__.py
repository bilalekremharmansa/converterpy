from converterpy.converter import Converter
from converterpy.unit import Unit
from converterpy.unit.quantityunit import QuantityUnit
from converterpy.converter.quantity_based_converter import QuantityBasedConverter, Quantity


MOCK_TIME_QUANTITY = Quantity("MOCK_TIME_QUANTITY")

UNIT_SEC = QuantityUnit('sec', 'seconds', MOCK_TIME_QUANTITY)
UNIT_MIN = QuantityUnit('min', 'minutes', MOCK_TIME_QUANTITY)
UNIT_HOUR = QuantityUnit('h', 'hours', MOCK_TIME_QUANTITY)

UNIT_SIMPLE_UNIT = Unit('simp', 'simple unit')
UNIT_IRRELEVANT = QuantityUnit('ir', 'irrelevant_unit', None)

MOCK_UNITS = [
    UNIT_SEC,
    UNIT_MIN,
    UNIT_HOUR
]


class MockQuantityBasedConverter(QuantityBasedConverter):

    def __init__(self):
        super(MockQuantityBasedConverter, self).__init__('Mock Quantity Based Converter', MOCK_UNITS, UNIT_SEC,
                                                         MOCK_TIME_QUANTITY)

        self.conversion_table = {
            UNIT_SEC: 1,
            UNIT_MIN: 60,
            UNIT_HOUR: 3600,
        }

    def _conversion_table(self):
        return self.conversion_table

# ------


UNIT_INT = Unit('int', 'integer')
UNIT_FLOAT = Unit('fl', 'float')


class NumberConverter(Converter):

    def __init__(self):
        super(NumberConverter, self).__init__('Number Converter')

    def supported_conversions(self):
        return {
            UNIT_INT: [UNIT_FLOAT],
            UNIT_FLOAT: [UNIT_INT]
        }

    def map_source_value(self, source_value):
        return source_value

    def convert(self, source_unit, source_value, target_unit):

        if source_unit == UNIT_INT and target_unit == UNIT_FLOAT:
            return float(source_value)
        elif source_unit == UNIT_FLOAT and target_unit == UNIT_INT:
            return float(source_value)

        raise Exception("Unknown conversion")
