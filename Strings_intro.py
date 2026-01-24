# Class containing the method to find string length
class Solution:

    def findLength(self, s):

        # printing last 3 letters
        st = s[-6:]
        
        return len(s), st

# Driver code
if __name__ == "__main__":

    obj = Solution()

    s = "Python is goated"

    print(obj.findLength(s))
