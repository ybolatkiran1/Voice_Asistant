import os
import random

# Çalışan dosyanın bulunduğu dizini al
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def tell_joke():
    file_path = os.path.join(BASE_PATH, "txt", "jokes.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        jokes = file.readlines()
    
    if jokes:
        return random.choice(jokes).strip()

    return "Şaka bulunamadı!"

def tell_word():
    file_path = os.path.join(BASE_PATH, "txt", "wordoftheday.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        words = file.readlines()
    
    if words:
        return random.choice(words).strip()

    return "Kelime bulunamadı!"

def tell_song():
    file_path = os.path.join(BASE_PATH, "txt", "songs.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        songs = file.readlines()
    
    if songs:
        return random.choice(songs).strip()

    return "Şarkı bulunamadı!"

def tell_movie():
    file_path = os.path.join(BASE_PATH, "txt", "movies.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        movies = file.readlines()
    
    if movies:
        return random.choice(movies).strip()

    return "Film bulunamadı!"

def tell_info():
    file_path = os.path.join(BASE_PATH, "txt", "info.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        infos = file.readlines()
    
    if infos:
        return random.choice(infos).strip()

    return "Bilgi bulunamadı!"

def tell_book():
    file_path = os.path.join(BASE_PATH, "txt", "books.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        books = file.readlines()
    
    if books:
        return random.choice(books).strip()

    return "Kitap bulunamadı!"

def tell_advices():
    file_path = os.path.join(BASE_PATH, "txt", "advices.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        advices = file.readlines()
    
    if advices:
        return random.choice(advices).strip()

    
