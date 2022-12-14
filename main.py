from tkinter import *
from tkinter import ttk
import math
import json as js
                                                                                                                                                                                                                                                                
window = Tk()
window.geometry("500x300")
window.title("Line of sight calculators")
# calculations
d = StringVar(window)
fresnel = StringVar(window)
R=6371*1000
def getD(h1, h2):
    d1 = math.sqrt(2*(4/3)*R*h1)
    d2 = math.sqrt(2*(4/3)*R*h2)
    return round(d1 + d2, 2)
    
def getFresnel(d, f):
    return round(17.31*(math.sqrt((d)/(4*f))), 2)

#display functions for tab 1

def calc():
    los = getD(tower1.get(), tower2.get())
    fres = getFresnel(los, int(freq.get()))
    d.set("Line of sight: {}".format(los))
    fresnel.set("Diameter of Fresnel area:\n {}".format(fres))
def saveToJson():
    h1 = tower1.get()
    h2 = tower2.get()
    f = int(freq.get())
    los = getD(h1, h2)
    fres = getFresnel(los, f)
    data = {
        "Tower 1 height": h1,
        "Tower 2 height": h2,
        "frequency": f, 
        "Line of sight": los, 
        "Fresnel zone": fres
        }
    with open("data_for_two_towers.json", "w") as outfile:
        js.dump(data, outfile)
#creating tabs
tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.pack(fill = "both")

# TAB 1 

labelt1 = Label(tab1, text="Height of\n first tower: [m]").grid(column = 0, row = 0, padx = 30)
tower1 = Scale(tab1, from_= 0, to = 100)
tower1.grid(column = 0, row = 1, padx = 30)
labelt2 = Label(tab1, text="Height of\n second tower: [m]").grid(column = 2, row = 0, padx = 30)
tower2 = Scale(tab1, from_= 0, to = 100)
tower2.grid(column = 2, row = 1, padx = 30)
freqlabel = Label(tab1, text="Frequency [GHz]").grid(row = 2, column = 1)
freq = Entry(tab1)
freq.grid(row = 3, column = 1)
calcbutton = Button(tab1, text = "Calculate", command = calc).grid(column = 0, row = 4)
json = Button(tab1, text = "Save to JSON", command = saveToJson).grid(column = 2, row = 4)
res1 = Label(tab1, textvariable = d)
res1.grid(row = 5, column = 1)
res2 = Label(tab1, textvariable = fresnel)
res2.grid(row = 6, column = 1)


# functions for tab 2


def saveToJson2():
    h = int(heightInput.get())
    d = round(math.sqrt(2*(4/3)*R*h), 2)
    data = {
        "Tower height": h,
        "X coords": xInput.get(),
        "Y coords": yInput.get(), 
        "Line of sight": d
        }
    with open("data_for_one_tower.json", "w") as outfile:
        js.dump(data, outfile)

# TAB 2

hlabel = Label(tab2, text = "Tower height:").grid(column = 0, row = 0)
heightInput = Entry(tab2, width = 15)
heightInput.grid(column = 0, row = 1, padx=5)
xlabel = Label(tab2, text = "X:").grid (column = 1, row = 0)
xInput = Entry(tab2)
xInput.grid(column = 1, row = 1, padx=5)
ylabel = Label(tab2, text = "Y:").grid(column = 2, row = 0)
yInput = Entry(tab2)
yInput.grid(column = 2, row = 1, padx=5)
jsonButton = Button(tab2, text = "Add to json", command=saveToJson2).grid(column = 1, row = 2, pady=30)
window.mainloop()