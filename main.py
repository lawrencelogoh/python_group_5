from tkinter import *
from tkinter import ttk

root = Tk()


def change_details():

    dash_win.withdraw()
    cd_win = Toplevel()
    cd_win.title("Add New Charges")
    cd_win.columnconfigure(0, weight=1)
    cd_win.rowconfigure(0, weight=1)

    cd_frame = ttk.LabelFrame(cd_win, text="Changes Details", padding=(3, 3, 12, 12))
    cd_btn_frame = ttk.Frame(cd_win, padding=(3, 3, 12, 12))
    cd_frame.columnconfigure(0, weight=1)
    cd_frame.rowconfigure(0, weight=1)
    cd_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    cd_btn_frame.grid(column=0, row=1)

    change_no, change_desc, change = StringVar(), StringVar(), StringVar()

    change_no_label = ttk.Label(cd_frame, text="Change No.")
    change_desc_label = ttk.Label(cd_frame, text="Change Desc.")
    change_label = ttk.Label(cd_frame, text="Change.")

    change_no_field = ttk.Entry(cd_frame, width=10, textvariable=change_no)
    change_desc_field = ttk.Entry(cd_frame, width=10, textvariable=change_desc)
    change_field = ttk.Entry(cd_frame, width=10, textvariable=change)

    change_no_label.grid(column=1, row=1, sticky=(W, E))
    change_desc_label.grid(column=1, row=2, sticky=(W, E))
    change_label.grid(column=1, row=3, sticky=(W, E))

    change_no_field.grid(column=2, row=1)
    change_desc_field.grid(column=2, row=2)
    change_field.grid(column=2, row=3)

    add_btn = ttk.Button(cd_btn_frame, text="Add")
    ignore_btn = ttk.Button(cd_btn_frame, text="Ignore")
    exit_btn = ttk.Button(cd_btn_frame, text="Exit")

    add_btn.grid(column=1, row=1)
    ignore_btn.grid(column=2, row=1)
    exit_btn.grid(column=3, row=1)

    for child in cd_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)


def book_type_details():
    dash_win.withdraw()
    bt_win = Toplevel()
    bt_win.title("Add New Book Type")
    bt_frame = ttk.LabelFrame(bt_win, text="Book Type Details", padding="3 3 12 12")
    bt_btn_frame = ttk.Frame(bt_win, padding="3 3 12 12")

    type_no_label = ttk.Label(bt_frame, text="Type No.")
    desc_label = ttk.Label(bt_frame, text="Description")

    type_no, desc = StringVar(), StringVar()
    type_no_field = ttk.Entry(bt_frame, textvariable=type_no)
    desc_field = ttk.Entry(bt_frame, textvariable=desc)

    add_btn = ttk.Button(bt_btn_frame, text="Add")
    ignore_btn = ttk.Button(bt_btn_frame, text="Ignore")
    exit_btn = ttk.Button(bt_btn_frame, text="Exit")

    bt_frame.grid(column=0, row=0, sticky=(N, W, E, S), padx=10, pady=10)
    bt_btn_frame.grid(column=0, row=1)

    type_no_label.grid(column=0, row=0)
    desc_label.grid(column=0, row=1)

    type_no_field.grid(column=1, row=0, columnspan=2)
    desc_field.grid(column=1, row=1, columnspan=2)

    add_btn.grid(column=0, row=0)
    ignore_btn.grid(column=1, row=0)
    exit_btn.grid(column=2, row=0)

    for child in bt_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)


def book_code_details():
    dash_win.withdraw()
    bc_win = Toplevel()
    bc_win.title("Add New Book Code")
    bc_frame = ttk.LabelFrame(bc_win, text="Book Code Details", padding="3 3 12 12")
    bc_btn_frame = ttk.Frame(bc_win, padding="3 3 12 12")

    book_code_label = ttk.Label(bc_frame, text="Book Code")
    desc_label = ttk.Label(bc_frame, text="Description")

    book_code, desc = StringVar(), StringVar()
    book_code_field = ttk.Entry(bc_frame, textvariable=book_code)
    desc_field = ttk.Entry(bc_frame, textvariable=desc)

    add_btn = ttk.Button(bc_btn_frame, text="Add")
    ignore_btn = ttk.Button(bc_btn_frame, text="Ignore")
    exit_btn = ttk.Button(bc_btn_frame, text="Exit")

    bc_frame.grid(column=0, row=0, sticky=(N, W, E, S), padx=10, pady=10)
    bc_btn_frame.grid(column=0, row=1)

    book_code_label.grid(column=0, row=0)
    desc_label.grid(column=0, row=1)

    book_code_field.grid(column=1, row=0, columnspan=2)
    desc_field.grid(column=1, row=1, columnspan=2)

    add_btn.grid(column=0, row=0)
    ignore_btn.grid(column=1, row=0)
    exit_btn.grid(column=2, row=0)

    for child in bc_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)


