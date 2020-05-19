class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fb_list = []
        for number in range(n+1):
            if number > 0:
                fb_list.append(number)
            for n in fb_list:
                if n % 3 == 0 and n % 5 == 0:
                    n = "FizzBuzz"
                    continue
                elif n % 3 == 0:
                    n = "Fizz"
                elif n % 5 == 0:
                    n = "Buzz"
                else:
                    n = str(n)
            return fb_list
    
    