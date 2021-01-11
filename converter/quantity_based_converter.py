from converter.converter import Converter
from converter.unit.quantityunit import QuantityUnit

from converter.util.assertion import assert_list_is_instance


class Quantity(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Quantity(%s)' % self.name


class QuantityBasedConverter(Converter):

    @staticmethod
    def create_supported_conversion_dictionary(units):
        supported_conversions = dict()
        for unit in units:
            supported_conversions[unit] = [u for u in units if u != unit]

        return supported_conversions

    # ------

    def __init__(self, units, base_unit, quantity):
        super(QuantityBasedConverter, self).__init__()

        assert isinstance(quantity, Quantity)
        assert isinstance(base_unit, QuantityUnit)
        assert_list_is_instance(units, QuantityUnit)

        # ---

        self.units = units  # list
        self.base_unit = base_unit
        self._quantity = quantity

        self._validate_init_args()

        self._supported_conversions = QuantityBasedConverter.create_supported_conversion_dictionary(self.units)

        # ----

    def _validate_init_args(self):
        if self.base_unit not in self.units:
            raise Exception("Base unit [%s] is not in units [%s]" % (self.base_unit, self.units))

        for unit in self.units:
            if unit.quantity() != self.quantity():
                raise Exception("Unit's quantity [%s] is not same with converter's quantity [%s]"
                                % (unit.quantity, self.quantity()))

    def _conversion_table(self):
        raise NotImplementedError()

    # -----

    def quantity(self):
        return self._quantity

    def _is_unit_supported(self, unit):
        assert isinstance(unit, QuantityUnit)
        return unit in self.units

    # -----

    def supported_conversions(self):
        return self._supported_conversions

    def convert(self, source_unit, source_value, target_unit):
        assert isinstance(source_unit, QuantityUnit)
        assert isinstance(target_unit, QuantityUnit)

        if not self._is_unit_supported(source_unit):
            raise Exception("Source unit is not supported [%s]" % source_unit)

        if not self._is_unit_supported(target_unit):
            raise Exception("Target unit is not supported [%s]" % target_unit)

        if not (self.quantity() == source_unit.quantity() == target_unit.quantity()):
            raise Exception("Source unit's [%s] or target unit's [%s] quantity are not matched with [%s]"
                            % (source_unit.fullname(), target_unit.fullname(), self.quantity()))

        # -----

        conversion_table = self._conversion_table()
        base_unit_value = conversion_table[source_unit] * source_value

        return base_unit_value / conversion_table[target_unit]
