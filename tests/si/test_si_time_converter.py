from converter.si.time_converter import *
from converter.unit import Unit


def test_init():
    converter = SITimeConverter()

    assert converter is not None


def test_base_unit():
    converter = SITimeConverter()

    assert converter.base_unit == UNIT_SI_SECOND


def test_time_units():
    converter = SITimeConverter()

    assert UNIT_SI_SECOND in converter.units
    assert UNIT_SI_MINUTE in converter.units
    assert UNIT_SI_HOUR in converter.units


def test_quantity():
    converter = SITimeConverter()

    assert converter.quantity() == QUANTITY_SI_TIME


def test_supported_conversions():
    converter = SITimeConverter()

    supported_conversions = converter.supported_conversions()
    for source_unit, target_units in supported_conversions.items():
        for unit in SI_TIME_UNITS:
            if source_unit == unit:
                continue

            assert unit in target_units, "unit should've been supported [%s]" % unit


def test_is_unit_supported():
    converter = SITimeConverter()

    for si_unit in SI_TIME_UNITS:
        assert converter.is_unit_supported(si_unit)

    # ---

    notQuantityUnit = Unit('nqu', 'not quantity unit')
    assert not converter.is_unit_supported(notQuantityUnit)

    notTimeUnit = QuantityUnit('ntu', 'not time unit', None)
    assert not converter.is_unit_supported(notTimeUnit)


def test_seconds_to_seconds():
    converter = SITimeConverter()

    assert converter.convert(UNIT_SI_SECOND, 1, UNIT_SI_SECOND) == 1
    assert converter.convert(UNIT_SI_SECOND, 15, UNIT_SI_SECOND) == 15


def test_seconds_to_minutes():
    converter = SITimeConverter()

    assert converter.convert(UNIT_SI_SECOND, 60, UNIT_SI_MINUTE) == 1
    assert converter.convert(UNIT_SI_SECOND, 120, UNIT_SI_MINUTE) == 2
    assert converter.convert(UNIT_SI_SECOND, 600, UNIT_SI_MINUTE) == 10


def test_seconds_to_hours():
    converter = SITimeConverter()

    assert converter.convert(UNIT_SI_SECOND, 3600, UNIT_SI_HOUR) == 1
    assert converter.convert(UNIT_SI_SECOND, 5400, UNIT_SI_HOUR) == 1.5


def test_minutes_to_seconds():
    converter = SITimeConverter()

    assert converter.convert(UNIT_SI_MINUTE, 1, UNIT_SI_SECOND) == 60
    assert converter.convert(UNIT_SI_MINUTE, 5, UNIT_SI_SECOND) == 300


def test_minutes_to_minutes():
    converter = SITimeConverter()

    assert converter.convert(UNIT_SI_MINUTE, 1, UNIT_SI_MINUTE) == 1
    assert converter.convert(UNIT_SI_MINUTE, 30, UNIT_SI_MINUTE) == 30


def test_minutes_to_hours():
    converter = SITimeConverter()

    assert converter.convert(UNIT_SI_MINUTE, 60, UNIT_SI_HOUR) == 1
    assert converter.convert(UNIT_SI_MINUTE, 30, UNIT_SI_HOUR) == 0.5


def test_hours_to_seconds():
    converter = SITimeConverter()

    assert converter.convert(UNIT_SI_HOUR, 1, UNIT_SI_SECOND) == 3600
    assert converter.convert(UNIT_SI_HOUR, 0.25, UNIT_SI_SECOND) == 900


def test_hours_to_minutes():
    converter = SITimeConverter()

    assert converter.convert(UNIT_SI_HOUR, 1, UNIT_SI_MINUTE) == 60
    assert converter.convert(UNIT_SI_HOUR, 1.5, UNIT_SI_MINUTE) == 90


def test_hours_to_hours():
    converter = SITimeConverter()

    assert converter.convert(UNIT_SI_HOUR, 1, UNIT_SI_HOUR) == 1
    assert converter.convert(UNIT_SI_HOUR, 20, UNIT_SI_HOUR) == 20

