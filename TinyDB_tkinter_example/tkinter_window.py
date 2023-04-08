import tkinter as tk
from my_tinydb import DB

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("My TinyDB")
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        # create input widgets
        self.name_label = tk.Label(self, text="Name:")
        self.name_entry = tk.Entry(self)
        self.age_label = tk.Label(self, text="Age:")
        self.age_entry = tk.Entry(self)

        # create buttons
        self.add_button = tk.Button(self, text="Add", command=self.add_person)
        self.show_button = tk.Button(self, text="Show All", command=self.show_people)
        self.clear_button = tk.Button(self, text="Clear", command=self.clear_entries)
        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)

        # create listbox to display people
        self.listbox = tk.Listbox(self)

        # pack widgets into grid
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.age_label.grid(row=1, column=0)
        self.age_entry.grid(row=1, column=1)

        self.add_button.grid(row=2, column=0, padx=5, pady=5)
        self.show_button.grid(row=2, column=1, padx=5, pady=5)
        self.clear_button.grid(row=3, column=0, padx=5, pady=5)
        self.quit_button.grid(row=3, column=1, padx=5, pady=5)

        self.listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def add_person(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        person = {"name": name, "age": age}
        self.db.create(person)
        self.show_people()
        self.clear_entries()

    def show_people(self):
        self.listbox.delete(0, tk.END)
        for person in self.db.read_all():
            self.listbox.insert(tk.END, f"{person.doc_id}: {person['name']} ({person['age']})")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)

    def run(self):
        self.db = DB()
        self.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.run()
