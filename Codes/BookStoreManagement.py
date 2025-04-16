def add_book(library: list, title: str, author: str):
    book_id = len(library) + 1
    library.append({"id": book_id, "title": title, "author": author, "available": True})

def remove_book(library: list, book_id: int):
    if book_id in range(1,len(library)+1):
        library[book_id-1]["available"]=False
            

def borrow_book(library: list, book_id: int):
    if book_id in range(1,len(library)+1) and library[book_id-1]["available"]:
        library[book_id-1]["available"] = False
        return f'You have borrowed "{library[book_id-1]["title"]}".'
    else:
        return "Book not available."
    

def return_book(library: list, book_id: int):
    if book_id in range(1,len(library)+1) and not library[book_id-1]["available"]:
        library[book_id-1]["available"] = True
        return f'You have returned "{library[book_id-1]["title"]}".'
    else:
        return "Book not found or already returned!"


num_books, num_borrowed, num_returned, num_removed=list(map(int, input().split()))
ans = []
library = []

for _ in range(num_books):
    title, author = input().split(": ")
    add_book(library, title, author)

if(num_borrowed>0):    
    ids=input().split()
    for book_id in ids:
        ans.append(borrow_book(library, int(book_id)))
if(num_returned>0):
    ids=input().split()
    for book_id in ids:
        ans.append(return_book(library, int(book_id)))
if(num_removed>0):
    ids=input().split()
    for book_id in ids:
        remove_book(library, int(book_id))

ans.append(sum(int(book["available"]) for book in library))

for k in ans:
    print(k)
