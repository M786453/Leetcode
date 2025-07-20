class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        stack = []

        i = 0

        while i < len(asteroids)-1:

            stack.append(asteroids[i])

            print("Index:", i)
            print("Stack:", stack)
            print("Asteroids:", asteroids)

            if (stack[-1] < 0 and asteroids[i+1] > 0) or (stack[-1] > 0 and asteroids[i+1] < 0):
                
                if abs(stack[-1]) < abs(asteroids[i+1]):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroids[i+1]):
                    stack.pop()
                    i += 1


            print("Stack C:", stack)
            print("")
                
            i += 1
        
        return stack
    
if __name__ == "__main__":

    ss = Solution()

    print("Answer:",ss.asteroidCollision([-2,-1,1,2]))