import MIDIplayer as mp
import matplotlib.pyplot as plt
import numpy as np
from plot import print_graph
from bar_format import bar_split

def print_data(data):
    for i in range(len(data)):
        input('Data[{}]'.format(i))
        print(data[i])

#
#   Input
#
info, data = mp.readFile('input.mid')

# info
name_inst   = info[0]
key_sign    = info[1]
time_sign   = info[2]
tempo       = info[3]
l_cod       = info[4]
durs        = info[5]

#data
events      = data[0]
cods        = data[1]
oct         = data[2]
time        = data[3]


#
# SETUP #
#=======#
#

n_frames = len(events)
on_frames = []
off_frames = []
for i, e in enumerate(events):
    if e:
        on_frames.append(i)
    else:
        off_frames.append(i)
data.append(on_frames)
data.append(off_frames)
# print(time) # 4: ON, 5: OFF
bars = bar_split(data, durs)

# print_data(bars)

# grafico
print_graph(time, cods, events)
