from tkinter import *
from tkinter import ttk

root = Tk()

def change_details():
    dash_win.withdraw()
    cd_win = Toplevel()
    cd_win.title("Add New Charges")
    cd_frame = ttk.LabelFrame(cd_win, text="Changes Details", padding="3 3 12 12")
    cd_frame.grid(column=0, row=0, sticky=(N,W,E,S))

    change_no, change_desc, change = StringVar(), StringVar(), StringVar()
    
    change_no_label = ttk.Label(cd_frame, text="Change No.")
    change_desc_label = ttk.Label(cd_frame, text="Change Desc.")
    change_label = ttk.Label(cd_frame, text="Change.")
    
    change_no_field = ttk.Entry(cd_frame, width=10, textvariable=change_no)
    change_desc_field = ttk.Entry(cd_frame, width=10, textvariable=change_desc)
    change_field = ttk.Entry(cd_frame, width=10, textvariable=change)

    change_no_label.grid(column=1, row=1)
    change_desc_label.grid(column=1, row=2)
    change_label.grid(column=1, row=3)

    change_no_field.grid(column=2, row=1)
    change_desc_field.grid(column=2, row=2)
    change_field.grid(column=2, row=3)

    # Add buttons

    for child in cd_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    

def book_type_details():
    dash_win.withdraw()
    bt_win = Toplevel()
    bt_win.title("Add New Book Type")
    bt_frame = ttk.LabelFrame(bt_win, text="Book Type Details", padding="3 3 12 12")

    for child in cd_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)
        
def book_code_details():
    dash_win.withdraw()
    bc_win = Toplevel()
    bc_win.title("Add New Book Code")
    bc_frame = ttk.LabelFrame(bc_win, text="Book Code Details", padding="3 3 12 12")

    
def dashboard():
    root.withdraw()
    global dash_win
    dash_win = Toplevel()
    dash_win.title("Admin Dashboard")
    dash_frame = ttk.LabelFrame(dash_win, text="Admin Dashboard", padding="3 3 12 12")
    dash_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    
    new_charges= ttk.Button(dash_frame, text="Add New Charges", command=change_details)
    new_book_type= ttk.Button(dash_frame, text="Add New Book Type", command=book_type_details)
    new_book_code= ttk.Button(dash_frame, text="Add New Book Code", command=book_code_details)

    for i, child in enumerate(dash_frame.winfo_children()):
        child.grid(column=1, row=i, sticky=(N,W,E,S))
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

    
