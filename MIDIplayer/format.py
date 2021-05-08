from rich import pretty
from rich.console import Console
from rich.text import Text
from rich.traceback import install

import networkx as nx
import matplotlib.pyplot as plt


from mido import MidiFile, tempo2bpm

def readFile(file, tr=7):

    mid = MidiFile(file)
    track = mid.tracks[0] + mid.tracks[tr]
    # Guitar -> 8

    tpb = mid.ticks_per_beat # duracao de uma seminima
    durs = [tpb*4,
            tpb*2,
            tpb*1,
            tpb/2,
            tpb/4,
            tpb/8]

    events  = []
    seq  = []
    l_cod  = []
    time  = []
    oct  = []


    # for i, track in enumerate(mid.tracks):
    #     print('Track {}: {}'.format(i, track.name))
    #     for msg in track:
    #         print(msg)

    first = True

    for msg in track:
        # print(msg)

        if msg.type == 'track_name':
            instrument = msg.name

        if msg.type == 'time_signature':
            time_signature = (msg.numerator, msg.denominator)

        if msg.type == 'set_tempo':
            tempo = tempo2bpm(msg.tempo)

        if msg.type == 'note_on' and msg.velocity != 0:

            if first:
                first = False
                time.append(0)
            else:
                time.append(time[-1] + msg.time)

            events.append(True)
            seq.append(msg.note)
            oct.append(int(msg.note/12))



        if ((msg.type == 'note_on' and msg.velocity == 0)
            or msg.type == 'note_off'):

            # print(msg)
            if first:
                first = False
                time.append(0)
            else:
                time.append(time[-1] + msg.time)

            events.append(False)
            seq.append(msg.note)
            oct.append(int(msg.note/12))


            pass

    l_cod = list(dict.fromkeys(seq))

    return events, seq, oct, time, l_cod, durs, time_signature, instrument
    # print(events) # sequencia de on/off de todas notas da faixa
    # print(seq) # sequencia de todas notas da faixa
    # print(oct) # sequencia de todas oitavas
    # print(time) # vetor que acumula todos times
    # print(l_cod) # lista de notas sem repeticao
