# Week 3 Activity 1 - Write a code that can open, read, over-write, and append a demo text file (lorenzoagaloos-270729354)

class TextFileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        file = open(self.file_path, 'r')
        data= file.read()
        file.close()
        print("The contents of the file is as follows:")
        print(data)

    def write_to_file(self, content):
        file = open(self.file_path, "w", encoding='utf-8')
        file.write(content)
        file.close()
        print("Content over-written successfully.")
    
    def append_to_file(self, content):
        file= open(self.file_path, "a", encoding='utf-8')
        file.write(content)
        file.close()
        print("\nContent appended successfully.")

def main():
    # Read current txt
    file_handler = TextFileHandler("Week3/demo_read.txt")
    content1 = file_handler.read_file()

    # Write to the file - uncomment the two line of codes below to call the write_to_file method
    # file_handler = TextFileHandler("Week3/demo_write.txt")
    # file_handler.write_to_file("Hello, this new line over-writes all the texts in the file.\nThis is another line.")

    # Append to the file - uncomment the two lines of codes below to call the append_to_file method
    # file_handler = TextFileHandler("Week3/demo_append.txt")
    # file_handler.append_to_file("\nThis is another appended line.")

if __name__ == "__main__":
    main()

    