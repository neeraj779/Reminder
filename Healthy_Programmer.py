from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def logs(user_log):
    with open("logs.txt", "a") as log_file:
        log_file.write(f"{user_log} at {datetime.now()}\n")
        print("logs has been saved")



if __name__ == "__main__":

    init_water = time()
    init_eyes_exercise = time()
    init_excercise = time()
    water_in_sec = 2400
    eyes_excercise_in_sec = 1800
    excercise_in_sec = 2700

    while True:
        if time() - init_water > water_in_sec:
            print("Its time to drink your water, type stop to stop the music ")
            musiconloop("water.mp3","stop")
            logs("drank water")
            init_water = time()

        if time() - init_eyes_exercise > eyes_excercise_in_sec:
            print("Its time for  your eyes exercise, type done to stop the music ")
            musiconloop("eyes.mp3","done")
            logs("eyes exercise done")
            init_eyes_exercise = time()

        
        if time() - init_excercise > excercise_in_sec:
            print("Its time for a exercise, type done to stop the music ")
            musiconloop("excercise.mp3","done")
            logs("exercise done")
            init_excercise = time()

        
