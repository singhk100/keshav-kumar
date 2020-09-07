from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import datetime
import speech_recognition as sr
import win32com.client as wincl
from textblob import TextBlob

def read():
    speak = wincl.Dispatch("SAPI.SpVoice")
    text=TextArea.get(1.0,END)
    lang=TextBlob(text)
    print(type(text))
    if len(text)==0:
        speak.Speak("please write something, so that i could spell")
    elif lang.detect_language()!='en':
        speak.Speak("Sorry microsoft api has english language so I could not speak other language ")
    else:
        speak.Speak(text)
    
def speak():
    # Initialize the recognizer 
    r = sr.Recognizer() 

	
# Loop infinitely for user to 
# speak 
    with sr.Microphone() as source:
        print("say something")
        audio=r.listen(source)
        print("time over, thanks")
    
    try:
        print(r.recognize_google(audio))
        text=r.recognize_google(audio)+' '
        TextArea.insert(END,text)
    except:
        showinfo("sorry","please speak clearly")
             
    
def dark():
    TextArea.configure(bg='black',insertbackground='white',fg='white')

def light():
    TextArea.configure(background='white',fg='black')


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        print("File opened")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    print("Notepad closed")
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))
    print("Something cut")

def copy():
    TextArea.event_generate(("<<Copy>>"))
    print("Something copied")

def paste():
    TextArea.event_generate(("<<Paste>>"))
    print("Something pasted")
    
def language_hin():
    lang=TextBlob(TextArea.get(1.0,END))
    if lang.detect_language()=='hi':
        pass
    else:
        try:
            lang=lang.translate(to='hi')
            TextArea.delete(1.0, END)
            TextArea.insert(END,lang)
            TextArea.insert(END," ")
        except:
            showinfo("translation","sorry can't translate")
        
def language_eng():
    lang=TextBlob(TextArea.get(1.0,END))
    if lang.detect_language()=='en':
        pass
    else:
        try:
            lang=lang.translate(to='en')
            TextArea.delete(1.0, END)
            TextArea.insert(END,lang)
            TextArea.insert(END," ")
        except:
            showinfo("translation","sorry can't translate")
        
def language_chi():
    lang=TextBlob(TextArea.get(1.0,END))
    if lang.detect_language()=='zh':
        pass
    else:
        try:
            lang=lang.translate(to='zh')
            TextArea.delete(1.0, END)
            TextArea.insert(END,lang)
            TextArea.insert(END," ")
        except:
            showinfo("translation","sorry can't translate")

def about():
    showinfo("Notepad", "Notepad by Dolly and Keshav")
    
def view():
    string=open("help.txt","r")
    string=""+str(list(string))
    showinfo("Notepad",string)

#main function

#def main():
     #Basic tkinter setup
    


if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("1.ico")
    root.geometry("644x788")
   


    #status bar
    statusvar=StringVar()        
    label=Label(root,relief=SUNKEN, anchor="w",textvariable=statusvar,font=('arial',16,'normal'))
    #statusvar.set(datetime.now())
    label.pack(fill=X,side=BOTTOM)        

   
       #Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New                  ctrl+N", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open                ctrl+O", command = openFile)

    # To save the current file

    FileMenu.add_command(label = "Save                 ctrl+S", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit                    alt+f4", command = quitApp)

    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut                     ctrl+X", command=cut)
    EditMenu.add_command(label = "Copy                 ctrl+C", command=copy)
    EditMenu.add_command(label = "Paste                 ctrl+V", command=paste)
    languageMenu=Menu(EditMenu, tearoff=0)
    languageMenu.add_command(label= "English", command=language_eng)
    languageMenu.add_command(label= "Hindi", command=language_hin)
    languageMenu.add_command(label= "chinese", command=language_chi)
    EditMenu.add_cascade(label="Language", menu=languageMenu)

    
    MenuBar.add_cascade(label="Edit", menu =EditMenu)

    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    HelpMenu.add_command(label = "View Help", command= view)

    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    # Mode menu starts
    ModeMenu = Menu(MenuBar, tearoff=0)
    ModeMenu.add_command(label="Dark",command=dark)
    ModeMenu.add_command(label="Light",command=light)

    MenuBar.add_cascade(label="Mode",menu=ModeMenu)
      # Mode menu ends
    
    #speak start
    SpeakMenu = Menu(MenuBar, tearoff=0)
    SpeakMenu.add_command(label="speak something",command=speak)
    SpeakMenu.add_command(label="read",command=read)
    MenuBar.add_cascade(label="voice",menu=SpeakMenu)
    #speak ends
    
    
    root.config(menu=MenuBar)

    #Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
   
