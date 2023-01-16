from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=500, height=300)
window.config(padx=200, pady=100)

font_type = ("Arial", 24, "bold")

the_input = Entry(width=15, font=font_type)
the_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=font_type)
miles_label.grid(column=2, row=0)
miles_label.config(padx=8)

convert_label = Label(text="is equal to", font=font_type)
convert_label.grid(column=0, row=1)
convert_label.config(padx=4)

km_label = Label(text="0", font=font_type)
km_label.grid(column=1, row=1)
km_label.config(padx=8)

kilometers = Label(text="Km", font=font_type)
kilometers.grid(column=2, row=1)


def convert():
    converted_unit = round(int(the_input.get()) * 1.609, 2)
    kms_label = Label(text=f"{converted_unit}", font=font_type)
    kms_label.grid(column=1, row=1)


button = Button(text="Calculate", command=convert, font=font_type)
button.grid(column=1, row=2)
button.config(padx=15)

window.mainloop()
