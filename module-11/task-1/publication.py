class Publication:
    def __init__(self, name: str):
        self.name: str = name


class Book(Publication):
    def __init__(self, name: str, author: str, page_count: int):
        super().__init__(name)
        self.author: str = author
        self.page_count: int = page_count


    def print_information(self):
        print(f"Book name: {self.name}, Pages: {self.page_count}, Author: {self.author}")


class Magazine(Publication):
    def __init__(self, name: str, chief_editor: str):
        super().__init__(name)
        self.chief_editor: str = chief_editor


    def print_information(self):
        print(f"Magazine name: {self.name}, Chief editor: {self.chief_editor}")


# Debug
pub = Publication("Test Publication")
print(f"Publication: {pub.name}")

book = Book("Test Book", "Test Author", 150)
print(f"Book: {book.name} by {book.author}, {book.page_count} pages")

mag = Magazine("Test Magazine", "Test Editor")
print(f"Magazine: {mag.name}, chief editor: {mag.chief_editor}")

donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
print(f"Name: {donald_duck.name}, Chief Editor: {donald_duck.chief_editor}")

compartment = Book("Compartment No. 6", "Rosa Liksom", 192)
print(f"Name: {compartment.name}, Author: {compartment.author}, Pages: {compartment.page_count}")
