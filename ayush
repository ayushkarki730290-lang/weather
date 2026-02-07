from tkinter import *
from tkinter import  ttk
import  requests

def data_get():
   city = city_name.get()
   data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c875dcc58d20aeb5ca39455f378f3e26").json()
   w_label1.config(text=data["weather"][0]["main"])
   d_label1.config(text=data["weather"][0]["description"])
   temp_label1.config(text=str(data["main"]["temp"]-273.15))
   p_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("GUI WEATHER APP")
win.config(bg = "sky blue")
win.geometry("500x550")

name_label = Label(win, text="gui weather app" ,
                   font=("times new roman" ,35,"bold"))
name_label.place(x=25,y=50,height=50, width=450)
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, text= "gui weather app" ,values=list_name ,
                   font=("times new roman" ,20,"bold"), textvariable=city_name)
com.place(x=25,y=120,height=50, width=450)


w_label = Label(win, text="Weather Climate" ,
                   font=("times new roman" ,15,"bold"))
w_label.place(x=25,y=250,height=50, width=200)

w_label1 = Label(win, text="" ,
                   font=("times new roman" ,15,"bold"))
w_label1.place(x=250,y=250,height=50, width=200)
d_label = Label(win, text="Weather Description" ,
                   font=("times new roman" ,15,"bold"))

d_label.place(x=25,y=330,height=50, width=200)

d_label1 = Label(win, text="" ,
                   font=("times new roman" ,15,"bold"))

d_label1.place(x=250,y=330,height=50, width=200)
temp_label = Label(win, text="Temperature" ,
                   font=("times new roman" ,15,"bold"))
temp_label.place(x=25,y=400,height=50, width=200)

temp_label1 = Label(win, text="" ,
                   font=("times new roman" ,15,"bold"))
temp_label1.place(x=250,y=400,height=50, width=200)

per_label = Label(win, text="Pressure" ,
                   font=("times new roman" ,15,"bold"))
per_label.place(x=25,y=470,height=50, width=200)


p_label1 = Label(win, text="" ,
                   font=("times new roman" ,15,"bold"))
p_label1.place(x=250,y=470,height=50, width=200)


done_button = Button(win, text="done" ,
                         font=("times new roman" ,20,"bold"), command=data_get )
done_button.place(x=200,y=190,height=50, width=100)



win.mainloop()
}
