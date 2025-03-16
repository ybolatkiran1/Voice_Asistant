from datetime import datetime
import webbrowser
from record import record
from speak import speak
from weather import get_weather
import os
import pyautogui
import time
from volume import volume_up, volume_down, max_volume, min_volume
import random
from openapp import find_program_path
from random_txt import *

# Komutları ve ilgili fonksiyonları tanımlayan bir sözlük oluşturduk.
COMMANDS = {
    "nasılsın": lambda: speak("İyiyim, senden?"),
    "ne haber": lambda: speak("İyiyim, senden?"),
    "iyiyim": lambda: speak("İyi olduğuna sevindim."),
    "saat kaç": lambda: speak(datetime.now().strftime('%H:%M:%S')),
    "arama yap": lambda: search_google(),
    "hava nasıl": lambda: weather_info(),
    "hava durumu": lambda: weather_info(),
    "şarkı aç": lambda: open_spotify(),
    "youtube ara": lambda: search_youtube(),
    "site aç": lambda: open_website(),
    "ses aç": lambda: change_volume("up"),
    "sesi aç": lambda: change_volume("up"),
    "ses azalt": lambda: change_volume("down"),
    "sesi azalt": lambda: change_volume("down"),
    "sesi kapat": lambda: change_volume("mute"),
    "sesi fulle": lambda: change_volume("max"),
    "uygulama aç": lambda: open_application(),
    "şaka yap": lambda: tell_something(tell_joke, "Şaka"),
    "tavsiye ver": lambda: tell_something(tell_advices, "Tavsiye"),
    "kitap öner": lambda: tell_something(tell_book, "Kitap önerisi"),
    "rastgele bilgi ver": lambda: tell_something(tell_info, "Bilgi"),
    "film öner": lambda: tell_something(tell_movie, "Film önerisi"),
    "müzik öner": lambda: tell_something(tell_song, "Müzik önerisi"),
    "günün sözü": lambda: tell_something(tell_word, "Günün sözü"),
    "tamam": lambda: exit_assistant(),
    "görüşürüz": lambda: exit_assistant(),
}

def response(voice):
    """Gelen sesi analiz eder ve ilgili fonksiyonu çalıştırır."""
    for command, action in COMMANDS.items():
        if command in voice:
            action()
            return 
    speak("Bu komutu anlayamadım.")

def wait_speak():
    time.sleep(0.3)
    speak('Başka bir isteğin varmı?')


def search_google():
    search = record("Ne aramak istiyorsun?")
    url = "https://google.com/search?q=" + search
    webbrowser.get().open(url)
    speak(f"{search} için bulduklarım.")
    wait_speak()
    

def search_youtube():
    video = record("YouTube üzerinden hangi videoyu arayayım?")
    url = "https://www.youtube.com/results?search_query=" + video
    webbrowser.open(url)
    wait_speak()

def open_website():
    site = record("Hangi siteyi açayım?")
    url = "https://www." + site + ".com"
    webbrowser.get().open(url)
    wait_speak()

def weather_info():
    speak("Hangi şehir için hava durumunu öğrenmek istiyorsun?")
    city = record()
    weather_data = get_weather(city)
    speak(weather_data)
    wait_speak()

def open_spotify():
    speak("Spotify açılıyor, en son dinlediğin şarkıyı çalıyorum.")
    os.startfile("spotify")
    time.sleep(5)
    pyautogui.press("space")
    exit()

def change_volume(action):
    if action == "up":
        speak("Ses seviyesini artırıyorum.")
        volume_up()
        wait_speak()
    elif action == "down":
        speak("Ses seviyesini düşürüyorum.")
        volume_down()
        wait_speak()
    elif action == "mute":
        speak("Ses kapatıldı.")
        min_volume()
        wait_speak()
    elif action == "max":
        speak("Ses fullendi.")
        max_volume()
        wait_speak()

def open_application():
    app_name = record("Hangi uygulamayı açayım?")
    speak(f"{app_name} açılıyor.")
    program_path = find_program_path(app_name)
    print(f"Bulunan uygulama yolu: {program_path}")
    if program_path:
        os.startfile(program_path)
        wait_speak()
    else:
        speak(f"{app_name} bulunamadı.")
        wait_speak()

def tell_something(func, title):
    """Dosyalardan rastgele içerik alıp seslendirir."""
    content = func()
    if content:
        print(f"{title}: {content}")
        speak(content)
        wait_speak()
    else:
        speak(f"Üzgünüm, şu an {title.lower()} veremiyorum.")
        wait_speak()

def exit_assistant():
    speak("Görüşürüz!")
    exit()
