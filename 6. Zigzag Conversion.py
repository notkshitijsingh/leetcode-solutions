''' OPTIMAL APPROACH '''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        list_of_items = [[] for i in range(numRows)]
        DOWN = -1
        i = 0
        if numRows == 1:
            return s
        for char in s:
            list_of_items[i].append(char)
            if i == 0 or i == numRows - 1:
                DOWN *= -1
            i += DOWN
        list_of_items = list(chain(*list_of_items))
        return ''.join(list_of_items)


'''THIS WAS MY OLDER APPROACH WHICH IS SIMPLER BUT'''
'''DID NOT PASS TIME COMPLEXITY'''
# # getting the first row
# first_row = []
# i = 0
# while i < len(s):
#     first_row.append(s[i])
#     i += 2*numRows - 2

# # getting the mid rows
# mid_rows = []
# for i in range(1, numRows-1):
#     while i < len(s):
#         mid_rows.append(s[i])
#         try:
#             j = i
#             if i > numRows:
#                 while j > numRows:
#                     j = j - (2*numRows - 2)
#             mid_term = i + (numRows - j - 1)*2
#             mid_rows.append(s[mid_term])
#         except:
#             pass
#         i += 2*numRows - 2

# # getting the last row
# last_row = []
# i = numRows - 1
# while i < len(s):
#     last_row.append(s[i])
#     i += 2*numRows - 2

# # final answer
# zigzag = first_row + mid_rows + last_row
# ans = ''
# for i in zigzag:
#   ans += i
# return ans
