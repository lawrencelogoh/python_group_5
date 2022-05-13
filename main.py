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
    for i in range(0, 2):
        cd_frame.columnconfigure(i, weight=1)
        cd_frame.rowconfigure(i, weight=1)

    cd_frame.rowconfigure(3, weight=1)
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
    exit_btn = ttk.Button(cd_btn_frame, text="Exit", command=cd_win.destroy)

    add_btn.grid(column=1, row=1)
    ignore_btn.grid(column=2, row=1)
    exit_btn.grid(column=3, row=1)

    for child in cd_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    cd_win.bind("<Destroy>", lambda e: dash_win.state("normal"))


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
    exit_btn = ttk.Button(bt_btn_frame, text="Exit", command=bt_win.destroy)

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

    bt_win.bind("<Destroy>", lambda e: dash_win.state("normal"))


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
    exit_btn = ttk.Button(bc_btn_frame, text="Exit", command=bc_win.destroy)

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

    bc_win.bind("<Destroy>", lambda e: dash_win.state("normal"))


def unlock_user():
    dash_win.withdraw()
    uu_win = Toplevel()
    uu_win.title("Unlock User Menu")
    uu_frame = ttk.LabelFrame(uu_win, text="Locked Users", padding="3 3 12 12")
    uu_btn_frame = ttk.Frame(uu_win, padding="3 3 12 12")

    box = Text(uu_frame, width=40)

    unlock_btn = ttk.Button(uu_btn_frame, text="Unlock User")
    exit_btn = ttk.Button(uu_btn_frame, text="Exit", command=uu_win.destroy)

    uu_frame.grid(column=0, row=0, sticky=(N, W, E, S), padx=10, pady=10)
    uu_btn_frame.grid(column=0, row=1)

    box.grid(column=0, row=0)
    unlock_btn.grid(column=0, row=0)

    exit_btn.grid(column=2, row=0)

    uu_win.bind("<Destroy>", lambda e: dash_win.state("normal"))


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
    exit_btn = ttk.Button(ch_pass_btn_frame, text="Exit", command=ch_pass_win.destroy)

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

    ch_pass_win.bind("<Destroy>", lambda e: dash_win.state("normal"))


