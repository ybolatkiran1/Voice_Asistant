from pycaw.pycaw import AudioUtilities
from pycaw.pycaw import IAudioEndpointVolume

# Ses cihazını al
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, 
    23, 
    None
)
volume = interface.QueryInterface(IAudioEndpointVolume)


def volume_up():
    current_volume = volume.GetMasterVolumeLevelScalar()  
    new_volume = min(current_volume + 0.1, 1.0) 
    volume.SetMasterVolumeLevelScalar(new_volume, None)
def volume_down():
    current_volume = volume.GetMasterVolumeLevelScalar()  
    new_volume = min(current_volume - 0.1, 1.0)  
    volume.SetMasterVolumeLevelScalar(new_volume, None)
def max_volume():
    current_volume=volume.GetMasterVolumeLevelScalar()
    new_volume=1
    volume.SetMasterVolumeLevelScalar(new_volume, None)
def min_volume():
    current_volume=volume.GetMasterVolumeLevelScalar()
    new_volume=0
    volume.SetMasterVolumeLevelScalar(new_volume, None)
