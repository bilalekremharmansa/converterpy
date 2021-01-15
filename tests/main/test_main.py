from converter.main.convert import ConvertMain
from converter.util.logger import LogManager
from tests.helper import NumberConverter, MockQuantityBasedConverter


logger = LogManager.get_logger()
number_converter = NumberConverter()
quantity_based_converter = MockQuantityBasedConverter()
converters = [
    number_converter,
    quantity_based_converter
]


def test_main():
    main = ConvertMain(logger, converters)

    assert len(main.converters) == len(converters)


def test_main_find_converter():
    main = ConvertMain(logger, converters)

    # -----

    number_adapter = main.find_converter('int', 'float')
    assert number_converter.name in number_adapter.name
    assert number_converter == number_adapter.realConverter

    # -----
    quantity_based_adapter = main.find_converter('seconds', 'minutes')
    assert quantity_based_converter.name in quantity_based_adapter.name
    assert quantity_based_converter == quantity_based_adapter.realConverter


def test_main_find_multiple_converters():
    number_converter2 = NumberConverter()
    converters2 = [number_converter2]
    converters2.extend(converters)

    main = ConvertMain(logger, converters2)
    suitable_converters = main.find_suitable_converters_to_convert('int', 'float')

    assert len(suitable_converters) == 2


def test_main_convert():
    main = ConvertMain(logger, converters)

    assert main.convert('int', 5, 'float') == 5.0
    assert main.convert('minutes', 5, 'seconds') == 300

