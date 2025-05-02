class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        stack = []
        
        for el in s:
            if el == '..':
                if stack:
                    stack.pop()
            elif el == '' or el == '.':
                continue
            else:
                stack.append(el)

        return '/'+'/'.join(stack)
