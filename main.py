from tkinter import *
from tkinter import messagebox
from pysurfline import SurfReport
import pandas

def changestring(paramater, id_):
	params = {
    "spotId": id_,
    "days": 3,
    "intervalHours": 3,
}
	report = SurfReport(params)
	sizelog = report.df[[paramater]].iat[0,0]
	return(str(sizelog))

def btn_clicked():
	messagebox.showwarning(title="Processing...", message = "Load Data?")
	useful_id = entry0.get()
	items = {"surf_humanRelation": [height, "Height: "], "temperature": [Temperature, "Temperature: "], "speed": [Wind_Speed, "Wind Speed: "], 
	"condition": [Condition, "Condition: "]}
	for val in items:
		canvas.itemconfigure(items[val][0], text="{0}{1}".format(items[val][1], changestring(val,useful_id)))

window = Tk()

window.geometry("700x400")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 400,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    652.0, 442.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    145.5, 38.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    fg = "#000000",
    highlightthickness = 0)

entry0.place(
    x = 27, y = 19,
    width = 240,
    height = 38)

height = canvas.create_text(
    137.5, 120.5,
    text = "Height:",
    fill = "#000000",
    font = ("None", int(15.0)))

Temperature = canvas.create_text(
    137.5, 184.5,
    text = "Temperature:",
    fill = "#000000",
    font = ("None", int(15.0)))

Wind_Speed = canvas.create_text(
    137.5, 248.5,
    text = "Wind Speed:",
    fill = "#000000",
    font = ("None", int(15.0)))

Condition = canvas.create_text(
    137.5, 312.5,
    text = "Condition:",
    fill = "#000000",
    font = ("None", int(15.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 576, y = 18,
    width = 100,
    height = 40)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 460, y = 18,
    width = 100,
    height = 40)

window.resizable(False, False)
window.mainloop()
