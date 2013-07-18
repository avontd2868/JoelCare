#JoelCare

from tkinter import*

class Application(Frame):
    """An application for providers that simplifies
    the handling of medical records."""
    def __init__(self, master):
        """Initialize frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """This is where the functions of the program will go"""
        #create description label
        Label(self,
              text = "Patient Info:"
              ).grid(row = 0, column = 0, sticky = W)


#main
root = Tk()
root.title("Joelcare")
root.geometry("640x480")
app = Application(root)
root.mainloop()
