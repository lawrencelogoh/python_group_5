from tkinter import *
from tkinter import ttk


def main():
      
    root = Tk()
    root.title("Login")
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    username, password = StringVar(), StringVar()
    username_field = ttk.Entry(mainframe, width=7, textvariable=username)
    password_field = ttk.Entry(mainframe, width=7, textvariable=password)

    username_field.grid(column=2, row=1, sticky=(W, E))
    password_field.grid(column=2, row=2, sticky=(W, E))

    username_label = ttk.Label(mainframe, text="Username")
    password_label = ttk.Label(mainframe, text="Password")
    login_btn = ttk.Button(mainframe, text="Login")
    
    username_label.grid(column=1, row=1, sticky=W)
    password_label.grid(column=1, row=2, sticky=W)
    login_btn.grid(column=2, row=3, sticky=S)

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
    root.mainloop()


if __name__ == "__main__":
    main()
