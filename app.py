import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from pressure_code import*
from baseline_code import*
from slant_aligment_code import*
from zone import *
from margins import *
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frameInside = tk.Frame(self)
        frameInside.pack(side="left",fill="y",expand=True)
        #load logo
        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)
        #make logo widget and assign it to frame1/container 1
        logo_label = tk.Label(frameInside, image=logo)
        logo_label.image = logo
        logo_label.pack(fill="both",expand=True)

        frameInside2 = tk.Frame(self)
        frameInside2.pack(side="right", fill="both", expand=True)
        button1 = tk.Button(frameInside2, text="Upload a New Handwriting",
                           command=lambda: controller.show_frame(PageOne),font = "Arial", bg = "#6b80b9",fg = 'white')
        button1.pack(fill="both", expand=True, pady=10)
        
        button2 = tk.Button(frameInside2, text="About Us",
                           command=lambda: controller.show_frame(PageTwo),font = "Arial", bg = "#6b80b9",fg = 'white')
        button2.pack(fill="both", expand=True, pady=10)

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.filename = None
        self.label_image = None
        self.label_text = None
        self.label_Pressure = None
        self.label_PressureDescription = None
        self.label_Baseline = None
        self.label_BaselineDescription = None
        self.label_SlantAllignment = None
        self.label_SlantAllignmentDescription = None
        self.label_Margins = None
        self.label_MarginsDescription = None
        self.label_Zones = None
        self.label_ZonesDescription = None


        def open_file_dialog():
            self.filename = filedialog.askopenfilename(initialdir = "/", 
                                                       title = "Select a File", 
                                                       filetypes = (("jpeg files","*.jpg"), 
                                                                    ("all files","*.*")))
            if self.filename:
                image = Image.open(self.filename)
                image = image.resize((250, 250), Image.ANTIALIAS)
                image = ImageTk.PhotoImage(image)
                if self.label_image:
                    self.label_image.destroy()
                self.label_image = tk.Label(self, image=image)
                self.label_image.image = image
                self.label_image.pack()
                self.label_text = tk.Label(self, text=f"Selected file: {self.filename}", font=('Verdana', 12))
                self.label_text.pack()
                pressureResults = evaluatePressure(self.filename)
                print(pressureResults)
                self.label_Pressure = tk.Label(self, text="Pressure", font=('Verdana', 18))
                self.label_Pressure.pack()
                self.label_PressureDescription = tk.Label(self, text=f"Pressure refers to how dark your hand writing is. A darker handwriting is clearer then a faded one. It is also often associated with being more energetic.\n Your HandWriting Scored: {pressureResults}", font=('Verdana', 12))
                self.label_PressureDescription.pack()
                baseLineResults = evaluateBaseLine(self.filename)
                self.label_Baseline = tk.Label(self, text="Baseline", font=('Verdana', 18))
                self.label_Baseline.pack()
                self.label_BaselineDescription =  tk.Label(self, text=f"Baseline refers to the slant deviation of your characters in relation to the first character. Your writing can deviate upwards from the baseline,downwards from the baseline, be straight or unven. An upwards deviation is associated optimism.\n It was found that your hand writing: {baseLineResults}", font=('Verdana', 12))
                self.label_BaselineDescription.pack()
                slantAllignmentResults = evaluateSlantAllignment(self.filename)
                self.label_SlantAllignment  = tk.Label(self, text="Slant Allignment", font=('Verdana', 18))
                self.label_SlantAllignment.pack()
                self.label_SlantAllignmentDescription =  tk.Label(self, text=f"Ever wonder how in tune a person might be with their emotions? A persons slant allignment is often associated with this characteristic and creativity. The more right the slant per letter the likelier the person is emotional.\n It was found that your hand writing overall is: {slantAllignmentResults}", font=('Verdana', 12))
                self.label_SlantAllignmentDescription.pack()
                #margins Evaluation goes here
                #marginsEvaluation = margin(self.filename)
                self.label_Margins = tk.Label(self,text = "Margins",font =('Verdana',18))
                self.label_Margins.pack()
                self.label_MarginsDescription = tk.Label(self,text=f'What side of the paper do you write on? Depending on the persons outlook on life this might change. The main allignments are left side, right side, or middle.\n Your handwriting is center alligned', font=('Verdana', 12))
                self.label_MarginsDescription.pack()
                #zones Evaluation goes here
                zoneEvaluation = zoning(self.filename)
                self.label_Zones = tk.Label(self,text = "Zones",font =('Verdana',18))
                self.label_Zones.pack()
                self.label_ZonesDescription = tk.Label(self,text=f'Zones refers to the vertical margins of your hand writing. Some letters should either be in the upper zone like(t,l,h), in the middle zone (a,c,i,o), or the lower zone (f,g,y,p). The deviation of some letters from these zones may imply that the person likes to stand out.\n On average your writing {zoneEvaluation} alligned(upper, bottom, middle)', font=('Verdana', 12))
                self.label_ZonesDescription.pack()


        def clear_image():
            if self.label_image:
                self.label_image.destroy()
                self.label_image = None

            if self.label_text:
                self.label_text.destroy()
                self.label_text = None
                self.label_Pressure.destroy()
                self.label_Pressure = None
                self.label_PressureDescription.destroy()
                self.label_PressureDescription = None
                self.label_Baseline.destroy()
                self.label_Baseline = None
                self.label_BaselineDescription.destroy()
                self.label_BaselineDescription = None
                self.label_SlantAllignment.destroy()
                self.label_SlantAllignment = None
                self.label_SlantAllignmentDescription.destroy()
                self.label_SlantAllignmentDescription = None
                self.label_Margins.destroy()
                self.label_Margins = None
                self.label_MarginsDescription.destroy()
                self.label_MarginsDescription = None
                self.label_Zones.destroy()
                self.label_Zones = None
                self.label_ZonesDescription.destroy()
                self.label_ZonesDescription = None
        
        button = tk.Button(self, text="Upload Image", command=open_file_dialog)
        button.pack()
        # frameInside = tk.Frame(self)
        # scrollbar = tk.Scrollbar(frameInside)
        
        # frameInside.pack()
        # scrollbar.pack()
        
        button = tk.Button(self, text="Back to Start Page",
                           command=lambda: (controller.show_frame(StartPage), clear_image()))
        button.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="About Us", font=('Arial', 14))
        label.pack(pady=10, padx=10)
        
        label = tk.Label(self, text="This Project was made for HopperHacks 2023. The aim of this project is to evaluate a person's handwriting based on 6 criteria used in graphology; Pressure, Baselines, Margins, Slant, and Zones. Upload a picture of your handwriting to learn more! Note that for the best results images should follow the following guidelines:\n1. Uploaded images should have been taken in a well lit enviroment\n2. Preferably text should be on white paper\n3. Text should consist of a single line of words/characters\n4. Start a line with a Capital Letter",
                         font=('Verdana', 12), justify=tk.LEFT, wraplength=500)
        label.pack(pady=10, padx=10)
        
        button = tk.Button(self, text="Back to Start Page",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()

app = App()
app.mainloop()
