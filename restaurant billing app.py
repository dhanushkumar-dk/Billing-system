### Importing required libraries ###
from tkinter import *
import random
import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import time
import csv


#It is definition of System
def system():
    root = Tk()
    root.geometry("1700x800")
    root.title("Restaurant Management System")
    root.configure(bg='red')


    # Function to display live time in HH : MM : SS 
    def display_time():  
        hour = str(time.strftime("%H"))  
        minute = str(time.strftime("%M"))  
        second = str(time.strftime("%S"))  
        if int(hour) >= 12 and int(hour) < 24 and int (minute) >= 0:  
            meridiem_label.config(text = "PM")  
        else:  
            meridiem_label.config(text = "AM")  
        if int(hour) > 12:  
            hour = str((int(hour) - 12))  
        elif int(hour) == 0:  
            hour = str(12)  
        hour_label.config(text = hour)  
        minute_label.config(text = minute)  
        second_label.config(text = second)  
        hour_label.after(200, display_time)  

    # Function to create database
    def Database():
        global connectn, cursor
        connectn = sqlite3.connect("Restaurant.db")
        cursor = connectn.cursor()
        # creating bill table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS Restaurantrecords(ordno text, ac_yes text, piz text,bur text,ice text, dr text, ct text,sb text,tax text,sr text,tot text, mem text)")

    # variable datatype assignment
    orderno = StringVar()
    AC_hall = StringVar()
    pizza = StringVar()
    burger = StringVar()
    icecream = StringVar()
    drinks = StringVar()
    cost = StringVar()
    subtotal = StringVar()
    tax = StringVar()
    service = StringVar()
    total = StringVar()
    membershipno = StringVar()
    radio1 = IntVar()
    radio2 = IntVar()

    def export_DB_to_CSV():
        connection = sqlite3.connect("Restaurant.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Restaurantrecords")
        result = cursor.fetchall()
        lst = []
        for r in result:
            lst.append(r)
        csvData = lst
        with open('Restaurant_records.csv', 'w') as CF:
            writer = csv.writer(CF)
            writer.writerows(csvData)
        CF.close()
        messagebox.showinfo("Message", "Stored successfully")

        
    
    def selection():
        tempvalue = radio1.get()
        if tempvalue == 50:
            print('50')
        elif tempvalue == 0:
            print('0')
            
    # defining total function
    def tottal():
        tempvalue1 = radio1.get()
        acc = 0
        if tempvalue1 == 50:
            acc = 1
        elif tempvalue1 == 0:
            acc = 0

        ac = float(acc)
        pi = float(pizza.get())
        bu = float(burger.get())
        ice = float(icecream.get())
        dr = float(drinks.get())
        member_ship = membershipno.get()
        tempvalue2 = radio2.get()
        if tempvalue2 == 25:
            ms = 25
        elif tempvalue2 == 0:
            ms = 0
        


        # computing the cost of items

        costac = ac * 50
        costpi = pi * 240
        costbu = bu * 125
        costice = ice * 80
        costdr = dr * 60
        costmem = ms

        # computing the charges or  total
        print(costac + costpi + costbu + costice + costdr)
        costofmeal = (costac + costpi + costbu + costice + costdr)
        ptax = ((costac + costpi + costbu + costice + costdr) * 0.18)
        sub = (costac + costpi + costbu + costice + costdr)
        ser = ((costac + costpi + costbu + costice + costdr) / 99)
        paidtax = str(ptax)
        Service = str(ser)
        overall = str(ptax + ser + sub - costmem)

        # Displaying the values
        cost.set(costofmeal)
        tax.set(ptax)
        subtotal.set(sub)
        service.set(ser)
        total.set(overall)

    # defining reset function
    def reset():
        orderno.set("")
        AC_hall.set("")
        pizza.set("")
        burger.set("")
        icecream.set("")
        drinks.set("")
        cost.set("")
        subtotal.set("")
        tax.set("")
        service.set("")
        total.set("")
        membershipno.set("")

    # defining exit function
    def exit():
        root.destroy()

    # Topframe
    topframe = Frame(root, bg="red", width=1600, height=50)
    topframe.pack(side=TOP)

    # Leftframe
    leftframe = Frame(root, bg="red", width=900, height=700)
    leftframe.pack(side=LEFT)

    # rightframe
    rightframe = Frame(root, bg="red", width=400, height=700)
    rightframe.pack(side=RIGHT)

    ################## display data ####################
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = connectn.execute("SELECT * FROM Restaurantrecords")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()

    style = ttk.Style()
    style.configure("Treeview",
                    foreground="black",
                    rowheight=40,
                    fieldbackground="white"
                    )
    style.map('Treeview',
              background=[('selected', 'lightblue')])

    ###########    data base table Creating table #############
    my_tree = ttk.Treeview(rightframe)
    my_tree['columns'] = ("ordno", "ac_yes", "piz", "bur", "ice", "dr", "ct", "sb", "tax", "sr", "tot", "mem")

    ############ creating  for table ################
    horizontal_bar = ttk.Scrollbar(rightframe, orient="horizontal")
    horizontal_bar.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=horizontal_bar.set)
    horizontal_bar.pack(fill=X, side=BOTTOM)

    vertical_bar = ttk.Scrollbar(rightframe, orient="vertical")
    vertical_bar.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vertical_bar.set)
    vertical_bar.pack(fill=Y, side=RIGHT)

    # defining column for table
    my_tree.column("#0", width=0, minwidth=0)
    my_tree.column("ordno" , anchor=CENTER, width =80  , minwidth=25)
    my_tree.column("ac_yes", anchor=CENTER, width =50  , minwidth=25)
    my_tree.column("piz"   , anchor=CENTER, width =60  , minwidth=25)
    my_tree.column("bur"   , anchor=CENTER, width =50  , minwidth=25)
    my_tree.column("ice"   , anchor=CENTER, width= 80  , minwidth=25)
    my_tree.column("dr"    , anchor=CENTER, width =50  , minwidth=25)
    my_tree.column("ct"    , anchor=CENTER, width =50  , minwidth=25)
    my_tree.column("sb"    , anchor=CENTER, width =100 , minwidth=25)
    my_tree.column("tax"   , anchor=CENTER, width =50  , minwidth=25)
    my_tree.column("sr"    , anchor=CENTER, width =100 , minwidth=25)
    my_tree.column("tot"   , anchor=CENTER, width =50  , minwidth=25)
    my_tree.column("mem"   , anchor=CENTER, width =50  , minwidth=25)

    # defining  headings for table
    my_tree.heading("ordno" , text="Order No"  , anchor=CENTER)
    my_tree.heading("ac_yes", text="AC_hall"   , anchor=CENTER)
    my_tree.heading("piz"   , text="Pizza"     , anchor=CENTER)
    my_tree.heading("bur"   , text="Burger"    , anchor=CENTER)
    my_tree.heading("ice"   , text="Ice cream" , anchor=CENTER)
    my_tree.heading("dr"    , text="Drinks"    , anchor=CENTER)
    my_tree.heading("ct"    , text="Cost"      , anchor=CENTER)
    my_tree.heading("sb"    , text="Subtotal"  , anchor=CENTER)
    my_tree.heading("tax"   , text="Tax"       , anchor=CENTER)
    my_tree.heading("sr"    , text="Service"   , anchor=CENTER)
    my_tree.heading("tot"   , text="Total"     , anchor=CENTER)
    my_tree.heading("mem"   , text="Discount"  , anchor=CENTER)

    my_tree.pack()
    DisplayData()

    # defining add function to add record
    def add():
        Database()
        # getting  data
        orders = orderno.get()
        AC_halls = radio1.get()
        pizzas = pizza.get()
        burgers = burger.get()
        ices = icecream.get()
        drinkss = drinks.get()
        costs = cost.get()
        subtotals = subtotal.get()
        taxs = tax.get()
        services = service.get()
        totals = total.get()
        Memberships = radio2.get()
        print(orders, AC_halls, pizzas, burgers, ices, drinkss, costs, subtotals, taxs, services, totals, Memberships)
        if orders == "" or AC_halls == "" or pizzas == "" or burgers == "" or ices == "" or drinkss == "" or costs == "" or subtotals == "" or taxs == "" or services == "" or totals == "" or Memberships == "":
            messagebox.showinfo("Warning", "Please fill the empty field!!!")
        else:
            connectn.execute(
                'INSERT INTO Restaurantrecords (ordno, ac_yes, piz, bur , ice ,dr ,ct ,sb ,tax, sr, tot, mem) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
                (orders, AC_halls, pizzas, burgers, ices, drinkss, costs, subtotals, taxs, services, totals, Memberships));
            connectn.commit()
            messagebox.showinfo("Message", "Stored successfully")
        # refresh table data
        DisplayData()
        connectn.close()

    # defining function to access data from sqlite datrabase
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = connectn.execute("SELECT * FROM Restaurantrecords")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()

    # defining function to delete record
    def Delete():
        # open database
        Database()
        if not my_tree.selection():
            messagebox.showwarning("Warning", "Select data to delete")
        else:
            result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                            icon="warning")
        if result == 'yes':
            curItem = my_tree.focus()
            contents = (my_tree.item(curItem))
            selecteditem = contents['values']
            my_tree.delete(curItem)
            cursor = connectn.execute("DELETE FROM Restaurantrecords WHERE ordno= %d" % selecteditem[0])
            connectn.commit()
            cursor.close()
            connectn.close()


    # Time
    localtime = time.asctime(time.localtime(time.time()))
    # Top part
    main_lbl = Label(topframe, font=('Calibri', 25, 'bold'), text="Restaurant Management System", fg="yellow", bg='red', anchor=W)
    main_lbl.grid(row=0, column=0, columnspan = 6)
    #main_lbl = Label(topframe, font=('Calibri', 15,), text=localtime, fg="lightgreen", bg='red', anchor=W)
    #main_lbl.grid(row=1, column=0)

    ### Labels
    # items

    # , columnspan = 2, rowspan = 2, padx = 5, pady = 5
    #
    #
    #
    #
    #



     
    hour_label = Label(topframe, text = "00", font = ("radioland", "48"), bg = "red", fg = "blue", anchor=W)
    
    colon_label_one = Label(topframe, text = ":", font = ("radioland", "48"), bg = "red",fg = "black", anchor=W)
    
    minute_label = Label(topframe, text = "00", font = ("radioland", "48"), bg = "red", fg = "green", anchor=W)
    
    colon_label_two = Label(topframe, text = ":", font = ("radioland", "48"), bg = "red",  fg = "black", anchor=W)
    
    second_label = Label(topframe,text = "00",font = ("radioland", "48"),bg = "red",fg = "white", anchor=W)
    
    meridiem_label = Label(topframe, text = "AM", font = ("radioland", "48"), bg = "red", fg = "blue", anchor=W)

    hour_label.grid(         row = 1, column = 0)  
    colon_label_one.grid(    row = 1, column = 1)  
    minute_label.grid(       row = 1, column = 2)
    colon_label_two.grid(    row = 1, column = 3)  
    second_label.grid(       row = 1, column = 4) 
    meridiem_label.grid(     row = 1, column = 5)
    #
    #
    #
    #
    #
    #
    #


    
    ordlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Order No.", fg="black", bg="red", padx = '30', bd=5, anchor=W).grid(row=1, column=0)
    ordtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=orderno).grid(row=1, column=1, columnspan = 2)
    # AC button
    ACbutton = Label(leftframe, font=('Calibri', 16, 'bold'), text="AC HALL", fg="black", bg="red", padx = '30', bd=5, anchor=W).grid(row=2, column=0)
    #ACbutton = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
    #               textvariable=AC_hall).grid(row=2, column=1)

    # Pizza
    pizlbl     = Label(leftframe, font=('Calibri', 16, 'bold'), text="Pizza", fg="black", bg="red", padx = '30', bd=5, anchor=W).grid(row=3, column=0)
    piztxt     = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=pizza).grid(row=3, column=1, columnspan = 2)
    # burger
    burlbl     = Label(leftframe, font=('Calibri', 16, 'bold'), text="Burger", fg="black", bg="red", padx = '30', bd=5, anchor=W).grid(row=4, column=0)
    burtxt     = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=burger).grid(row=4, column=1, columnspan = 2)
    # icecream
    icelbl     = Label(leftframe, font=('Calibri', 16, 'bold'), text="Ice Cream", fg="black", bg="red", padx = '30', bd=5, anchor=W).grid(row=5, column=0)
    icetxt     = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=icecream).grid(row=5, column=1, columnspan = 2)
    # drinks
    drinklbl   = Label(leftframe, font=('Calibri', 16, 'bold'), text="Drinks", fg="black", bg="red", padx = '30', bd=5, anchor=W).grid(row=6, column=0)
    drinktxt   = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=drinks).grid(row=6, column=1, columnspan = 2)
    # costmembershipno
    costlbl    = Label(leftframe, font=('Calibri', 16, 'bold'), text="Cost", padx = '30', bg="red", bd=5, anchor=W).grid(row=7, column=0)
    costtxt    = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=cost).grid(row=7, column=1, columnspan = 2)
    # subtotal
    sublbl     = Label(leftframe, font=('Calibri', 16, 'bold'), text="Subtotal", padx = '30', bg="red", bd=5, anchor=W).grid(row=8, column=0)
    subtxt     = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=subtotal).grid(row=8, column=1, columnspan = 2)
    # tax
    taxlbl     = Label(leftframe, font=('Calibri', 16, 'bold'), text="Tax", bg="red", padx = '30', bd=5, anchor=W).grid(row=9, column=0)
    taxtxt     = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=tax).grid(row=9, column=1, columnspan = 2)
    # service
    servicelbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Service", bg="red", padx = '30', bd=5, anchor=W).grid(row=10, column=0)
    servicetxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=4, insertwidth=3, justify='right', textvariable=service).grid(row=10, column=1, columnspan = 2)
    # total
    totallbl   = Label(leftframe, font=('Calibri', 16, 'bold'), text="Total", padx = '30', bg="red", bd=5, anchor=W).grid(row=11, column=0)
    totaltxt   = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=4, insertwidth=3, justify='right', textvariable=total).grid(row=11, column=1, columnspan = 2)
    
    # membership
    Membershiplbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Membership", bg="red", padx = '30', bd=5, anchor=W).grid(row=12, column=0)
    #Membershiptxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=membershipno).grid(row=12, column=1, columnspan = 2)


