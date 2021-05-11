import MIDIplayer as mp
import matplotlib.pyplot as plt
import numpy as np
import plot

def bar_split(data, durs):
    bar_len = durs[0]
    time = data[3]

    bars = []

#
#   encontrar os indices onde iremos dividir os
#   vetores
#
    count = 0
    list = []
    for i in range(len(time)):
        # print('{}   ->  {}'.format(i, time[i]))
        if(time[i] > bar_len*(len(bars)+1)):
            # nao cabe na barra, quebra
            count = 0
            bars.append(list)
            list = []
            # print('ai:{}; time[i]: {}; count:{} len(list):{} '.format(i, time[i], count, len(bars)))
            # input()
        else:
            count = time[i]
            list.append(i)
            # print('i:{}; time[i]: {}; count:{} len(bars):{} '.format(i, time[i], count, len(bars)))
            # input()

    return bars
