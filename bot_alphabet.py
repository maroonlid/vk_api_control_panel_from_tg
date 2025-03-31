import random
import os

dir = os.path.abspath(os.curdir) #путь к программе

def write_in_file(list_number, list_password):
    file = open("C:\\Users\\User\\PycharmProjects\\vk_elfbot\\data\\account_data", "w")
    for i in range(len(list_number)):
        file.write(list_number[i] + "\n")
        file.write(list_password[i] + "\n")
    file.close()


def map_transl_func():
    txt_file = open(dir + "//data//account_data")

    data = txt_file.read()

    data_list = data.split("\n")

    txt_file.close()

    list_number = []
    list_password = []

    for i in range(len(data_list)):
        if i % 2 == 0:
            list_number.append(data_list[i])
        else:
            list_password.append(data_list[i])

    return list_number, list_password

def get_line(length):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-"
    line = ""
    for i in range(length):
        line += letters[random.randint(0, len(letters) - 1)]

    return line

list_number, list_password = [], []
if list_number == ['']:
    list_number = [ ]
blocking_password = "42g-eG(qe5*&TRd7%d"

check1 = False
check2 = False
check3 = False

apiToken = '6512588978:AAE_M2JvYUXV8Av0ZOTEd08L804D_9gFhmo'
groups_id_list = ["-80979282", "-98500837", "-155000664", "-155000664", "-137130240", "-214331295 ",
                  "-141601326", "-200065472", "-206582223", "-198474825", "-80979282", "-107796603",
                  "-147961469", "-123912386", "-98500837", "-200101053", "-200063311", "-219252338",
                  "-101450101", "-54401469", "-155000664", "-7299025", "-25158150", "-137130240",
                  "-214331295", "-217432851", "-138520920", "-141601326", "-194293256",
                  "-206582223", "-58341182", "-150637622", "-130603931", "-152420902", "-63569611",
                  "-25132036", "-26982127", "-149126430", "-196713786", "-110572749", "-67433974",
                  "-133655506", "-102535646", "-148184772", "-26136032", "-109250270", "-96692953",
                  "-53481157", "-50145692"]

print("Summ of id -", len(groups_id_list))