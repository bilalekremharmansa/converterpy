from converter.unit import Unit
from converter.unit.quantityunit import QuantityUnit
from converter.converter.quantity_based_converter import QuantityBasedConverter, Quantity


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
