from converterpy.converter.si.length_converter import *
from converterpy.unit import Unit


def test_init():
    converter = SILengthConverter()

    assert converter is not None


def test_base_unit():
    converter = SILengthConverter()

    assert converter.base_unit == UNIT_SI_METER


def test_units():
    converter = SILengthConverter()

    assert UNIT_SI_MILLIMETER in converter.units
    assert UNIT_SI_CENTIMETER in converter.units
    assert UNIT_SI_METER in converter.units
    assert UNIT_SI_KILOMETER in converter.units


def test_quantity():
    converter = SILengthConverter()

    assert converter.quantity() == QUANTITY_SI_LENGTH


def test_supported_conversions():
    converter = SILengthConverter()

    supported_conversions = converter.supported_conversions()
    for source_unit, target_units in supported_conversions.items():
        for unit in SI_LENGTH_UNITS:
            if source_unit == unit:
                continue

            assert unit in target_units, "unit should've been supported [%s]" % unit


def test_is_convertible():
    converter = SILengthConverter()

    assert converter.is_convertible(UNIT_SI_METER, UNIT_SI_KILOMETER)
    assert converter.is_convertible(UNIT_SI_KILOMETER, UNIT_SI_CENTIMETER)
    assert converter.is_convertible(UNIT_SI_MILLIMETER, UNIT_SI_METER)
    assert converter.is_convertible(UNIT_SI_METER, UNIT_SI_METER)

    # ---

    not_quantity_unit = Unit('nqu', 'not quantity unit')
    assert not converter.is_convertible(UNIT_SI_METER, not_quantity_unit)
    assert not converter.is_convertible(UNIT_SI_KILOMETER, not_quantity_unit)
    assert not converter.is_convertible(not_quantity_unit, UNIT_SI_MILLIMETER)
    assert not converter.is_convertible(not_quantity_unit, UNIT_SI_CENTIMETER)

    not_time_unit = QuantityUnit('ntu', 'not time unit', None)
    assert not converter.is_convertible(UNIT_SI_KILOMETER, not_time_unit)
    assert not converter.is_convertible(UNIT_SI_CENTIMETER, not_time_unit)
    assert not converter.is_convertible(not_time_unit, UNIT_SI_MILLIMETER)
    assert not converter.is_convertible(not_time_unit, UNIT_SI_METER)


def test_meter_to_meter():
    converter = SILengthConverter()

    assert converter.convert(UNIT_SI_METER, 1, UNIT_SI_METER) == 1
    assert converter.convert(UNIT_SI_METER, 15, UNIT_SI_METER) == 15


def test_meter_to_centimeter():
    converter = SILengthConverter()

    assert converter.convert(UNIT_SI_METER, 1, UNIT_SI_CENTIMETER) == 100
    assert converter.convert(UNIT_SI_METER, 5, UNIT_SI_CENTIMETER) == 500
    assert converter.convert(UNIT_SI_METER, 20, UNIT_SI_CENTIMETER) == 2000


def test_centimeter_to_meter():
    converter = SILengthConverter()

    assert converter.convert(UNIT_SI_CENTIMETER, 350, UNIT_SI_METER) == 3.5
    assert converter.convert(UNIT_SI_CENTIMETER, 200, UNIT_SI_METER) == 2


def test_centimeter_to_millimeter():
    converter = SILengthConverter()

    assert converter.convert(UNIT_SI_CENTIMETER, 1, UNIT_SI_MILLIMETER) == 10
    assert converter.convert(UNIT_SI_CENTIMETER, 2.5, UNIT_SI_MILLIMETER) == 25


def test_kilometer_to_meter():
    converter = SILengthConverter()

    assert converter.convert(UNIT_SI_KILOMETER, 1, UNIT_SI_METER) == 1000
    assert converter.convert(UNIT_SI_KILOMETER, 1.5, UNIT_SI_METER) == 1500

