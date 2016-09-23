
class Clock(object):
    """docstring for Clock."""
    def __init__(self, hour, minutes):
        super(Clock, self).__init__()
        self.setup(hour, minutes)

    def setup(self, hour, minutes):
        # to make sure the time is valid
        self.minute     = minutes%60
        self.min_carry  = minutes//60
        self.hour       = hour + self.min_carry
        self.hour       = self.hour%24
        # Don't know if this is needed yet.
        # probably not...
        #self.hour_carry = hour//24
        self.build()


    def add(self, val):
        self.minute += val
        self.setup(self.hour, self.minute)
        return self.t


    def build(self):
        self.t = '{:02}:{:02}'.format(self.hour, self.minute)
        #print(self.t)

    def __str__(self):
        return self.t

    def __repr__(self):
        return self.t
