import requests
from PIL import Image
from io import BytesIO
from tkinter import Tk, Label
from PIL import ImageTk

API_KEY = '3a76646e87494122986db93507fb9d11'
BASE_url = 'https://ip-intelligence.abstractapi.com/v1/'

ip_address = input('What is the IP address you want to locate?: ')

def show_img(flag_image_url):
    response = requests.get(flag_image_url)
    img = Image.open(BytesIO(response.content))
    
    root = Tk()
    root.title('Flag')
    
    photo = ImageTk.PhotoImage(img)
    label = Label(root, image=photo)
    label.pack()
    
    root.mainloop()

def locate_ip(ip_address):
    
    params = {
        'api_key': API_KEY,
        'ip_address': ip_address
    }
    
    request = requests.get(BASE_url, params=params)
    data = request.json()
    
    try:
        country = data['location']['country']
        country_code = data['location']['country_code']
        city = data['location']['city']
        continent = data['location']['continent']
        local_time = data['timezone']['local_time']
        flag_image_url = data['flag']['png']
        
        print(f'This IP address is located in {city}, {country}({country_code}), {continent}.')
        print('Local time at IP address location: ', local_time)
        answer = input('Do you want to see the flag of this country (Y/N)?: ')
        
        if answer.strip().upper() == 'Y':
            print('Image is shown in new window.')
            show_img(flag_image_url)
    except:
        print('Error Status: ', data.status_code)
        
locate_ip(ip_address)
    