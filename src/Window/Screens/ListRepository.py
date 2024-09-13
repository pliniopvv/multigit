from Window.Screens import MainWindow
from CTkListbox import *

class ListRepository(MainWindow):
    def __init__(self):
        super().__init__()

    def _build(self):
        def show_value(selected_option):
            print(selected_option)
    
        self.listView = CTkListbox(self.win, command=show_value)
        self.listView.pack(fill="both", expand=True, padx=10, pady=10)
        self.listView.insert(0, "Option 0")
        self.listView.insert(1, "Option 1")
        self.listView.insert(2, "Option 2")
        self.listView.insert(3, "Option 3")
        pass


# def button_callback():
#     print("button pressed")

# app = customtkinter.CTk()
# app.title("my app")
# app.geometry("400x150")

# button = customtkinter.CTkButton(app, text="my button", command=button_callback)
# button.grid(row=0, column=0, padx=20, pady=20)

# app.mainloop()