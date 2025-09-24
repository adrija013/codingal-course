class Library:

    def __init__(self, list_of_books, name):
        self.booksList = list_of_books
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")  
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.booksList:
            print("Sorry, we do not have that book.")  
        elif book in self.lendDict:
             print(f"The book is already being used by {self.lendDict[book]}.") 
        else:
            self.lendDict[book] = user
            print(
                "Lender-Book database has been updated. You can take the book now."
            )
    def addBook(self, book):
        if book not in self.booksList:
            self.booksList.append(book)
            print(f"{book} has been added to the book list.")
        else:
                print(f"{book} already exists in library.")

    def addBook(self, book):
        if book not in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned.")
        else:
                print("That book wasn't borrowed from us.")

if __name__ == '__main__':
     books = Library(['Python',
                      'Rich dad Poor dad',
                      'Harry Potter',
                      'C++ basics',
                      'Algorithms by CLRS'], "Let's Upskill")
     
     user_name = input("Welcome to our library! Please enter your name: ")

     while True:
          print(f"\nHello {user_name}, welcome to the {books.name} library. Please choose an option:")
          print("1. Display Books\n2.Lend a book\n3. Add a book\n4. Return a book\n5. Quit" )
          user_choice = input("Enter your choice to continue: ")

          