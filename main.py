
class Library:

    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)

        lines = self.file.read().splitlines()

        for line in lines:
            book_info = line.split(", ")
            if len(book_info)>=2:
                book_name, author = book_info[:2]
                print(f"Book: {book_name}, Author: {author}")

    def add_book(self):
        book_name = input("Book name: ")
        author = input("Author: ")
        first_release = input("First Release Date: ")
        pages = input("Number of Pages: ")

        book_name = book_name.upper()
        author = author.upper()
        first_release = first_release.upper()
        pages = pages.upper()


        new_book = f"{book_name}, {author}, {first_release}, {pages}\n"
        self.file.write(new_book)

        self.file.close()
        self.file = open("books.txt","a+")

    def remove_book(self):
        remove_name = input("Enter the book title you want to remove: ")
        remove_name = remove_name.upper()

        self.file.seek(0)

        lines = self.file.readlines()

        updated_lines = [line for line in lines if remove_name not in line]

        # Rewrite the file with updated lines
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updated_lines)
        self.file.close()
        self.file = open("books.txt","a+")



lib = Library()

while True:
    print("*** MENU***\n1) List Books\n2) Add Book\n3) Remove Book\n***PRESS 'Q' TO EXIT THE PROGRAM")
    choice = input()
    choice = choice.upper()

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "Q":
        break
    else:
        print("Invalid choice. Try Again")