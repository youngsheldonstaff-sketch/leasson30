class WordReverser:
    def __init__(self, text):
    
        self.__text = text

    def get_result(self):
     
        words = []
        word = ""
        for char in self.__text:
            if char == " ":
                words.append(word)
                word = ""
            else:
                word += char
        words.append(word) 
        
       
        reversed_words = []
        for i in range(len(words) - 1, -1, -1):
            reversed_words.append(words[i])
            
       
        output = ""
        for i in range(len(reversed_words)):
            output += reversed_words[i]
            if i < len(reversed_words) - 1:
                output += " "
        return output

    def __str__(self):
       
        return self.get_result()


my_string = "Hello World"
reverser = WordReverser(my_string)
print(reverser) 