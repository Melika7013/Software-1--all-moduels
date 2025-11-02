# --- Publication Hierarchy ---

class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.page_count}\n")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"Chief Editor: {self.chief_editor}\n")


# --- Main program ---

def main():
    magazine = Magazine("Technology", "Melika Payandeh")
    book = Book("User Experience Design", "Saman Pourbarzegar", 220)

    magazine.print_information()
    book.print_information()


if __name__ == "__main__":
    main()
