from converterpy.main.convert import ConvertMain, Config
from converterpy.provider import ConverterProvider
from converterpy.util.logger import LogManager
from tests.helper import NumberConverter, MockQuantityBasedConverter


class TestConverterProvider(ConverterProvider):

    def provide(self):
        return [
            number_converter,
            quantity_based_converter
        ]

# ------


logger = LogManager.get_logger()
number_converter = NumberConverter()
quantity_based_converter = MockQuantityBasedConverter()
converters = [
    number_converter,
    quantity_based_converter
]

config = Config(use_built_in_provider=False)
provider = TestConverterProvider()


def create_main():
    main = ConvertMain(logger, config)
    main.provide_converters(provider)
    return main


def test_main():
    main = create_main()

    assert len(main.converters) == len(converters)


def test_init_providers():
    custom_provider_config = []
    config_1 = Config(custom_provider_config, use_built_in_provider=False)
    main_1 = ConvertMain(logger, config_1)

    assert len(main_1.converters) == 0

    # ------

    custom_provider_config = [
        {
            "base_path": ".",
            "module_name": "converterpy.provider.builtin",
            "class_name": "BuiltinConverterProvider"
        }
    ]

    config_2 = Config(custom_provider_config, use_built_in_provider=False)
    main_2 = ConvertMain(logger, config_2)

    assert len(main_2.converters) > 0


def test_main_find_converter():
    main = create_main()

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

    main = create_main()
    main.add_converters([number_converter2])
    suitable_converters = main.find_suitable_converters_to_convert('int', 'float')

    assert len(suitable_converters) == 2


def test_main_convert():
    main = create_main()

    assert main.convert('int', 5, 'float') == 5.0
    assert main.convert('minutes', 5, 'seconds') == 300

