from morse_code_utils import text_to_morse_code, morse_code_to_audio

text = "I love you"
morse_code = text_to_morse_code(text)
print(morse_code)

filename = "output.wav"
morse_code_to_audio(morse_code, filename)
