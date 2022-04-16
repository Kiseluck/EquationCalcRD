import re
from colorama import init, Fore
from colorama import Back
from colorama import Style
import os


init(autoreset=True)
symbols = []
unknown = []
symbols_allow = ["=", "-", "+", "*", "/"]
os.system("clear")
print(Fore.RED + """
╭━━━╮╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━━╮╱╱╭╮╱╱╱╭━━━┳━━━╮
┃╭━━╯╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱╱╱┃╭━╮┃╱╱┃┃╱╱╱┃╭━╮┣╮╭╮┃
┃╰━━┳━━┳╮╭┳━┻╮╭╋┳━━┳━╮┃┃╱╰╋━━┫┃╭━━┫╰━╯┃┃┃┃┃
┃╭━━┫╭╮┃┃┃┃╭╮┃┃┣┫╭╮┃╭╮┫┃╱╭┫╭╮┃┃┃╭━┫╭╮╭╯┃┃┃┃
┃╰━━┫╰╯┃╰╯┃╭╮┃╰┫┃╰╯┃┃┃┃╰━╯┃╭╮┃╰┫╰━┫┃┃╰┳╯╰╯┃
╰━━━┻━╮┣━━┻╯╰┻━┻┻━━┻╯╰┻━━━┻╯╰┻━┻━━┻╯╰━┻━━━╯
╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╰╯
""" + Fore.GREEN +
"""
Для действий используйте знаки:
  Вычитание (-)
  Сложение (+)
  Умножение (*)
  Деление (/)

Если в вашем уравнение используется умножение в виде 2x,
то впишите знак умножения между ними

Любое неизвестное заменяйте на "x"

""")

def calc(s, s2, unknown):
    if s2[0] == "-" and unknown_height == 0:
        x = float(s[len_num-1]) + float(s[0])
        print("x - уменьшаемое")
        print("Ответ: x=" + str(x))
    if s2[0] == "+":
        x = float(s[len_num-1]) - float(s[0])
        print("x - слагаемое")
        print("Ответ: x=" + str(x))
    if s2[0] == "*":
        x = float(s[len_num-1]) / float(s[0])
        print("x - множитель")
        print("Ответ: x=" + str(x))
    if s2[0] == "/" and unknown_height == 0:
        x = float(s[len_num-1]) * float(s[0])
        print("x - делимое")
        print("Ответ: x=" + str(x))
    if s2[0] == "-" and unknown_height == 1:
        x = float(s[0]) - float(s[len_num-1])
        print("x - вычитаемое")
        print("Ответ: x=" + str(x))
    if s2[0] == "/" and unknown_height == 1:
        x = float(s[0]) / float(s[len_num-1])
        print("x - делитель")
        print("Ответ: x=" + str(x))



equation = input("Введите ваше уравнение: ")
print("""



""")
s = [float(s) for s in re.findall(r'\d+\.?\d*', equation)]
s2 = [str(s2) for s2 in re.findall("[-+*/=]+", equation)]
s3 = [str(s2) for s2 in re.split("[-+*/=]+", equation)]
unknown = " ".join(re.findall("[a-zA-Z]+", equation))
#print(s)
#print(s2)
#print(unknown)
#print(s3)
unknown_height = s3.index("x")
#print(unknown_height)
len_num = len(s)
#print(len_num)
calc(s, s2, unknown)