########################################################################################################

    def selection():
        tempvalue = radio1.get()
        if tempvalue == 50:
            print('50')
        elif tempvalue == 0:
            print('0')


    def selection1():
        tempvalue = radio2.get()
        if tempvalue == 25:
            print('25')
        elif tempvalue == 0:
            print('0')

        #selected = "You selected the option " + str(radio.get())
        #label.config(text=selected)
        #value_ = radio.get()
        #print(value_)


########################################################################################################
########################################################################################################
    
    #radio = StringVar()
    #Label(text="Your Favourite programming language:", font=('Aerial 11')).grid(row=13, column=0)

    # Define radiobutton for each options
    r1 = Radiobutton(leftframe, font=('Calibri', 12, 'bold'),bd=4, text="YES", variable=radio1, fg = 'green', value=50, padx = '30', pady = '10', command=selection)

    r1.grid(row=2, column=1)
    r2 = Radiobutton(leftframe, font=('Calibri', 12, 'bold'),bd=4, text="NO", variable=radio1, fg = 'red', value=0, padx = '30', pady = '10', command=selection)

    r2.grid(row=2, column=2)
#-------------------------------------------------------------------------------------------------#
    r3 = Radiobutton(leftframe, font=('Calibri', 12, 'bold'),bd=4, text="YES", variable=radio2, fg = 'green', value=25, padx = '30', pady = '4', command=selection1)

    r3.grid(row=12, column=1)
    r4 = Radiobutton(leftframe, font=('Calibri', 12, 'bold'),bd=4, text="NO", variable=radio2, fg = 'red', value=0, padx = '30', pady = '4', command=selection1)

    r4.grid(row=12, column=2)

    


