class Solution:
   def calPoints(self, ops):
      stack = []
      for i in ops:
         if i == "+":
            first = stack[len(stack) - 1]
            second  = stack[len(stack) - 2]
            stack.append(first + second)
         elif i == "D":
            stack.append(stack[-1] * 2)
         elif i == "C":
            stack.pop()
         else:
            stack.append(int(i))
      return sum(stack)
ob = Solution()
print(ob.calPoints(["5","2","C","D","+"]))