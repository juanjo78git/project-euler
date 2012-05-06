#! /usr/bin/python2

def p17():
    def lowest_digit(n):
        return n/10, n%10
    def words(n):
        if n > 999:
            raise ValueError, "Number too big."
 
        digits = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                  'eight', 'nine']
 
        teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                 'sixteen', 'seventeen', 'eighteen', 'nineteen']
 
        tens = [None, None, 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
                'seventy', 'eighty', 'ninety']
 
        n, o = lowest_digit(n)
        n, t = lowest_digit(n)
        n, h = lowest_digit(n)
 
        result = []
 
        if t == 1:
            result.append(teens[o])
        else:
            if o:
                result.append(digits[o])
            if t:
                result.append(tens[t])
 
        if h:
            if t or o:
                result.append('and')
            result.append('hundred')
            result.append(digits[h])
 
        #return ''.join(reversed(result))
        #print ''.join(result)
        return ''.join(result)
 
    c = 0
    for i in range(1,1000):
        c += len(words(i))
    c+=len('onethousand')
    print c
 
p17()
