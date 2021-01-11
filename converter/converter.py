class Converter(object):

    def supported_conversions(self):
        raise NotImplementedError()

    def is_unit_supported(self, unit):
        raise NotImplementedError()

    def convert(self, source_unit, source_value, target_unit):
        raise NotImplementedError()
