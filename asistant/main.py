import time
from record import record
from responses import response
from speak import speak

speak('Efendim')
time.sleep(1)
while True:
    voice = record()
    print(voice)
    response(voice)
