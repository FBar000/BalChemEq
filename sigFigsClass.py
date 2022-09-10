
# Built-in namespace
import decimal

# Extended subclass
class sfFloat(float):
    def __init__(self, value):
        self.value = float(value)
        self.sf = self.find_sigfigs()
        self.mantissa = abs(decimal.Decimal(self.value).as_tuple().exponent)

    
    def __add__(self, other):
        mantissa_len = min(self.mantissa, other.mantissa)
        tmp = self.value + other.value
        return round(tmp, mantissa_len)
    
    def __mul__(self, other):
        sf = min(self.sf, other.sf)
        tmp = str(self.value * other.value)
        return float(tmp[:sf])

    def __truediv__(self, other):
        sf = min(self.sf, other.sf)
        tmp = str(self.value / other.value)
        return float(tmp[:sf])

    def find_sigfigs(self):
        """CREDIT: durden2.0 on StackOverflow"""
        """Returns the number of significant digits in a number"""
        # Turn it into a float first to take into account stuff in exponential
        # notation and get all inputs on equal footing. Then number of sigfigs is
        # the number of non-zeros after stripping extra zeros to left of whole
        # number and right of decimal
        self = repr(float(self))
        tokens = self.split('.')
        whole_num = tokens[0].lstrip('0')
        if len(tokens) > 2:
            raise ValueError('Invalid number "%s" only 1 decimal allowed' % (self))
        if len(tokens) == 2:
            decimal_num = tokens[1].rstrip('0')
            return len(whole_num) + len(decimal_num)
        return len(whole_num)


print(sfFloat(sfFloat(2.5)))