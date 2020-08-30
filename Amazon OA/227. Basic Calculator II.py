class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        num, presign = 0, "+"
        for n in s + '+':
            if n.isdigit():
                num = num * 10 + int(n)
            elif n in '+-*/':
                if presign == '+':
                    stack.append(num)
                elif presign == '-':
                    stack.append(-num)
                elif presign == '*':
                    stack.append(stack.pop() * num)
                elif presign == '/':
                    stack.append(math.trunc(stack.pop() / num))
                presign = n
                num = 0
        return sum(stack)


