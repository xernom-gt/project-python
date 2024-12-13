from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        # Ganti 'x' dengan '*' agar eval bisa memproses perkalian
        equation_text_modified = equation_text.replace("x", "*")
        
        # Cek apakah ekspresi kosong
        if equation_text == "":
            equation_label.set("Input kosong")
            return
        
        # Evaluasi ekspresi matematika
        total = str(eval(equation_text_modified))

        equation_label.set(total)
        equation_text = total
    
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text = "" 
    except Exception as e:
        equation_label.set(f"Error: {str(e)}")
        equation_text = ""

def clear():
    global equation_text
    equation_text = ""
    equation_label.set("")

# Membuat jendela aplikasi
window = Tk()
window.title("Kalkulator")
window.geometry("500x600")

# Mengubah warna background window menjadi navy
window.config(bg="#000080")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("consolas", 20), bg="white", width=20, height=2)
label.pack()

frame = Frame(window)
frame.pack()

# Membuat tombol angka
buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('0', 3, 0)
]

for (text, row, col) in buttons:
    Button(frame, text=text, width=9, height=4, font=35, 
           command=lambda t=text: button_press(t)).grid(row=row, column=col)

# Membuat tombol operator
operators = [
    ('+', 0, 3), ('-', 1, 3), ('x', 2, 3), ('/', 3, 3),
    ('.', 3, 1)
]

for (text, row, col) in operators:
    Button(frame, text=text, width=9, height=4, font=35, 
           command=lambda t=text: button_press(t)).grid(row=row, column=col)

# Tombol equals (=)
Button(frame, text="=", width=9, height=4, font=35, command=equals).grid(row=3, column=2)

# Tombol clear
Button(window, text="clear", width=9, height=4, font=35, command=clear).pack()

window.mainloop()
