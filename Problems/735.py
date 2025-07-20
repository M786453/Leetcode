class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        st = []

        for a in asteroids:

            while st and a < 0 < st[-1]:

                if -a > st[-1]:
                    st.pop()
                    continue
                elif -a == st[-1]:
                    st.pop()
                break

            else:
                st.append(a)    
        
        return st
    
if __name__ == "__main__":

    ss = Solution()

    print("Answer:",ss.asteroidCollision([-2,-1,1,2]))