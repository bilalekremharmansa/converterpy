from converter.unit import Unit


class QuantityUnit(Unit):

    def __init__(self, shortname, fullname, quantity):
        super(QuantityUnit, self).__init__(shortname, fullname)
        self._quantity = quantity

    # time[seconds, minutes] # length[centimetre, meter]
    def quantity(self):
        return self._quantity
