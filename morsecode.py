morsecode= {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    'd':'--.',
    'e':'.',
    'f':'..-.',
    'g':'--.',
    'h':'....',
    'i':'..',
    'j':'.---',
    'k':'-.-',
    'l':'.-..',
    'm':'--',
    'n':'-.',
    'o':'---',
    'p':'.--.',
    'q':'--.-',
    'r':'.-.',
    's':'...',
    't':'-',
    'u':'..-',
    'v':'...-',
    'w':'.--',
    'x':'-..-',
    'y':'-.--',
    'z':'--..',
    ' ':'|'
}
completedstr = []
userinput = input("Normal text to convert to binary: ").lower()
for letter in userinput:
    completedstr.append(morsecode.get(letter))
print(" ".join(completedstr))