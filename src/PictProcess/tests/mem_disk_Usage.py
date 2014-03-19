#!/bin/env python2

import time, os

if __name__ == '__main__':


    pid = os.fork()

    if not pid:
        os.chdir('..')
        os.execv('./Main.py', [''])


    file = open( 'mem_disk_Usage.csv' ,'a')
    file.write('pos,memory,disk\n')
    file.close()

    i = 0
    while True:
        i +=1
        memory = os.popen('pmap -x ' + str(pid) + '|grep total')
        memory = memory.read()
        memory = memory.split(' ')
        memory = memory [ len(memory) -1 ]
        memory = memory.strip('\n')

        disk = os.popen('du /var/floucapt')
        disk = disk.read()

        disk = disk.split('\n')
        disk = disk[ len(disk) -2 ]


        disk = disk.split('\t')
        disk = disk[ 0 ]



        file = open( 'mem_disk_Usage.csv' ,'a')

        file.write(str(i) +',' + memory + ','+ disk+'\n')

        file.close()

        print "Salut Michel !"

        time.sleep(60)



