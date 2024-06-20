class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        A = A.strip()  # Remove leading/trailing whitespace
        if len(A) == 0:
            return 0

        sign = 1
        if A[0] == '-':
            sign = -1
            A = A[1:]
        elif A[0] == '+':
            A = A[1:]

        ans = 0
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        for char in A:
            if not char.isdigit():
                break
            ans = ans * 10 + int(char)
            # Check for overflow
            if sign == -1 and -ans < MIN_INT:
                return MIN_INT
            if sign == 1 and ans > MAX_INT:
                return MAX_INT

        return sign * ans
