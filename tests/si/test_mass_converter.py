from converter.converter.si.mass_converter import *
from converter.unit import Unit


def test_init():
    converter = SIMassConverter()

    assert converter is not None


def test_base_unit():
    converter = SIMassConverter()

    assert converter.base_unit == UNIT_SI_GRAM


def test_units():
    converter = SIMassConverter()

    assert UNIT_SI_MILLIGRAM in converter.units
    assert UNIT_SI_GRAM in converter.units
    assert UNIT_SI_KILOGRAM in converter.units


def test_quantity():
    converter = SIMassConverter()

    assert converter.quantity() == QUANTITY_SI_MASS


def test_supported_conversions():
    converter = SIMassConverter()

    supported_conversions = converter.supported_conversions()
    for source_unit, target_units in supported_conversions.items():
        for unit in SI_MASS_UNITS:
            if source_unit == unit:
                continue

            assert unit in target_units, "unit should've been supported [%s]" % unit


def test_is_convertible():
    converter = SIMassConverter()

    assert converter.is_convertible(UNIT_SI_GRAM, UNIT_SI_KILOGRAM)
    assert converter.is_convertible(UNIT_SI_KILOGRAM, UNIT_SI_MILLIGRAM)
    assert converter.is_convertible(UNIT_SI_MILLIGRAM, UNIT_SI_GRAM)
    assert converter.is_convertible(UNIT_SI_MILLIGRAM, UNIT_SI_KILOGRAM)

    # ---

    not_quantity_unit = Unit('nqu', 'not quantity unit')
    assert not converter.is_convertible(UNIT_SI_GRAM, not_quantity_unit)
    assert not converter.is_convertible(UNIT_SI_KILOGRAM, not_quantity_unit)
    assert not converter.is_convertible(not_quantity_unit, UNIT_SI_MILLIGRAM)
    assert not converter.is_convertible(not_quantity_unit, UNIT_SI_MILLIGRAM)

    not_mass_unit = QuantityUnit('ntu', 'not mass unit', None)
    assert not converter.is_convertible(UNIT_SI_KILOGRAM, not_mass_unit)
    assert not converter.is_convertible(UNIT_SI_GRAM, not_mass_unit)
    assert not converter.is_convertible(not_mass_unit, UNIT_SI_MILLIGRAM)
    assert not converter.is_convertible(not_mass_unit, UNIT_SI_GRAM)


def test_gram_to_gram():
    converter = SIMassConverter()

    assert converter.convert(UNIT_SI_GRAM, 1, UNIT_SI_GRAM) == 1
    assert converter.convert(UNIT_SI_GRAM, 15, UNIT_SI_GRAM) == 15


def test_gram_to_milligram():
    converter = SIMassConverter()

    assert converter.convert(UNIT_SI_GRAM, 1, UNIT_SI_MILLIGRAM) == 1000
    assert converter.convert(UNIT_SI_GRAM, 5, UNIT_SI_MILLIGRAM) == 5000
    assert converter.convert(UNIT_SI_GRAM, 2.5, UNIT_SI_MILLIGRAM) == 2500


def test_milligram_to_gram():
    converter = SIMassConverter()

    assert converter.convert(UNIT_SI_MILLIGRAM, 360, UNIT_SI_GRAM) == 0.36
    assert converter.convert(UNIT_SI_MILLIGRAM, 200, UNIT_SI_GRAM) == 0.2


def test_gram_to_kilogram():
    converter = SIMassConverter()

    assert converter.convert(UNIT_SI_GRAM, 1000, UNIT_SI_KILOGRAM) == 1
    assert converter.convert(UNIT_SI_GRAM, 4750, UNIT_SI_KILOGRAM) == 4.75


def test_kilogram_to_milligram():
    converter = SIMassConverter()

    assert converter.convert(UNIT_SI_KILOGRAM, 0.01, UNIT_SI_MILLIGRAM) == 10000
    assert converter.convert(UNIT_SI_KILOGRAM, 0.44, UNIT_SI_MILLIGRAM) == 440000

