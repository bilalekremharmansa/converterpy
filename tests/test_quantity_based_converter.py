from tests.helper import *


def test_init():
    converter = MockQuantityBasedConverter()

    assert converter.base_unit == UNIT_SEC


def test_supported_conversions():
    converter = MockQuantityBasedConverter()

    supported_conversions = converter.supported_conversions()
    for source_unit, target_units in supported_conversions.items():
        for unit in MOCK_UNITS:
            if source_unit == unit:
                continue

            assert unit in target_units, "unit should've been supported [%s]" % unit


def test_supported_conversions_2():
    converter = MockQuantityBasedConverter()

    supported_conversions = converter.supported_conversions()
    assert UNIT_SEC in supported_conversions[UNIT_MIN]
    assert UNIT_MIN in supported_conversions[UNIT_MIN]
    assert UNIT_HOUR in supported_conversions[UNIT_MIN]


def test_is_convertible():
    converter = MockQuantityBasedConverter()

    assert converter.is_convertible(UNIT_SEC, UNIT_MIN)
    assert converter.is_convertible(UNIT_SEC, UNIT_HOUR)

    assert converter.is_convertible(UNIT_MIN, UNIT_HOUR)
    assert converter.is_convertible(UNIT_HOUR, UNIT_MIN)

    assert not converter.is_convertible(UNIT_SEC, UNIT_IRRELEVANT)
    assert not converter.is_convertible(UNIT_MIN, UNIT_IRRELEVANT)

    assert not converter.is_convertible(UNIT_IRRELEVANT, UNIT_SEC)
    assert not converter.is_convertible(UNIT_IRRELEVANT, UNIT_MIN)


def test_convert():
    converter = MockQuantityBasedConverter()

    assert converter.convert(UNIT_SEC, 60, UNIT_MIN) == 1
    assert converter.convert(UNIT_MIN, 60, UNIT_HOUR) == 1
    assert converter.convert(UNIT_HOUR, 1, UNIT_MIN) == 60
    assert converter.convert(UNIT_HOUR, 1, UNIT_SEC) == 3600
