# your code goes here!

class Anagram:
    


    def __init__(self, word = "word"):
        self.word = word


    def match(self, word_list):

        result = []

        for word in word_list:
            if sorted(self.word.lower()) == sorted(word.lower()):
                result.append(word)

        return result




#  anagrams = [word for word in word_list if sorted(self.word.lower()) == sorted(word.lower())]
        

#   sorted(self.word.lower()) == sorted(word.lower()) and self.word.lower() != word.lower()

        





















# class Anagram:
#     def __init__(self, word):
#         self.word = word

#     def match(self, word_list):
#         return [word for word in word_list if self.is_anagram(word)]

#     def is_anagram(self, word):
#         return sorted(self.word.lower()) == sorted(word.lower()) and self.word.lower() != word.lower()
