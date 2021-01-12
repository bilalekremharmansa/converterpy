class Converter(object):

    def supported_conversions(self):
        raise NotImplementedError()

    def is_convertible(self, source_unit, target_unit):
        raise NotImplementedError()

    def convert(self, source_unit, source_value, target_unit):
        raise NotImplementedError()