def unlock_user():
    dash_win.withdraw()
    uu_win = Toplevel()
    uu_win.title("Unlock User Menu")
    uu_frame = ttk.LabelFrame(uu_win, text="Locked Users", padding="3 3 12 12")
    uu_btn_frame = ttk.Frame(uu_win, padding="3 3 12 12")

    box = Text(uu_frame, width=40)

    unlock_btn = ttk.Button(uu_btn_frame, text="Unlock User")
    exit_btn = ttk.Button(uu_btn_frame, text="Exit")

    uu_frame.grid(column=0, row=0, sticky=(N, W, E, S), padx=10, pady=10)
    uu_btn_frame.grid(column=0, row=1)

    box.grid(column=0, row=0)
    unlock_btn.grid(column=0, row=0)

    exit_btn.grid(column=2, row=0)


def change_password():
    dash_win.withdraw()
    ch_pass_win = Toplevel()
    ch_pass_win.title("Change Password")
    ch_pass_frame = ttk.LabelFrame(
        ch_pass_win, text="User Details", padding="3 3 12 12"
    )
    ch_pass_btn_frame = ttk.Frame(ch_pass_win, padding="3 3 12 12")

    user_id_label = ttk.Label(ch_pass_frame, text="User ID")
    o_pass_label = ttk.Label(ch_pass_frame, text="Old Password")
    n_pass_label = ttk.Label(ch_pass_frame, text="New Password")
    c_pass_label = ttk.Label(ch_pass_frame, text="Confirm Password")

    user_id, o_pass, n_pass, c_pass = StringVar(), StringVar(), StringVar(), StringVar()

    user_id_field = ttk.Entry(ch_pass_frame, textvariable=user_id)
    o_pass_field = ttk.Entry(ch_pass_frame, textvariable=o_pass)
    n_pass_field = ttk.Entry(ch_pass_frame, textvariable=n_pass)
    c_pass_field = ttk.Entry(ch_pass_frame, textvariable=c_pass)

    change_pass_btn = ttk.Button(ch_pass_btn_frame, text="Change Password")
    ignore_btn = ttk.Button(ch_pass_btn_frame, text="Ignore")
    exit_btn = ttk.Button(ch_pass_btn_frame, text="Exit")

    ch_pass_frame.grid(column=0, row=0, sticky=(N, W, E, S), padx=10, pady=10)
    ch_pass_btn_frame.grid(column=0, row=1)

    user_id_label.grid(column=0, row=0)
    o_pass_label.grid(column=0, row=1)
    n_pass_label.grid(column=0, row=2)
    c_pass_label.grid(column=0, row=3)

    user_id_field.grid(column=1, row=0)
    o_pass_field.grid(column=1, row=1)
    n_pass_field.grid(column=1, row=2)
    c_pass_field.grid(column=1, row=3)

    change_pass_btn.grid(column=0, row=0)
    ignore_btn.grid(column=1, row=0)
    exit_btn.grid(column=2, row=0)

    for child in ch_pass_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)


def dashboard():
    root.withdraw()
    global dash_win
    dash_win = Toplevel()
    dash_win.title("Admin Dashboard")
    dash_frame = ttk.LabelFrame(dash_win, text="Admin Dashboard", padding="3 3 12 12")
    dash_frame.grid(column=0, row=0, sticky=(N, W, E, S))

    new_charges = ttk.Button(dash_frame, text="Add New Charges", command=change_details)
    new_book_type = ttk.Button(
        dash_frame, text="Add New Book Type", command=book_type_details
    )
    new_book_code = ttk.Button(
        dash_frame, text="Add New Book Code", command=book_code_details
    )
    # second section
    unlock_user_btn = ttk.Button(dash_frame, text="Unlock User", command=unlock_user)
    change_password_btn = ttk.Button(
        dash_frame, text="Change Password", command=change_password
    )
    # third section

    for i, child in enumerate(dash_frame.winfo_children()):
        child.grid(column=1, row=i, sticky=(N, W, E, S))
        child.grid_configure(padx=5, pady=5)

    dash_win.bind("<Destroy>", lambda e: root.state("normal"))


def login():

    root.title("Login")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    username, password = StringVar(), StringVar()
    username_field = ttk.Entry(mainframe, width=7, textvariable=username)
    password_field = ttk.Entry(mainframe, width=7, textvariable=password)

    username_field.grid(column=2, row=1, sticky=(W, E))
    password_field.grid(column=2, row=2, sticky=(W, E))

    username_label = ttk.Label(mainframe, text="Username")
    password_label = ttk.Label(mainframe, text="Password")
    login_btn = ttk.Button(mainframe, text="Login", command=dashboard)

    username_label.grid(column=1, row=1, sticky=W)
    password_label.grid(column=1, row=2, sticky=W)
    login_btn.grid(column=1, row=3, columnspan=2, sticky=S)

    for i, child in enumerate(mainframe.winfo_children()):
        mainframe.columnconfigure(i, weight=1)
        mainframe.rowconfigure(i, weight=1)
        root.columnconfigure(i, weight=1)
        root.rowconfigure(i, weight=1)
        child.grid_configure(padx=5, pady=5)
    root.mainloop()


def main():
    login()


if __name__ == "__main__":
    main()
