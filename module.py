from datetime import datetime

def obtenir_temps():
    return "Hello ! il est {}.".format(datetime.now().strftime("%H:%M:%S"))
