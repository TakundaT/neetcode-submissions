class Solution:

    def encode(self, strs: List[str]) -> str:
        #need to create a delimer between each code, seperate strings
        #maintain an array to count the num characters in each word, not supposed to store state variable, store in string itself. #encode length of strong and delimiter before string
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + ";" + string
        return encoded 
    def decode(self, s: str) -> List[str]:
        res, i = [], 0 #i is position in the ecoded string, start at 0

        while i < len(s):
            j = i #position starts at0
            while s[j] != ";": #not at delimeter, starting an number
                j+=1
            length = int(s[i:j]) #from 0 up until the delimeter, excluding delimter
            res.append(s[j+1: j+length+1])
            i = j + 1 + length
        return res
        

