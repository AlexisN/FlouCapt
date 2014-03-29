#!/usr/bin/python2
# -*-coding:UTF-8 -*

def main():
    password = raw_input("Veuillez entrer le mot de passe administrateur de Floucapt\n :")

    f = open('/etc/floucapt/webConf.ini', 'r')
    tab = f.readlines()
    f.close()
    tab[0] = password + "\n"



    f = open('/etc/floucapt/webConf.ini', 'w+')
    f.writelines(tab)
    f.close()


if __name__ == "__main__":
    main()
