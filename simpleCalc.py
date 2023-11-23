from tkinter import *
import operator

window = Tk()


def submit2():
    global num1
    global entry2
    global entry3
    num1 = entry2.get()
    num2 = entry3.get()
    try:
        Label(window, text=(y(int(num1), int(num2))), font=("Arial", 30)).pack()
    except:
        print(ZeroDivisionError)
        submit()

def submit():

    # SETS THE FIRST ENTRY BOX TO CHOSEN OPERATOR
    global value
    global entry2
    global entry3
    global y
    value = myEntry.get()
    print(value)
    ops = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul}
    if value == '1':
        for i in range(10):
            print("test")
    elif value == '2':
        y = ops['+']
    elif value == '3':
        y = ops['-']
    elif value == '4':
        y = ops['/']
    elif value == '5':
        y = ops['*']

    #   MAKES THE ENTRY BOXES FOR NUMBERS
    Label(window, text="First number: ").pack()
    entry2 = Entry(window, bd=0, borderwidth=8)
    entry2.pack()
    Label(window, text="Second number: ").pack()
    entry3 = Entry(window, borderwidth=8)
    entry3.pack()
    Button(window,
           text="Submit",
           relief='ridge',
           font=("Arial",12),
           borderwidth=4,
           command=submit2).pack()


#   MAKES WINDOW
window.title("Calc")
window.geometry("400x800")

Label(window,font=("Arial", 17), text="1)Test 2)Addition 3)Subtraction \n4)Division 5)Multiplication").pack()

#   FIRST ENTRY BOX
myEntry = Entry(window, bd=0,
                font=("Arial", 12),
                borderwidth=8)
myEntry.pack()

#   CALLS SUBMIT FUNCTION

submitButton = Button(window,
                      text="Submit",
                      command=submit,
                      borderwidth=4,
                      font=("Arial",12),
                      relief='ridge')
submitButton.pack()


window.mainloop()
