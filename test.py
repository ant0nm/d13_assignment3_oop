from book_lending import Book
from datetime import datetime
import random

# testing out the Book class
sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
print("Browsing for 2 books:")
print(Book.browse().title)
print(Book.browse().title)

print()
print("Number of books on shelf:")
print(len(Book.on_shelf))
print("Number of book on loan:")
print(len(Book.on_loan))

print()
print("Is `Sister Outside` lent out at the moment?")
print(sister_outsider.lent_out())

print()
print("Can `Sister Outsider` be borrowed?")
print(sister_outsider.borrow())

print()
print("Number of books on shelf:")
print(len(Book.on_shelf))
print("Number of books on loan:")
print(len(Book.on_loan))

print()
print("Is `Sister Outside` lent out at the moment?")
print(sister_outsider.lent_out())

print()
print("Can `Sister Outsider` be borrowed?")
print(sister_outsider.borrow())

print()
print("`Sister Outsider`'s due date:")
print(sister_outsider.due_date)

print()
print("Number of books overdue:")
print(len(Book.overdue()))

print()
print("Reduce `Sister Outsider`'s due date by 3 weeks:")
three_weeks = 60 * 60 * 24 * 21
new_timestamp = sister_outsider.due_date.timestamp() - three_weeks
sister_outsider.due_date = datetime.fromtimestamp(new_timestamp)
print(sister_outsider.due_date)

print()
print("Number of books overdue:")
print(len(Book.overdue()))

print()
print("Return `Sister Outsider` back to the library:")
print(sister_outsider.return_to_library())
print(sister_outsider.lent_out())
print(sister_outsider.due_date)

print()
print("Number of books overdue:")
print(len(Book.overdue()))

print()
print("Number of books on loan:")
print(len(Book.on_loan))
