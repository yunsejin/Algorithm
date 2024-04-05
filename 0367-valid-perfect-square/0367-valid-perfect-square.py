class Solution(object):
    def isPerfectSquare(self, num):
        if num < 2:
            return True
        left, right = 2, num // 2
        while left <= right:
            mid = (left + right) // 2
            guessed_square = mid * mid
            if guessed_square == num:
                return True
            elif guessed_square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False