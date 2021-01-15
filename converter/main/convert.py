import logging
import sys

from converter.adapter import ConverterTextAdapter
from converter.cli import Cli

from converter.exception import SuitableConverterNotFoundException, MultipleSuitableConverterException
from converter.util.logger import LogManager, LEVEL_OUT

# ---- built-in converters
from converter.converter.si.time_converter import SITimeConverter
from converter.converter.si.length_converter import SILengthConverter
from converter.converter.si.mass_converter import SIMassConverter
from converter.converter.TimestampToDateConverter import TimestampToDateConverter


class ConvertMain(object):

    def __init__(self, logger, converters):
        self.converters = [ConverterTextAdapter(converter) for converter in converters]
        self.logger = logger

    def find_suitable_converters_to_convert(self, source_selector, target_selector):
        assert isinstance(source_selector, str)
        assert isinstance(target_selector, str)

        return [c for c in self.converters if c.is_convertible(source_selector, target_selector)]

    def find_converter(self, source_selector, target_selector):
        suitable_converters = self.find_suitable_converters_to_convert(source_selector, target_selector)

        if len(suitable_converters) == 0:
            raise SuitableConverterNotFoundException("Suitable converter not found for for source [%s] and target [%s] "
                                                     "selectors" % (source_selector, target_selector))
        elif len(suitable_converters) > 1:
            raise MultipleSuitableConverterException("More than one converter found found for source [%s] and target "
                                                     "[%s] selectors, found: [%s]" % (source_selector, target_selector,
                                                                                      suitable_converters))

        return suitable_converters[0]

    def convert(self, source_selector, source_value, target_selector):
        converter = self.find_converter(source_selector, target_selector)

        self.logger.debug('Converter [%s] is selected for conversion [%s] to [%s]' %
                          (converter.name, source_selector, target_selector))

        return converter.convert(source_selector, source_value, target_selector)


def main():
    args = sys.argv

    # be initializer of logger to set log_format
    logger_name = LogManager.DEFAULT_LOGGER_NAME
    logger = LogManager.create_logger(name=logger_name, level=LEVEL_OUT, log_format='%(message)s')

    cli = Cli(logger)
    args = cli.parse(args[1:])

    # ------

    if args.get('help', False):
        logger.out(cli.usage())
        exit(0)

    if args.get('verbose', False):
        LogManager.override_format(logger_name, LogManager.DEFAULT_LOG_FORMAT)
        LogManager.override_log_level(logger_name, logging.DEBUG)

    # ------

    source_value = args['value']
    source_selector = args['source']
    target_selector = args['target']

    # ------

    converters = [
        SITimeConverter(),
        SILengthConverter(),
        SIMassConverter(),
        TimestampToDateConverter(),
    ]
    result_value = ConvertMain(logger, converters).convert(source_selector, source_value, target_selector)
    logger.out(result_value)


if __name__ == "__main__":
    main()
