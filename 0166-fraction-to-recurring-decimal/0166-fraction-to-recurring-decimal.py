class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator * denominator < 0:
            sign = "-"
        else:
            sign = ""
        
        numerator, denominator = abs(numerator), abs(denominator)

        integer_part = numerator // denominator
        remainder = numerator % denominator
        if remainder == 0:
            return sign + str(integer_part)
        
        result = [sign + str(integer_part), '.']
        remainders = {}

        while remainder != 0:
            if remainder in remainders:
                result.insert(remainders[remainder], '(')
                result.append(')')
                break
            remainders[remainder] = len(result)
            numerator = remainder * 10
            result.append(str(numerator // denominator))
            remainder = numerator % denominator
        
        return ''.join(result)