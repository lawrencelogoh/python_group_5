from tkinter import *
from tkinter import ttk

root = Tk()

def dashboard():
    root.withdraw()
    dash_win = Toplevel()
    dash_win.title("Admin Dashboard")
    dash_frame = ttk.Frame(dash_win, padding="3 3 12 12")
    dash_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    
    new_charges= ttk.Button(dash_frame, text="Add New Charges")
    new_book_type= ttk.Button(dash_frame, text="Add New Book Type")
    new_book_code= ttk.Button(dash_frame, text="Add New Book Code")
    
    # new_charges.grid(column=1, row=1)
    # new_book_type.grid(column=1, row=2)
    # new_book_code.grid(column=1, row=3)

    for i, child in enumerate(dash_frame.winfo_children()):
        child.grid(column=1, row=i)
        child.grid_configure(padx=5, pady=5)

    
    
    dash_win.bind("<Destroy>", lambda e: root.state('normal'))

def login():
    
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
    login_btn = ttk.Button(mainframe, text="Login",command=dashboard)
    
    username_label.grid(column=1, row=1, sticky=W)
    password_label.grid(column=1, row=2, sticky=W)
    login_btn.grid(column=2, row=3, sticky=S)

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
    root.mainloop()

def main():
      login()
    


if __name__ == "__main__":
    main()

    
