class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        str_b=bin(n)[2:]
        str=str_b.zfill(32)
        return int('0b'+str[::-1],2)