class Book:
    def __init__(self, title, author, pages):
        self.title=title
        self.author=author
        self.pages=pages
    def check(self):
        if self.pages>300:
            f="You require a packet! The book is heavy."
        else:
            f="That's a light book!"
        return f

b=Book("Kafka on the Shore", "Haruki Murakami", 1500)
print(b.check())