python
# Import the csv module to read and write csv files
import csv
import pandas as pd
import zipfile

with zipfile.ZipFile ("data.zip") as z:
  for filename in z.namelist ():
    with z.open (filename) as f:
      df = pd.read_csv (f) 
      
# Define a function to sort books by ISBN number
def sort_by_isbn(books):
  # Use the sorted function with a lambda expression to sort the books list by the first element of each sublist, which is the ISBN number
  return sorted(books, key=lambda book: book[0])

# Define a function to sort books by author name
def sort_by_author(books):
  # Use the sorted function with a lambda expression to sort the books list by the second element of each sublist, which is the author name
  return sorted(books, key=lambda book: book[1])

# Open the books.csv file in read mode
with open("books.csv", "r") as infile:
  # Create a csv reader object to read the file
  reader = csv.reader(infile)
  # Skip the header row
  next(reader)
  # Create an empty list to store the books data
  books = []
  # Loop through each row in the file
  for row in reader:
    # Append each row as a sublist to the books list
    books.append(row)

# Call the sort_by_isbn function and store the result in a new list
books_by_isbn = sort_by_isbn(books)

# Call the sort_by_author function and store the result in a new list
books_by_author = sort_by_author(books)

# Open a new file in write mode to store the sorted books by ISBN number
with open("books_by_isbn.csv", "w") as outfile:
  # Create a csv writer object to write to the file
  writer = csv.writer(outfile)
  # Write the header row
  writer.writerow(["ISBN", "Author", "Title"])
  # Write each book as a row to the file
  for book in books_by_isbn:
    writer.writerow(book)

# Open a new file in write mode to store the sorted books by author name
with open("books_by_author.csv", "w") as outfile:
  # Create a csv writer object to write to the file
  writer = csv.writer(outfile)
  # Write the header row
  writer.writerow(["ISBN", "Author", "Title"])
  # Write each book as a row to the file
  for book in books_by_author:
    writer.writerow(book)
