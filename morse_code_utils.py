from pydub import AudioSegment
from pydub.generators import Sine

def text_to_morse_code(text):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', 
        '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', 
        ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
        '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
    }
    return ' '.join(morse_dict.get(char.upper(), '') for char in text)

def morse_code_to_audio(morse_code, filename):
    dot_length = 200
    dash_length = dot_length * 3
    gap_length = dot_length
    freq = 1000

    audio = AudioSegment.silent(duration=0)
    dot_sound = Sine(freq).to_audio_segment(duration=dot_length).fade_in(50).fade_out(50)
    dash_sound = Sine(freq).to_audio_segment(duration=dash_length).fade_in(50).fade_out(50)
    gap = AudioSegment.silent(duration=gap_length)
    word_gap = AudioSegment.silent(duration=dot_length * 7)

    for char in morse_code:
        if char == ".":
            audio += dot_sound + gap
        elif char == "-":
            audio += dash_sound + gap
        elif char == "/":
            audio += word_gap

    audio.export(filename, format="wav")
