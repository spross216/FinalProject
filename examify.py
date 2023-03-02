import tkinter as tk

class Examify(tk.Tk): 

    def __init__(self):
        super().__init__()
        
        '''
        Gui elements have been placed in the class constructor. I wanted to have a dark blue stripe to the left. This is where I will have the file 
        upload button. To try and color match the window decorator icon, I wanted to accent the dark blue with yellow. I wanted to keep the 
        application window simple and attractive, while foregoing the creation of additional windows.
        
        '''
        
        self.title("Examify")
        self.configure(bg="White")
        self.iconbitmap('exam.ico')
        self.geometry('800x400')

        blueFrame = tk.Frame(
            self, 
            width=300, 
            height=self.winfo_screenheight(),
            bg='dark blue'
        )
        blueFrame.pack(side='left', fill='y')

        entry = tk.Entry(
            blueFrame, 
            bg='white', 
            borderwidth=0, 
            highlightthickness=2, 
            highlightbackground='gold'
        )
        entry.pack(side='top', padx=20, pady=20)

        uploadFileButton = tk.Button(blueFrame, text='Upload File')
        uploadFileButton.pack(side='top', pady=10)

        examifyButton = tk.Button(blueFrame, text='Examify!')
        examifyButton.pack(side='top')

        dynamicFrame = tk.Frame(
            self,
            bg='white',
            bd=2,
            highlightthickness=2,
            highlightbackground='dark blue'
        )
        dynamicFrame.pack(fill='both', expand=True, padx=20, pady=20)
        

if __name__ == "__main__":
   Examify().mainloop()