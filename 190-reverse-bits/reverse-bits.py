class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]  # Convert to binary string and remove '0b' prefix
        s = s.zfill(32)  # Pad with leading zeros to ensure 32-bit representation
        s = s[::-1]  # Reverse the binary string
        return int(s, 2)