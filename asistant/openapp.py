import os
import subprocess

def find_program_path(program_name):
    """ Verilen program adını Program Files dizinlerinde ara ve tam yolunu döndür. """
    possible_paths = [
        r"C://Program Files",
        r"C://Program Files (x86)"
    ]
    
    for path in possible_paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                if program_name.lower() in file.lower() and file.endswith(".exe"):
                    return os.path.join(root, file)
    
    return None