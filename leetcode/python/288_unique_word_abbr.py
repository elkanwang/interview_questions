class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self. dict = {}
        for word in dictionary:
            abbr = self.process_word(word)
            if abbr not in self.dict:
                self.dict[abbr] = [1, [word]]
            else:
                if word not in self.dict[abbr][1]:
                    self.dict[abbr][0] += 1
                    self.dict[abbr][1].append(word)


    def process_word(self, word):
        word_len = len(word)
        if word_len < 3:
            return word
        else:
            return word[0] + str(word_len - 2) + word[-1]

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.process_word(word)
        if abbr not in self.dict:
            return True
        elif self.dict[abbr][0] == 1 and word in self.dict[abbr][1]:
            return True
        else:
            return False



# Your ValidWordAbbr object will be instantiated and called as such:
vwa = ValidWordAbbr(['dog'])
print vwa.isUnique("dig")
print vwa.isUnique("dug")
print vwa.isUnique("dog")
print vwa.isUnique("doge")