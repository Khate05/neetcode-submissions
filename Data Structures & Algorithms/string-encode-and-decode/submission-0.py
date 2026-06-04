class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            length = len(i)
            encoded_string += str(length) + "#" + i
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        while i < len(s):          
            j = i
            while s[j] != "#":     
                j += 1
            length = int(s[i:j])
            start = j + 1
            word = s[start : start + length]
            decoded_string.append(word)
            i = start + length
        return decoded_string

