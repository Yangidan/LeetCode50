# day 05 2019-05-14 Tue
# 8. String to Integer (atoi)
# This is a copy from discussion.
# Through this piece of code, I learned that this problem can be solved with graph.
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # A graph where vertices are states in a
        # DFA. Labeled edges lead to new vertices/
        # states. Edge labels correspond to how each
        # character in the string is classified.
        # NOTE: there is no state 4 even though there
        # might be more characters after ending
        # state 3
        graph = {
            1: {
                'blank': 1,
                'sign': 2,
                'digit': 3
            },
            2: {
                'digit': 3
            },
            3: {
                'digit': 3
            }
        }
        val = 0
        negative = False
        A = 1 << 31  # 2^31
        B = A // 10
        C = A % 10
        
        current_state = 1
        for c in str:
            if c == ' ':
                edge = 'blank'
            elif c.isdigit():
                edge = 'digit'
            elif c in ('-', '+'):
                edge = 'sign'
            else:
                edge = 'other'
                
            if edge not in graph[current_state]:
                break

            if edge == 'digit':
                # check for potential overflow/underflow
                if negative:
                    if val > B or val == B and int(c) > C:
                        return -A
                else:
                    if val > B or val == B and int(c) >= C:
                        return A - 1
                # it's now 'safe' to do the multiplication;
                # remembering that this is python and overflow
                # detection is just for fun.
                val = val * 10 + int(c)
                
            if current_state == 1 and edge == 'sign':
                negative = c == '-'
                
            current_state = graph[current_state][edge]

        if current_state == 3:
            return val * -1 if negative else val
        
        return 0