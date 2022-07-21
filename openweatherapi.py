"""
@author: Aslihan Erkan
"""

import requests
import tkinter as tk
import webbrowser

#Getting data from OpenWeatherAPI
def getData(window):
    city = textBox.get()
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=689476c30d411a39da929fe78078928c"
    api_data = requests.get(api).json() 


    if api_data['cod']=='404':
        tk.messagebox.showerror("Error", "Invalid city name.")
    
    else:
        weather = api_data['weather'][0]['main']
        temp = int(api_data['main']['temp'] - 273.15)
        temp_min = int(api_data['main']['temp_min'] - 273.15)
        temp_max = int(api_data['main']['temp_max'] - 273.15)
        pressure = api_data['main']['pressure']
        humidity = api_data['main']['humidity']
        wind = api_data['wind']['speed']
        lon=str(api_data['coord']['lon'])
        lat=str(api_data['coord']['lat'])
    
        condition = weather + "\n" + str(temp) + "°C" 
        info = "\n"+ "Min Temperature: " + str(temp_min) + "°C" + "\n" + "Max Temperature: " + str(temp_max) + "°C" +"\n" + "Humidity: " + str(humidity) +"\n" + "Pressure: " + str(pressure) + "\n" +"Wind Speed: " + str(wind) 
        labelCondition.config(text = condition)
        labelInfo.config(text = info)
        
        link1.pack()
        link2.pack()
        link3.pack()
        link4.pack()
        link5.pack()
        link1.bind("<Button-1>", lambda e: callback("https://openweathermap.org/weathermap?basemap=map&cities=false&layer=precipitation&lat="+lat+"&lon="+lon+"&zoom=8"))
        link2.bind("<Button-1>", lambda e: callback("https://openweathermap.org/weathermap?basemap=map&cities=false&layer=temperature&lat="+lat+"&lon="+lon+"&zoom=8"))
        link3.bind("<Button-1>", lambda e: callback("https://openweathermap.org/weathermap?basemap=map&cities=false&layer=pressure&lat="+lat+"&lon="+lon+"&zoom=8"))
        link4.bind("<Button-1>", lambda e: callback("https://openweathermap.org/weathermap?basemap=map&cities=false&layer=windspeed&lat="+lat+"&lon="+lon+"&zoom=8"))
        link5.bind("<Button-1>", lambda e: callback("https://openweathermap.org/weathermap?basemap=map&cities=false&layer=clouds&lat="+lat+"&lon="+lon+"&zoom=8"))

#Creating and designing window
global window
window = tk.Tk()
window.geometry("400x500")
window.configure(background='light blue')

window.title("Weather")
f = ("Lato", 10)
t = ("Lato", 20, "bold")
    
labelRequest = tk.Label(window, text="Please enter a city name:")
labelRequest.pack()
labelRequest.configure(background='light blue')

#Text box to enable user input for city names
textBox = tk.Entry(window, justify='center', width = 20, font = t)
textBox.pack(pady = 5)
textBox.focus()
textBox.bind("<Return>", getData)


#Buttons for Maribor and my city (Istanbul)
def click_istanbul():
    window1 = window
    textBox.delete(0, "end")
    textBox.insert(0, "Istanbul")
    getData(window1)

def click_maribor():
    window1 = window
    textBox.delete(0, "end")
    textBox.insert(0, "Maribor")
    getData(window1)    
    

buttonMaribor = tk.Button(window, text="Get Maribor", command=click_maribor, padx = 127, pady = 5, cursor="hand2")
buttonIstanbul = tk.Button(window, text="Get Istanbul", command=click_istanbul, padx = 127, pady = 5, cursor="hand2")

buttonIstanbul.pack()
buttonMaribor.pack()

#Links for maps
def callback(url):
    webbrowser.open_new(url)

link1 = tk.Label(window, text="Precipitation map", bg="light blue", fg="blue", cursor="hand2")
link2 = tk.Label(window, text="Temperature map", bg="light blue", fg="blue", cursor="hand2")
link3 = tk.Label(window, text="Pressure map", bg="light blue", fg="blue", cursor="hand2")
link4 = tk.Label(window, text="Windspeed map", bg="light blue", fg="blue", cursor="hand2")
link5 = tk.Label(window, text="Clouds map", bg="light blue", fg="blue", cursor="hand2")

#Labels to display weather info and condition
labelCondition = tk.Label(window, font=t)
labelCondition.pack(pady=10)
labelInfo = tk.Label(window, font=f)
labelInfo.pack(pady=10)
labelCondition.configure(background='light blue')
labelInfo.configure(background='light blue')


window.mainloop()