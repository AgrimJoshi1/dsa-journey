#Problem No. 412 - Fizz Buzz
from ast import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l1 = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                l1.append("FizzBuzz")
            elif i % 3 == 0:
                l1.append("Fizz")
            elif i % 5 == 0:
                l1.append("Buzz")
            else:
                l1.append(str(i))
        return l1
#Approach   
#Basic iteration and checking for divisibility by 3 and 5, if divisible by both then add "FizzBuzz" to the list, if divisible by only 3 then add "Fizz", if divisible by only 5 then add "Buzz", otherwise add the number as a string to the list. Finally return the list.