def user_maintenance():
    dash_win.withdraw()
    um_win = Toplevel()
    um_win.title("User Maintenance Menu")

    ui_frame, pd_frame, uru_frame, um_btn_frame = (
        ttk.Frame(um_win, padding="3 3 12 12"),
        ttk.LabelFrame(um_win, text="Personal Details", padding="3 3 12 12"),
        ttk.LabelFrame(um_win, text="User Rights Update", padding="3 3 12 12"),
        ttk.Frame(um_win, padding="3 3 12 12"),
    )

    user_id, username, al1, al2, phone, cell, email, ar, lr, ur = (
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
    )

    (
        user_id_label,
        username_label,
        al1_label,
        al2_label,
        phone_label,
        cell_label,
        email_label,
        ar_label,
        lr_label,
        ur_label,
    ) = (
        ttk.Label(ui_frame, text="User ID"),
        ttk.Label(pd_frame, text="User Name"),
        ttk.Label(pd_frame, text="Address Line 1"),
        ttk.Label(pd_frame, text="Address Line 2"),
        ttk.Label(pd_frame, text="Phone"),
        ttk.Label(pd_frame, text="Cell"),
        ttk.Label(pd_frame, text="Email"),
        ttk.Label(uru_frame, text="Admin Rights"),
        ttk.Label(uru_frame, text="Librarian Rights"),
        ttk.Label(uru_frame, text="User Rights"),
    )

    (
        user_id_field,
        username_field,
        al1_field,
        al2_field,
        phone_field,
        cell_field,
        email_field,
        ar_field,
        lr_field,
        ur_field,
    ) = (
        ttk.Entry(ui_frame, textvariable=user_id),
        ttk.Entry(pd_frame, textvariable=username),
        ttk.Entry(pd_frame, textvariable=al1),
        ttk.Entry(pd_frame, textvariable=al2),
        ttk.Entry(pd_frame, textvariable=phone),
        ttk.Entry(pd_frame, textvariable=cell),
        ttk.Entry(pd_frame, textvariable=email),
        ttk.Combobox(uru_frame, textvariable=ar),
        ttk.Combobox(uru_frame, textvariable=lr),
        ttk.Combobox(uru_frame, textvariable=ur),
    )

    update_btn = ttk.Button(um_btn_frame, text="Update")
    ignore_btn = ttk.Button(um_btn_frame, text="Ignore")
    exit_btn = ttk.Button(um_btn_frame, text="Exit", command=um_win.destroy)

    um_win.columnconfigure(0, weight=1)
    um_win.rowconfigure(0, weight=1)
    um_win.rowconfigure(1, weight=1)

    ui_frame.grid(column=0, row=0)
    pd_frame.grid(column=0, row=1, sticky=(W, E))
    uru_frame.grid(column=0, row=2, sticky=(W, E))
    um_btn_frame.grid(column=0, row=3)

    user_id_label.grid(column=0, row=0)
    user_id_field.grid(column=1, row=0)

    for i in range(0, 3):
        pd_frame.columnconfigure(i, weight=1)
        pd_frame.rowconfigure(i, weight=1)

    pd_frame.rowconfigure(4, weight=1)

    uru_frame.columnconfigure(0, weight=1)
    uru_frame.columnconfigure(1, weight=1)
    uru_frame.rowconfigure(0, weight=1)
    uru_frame.rowconfigure(1, weight=1)
    uru_frame.rowconfigure(2, weight=1)

    username_label.grid(column=0, row=0)
    username_field.grid(column=1, row=0)
    al1_label.grid(column=0, row=1)
    al1_field.grid(column=1, row=1)
    al2_label.grid(column=0, row=2)
    al2_field.grid(column=1, row=2)
    phone_label.grid(column=0, row=3)
    phone_field.grid(column=1, row=3)
    cell_label.grid(column=2, row=3)
    cell_field.grid(column=3, row=3)
    email_label.grid(column=0, row=4)
    email_field.grid(column=1, row=4)

    ar_label.grid(column=0, row=0)
    ar_field.grid(column=1, row=0)
    lr_label.grid(column=0, row=1)
    lr_field.grid(column=1, row=1)
    ur_label.grid(column=0, row=2)
    ur_field.grid(column=1, row=2)

    update_btn.grid(column=0, row=0)
    ignore_btn.grid(column=1, row=0)
    exit_btn.grid(column=2, row=0)

    # frame padding
    for child in ui_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    for child in pd_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    for child in uru_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    um_win.bind("<Destroy>", lambda e: dash_win.state("normal"))


