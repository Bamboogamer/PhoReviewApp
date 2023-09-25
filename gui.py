import tkinter as tk
from tkinter import *
from tkinter import messagebox


def gui(data_list):

    # Fonts
    font_courier15B = "Courier 15 bold"
    font_courier15 = "Courier 15"

    # Window Setup
    window = tk.Tk()
    window.title('PHO REVIEW DATA')
    window.geometry("1000x375")
    window.eval('tk::PlaceWindow . center')
    window.resizable(width=False, height=False)

    # TODO: Potential feature? instead of hard coding column names, I could ask the user for column names so they can
    #  create any "questionnaire" they want
    # label_names = ["Name of Restaurant",
    #                "Location (FullAddress)",
    #                "Spring Rolls",
    #                "Sauce Rating",
    #                "Broth Rating",
    #                "Noodles Rating",
    #                "RawSteak Rating",
    #                "Brisket Rating",
    #                "Tripe Rating",
    #                "Tendon Rating",
    #                "Meatballs Rating",
    #                "Additional Comments"]
    # for i in range(len(label_names)):
    #     label_name = StringVar(window, label_names[i])
    #     label_name_Dir = Label(window, textvariable=label_name, font=font_courier15B)
    #     label_name_Dir.grid(row=i+1, column=1)
    #     name_ = Entry(window, width=100, font=font_courier15)
    #     name_.grid(row=i+1, column=2)

    label_NameOfRestaurant = StringVar(window, "Name of Restaurant: ")
    label_NameOfRestaurant_Dir = Label(window, textvariable=label_NameOfRestaurant, font=font_courier15B)
    label_NameOfRestaurant_Dir.grid(row=1, column=1)
    nameOfRestaurant_ = Entry(window, width=100, font=font_courier15)
    nameOfRestaurant_.grid(row=1, column=2)

    label_Location = StringVar(window, "Location (Full Address): ")
    label_Location_Dir = Label(window, textvariable=label_Location, font=font_courier15B)
    label_Location_Dir.grid(row=2, column=1)
    location_ = Entry(window, width=100, font=font_courier15)
    location_.grid(row=2, column=2)

    label_SpringRolls = StringVar(window, "Spring Rolls Rating: ")
    label_SpringRolls_Dir = Label(window, textvariable=label_SpringRolls, font=font_courier15B)
    label_SpringRolls_Dir.grid(row=3, column=1)
    springRolls_ = Entry(window, width=100, font=font_courier15)
    springRolls_.grid(row=3, column=2)

    label_SR_Sauce = StringVar(window, "Sauce Rating: ")
    label_SR_Sauce_Dir = Label(window, textvariable=label_SR_Sauce, font=font_courier15B)
    label_SR_Sauce_Dir.grid(row=4, column=1)
    SR_Sauce_ = Entry(window, width=100, font=font_courier15)
    SR_Sauce_.grid(row=4, column=2)

    label_Broth = StringVar(window, "Broth Rating: ")
    label_Broth_Dir = Label(window, textvariable=label_Broth, font=font_courier15B)
    label_Broth_Dir.grid(row=5, column=1)
    Broth_ = Entry(window, width=100, font=font_courier15)
    Broth_.grid(row=5, column=2)

    label_Noodles = StringVar(window, "Noodles Rating: ")
    label_Noodles_Dir = Label(window, textvariable=label_Noodles, font=font_courier15B)
    label_Noodles_Dir.grid(row=6, column=1)
    Noodles_ = Entry(window, width=100, font=font_courier15)
    Noodles_.grid(row=6, column=2)

    label_RawSteak = StringVar(window, "Raw Steak Rating: ")
    label_RawSteak_Dir = Label(window, textvariable=label_RawSteak, font=font_courier15B)
    label_RawSteak_Dir.grid(row=7, column=1)
    RawSteak_ = Entry(window, width=100, font=font_courier15)
    RawSteak_.grid(row=7, column=2)

    label_Brisket = StringVar(window, "Brisket Rating: ")
    label_Brisket_Dir = Label(window, textvariable=label_Brisket, font=font_courier15B)
    label_Brisket_Dir.grid(row=8, column=1)
    Brisket_ = Entry(window, width=100, font=font_courier15)
    Brisket_.grid(row=8, column=2)

    label_Tripe = StringVar(window, "Tripe Rating: ")
    label_Tripe_Dir = Label(window, textvariable=label_Tripe, font=font_courier15B)
    label_Tripe_Dir.grid(row=9, column=1)
    Tripe_ = Entry(window, width=100, font=font_courier15)
    Tripe_.grid(row=9, column=2)

    label_Tendon = StringVar(window, "Tendon Rating: ")
    label_Tendon_Dir = Label(window, textvariable=label_Tendon, font=font_courier15B)
    label_Tendon_Dir.grid(row=10, column=1)
    Tendon_ = Entry(window, width=100, font=font_courier15)
    Tendon_.grid(row=10, column=2)

    label_Meatballs = StringVar(window, "Meatballs Rating: ")
    label_Meatballs_Dir = Label(window, textvariable=label_Meatballs, font=font_courier15B)
    label_Meatballs_Dir.grid(row=11, column=1)
    Meatballs_ = Entry(window, width=100, font=font_courier15)
    Meatballs_.grid(row=11, column=2)

    label_AddComments = StringVar(window, "Additional Comments: ")
    label_AddComments_Dir = Label(window, textvariable=label_AddComments, font=font_courier15B)
    label_AddComments_Dir.grid(row=12, column=1)
    AddComments_ = Entry(window, width=100, font=font_courier15)
    AddComments_.grid(row=12, column=2)

    # Consolidating Data into end data dictionary
    def submit():

        # TODO: Error check for when user inputs invalid entries for data
        # I.E. a rating not in range 1 - 10, letters, special characters, etc.

        data_dict = \
            {
                "NameofRestaurant": str(nameOfRestaurant_.get()),
                "Location(FullAddress)": location_.get(),
                "SpringRolls": springRolls_.get(),
                "SR_Sauce": SR_Sauce_.get(),
                "Broth": Broth_.get(),
                "Noodles": Noodles_.get(),
                "RawSteak": RawSteak_.get(),
                "Brisket": Brisket_.get(),
                "Tripe": Tripe_.get(),
                "Tendon": Tendon_.get(),
                "Meatballs": Meatballs_.get(),
                "AdditionalComments": AddComments_.get()
            }
        # Error checks
        keys = list(data_dict.keys())
        values = list(data_dict.values())

        # Empty Data Entries
        if "" in values:
            print("EMPTY DATA ENTRY DETECTED")
            raise EXCEPTION

        # Numeric entries for ratings only, between 1 and 10
        for key in keys[2:11]:
            if not data_dict[key].isdigit():
                print("INVALID INPUT FOR RATING, PLEASE ENTER A NUMERIC VALUE BETWEEN 1 - 10")
                raise EXCEPTION
            else:
                if int(data_dict[key]) > 10 or int(data_dict[key]) < 1:
                    print("INVALID INPUT FOR RATING, NUMERIC VALUE MUST BE BETWEEN 1 - 10")
                    raise EXCEPTION

        data_list.append(data_dict)

        # Clear Data from Entry Boxes
        nameOfRestaurant_.delete(0, END)
        location_.delete(0, END)
        springRolls_.delete(0, END)
        SR_Sauce_.delete(0, END)
        Broth_.delete(0, END)
        Noodles_.delete(0, END)
        RawSteak_.delete(0, END)
        Brisket_.delete(0, END)
        Tripe_.delete(0, END)
        Tendon_.delete(0, END)
        Meatballs_.delete(0, END)
        AddComments_.delete(0, END)

    button = tk.Button(window, text="Submit", command=submit)
    button.grid(row=13, column=1)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()
    button2 = tk.Button(window, text="Exit", command=on_closing)
    button2.grid(row=13, column=2)
    window.protocol("WM_DELETE_WINDOW", on_closing)

    window.mainloop()
    return data_list

