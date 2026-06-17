#Problem No. 65 - Valid Number
class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        """
        :type s: str
        :rtype: bool
        """
#These are used to remember what we have already seen
        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i in range(len(s)):
            c = s[i]

            if c.isdigit():
                seen_digit = True
            elif c == '+' or c == '-':
                if i > 0 and s[i-1] not in ('e','E'):
                    return False
            elif c == '.':
                if seen_dot or seen_exp:
                    return False 
                seen_dot = True
            elif c == 'e' or c == 'E':
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False
            else:
                return False
        return seen_digit

        