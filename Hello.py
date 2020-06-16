from random import randint
import sys
from Battleship import *
from TicTacToe import *
from Pong import *

name = input("Въведете Вашето име : ")
print("Здравейте ," , name ,"!\n" )



def startgame():
    print("Изберете някоя от следните игри,която Ви се играе днес!")
    print("1. Параходи")
    print("2. Морски шах")
    print("3. Пинг Понг")
    num = input("")
    
    if num == "1":
        a()
    print("-" * 20)
    if num == "2":
        b()
    if num == "3":
        c()

startgame()

end = input("Искате ли да продължите (Да / Не): ")
if end == "Да":
    startgame()

elif end == "Не":
    sys.exit(0)
