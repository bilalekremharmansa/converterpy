from converter.util import logger as loggerutils


class Converter(object):

    def __init__(self, name):
        self.name = name
        self.logger = loggerutils.create_logger(name)

    def supported_conversions(self):
        raise NotImplementedError()

    def is_convertible(self, source_unit, target_unit):
        raise NotImplementedError()

    def convert(self, source_unit, source_value, target_unit):
        raise NotImplementedError()

    # ----

    def __repr__(self):
        return 'Converter{%s}' % self.name
