class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        for char in word:
            tmp = []
            # char
            if not res:
                tmp.append(char)
            else:
                for item in res:
                    tmp.append(item+char)
            # number
            if not res:
                tmp.append(str(1))
                for item in res:
                    if item[-1].isdigit():
                        tmp.append()