#!/bin/env python2
# -*- coding: utf-8 -*-

import time, os, signal
from signal import SIGTERM



def signal_handler(signal, frame):
    global pidFloucapt
    os.kill(pidFloucapt, SIGTERM)

    global quit
    quit = True




if __name__ == '__main__':


    pid = os.fork()

    if not pid:
        os.chdir('..')
        os.execv('/usr/bin/python2',['python2', 'floucapt.py', 'no-daemon'] )

    global pidFloucapt
    pidFloucapt = pid

    signal.signal(signal.SIGINT , signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    filee = open( 'mem_disk_Usage.csv' ,'w+')
    #filee.write('pos,memory,disk\n')
    filee.write('hour\t\tmemory\n')
    filee.close()

    i = 0
    global quit
    quit = False

    time.sleep(5)

    while not quit:
        memory = os.popen('pmap -x ' + str(pid) + '|grep total')
        memory = memory.read()
        memory = memory.split(' ')
        memory = memory [ len(memory) -1 ]
        memory = memory.strip('\n')

        #disk = os.popen('du /var/floucapt')
        disk = os.popen('du ../out/pictures')
        disk = disk.read()

        disk = disk.split('\n')
        disk = disk[ len(disk) -2 ]


        disk = disk.split('\t')
        disk = disk[ 0 ]


        filee = open( 'mem_disk_Usage.csv' ,'a')
        #filee.write(str(i) +',' + memory + ','+ disk+'\n')
        filee.write(str(i) + " hours\t\tRAM : " + memory + "ko\n")
        filee.close()


        print "Write mem_disk_Usage.csv"
        if not quit:
            time.sleep(3600)
        i +=1



