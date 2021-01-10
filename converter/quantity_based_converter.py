from converter.converter import Converter
from converter.unit.quantityunit import QuantityUnit


class Quantity(object):

    def __init__(self, name):
        self.name = name


class QuantityBasedConverter(Converter):

    def __init__(self, base_unit, quantity):
        super(QuantityBasedConverter, self).__init__()

        self.base_unit = base_unit
        self._quantity = quantity

    def supported_conversions(self):
        # todo methot not implemented error
        return {}

    def _conversion_table(self):
        # todo methot not implemented error
        return {}

    def quantity(self):
        return self._quantity

    def convert(self, source_unit, source_value, target_unit):
        assert isinstance(source_unit, QuantityUnit)
        assert isinstance(target_unit, QuantityUnit)

        if not (self.quantity() == source_unit.quantity() == target_unit.quantity()):
            raise Exception("Source unit's [%s] or target unit's [%s] quantity are not matched with [%s]"
                            % (source_unit.fullname(), target_unit.fullname(), self.quantity()))

        conversion_table = self._conversion_table()
        base_unit_value = conversion_table[source_unit] * source_value

        return base_unit_value / conversion_table[target_unit]
