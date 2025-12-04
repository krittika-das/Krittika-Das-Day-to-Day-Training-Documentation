class Library:
    def __init__(self):
        self.books=[]

    def add_books(self, title, author):
        self.books.append({"title": title, "author": author})
    def search(self, keyword):
        result=[]
        for book in self.books:
            if keyword in book["title"]:
                result.append(book)
        return result

lib=Library()
lib.add_books("Kafka on the Shore", "Haruki Murakami")
lib.add_books("Atomic Habits", "DN")

print(lib.search("Kafka on the Shore"))