def edit_book():
    dash_win.withdraw()
    eb_win = Toplevel()
    eb_win.title("Edit Book Details")

    sn_frame, bd_frame, eb_btn_frame = (
        ttk.Frame(eb_win, padding="3 3 12 12"),
        ttk.LabelFrame(eb_win, text="Book Details", padding="3 3 12 12"),
        ttk.Frame(eb_win, padding="3 3 12 12"),
    )

    (
        serial_no_label,
        bk_name_label,
        auth_name_label,
        book_type_label,
        book_code_label,
        book_desc_label,
        pub_date_label,
        lib_date_label,
    ) = (
        ttk.Label(sn_frame, text="Serial No."),
        ttk.Label(bd_frame, text="Book Name"),
        ttk.Label(bd_frame, text="Author Name"),
        ttk.Label(bd_frame, text="Book Type"),
        ttk.Label(bd_frame, text="Book Code"),
        ttk.Label(bd_frame, text="Book Des"),
        ttk.Label(bd_frame, text="Publish Date"),
        ttk.Label(bd_frame, text="Lib Date"),
    )

    (
        serial_no,
        bk_name,
        auth_name,
        book_type,
        book_code,
        book_desc,
        pub_date,
        lib_date,
        ed,
        pg,
    ) = (
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
        StringVar(),
    )

    (
        serial_no_field,
        bk_name_field,
        auth_name_field,
        book_type_field,
        book_code_field,
        book_desc_field,
        pub_date_field,
        lib_date_field,
        ed_field,
        pg_field,
    ) = (
        ttk.Entry(sn_frame, textvariable=serial_no),
        ttk.Entry(bd_frame, textvariable=bk_name),
        ttk.Entry(bd_frame, textvariable=auth_name),
        ttk.Combobox(bd_frame, width=2, textvariable=book_type),
        ttk.Combobox(bd_frame, width=2, textvariable=book_code),
        ttk.Entry(bd_frame, textvariable=book_desc),
        ttk.Entry(bd_frame, textvariable=pub_date),
        ttk.Entry(bd_frame, textvariable=lib_date),
        ttk.Entry(bd_frame, textvariable=ed),
        ttk.Entry(bd_frame, textvariable=pg),
        # ttk.Entry(bd_frame, state="disabled", textvariable=ed),
        # ttk.Entry(bd_frame, state="disabled", textvariable=pg),
    )

    # ed_field.configure(state="normal")
    ed_field.insert("end", "Educational")
    # ed_field.state(["disabled"])

    # pg_field.configure(state="normal")
    pg_field.insert("insert", "Post Graduate Studies")
    # pg_field.state(["disabled"])

    change_picture_btn = ttk.Button(bd_frame, text="Change Picture")
    edit_btn = ttk.Button(eb_btn_frame, text="Edit")
    ignore_btn = ttk.Button(eb_btn_frame, text="Ignore")
    exit_btn = ttk.Button(eb_btn_frame, text="Exit", command=eb_win.destroy)

    sn_frame.grid(column=0, row=0)
    bd_frame.grid(column=0, row=1)
    eb_btn_frame.grid(column=0, row=2)
    serial_no_label.grid(column=0, row=0)
    serial_no_field.grid(column=1, row=0)
    bk_name_label.grid(column=0, row=0)
    bk_name_field.grid(column=1, row=0)
    auth_name_label.grid(column=0, row=1)
    auth_name_field.grid(column=1, row=1)
    book_type_label.grid(column=0, row=2)
    book_type_field.grid(column=1, row=2)
    ed_field.grid(column=2, row=2)
    book_code_label.grid(column=0, row=3)
    book_code_field.grid(column=1, row=3)
    pg_field.grid(column=2, row=3)
    book_desc_label.grid(column=0, row=4)
    book_desc_field.grid(column=1, row=4)
    change_picture_btn.grid(column=2, row=4)
    pub_date_label.grid(column=0, row=5)
    pub_date_field.grid(column=1, row=5)
    lib_date_label.grid(column=2, row=5)
    lib_date_field.grid(column=3, row=5)

    edit_btn.grid(column=0, row=0)
    ignore_btn.grid(column=1, row=0)
    exit_btn.grid(column=2, row=0)

    for child in sn_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    for child in bd_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    eb_win.bind("<Destroy>", lambda e: dash_win.state("normal"))


