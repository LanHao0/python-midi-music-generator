#!/usr/bin/env python

from midiutil import MIDIFile
import mido
from random import randrange

# mid = mido.MidiFile('./illness_recover_by_LanHao.mid', clip=True)
# for i, track in enumerate(mid.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for msg in track:
#         print(msg)

degrees = []  # MIDI note number
degrees2 = []

def generate_tracks(arr):
    for i in range(100):
        arr.append(randrange(100))


generate_tracks(degrees)
generate_tracks(degrees2)
track = 0
channel = 0
time = 0  # In beats
duration = 1  # In beats
tempo = 130  # In BPM
volume = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(2)  # One track, defaults to format 1 (tempo track is created
# automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    MyMIDI.addNote(0, channel, pitch, time + i, duration, volume)
for i, pitch in enumerate(degrees2):
    MyMIDI.addNote(1, channel, pitch, time + i, duration, volume)

with open("major-scale" + str(randrange(1000)) + ".mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
