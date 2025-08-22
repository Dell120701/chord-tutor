import random
import time

PRACTICE_FILENAME = "chord_list.txt"
CHORD_POSITION_FILENAME = "chord_position.txt"
DISPLAY_FINGER = False
DELAY = 5
RANDOM = True


practice_chords = []
weights = []
n_practice = 0

with open(PRACTICE_FILENAME, "r") as f:
    for line in f:
        if ' ' in line:
            chord, freq = line.split()
        else:
            chord = line.strip()
            freq = 1
        practice_chords.append(chord)
        weights.append(int(freq))
        n_practice += 1

chord_position = {}

with open(CHORD_POSITION_FILENAME, "r") as f:
    for line in f:
        chord, position, first_line = line.split()
        chord_position[chord] = (position, first_line)


index = 0
while True:
    if RANDOM:
        chord = random.choices(practice_chords, weights=weights)[0]
    else:
        chord = practice_chords[index % n_practice]
        index += 1

    print("Chord: ", chord)
    print()

    if DISPLAY_FINGER:
        for i in range(5, -1, -1):
            s = "X┣" if i < int(chord_position[chord][1]) else " ┣"
            for j in range(4):
                if int(chord_position[chord][0][i]) == j + 1:
                    s += "━━o━━┿"
                else:
                    s += "━━━━━┿"
            print(s)
        print('\n')
    time.sleep(DELAY)
