# Program to calculate bmi from height and weight
""""The BMI is calculated by dividing an adult's weight in kilograms by their height in metres squared.
For example, if you weigh 70kg (around 11 stone) and are 1.73m (around 5 foot 8 inches) tall,
 you work out your BMI by: squaring your height in metres: 1.73 x 1.73 = 2.99."""

# importing modules
from tkinter import *
from tkinter import messagebox

# setting up the window


window = Tk()
window.title("BMI Index Calculator")
window.config(padx=50, pady=20)

# -----------------------Calculate Mechanism---------------
"""1 foot = 30.48, 1 in = 2.54 cm  and The BMI is calculated by dividing an adult's weight in kilograms 
by their height in metres squared.  """


def reset():
    feet_input.delete(0, END)
    inch_input.delete(0, END)
    weight_input.delete(0, END)
    result_output.configure(text="0")


def convert():
    feet = float(feet_input.get())
    inch = float(inch_input.get())
    cm = (feet * 30.48) + (inch * 2.54)
    m = cm / 100
    weight = float(weight_input.get())
    bmi = round(weight / pow(m, 2), 2)
    result_output.configure(text=f"{bmi}")
    bmi_description = describe_bmi(bmi)
    optimal_weight = optimal_weight_range(m)
    messagebox.showinfo("BMI and Optimal Weight Range", f"BMI: {bmi}\n{bmi_description}\n\n{optimal_weight}")


def describe_bmi(bmi):
    if bmi < 18.5:
        description = "Status: Underweight\nSuggestion: You may need to gain some weight. Consult with a healthcare " \
                      "provider for guidance. "
    elif 18.5 <= bmi < 25:
        description = "Status: Normal weight\nSuggestion: Your weight is considered normal for your height."
    elif 25 <= bmi < 30:
        description = "Status: Overweight\nSuggestion: You may need to lose some weight. Consult with a healthcare " \
                      "provider for guidance. "
    else:
        description = "Status: Obese\nSuggestion: You may need to lose weight for health reasons. Consult with a " \
                      "healthcare provider for guidance. "
    return description


def optimal_weight_range(height):
    lower_bmi = 18.5
    upper_bmi = 24.9
    lower_weight = lower_bmi * pow(height, 2)
    upper_weight = upper_bmi * pow(height, 2)
    return f"Optimal weight range for your height is {lower_weight:.2f} kg to {upper_weight:.2f} kg."


# ----------------------Ui design-----------------------
# Height in Feet and Inch
height_label = Label(text="Your Height:")
height_label.grid(column=0, row=0)

feet_input = Entry()
feet_input.grid(column=1, row=0)

inch_input = Entry()
inch_input.grid(column=2, row=0)

feet_label = Label(text="Feet")
feet_label.grid(column=1, row=1)

inch_label = Label(text="Inch")
inch_label.grid(column=2, row=1)

weight_label = Label(text="Your Weight:")
weight_label.grid(column=0, row=2)

weight_input = Entry()
weight_input.grid(column=1, row=2)

kg_label = Label(text="Kg")
kg_label.grid(column=1, row=3)

calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=5)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=5)

# Result
result_label = Label(text="Your BMI:")
result_label.grid(column=0, row=6)

result_output = Label(text="0")
result_output.grid(column=1, row=6)

status_output = Label(text="")
status_output.grid(column=1, row=7, columnspan=2)

window.mainloop()
