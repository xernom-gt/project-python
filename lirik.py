import sys
import time
from threading import Thread


song_lines = [

    ("I see forever in your eyes", 0.09),
    ("I feel okay when I see you smile,| smile",0.09),
    ("Wishing on dandelions all of the time", 0.07),
    ("Praying to God that one day you'll be mine", 0.06),
    ("Wishing on dandelions all of the time,/ all of the time", 0.07)
]


line_delays = [0, 0.7, 1.7 , 0.7, 0.5]

def display_text_slowly(content, char_delay=0.1, extra_pause=3.0, extra_pause1=0.2):
    """Menampilkan teks dengan animasi per karakter dan jeda khusus."""
    for letter in content:
        if letter == "|":
            time.sleep(extra_pause)
        elif letter == "/":
            time.sleep(extra_pause1)

        else:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(char_delay)
    print()

def play_line(line, start_delay, char_speed):
    """Menampilkan satu baris lirik dengan jeda awal."""
    time.sleep(start_delay)
    display_text_slowly(line, char_speed)

def play_song():
    """Memainkan seluruh lirik lagu dengan delay dan animasi."""
    for idx in range(len(song_lines)):
        text, speed = song_lines[idx]
        time.sleep(line_delays[idx])
        display_text_slowly(text, speed)

if __name__ == "__main__":
    play_song()
