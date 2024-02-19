import tkinter as tk

class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.file = open(self.filename, "a+",encoding="utf-8")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        books_info = []
        for line in lines:
            book_info = line.split(',')
            books_info.append(f"Book: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Number of Pages: {book_info[3]}")
        return "\n".join(books_info)

    def add_book(self, title, author, release_year, num_pages):
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        return f"Book '{title}' added successfully!"

    def remove_book(self, title_to_remove):
        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()

        for line in lines:
            if title_to_remove not in line:
                self.file.write(line)

        return f"Book '{title_to_remove}' removed successfully!"

def list_books_command():
    result = lib.list_books()
    text_output.config(state=tk.NORMAL)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)
    text_output.config(state=tk.DISABLED)

def add_book_command():
    title = entry_title.get()
    author = entry_author.get()
    release_year = entry_release_year.get()
    num_pages = entry_num_pages.get()
    result = lib.add_book(title, author, release_year, num_pages)
    text_output.config(state=tk.NORMAL)
    text_output.insert(tk.END, result + "\n")
    text_output.config(state=tk.DISABLED)

def remove_book_command():
    title_to_remove = entry_remove_title.get()
    result = lib.remove_book(title_to_remove)
    text_output.config(state=tk.NORMAL)
    text_output.insert(tk.END, result + "\n")
    text_output.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Library Management System")

lib = Library()

# Pencere boyutunu 600x500 olarak ayarla
root.geometry("600x500")

label_title = tk.Label(root, text="Title:",bg="black", fg="white")
label_title.grid(row=0, column=0, padx=10, pady=5)

label_author = tk.Label(root, text="Author:",bg="black", fg="white")
label_author.grid(row=1, column=0, padx=10, pady=5)

label_release_year = tk.Label(root, text="Release Year:",bg="black", fg="white")
label_release_year.grid(row=2, column=0, padx=10, pady=5)

label_num_pages = tk.Label(root, text="Number of Pages:",bg="black", fg="white")
label_num_pages.grid(row=3, column=0, padx=10, pady=5)

label_remove_title = tk.Label(root, text="Title to Remove:",bg="black", fg="white")
label_remove_title.grid(row=4, column=0, padx=10, pady=5)

entry_title = tk.Entry(root)
entry_title.grid(row=0, column=1, padx=10, pady=5)

entry_author = tk.Entry(root)
entry_author.grid(row=1, column=1, padx=10, pady=5)

entry_release_year = tk.Entry(root)
entry_release_year.grid(row=2, column=1, padx=10, pady=5)

entry_num_pages = tk.Entry(root)
entry_num_pages.grid(row=3, column=1, padx=10, pady=5)

entry_remove_title = tk.Entry(root)
entry_remove_title.grid(row=4, column=1, padx=10, pady=5)

button_list_books = tk.Button(root, text="List Books", command=list_books_command, bg="black", fg="white")
button_list_books.grid(row=5, column=0, columnspan=2, pady=5)

button_add_book = tk.Button(root, text="Add Book", command=add_book_command, bg="black", fg="white")
button_add_book.grid(row=6, column=0, columnspan=2, pady=5)

button_remove_book = tk.Button(root, text="Remove Book", command=remove_book_command, bg="black", fg="white")
button_remove_book.grid(row=7, column=0, columnspan=2, pady=5)

text_output = tk.Text(root, height=10, width=50)
text_output.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
text_output.config(state=tk.DISABLED)

root.configure(background="light blue")
root.mainloop()