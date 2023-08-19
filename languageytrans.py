from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk

root1= Tk()

# size of the window
root1.geometry('1200x510')

root1.resizable(0, 0)

# background color of window
root1.config(bg='white')

# title of window
root1.title("Language Translator")

# resizing the images for ON button
on_img = Image.open("On.png")
resize_on_img= on_img.resize((70, 40))
on= ImageTk.PhotoImage(resize_on_img)

# resizing the images for OFF button
off_img= Image.open("Off.png")
resize_off_img= off_img.resize((70, 40))
off= ImageTk.PhotoImage(resize_off_img)

global is_on
is_on= False

# heading
Label(root1, text="Language Translator with GUI", font="arial 20 bold", bg= 'light blue').pack()

# space for input text
Label(root1, text="Enter Text", font='arial 14 bold', bg= 'light green').place(x=350, y=60)
Input_text = Text(root1, font='arial 10', height=15, wrap=WORD, width=60, padx=5, pady=10)
Input_text.place(x=30, y=100)

# creating space for output text
Label(root1, text="Output", font='arial 13 bold').place(x=650, y=60)
Output_text = Text(root1, font='arial 10', height=15, wrap=WORD, width=60, padx=5, pady=10)
Output_text.place(x=600, y=100)

# list of all languages that can be translated.
languages = list(LANGUAGES.values())

# list of languages for input in combobox.
source_language = ttk.Combobox(root1, value= languages, width= 23, font= 'ariel')
source_language.place(x=30, y=60)
source_language.set("Choose the input language")


# list of languages for output in combobox
destination_language = ttk.Combobox(root1, value= languages, width= 23, font= 'ariel')
destination_language.place(x=790, y=60)
destination_language.set("Choose the output language")




def Translate():
    # error handling method used
    try:
        translator = Translator()

        #checking if the input/output language is selected or not
        if(source_language.get() == "choose the input language" or source_language.get() == "" or destination_language.get() == "choose the output language" or destination_language.get() == ""):
            print("Please select the input/output language")

        #checking if any letter is typed or not
        elif len(Input_text.get(1.0, END)) == 1:
            print("Please type any sentence or word")

        else:
            translated_text = translator.translate(text=Input_text.get(1.0, END), src=source_language.get(),dest=destination_language.get())
            Output_text.delete(1.0, END)
            Output_text.insert(END, translated_text.text)

    except:
        print("Check your network connection.")


# creating the button to translate
translate_button= Button(root1, text= "Translate", font= 'arial 13 bold', command= Translate, width= 10, height= 5, bg='red')
translate_button.place(x=475, y=150)


# switch function to ON and OFF the switch
def switch():
    global is_on

    if is_on:
        auto_translate_button.config(image=off)
        is_on = False

    else:
        auto_translate_button.config(image=on)
        is_on = True
        # if auto_translate button is ON then calling the auto_translate funtion
        root1.after(3000, auto_translate)

# button for auto translate
auto_translate_button= Button(root1, image= off, bd= 0, command= switch)
auto_translate_button.place(x= 980)


# label for auto translate
auto_translate_label = Label(root1, text= "Auto-Translate", font= ("ariel", 15))
auto_translate_label.place(x= 840, y= 9)



# function auto_translate will translate automatically without pressing translate button in every 3 seconds.
def auto_translate():
    if Input_text.get(1.0,END) is not None and is_on:
        Translate()
        root1.after(3000, auto_translate)


root1.mainloop()
