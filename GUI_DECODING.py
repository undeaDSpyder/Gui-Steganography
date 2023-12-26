import tkinter as tk
import tkinter.font as tkFont
import stepic #for stagnoGraphy
from PIL import Image #for image import

def dec():
    file=GLineEdit_810.get()
    # file=input("PHOTO: ")
    img= Image.open(file)
    data=GMessage_150.get()
    data=stepic.decode(img)
    # print("DATA:"+str(data))
    decoded_txt=str(data)
    # print("*----------------------------*") 
class App:
    def __init__(self, root):
        root.configure(background="Black")
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_866=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_866["font"] = ft
        GLabel_866["fg"] = "#333333"
        GLabel_866["justify"] = "center"
        GLabel_866["text"] = "DECODER"
        GLabel_866["background"] = "#fab055"
        GLabel_866.place(x=130,y=30,width=317,height=30) 

        GMessage_764=tk.Message(root)
        GMessage_764["bg"] = "#ffe554"
        ft = tkFont.Font(family='Times',size=15)
        GMessage_764["font"] = ft
        GMessage_764["fg"] = "#333333"
        GMessage_764["justify"] = "center"
        GMessage_764["text"] = "Enter The Image location/Name with Extension!"
        GMessage_764.place(x=0,y=130,width=601,height=90)

        global GLineEdit_810
        GLineEdit_810=tk.Entry(root)
        GLineEdit_810["bg"] = "#90ee90"
        GLineEdit_810["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_810["font"] = ft
        GLineEdit_810["fg"] = "#333333"
        GLineEdit_810["justify"] = "center"
        GLineEdit_810["text"] = "Entry"
        GLineEdit_810.place(x=0,y=220,width=597,height=52)

        GButton_771=tk.Button(root)
        GButton_771["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        GButton_771["font"] = ft
        GButton_771["fg"] = "#000000"
        GButton_771["justify"] = "center"
        GButton_771["text"] = "DECODE"
        GButton_771.place(x=230,y=310,width=144,height=46)
        GButton_771["command"] = self.GButton_771_command


    def GButton_771_command(self):
        global GMessage_150
        GMessage_150=tk.Message(root)
        GMessage_150["bg"] = "#ffba75"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_150["font"] = ft
        GMessage_150["fg"] = "#333333"
        GMessage_150["justify"] = "center"
        GMessage_150["text"] = dec()
        GMessage_150.place(x=0,y=390,width=599,height=61)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
