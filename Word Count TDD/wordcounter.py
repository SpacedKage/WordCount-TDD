class WordCounter:
    def count_words(self, sentence):
        if sentence == ""
        return 0

        sentence = " ".join([x for x in sentence.split(" ") if len(x)>0])
        ptint(sentence)
       # parts = sentence.split()
       count = 0
       for char in sentence:
           if char == " ":
               count += 1
       return count + 1

        #return len(parts)