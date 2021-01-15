from converterpy.provider import ConverterProvider

from tests.helper import NumberConverter, MockQuantityBasedConverter


class TestConverterProvider(ConverterProvider):

    def provide(self):
        return [
            NumberConverter(),
            MockQuantityBasedConverter()
        ]


def test_provide():
    assert len(TestConverterProvider().provide()) == 2