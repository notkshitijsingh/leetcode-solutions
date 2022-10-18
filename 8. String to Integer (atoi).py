class Solution:
    def myAtoi(self, s: str) -> int:
        # step 1
        # read and remove leading white spaces
        s = list(s)
        if len(s) != 0:
            while s[0] == ' ':
                s.pop(0)
                if len(s) == 0:
                    break
        # step 2
        # checking for +/- sign
        if len(s) != 0:
            if s[0] == "-":
                sign = -1
                s.pop(0)
            elif s[0] == "+":
                sign = 1
                s.pop(0)
            else:
                sign = 1

        # step 3
        # converting digits to number
        if len(s) != 0:
            strnum = []
            num = ''
            while s[0] in [str(i) for i in range(10)]:
                strnum.append(s[0])
                s.pop(0)
                if len(s) == 0:
                    break
            if len(strnum) == 0:
                num = 0
            else:
                for i in strnum:
                    num += i
                num = int(num)
        # final num
            num *= sign

        # step 4
        # check for 32-bit range
            if num > (2**31)-1:
                num = (2**31)-1
            elif num < -1*(2**31):
                num = -1*(2**31)
        else:
            num = 0

        return num
