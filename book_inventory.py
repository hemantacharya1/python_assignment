bookList = []

def main():
    print("Program started:")
    addBook("Atomic Habits","James Clear")
    addBook("Clean Code","Robert C. Martin")
    getInventory()
    print("searching a book:","Clean Code")
    searchBook("Clean Code")
def addBook(book,author):
    bookList.append({"book":book,"author":author})
    print("Book added successfully:",book)

def getInventory():
    for i,book in enumerate(bookList,start=1):
        print(f"- Book: {book['book']} | Author: {book['author']}")

def searchBook(bookName):
    for i in bookList:
        if i['book'].lower()==bookName.lower():
            print("Found the book: ",i['book'],"written by",i['author'])
            return
    
    print("Not found the book",bookName)


if __name__ == "__main__":
    main()