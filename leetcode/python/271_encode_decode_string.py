class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str

        allocate first 8 bit to length of string

        """
        res = ""
        for string in strs:
            length = len(string)
            res += format(length, '08d') + str(string)
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        index = 0
        res = []
        while index < len(s):
            length = int(s[index:index+8])
            index += 8
            string = s[index:index+length]
            index += length
            res.append(string)
        return res


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(strs))

codec = Codec()
a = codec.encode(['', 'asdf', '2341', '#@%$%'])
print codec.decode(a)