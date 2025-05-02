class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '+-*/'

        for el in tokens:
            if el in operators:
                el2 = int(stack.pop())
                el1 = int(stack.pop())
                if el == '+':
                    new_ex = el1 + el2
                elif el =='-':
                    new_ex = el1 - el2
                elif el == '*':
                    new_ex = el1 * el2
                elif el == '/':
                    new_ex = abs(el1) // abs(el2)
                    if el1 < 0 and el2 < 0:
                        pass
                    elif el1 < 0 or el2 < 0:
                        new_ex = -new_ex
                stack.append(new_ex)
            else:
                stack.append(el)
        
        return int(stack[0])