########################################################################################################




    # ---button--


    totbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Total", bg="Lightgrey", fg="black", bd=3, padx=5, pady=5,
                    width=6, command=tottal).grid(row=6, column=4)

    resetbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Reset", bg="lightgrey", fg="black", bd=3, padx=5,
                      pady=5, width=6, command=reset).grid(row=4, column=4)

    exitbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Exit The System", bg="lightgrey", fg="black", bd=3, padx=5,
                     pady=5, width=12, command=exit).grid(row=8, column=3)

    addbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Add", bg="lightgrey", fg="black", bd=3, padx=5, pady=5,
                    width=6, command=add).grid(row=2, column=4)

    deletebtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Delete Record", bg="lightgrey", fg="black", bd=3,
                       padx=5, pady=5, width=12, command=Delete).grid(row=4, column=3)
    #exportbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Export", bg="lightgrey", fg="black", bd=3, padx=6, pady=6,
    #                   width=12, command=menu).grid(row=8, column=3)
    exportbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Export", bg="lightgrey", fg="black", bd=3, padx=5,
                      pady=5, width=6, command=export_DB_to_CSV).grid(row=8, column=4)
    

    ########################### feedback form   data basess connection  start  ################################

    def feedbackk():
        feed = Tk()
        feed.geometry("600x500")
        feed.title("Submit Feedback form")
        # database connective  #
        connectn = sqlite3.connect("Restaurant.db")
        cursor = connectn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS FEEDBACK(n text,eid text,feedback5 text,com text)")
        # variable datatype asssignment #
        name = StringVar()
        email = StringVar()
        comments = StringVar()

        # defiing submit function
        def submit():
            n = name.get()
            eid = email.get()
            com = txt.get('1.0', END) 
            feedback1 = ""
            feedback2 = ""
            feedback3 = ""
            feedback4 = ""
            if (checkvar1.get() == "1"):
                feedback1 = "Excellent"
            if (checkvar2.get() == "1"):
                feedback2 = "Good"
            if (checkvar3.get() == "1"):
                feedback2 = "Average"
            if (checkvar4.get() == "1"):
                feedback2 = "Poor"
            feedback5 = feedback1 + " " + feedback2 + " " + feedback3 + " " + feedback4
            conn = sqlite3.connect("Restaurant.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO FEEDBACK VALUES ('" + n + "','" + eid + "','" + com + "','" + feedback5 + "')")
            messagebox.showinfo("message", "data inserted !")
            feed.destroy()

        # defining cancel button
        def cancel():
            feed.destroy()

        # label#
        lb1 = Label(feed, font=("Calisto MT", 15, "bold"), text="Thanks for Visiting!", fg="black").pack(side=TOP)
        lbl2 = Label(feed, font=("calisto MT", 15), text="We're glad you chose us ! Please tell us how it was!",
                     fg="black").pack(side=TOP)
        # name
        namelbl = Label(feed, font=('vardana', 15), text="Name:-", fg="black", bd=10, anchor=W).place(x=10, y=150)
        nametxt = Entry(feed, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                        textvariable=name).place(x=15, y=185)
        # email
        emaillbl = Label(feed, font=('vardana', 15), text="Email:-", fg="black", bd=10, anchor=W).place(x=280, y=150)
        emailtxt = Entry(feed, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                         textvariable=email).place(x=285, y=185)
        ###checkbutton
        ratelbl = Label(feed, font=('vardana', 15), text="How would you rate us?", fg="black", bd=10, anchor=W).place(
            x=10, y=215)
        checkvar1 = StringVar()
        checkvar2 = StringVar()
        checkvar3 = StringVar()
        checkvar4 = StringVar()
        c1 = Checkbutton(feed, font=('Calibri', 10, "bold"), text="Excellent", bg="white", variable=checkvar1)
        c1.deselect()
        c1.place(x=15, y=265)
        c2 = Checkbutton(feed, font=('Calibri', 10, "bold"), text="Good", bg="white", variable=checkvar2, )
        c2.deselect()
        c2.place(x=120, y=265)
        c3 = Checkbutton(feed, font=('Calibri', 10, "bold"), text=" Average", bg="white", variable=checkvar3, )
        c3.deselect()
        c3.place(x=220, y=265)
        c4 = Checkbutton(feed, font=('Calibri', 10, "bold"), text="   Poor  ", bg="white", variable=checkvar4, )
        c4.deselect()
        c4.place(x=320, y=265)
        # comments"
        commentslbl = Label(feed, font=('Calibri', 15), text="Comments", fg="black", bd=10, anchor=W).place(x=10, y=300)
        txt = Text(feed, width=50, height=5)
        txt.place(x=15, y=335)
        # button
        submit = Button(feed, font=("Calibri", 15), text="Submit", fg="black", bg="green", bd=2, command=submit).place(
            x=145, y=430)
        cancel = Button(feed, font=("Calibri", 15), text="Cancel", fg="black", bg="red", bd=2, command=cancel).place(
            x=245, y=430)
        feed.mainloop()



    # Feedbackbutton
    feedbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Feedback Form", fg="black", bg="lightgrey", bd=3, padx=5,
                     pady=5, width=12, command=feedbackk).grid(row=6, column=3, columnspan=1)

    ##################### Menu card ################################
    def menu():
        roott = Tk()
        roott.title("Price Menu")
        roott.geometry("300x300")
        lblinfo = Label(roott, font=("Calibri", 20, "bold"), text="ITEM LIST", fg="black", bd=10)
        lblinfo.grid(row=0, column=0)
        lblprice = Label(roott, font=("Calibri", 20, "bold"), text="Prices", fg="black", bd=10)
        lblprice.grid(row=0, column=3)
        lblpizza = Label(roott, font=("Calibri", 20, "bold"), text="Pizza", fg="Blue", bd=10)
        lblpizza.grid(row=1, column=0)
        lblpricep = Label(roott, font=("Calibri", 20, "bold"), text="240/-", fg="blue", bd=10)
        lblpricep.grid(row=1, column=3)
        lblburger = Label(roott, font=("Calibri", 20, "bold"), text="Burger", fg="Blue", bd=10)
        lblburger.grid(row=3, column=0)
        lblpriceb = Label(roott, font=("Calibri", 20, "bold"), text="125/-", fg="blue", bd=10)
        lblpriceb.grid(row=3, column=3)
        lblicecream = Label(roott, font=("Calibri", 20, "bold"), text="Ice-Cream", fg="Blue", bd=10)
        lblicecream.grid(row=4, column=0)
        lblpricei = Label(roott, font=("Calibri", 20, "bold"), text="80/-", fg="blue", bd=10)
        lblpricei.grid(row=4, column=3)
        lbldrinks = Label(roott, font=("Calibri", 20, "bold"), text="Drinks", fg="Blue", bd=10)
        lbldrinks.grid(row=5, column=0)
        lblpriced = Label(roott, font=("Calibri", 20, "bold"), text="60/-", fg="blue", bd=10)
        lblpriced.grid(row=5, column=3)
        roott.mainloop()

    # menubutton
    menubtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Menu Card", bg="lightgrey", fg="black", bd=3, padx=6, pady=6, width=12, command=menu).grid(row=2, column=3)
    display_time() 
    root.mainloop()

    
system()
