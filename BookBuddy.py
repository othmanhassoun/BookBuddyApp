import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Main Application Class
class BookBuddyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BookBuddy - Personal Library Manager")
        
        # Main Window
        self.create_main_window()

    def create_main_window(self):
        self.clear_window()

        title_label = tk.Label(self.root, text="Welcome to BookBuddy", font=("Arial", 24))
        title_label.pack(pady=20)

        add_book_button = tk.Button(self.root, text="Add Book", command=self.open_add_book_window)
        add_book_button.pack(pady=10)

        view_library_button = tk.Button(self.root, text="View Library", command=self.open_view_library_window)
        view_library_button.pack(pady=10)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.pack(pady=10)

    def open_add_book_window(self):
        self.clear_window()

        tk.Label(self.root, text="Add a New Book", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Title:").pack()
        self.title_entry = tk.Entry(self.root)
        self.title_entry.pack()

        tk.Label(self.root, text="Author:").pack()
        self.author_entry = tk.Entry(self.root)
        self.author_entry.pack()

        tk.Label(self.root, text="Genre:").pack()
        self.genre_entry = tk.Entry(self.root)
        self.genre_entry.pack()

        tk.Label(self.root, text="Notes:").pack()
        self.notes_entry = tk.Entry(self.root)
        self.notes_entry.pack()

        tk.Button(self.root, text="Save", command=self.save_book).pack(pady=5)
        tk.Button(self.root, text="Clear", command=self.clear_entries).pack(pady=5)
        tk.Button(self.root, text="Cancel", command=self.create_main_window).pack(pady=5)

    def open_view_library_window(self):
        self.clear_window()

        tk.Label(self.root, text="Library", font=("Arial", 18)).pack(pady=10)

        self.library_tree = ttk.Treeview(self.root, columns=("Title", "Author", "Genre", "Notes"), show='headings')
        self.library_tree.heading("Title", text="Title")
        self.library_tree.heading("Author", text="Author")
        self.library_tree.heading("Genre", text="Genre")
        self.library_tree.heading("Notes", text="Notes")
        self.library_tree.pack(pady=10, fill=tk.BOTH, expand=True)

        tk.Button(self.root, text="Back", command=self.create_main_window).pack(pady=5)

        # Load books into the treeview
        self.load_books()

    def save_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        notes = self.notes_entry.get()

        if not title or not author or not genre:
            messagebox.showwarning("Validation Error", "Please fill in all fields.")
            return

        with open("library.txt", "a") as f:
            f.write(f"{title},{author},{genre},{notes}\n")

        messagebox.showinfo("Success", "Book added successfully!")
        self.clear_entries()

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.notes_entry.delete(0, tk.END)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def load_books(self):
        for item in self.library_tree.get_children():
            self.library_tree.delete(item)

        try:
            with open("library.txt", "r") as f:
                for line in f:
                    title, author, genre, notes = line.strip().split(",")
                    self.library_tree.insert("", "end", values=(title, author, genre, notes))
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = BookBuddyApp(root)
    root.mainloop()
