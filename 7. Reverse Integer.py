class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            y = int(str(x)[::-1])
        elif x < 0:
            z = list(str(x))
            z.pop(0)
            y = ''
            for i in z:
                y += i
            y = int(y[::-1])*-1
        else:
            y = x
        if y not in range(-2**31, 2**31):
            y = 0
        return y
