class Book():
    def __init__(self,title,author):
        self.title=title
        self.author=author


class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self,title,author)
        self.price = price

    def display(self):
        print('Title:', self.title)
        print('Author:', self.author)
        print('Price:', str(self.price))


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()