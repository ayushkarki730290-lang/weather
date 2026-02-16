from tkinter import *
from tkinter import  ttk
import  requests
import json
import traceback
import os

def data_get():
   # #region agent log
   try: log_path = r"c:\Users\singh\GITHUB\weather\.cursor\debug.log"; os.makedirs(os.path.dirname(log_path), exist_ok=True); log_file = open(log_path, "a", encoding="utf-8"); log_file.write(json.dumps({"id":"log_1","timestamp":int(__import__("time").time()*1000),"location":"ayush.py:8","message":"Function entry","data":{"function_called":True},"runId":"run1","hypothesisId":"A"})+"\n"); log_file.close()
   except: pass
   # #endregion
   try:
      city = city_name.get()
   except Exception as e:
      # #region agent log
      try: log_path = r"c:\Users\singh\GITHUB\weather\.cursor\debug.log"; os.makedirs(os.path.dirname(log_path), exist_ok=True); log_file = open(log_path, "a", encoding="utf-8"); log_file.write(json.dumps({"id":"log_1b","timestamp":int(__import__("time").time()*1000),"location":"ayush.py:12","message":"Error getting city_name","data":{"error_type":type(e).__name__,"error_msg":str(e)},"runId":"run1","hypothesisId":"A"})+"\n"); log_file.close()
      except: pass
      # #endregion
      raise
   # #region agent log
   try: log_path = r"c:\Users\singh\GITHUB\weather\.cursor\debug.log"; os.makedirs(os.path.dirname(log_path), exist_ok=True); log_file = open(log_path, "a", encoding="utf-8"); log_file.write(json.dumps({"id":"log_2","timestamp":int(__import__("time").time()*1000),"location":"ayush.py:21","message":"Before API call","data":{"city":city,"city_empty":not city or city.strip()==""},"runId":"run1","hypothesisId":"C"})+"\n"); log_file.close()
   except: pass
   # #endregion
   try:
      response = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c875dcc58d20aeb5ca39455f378f3e26")
      # #region agent log
      try: log_path = r"c:\Users\singh\GITHUB\weather\.cursor\debug.log"; os.makedirs(os.path.dirname(log_path), exist_ok=True); log_file = open(log_path, "a", encoding="utf-8"); log_file.write(json.dumps({"id":"log_3","timestamp":int(__import__("time").time()*1000),"location":"ayush.py:20","message":"API response received","data":{"status_code":response.status_code},"runId":"run1","hypothesisId":"B"})+"\n"); log_file.close()
      except: pass
      # #endregion
      data = response.json()
      # #region agent log
      try: log_path = r"c:\Users\singh\GITHUB\weather\.cursor\debug.log"; os.makedirs(os.path.dirname(log_path), exist_ok=True); log_file = open(log_path, "a", encoding="utf-8"); log_file.write(json.dumps({"id":"log_4","timestamp":int(__import__("time").time()*1000),"location":"ayush.py:23","message":"JSON parsed","data":{"has_weather":("weather" in data),"has_main":("main" in data),"response_keys":list(data.keys())[:10]},"runId":"run1","hypothesisId":"D"})+"\n"); log_file.close()
      except: pass
      # #endregion
      # #region agent log
      try: log_path = r"c:\Users\singh\GITHUB\weather\.cursor\debug.log"; os.makedirs(os.path.dirname(log_path), exist_ok=True); log_file = open(log_path, "a", encoding="utf-8"); log_file.write(json.dumps({"id":"log_5","timestamp":int(__import__("time").time()*1000),"location":"ayush.py:26","message":"Before accessing weather data","data":{"weather_exists":("weather" in data and len(data.get("weather",[]))>0),"main_exists":("main" in data),"error_in_response":("cod" in data and str(data.get("cod"))!="200"),"full_response":str(data)[:200]},"runId":"run1","hypothesisId":"A"})+"\n"); log_file.close()
      except: pass
      # #endregion
      w_label1.config(text=data["weather"][0]["main"])
      d_label1.config(text=data["weather"][0]["description"])
      temp_label1.config(text=str(data["main"]["temp"]-273.15))
      p_label1.config(text=data["main"]["pressure"])
      # #region agent log
      try: log_path = r"c:\Users\singh\GITHUB\weather\.cursor\debug.log"; os.makedirs(os.path.dirname(log_path), exist_ok=True); log_file = open(log_path, "a", encoding="utf-8"); log_file.write(json.dumps({"id":"log_6","timestamp":int(__import__("time").time()*1000),"location":"ayush.py:32","message":"Function exit success","data":{},"runId":"run1","hypothesisId":"A"})+"\n"); log_file.close()
      except: pass
      # #endregion
   except requests.exceptions.RequestException as e:
      # #region agent log
      try: log_path = r"c:\Users\singh\GITHUB\weather\.cursor\debug.log"; os.makedirs(os.path.dirname(log_path), exist_ok=True); log_file = open(log_path, "a", encoding="utf-8"); log_file.write(json.dumps({"id":"log_7","timestamp":int(__import__("time").time()*1000),"location":"ayush.py:36","message":"Network/API error","data":{"error_type":type(e).__name__,"error_msg":str(e)},"runId":"run1","hypothesisId":"B"})+"\n"); log_file.close()
      except: pass
      # #endregion
      raise
   except (KeyError, IndexError, TypeError) as e:
      # #region agent log
      try: log_path = r"c:\Users\singh\GITHUB\weather\.cursor\debug.log"; os.makedirs(os.path.dirname(log_path), exist_ok=True); log_file = open(log_path, "a", encoding="utf-8"); log_file.write(json.dumps({"id":"log_8","timestamp":int(__import__("time").time()*1000),"location":"ayush.py:40","message":"Data structure error","data":{"error_type":type(e).__name__,"error_msg":str(e)},"runId":"run1","hypothesisId":"D"})+"\n"); log_file.close()
      except: pass
      # #endregion
      raise
   except Exception as e:
      # #region agent log
      try: log_path = r"c:\Users\singh\GITHUB\weather\.cursor\debug.log"; os.makedirs(os.path.dirname(log_path), exist_ok=True); log_file = open(log_path, "a", encoding="utf-8"); log_file.write(json.dumps({"id":"log_9","timestamp":int(__import__("time").time()*1000),"location":"ayush.py:45","message":"Unexpected error","data":{"error_type":type(e).__name__,"error_msg":str(e)},"runId":"run1","hypothesisId":"E"})+"\n"); log_file.close()
      except: pass
      # #endregion
      raise


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
