class ConversionNotSupportedException(Exception):

    def __init__(self, converter, source, target):
        super(ConversionNotSupportedException, self).__init__('Converter [%s] does not support conversion from [%s] to'
                                                              ' [%s]' % (converter.name, source, target))


class UnexpectedResultException(Exception):
    pass
