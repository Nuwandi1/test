from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import  datetime
import requests
import pytz

root =Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
root.configure(bg='white')

def getweather():
    try:
        city=textfield.get()

        geolocator=Nominatim(user_agent="geoapiExercises")
        location =geolocator.geocode(city)
        obj= TimezoneFinder()
        results= obj.timezone_at(lng=location.longitude,lat=location.latitude)
        #print(results)

        home=pytz.timezone(results)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

       #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c34e59a4cbfe4d410ff81a743a406d37"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("weather App","Invalid Entry!!")

#Search Box
Search_image=PhotoImage(file="")
myimage = Label(root,image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center", width=17, font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=300,y=40)
textfield.focus()

seach_icon=PhotoImage(file="searchi.png")
myimage_icon = Button(image=seach_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myimage_icon.place(x=620,y=44)

#logo
Logo_image=PhotoImage(file="wheather.png")
logo=Label(image=Logo_image)
logo.place(x=250,y=100)

#bottom Bocx
frame_image=PhotoImage(file="box1.png")
frame_myimage=Label(image=frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("helvetica",20))
clock.place(x=30,y=130)

#lable
lable1=Label(root,text="WIND",font=("Helvetic",15,'bold'),fg="white",bg="#1ab5ef")
lable1.place(x=120,y=400)

lable2=Label(root,text="HUMIDITY",font=("Helvetic",15,'bold'),fg="white",bg="#1ab5ef")
lable2.place(x=250,y=400)

lable3=Label(root,text="DESCRIPTION",font=("Helvetic",15,'bold'),fg="white",bg="#1ab5ef")
lable3.place(x=430,y=400)

lable4=Label(root,text="PRESSURE",font=("Helvetic",15,'bold'),fg="white",bg="#1ab5ef")
lable4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=250,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=430,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)

root.mainloop()