morsecode = {
    "a": ".-",   "b": "-...", "c": "-.-.", "d": "-..",  "e": ".",
    "f": "..-.", "g": "--.",  "h": "....", "i": "..",   "j": ".---",
    "k": "-.-",  "l": ".-..", "m": "--",   "n": "-.",   "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.",  "s": "...",  "t": "-",
    "u": "..-",  "v": "...-", "w": ".--",  "x": "-..-", "y": "-.--",
    "z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    " ": "/"
}
reverse_morse = {value: key for key, value in morsecode.items()}

def letters_to_morse():
    '''converts text to morse code'''
    user_input = input("Text: ").lower()
    completed = []
    for letter in user_input:
        completed.append(morsecode.get(letter, "?"))
    print(" ".join(completed))

def morse_to_letters():
    '''converts morse code to text'''
    user_input = input("Enter Morse code (separate letters with spaces, words with /): ")
    result = "" 
    for code in user_input.split():
        result += reverse_morse.get(code, "?")
    print("Translated text:", result)

while True:
    choice = input("""
    Letters to morse code (1)
    Morse code to Letters (2)
    Other to quit: """)
    if choice == '2':
        morse_to_letters()
    elif choice == '1':
        letters_to_morse()
    else:
      break
