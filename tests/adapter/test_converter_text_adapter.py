from converterpy.adapter import ConverterTextAdapter
from tests.helper import *


def test_init():
    converter = MockQuantityBasedConverter()
    adapter = ConverterTextAdapter(converter)

    assert converter.name == adapter.name


def test_is_convertible():
    converter = MockQuantityBasedConverter()
    adapter = ConverterTextAdapter(converter)

    assert adapter.is_convertible('seconds', 'minutes')
    assert adapter.is_convertible('hours', 'minutes')
    assert adapter.is_convertible('hours', 'seconds')
    assert adapter.is_convertible('seconds', 'hours')
    assert adapter.is_convertible('minutes', 'minutes')

    # -----

    assert adapter.is_convertible('sec', 'min')
    assert adapter.is_convertible('min', 'h')
    assert adapter.is_convertible('h', 'sec')
    assert adapter.is_convertible('sec', 'h')
    assert adapter.is_convertible('min', 'min')
    assert adapter.is_convertible('sec', 'sec')

    # -----

    assert adapter.is_convertible('sec', 'minutes')
    assert adapter.is_convertible('hours', 'min')
    assert adapter.is_convertible('hours', 'sec')

    # -----

    assert not adapter.is_convertible('test', 'minutes')
    assert not adapter.is_convertible('hours', 'test')
    assert not adapter.is_convertible('test', 'seconds')
    assert not adapter.is_convertible('test', 'test')


def test_seconds_to_seconds():
    converter = MockQuantityBasedConverter()
    adapter = ConverterTextAdapter(converter)

    val = 10
    assert adapter.convert('seconds', val, 'seconds') == val
    assert adapter.convert('seconds', val, 'sec') == val
    assert adapter.convert('sec', val, 'seconds') == val
    assert adapter.convert('sec', val, 'sec') == val


def test_minutes_to_seconds():
    converter = MockQuantityBasedConverter()
    adapter = ConverterTextAdapter(converter)

    val = 10
    assert adapter.convert('minutes', val, 'seconds') == val * 60
    assert adapter.convert('minutes', val * 2, 'sec') == val * 2 * 60
    assert adapter.convert('min', val * 3, 'sec') == val * 3 * 60
    assert adapter.convert('min', val * 4, 'seconds') == val * 4 * 60


def test_hours_to_minutes():
    converter = MockQuantityBasedConverter()
    adapter = ConverterTextAdapter(converter)

    val = 1
    assert adapter.convert('hours', val, 'minutes') == val * 60
    assert adapter.convert('hours', val * 2, 'min') == val * 2 * 60
    assert adapter.convert('h', val * 3, 'min') == val * 3 * 60
    assert adapter.convert('h', val * 3, 'minutes') == val * 3 * 60


def test_is_source_unit_supported():
    converter = MockQuantityBasedConverter()
    adapter = ConverterTextAdapter(converter)

    assert adapter.is_source_unit_supported('sec')
    assert adapter.is_source_unit_supported('seconds')
    assert adapter.is_source_unit_supported('hours')

    assert not adapter.is_source_unit_supported('meter')
    assert not adapter.is_source_unit_supported('centimeter')
    assert not adapter.is_source_unit_supported('SECONDS')
    assert not adapter.is_source_unit_supported('second')


def test_all_convertible_target_units_are_convertible():
    converter = MockQuantityBasedConverter()
    adapter = ConverterTextAdapter(converter)

    def __test(source_selector):
        target_units = adapter.get_convertible_target_units(source_selector)
        for target_unit in target_units:
            assert adapter.is_convertible(source_selector, target_unit.shortname())
            assert adapter.is_convertible(source_selector, target_unit.fullname())

    __test('sec')
    __test('seconds')
    __test('hours')


def test_get_convertible_target_units():
    converter = MockQuantityBasedConverter()
    adapter = ConverterTextAdapter(converter)

    target_units = adapter.get_convertible_target_units('sec')
    assert target_units
    assert len(target_units) > 1
