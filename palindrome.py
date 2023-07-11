class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        front = 0
        end = len(x) - 1
        palindrome = True
        while front <= end:
            if x[front] != x[end]:
                palindrome = False
            front += 1
            end -= 1
        return (palindrome)
x = Solution()
y = x.isPalindrome(input())
print(y)