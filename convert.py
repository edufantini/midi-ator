import MIDIplayer as mp
import matplotlib.pyplot as plt
import numpy as np

events, seq, oct, time, l_cod, durs, time_signature, instrument = mp.readFile('input.mid')

n_frames = len(events)
on_frames = []
off_frames = []
for i, e in enumerate(events):
    if e:
        on_frames.append(i)
    else:
        off_frames.append(i)


# plt.plot(time, seq, 'ro')
# print([print(x) for x in e])
# plt.plot(on_frames, seq.difference(off_frames), 'bo')

fig, ax = plt.subplots()
scatter = ax.scatter(time, seq, c=events)

# produce a legend with the unique colors from the scatter
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="best", title="Evento")

plt.show()

# print(data)