def dashboard():
    root.withdraw()
    global dash_win
    dash_win = Toplevel()
    dash_win.title("Administrator Main Menu - Library Management System")
    ao_frame = ttk.LabelFrame(dash_win, text="Admin Options", padding="3 3 12 12")
    ro_frame = ttk.LabelFrame(dash_win, text="Report Options", padding="3 3 12 12")
    to_frame = ttk.LabelFrame(dash_win, text="Types Options", padding="3 3 12 12")
    exit_frame = ttk.Frame(dash_win, padding="3 3 12 12")

    new_user_btn = ttk.Button(ao_frame, text="Add A New User")
    unlock_user_btn = ttk.Button(
        ao_frame, text="Unlock User Utility", command=unlock_user
    )
    edit_book_btn = ttk.Button(ao_frame, text="Edit Book Details", command=edit_book)
    user_maintenance_btn = ttk.Button(
        ao_frame, text="User Maintenance", command=user_maintenance
    )
    change_password_btn = ttk.Button(
        ao_frame, text="Change User Password", command=change_password
    )
    take_backup_btn = ttk.Button(ao_frame, text="Take Backup")
    exit_btn = ttk.Button(exit_frame, text="Exit", command=dash_win.destroy)

    v_book_code_listing = ttk.Button(ro_frame, text="View Book Code Listing")
    v_user_listing = ttk.Button(ro_frame, text="View User Listing")
    v_book_type_listing = ttk.Button(ro_frame, text="View Book Type Listing")

    new_charges = ttk.Button(to_frame, text="Add Charges", command=change_details)
    new_book_type = ttk.Button(
        to_frame, text="Add New Book Type", command=book_type_details
    )
    new_book_code = ttk.Button(
        to_frame, text="Add New Book Code", command=book_code_details
    )

    ao_frame.grid(column=0, row=0, padx=5, pady=5)
    exit_frame.grid(column=0, row=1, padx=5, pady=5)
    ro_frame.grid(column=1, row=0, padx=5, pady=5)
    to_frame.grid(column=1, row=1, padx=5, pady=5)

    for i in range(0, 1):
        dash_win.columnconfigure(i, weight=1)
        dash_win.rowconfigure(i, weight=1)

    ao_frame.columnconfigure(0, weight=1)
    exit_frame.columnconfigure(0, weight=1)
    ro_frame.columnconfigure(0, weight=1)
    to_frame.columnconfigure(0, weight=1)

    for i in range(0, 2):
        ro_frame.rowconfigure(i, weight=1)
        to_frame.rowconfigure(i, weight=1)

    for i in range(0, 4):
        ao_frame.rowconfigure(i, weight=1)

    for i, child in enumerate(ao_frame.winfo_children()):
        child.grid(column=0, row=i, sticky=(N, W, E, S))
        child.grid_configure(padx=5, pady=5)

    for i, child in enumerate(exit_frame.winfo_children()):
        child.grid(column=0, row=i, sticky=(N, W, E, S))
        child.grid_configure(padx=5, pady=5)

    for i, child in enumerate(ro_frame.winfo_children()):
        child.grid(column=0, row=i, sticky=(N, W, E, S))
        child.grid_configure(padx=5, pady=5)

    for i, child in enumerate(to_frame.winfo_children()):
        child.grid(column=0, row=i, sticky=(N, W, E, S))
        child.grid_configure(padx=5, pady=5)

    dash_win.bind("<Destroy>", lambda e: root.state("normal"))


def login():

    root.title("Login")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    username, password = StringVar(), StringVar()
    username_field = ttk.Entry(mainframe, width=7, textvariable=username)
    password_field = ttk.Entry(mainframe, width=7, textvariable=password, show="*")

    username_field.grid(column=2, row=1, sticky=(W, E))
    password_field.grid(column=2, row=2, sticky=(W, E))

    username_label = ttk.Label(mainframe, text="Username")
    password_label = ttk.Label(mainframe, text="Password")
    login_btn = ttk.Button(mainframe, text="Login", command=dashboard)

    username_label.grid(column=1, row=1, sticky=W)
    password_label.grid(column=1, row=2, sticky=W)
    login_btn.grid(column=1, row=3, columnspan=2, sticky=S)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    for i, child in enumerate(mainframe.winfo_children()):
        mainframe.columnconfigure(i, weight=1)
        mainframe.rowconfigure(i, weight=1)
        child.grid_configure(padx=5, pady=5)
    root.mainloop()


def main():
    login()


if __name__ == "__main__":
    main()
