# Week 3 Activity 2 - Write a code that counts the number of words in a demo text file (lorenzoagaloos-270729354)


class TextFileWordCounter:
    def __init__(self, file_path):
        self.file_path = file_path
  
    def count_words(self):
        file = open(self.file_path, 'r', encoding='utf-8')
        data = file.read()
        file.close()
        
        # Count words
        words = data.split()
        word_count = len(words)
        
        print(f"\nThe number of words in the text file is: {word_count}\n")
        return word_count
    
  
if __name__ == "__main__":
    
    # Count words in the file
    file_handler = TextFileWordCounter("Week3/demo_count.txt")
    TextFileWordCounter.count_words(file_handler)
        