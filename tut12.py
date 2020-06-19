from tkinter import *

root = Tk()


def getvals():
    print("Submitting form")
    # name_value.get()

    print(f"{name_value.get(), phone_value.get(), gender_value.get(), emergency_value.get(), payment_mode_value.get(), food_service_value.get()}")

    with open("records.txt", "a") as f:
        f.write(f"{name_value.get(), phone_value.get(), gender_value.get(), emergency_value.get(), payment_mode_value.get(), food_service_value.get()}\n")


root.geometry("644x344")
# Heading
Label(root, text="Welcome to Harry Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

# Text for our form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
payment_mode = Label(root, text="Payment Mode")

# Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment_mode.grid(row=5, column=2)

# Tkinter variable for storing entries
name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
emergency_value = StringVar()
payment_mode_value = StringVar()
food_service_value = IntVar()

# Entries for our form
name_entry = Entry(root, textvariable=name_value)
phone_entry = Entry(root, textvariable=phone_value)
gender_entry = Entry(root, textvariable=gender_value)
emergency_entry = Entry(root, textvariable=emergency_value)
payment_mode_entry = Entry(root, textvariable=payment_mode_value)

# Packing the Entries
name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
emergency_entry.grid(row=4, column=3)
payment_mode_entry.grid(row=5, column=3)

# Checkbox & Packing it
food_service = Checkbutton(text="Want to prebook your meals?", variable=food_service_value)
food_service.grid(row=6, column=3)

# Button & Packing it and assigning it a command
Button(text="Submit to Harry Travels", command=getvals).grid(row=7, column=3)

root.mainloop()
