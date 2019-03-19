import collections
alphabet = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11,
            'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18,
            'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26, ' ':' '}
reversed ={}

for k,v in alphabet.items():
    reversed[v] = k

text_raw = "alex evi csy hsmr' xshec, lsric? m'q ksmrk xs wamqqmrk tssp."
# todo text_raw = str(input("Insert text in English to decode: "))
text = text_raw.lower()


sentences=[]
for y in range(0,26):
    changed = []
    for i in text:
        original_position = alphabet.get(i)
        try:
            if original_position + y >= 27:
                coded = (original_position + y) - 26
                changed.append(reversed.get(coded))
            if original_position +y <= 26:
                coded = int(original_position) + y
                changed.append(reversed.get(coded))
        except:
                changed.append(i)
    coded = "".join(changed)
    print(coded, "relocation =", y)
    sentences.append(coded)

by_word=[]
for s in sentences:
    abc = s.split()
    by_word.append(abc)

with open("EN_most_common.txt") as f:
    most_common = []
    for line in f:
        most_common.append(line.strip())

for w in by_word:
   for c in most_common:
       count = 0
       if c in w:
           count += 1
           print("Sentence choosen by program:", w," -- what is the keyword and how many times occurs? ->", c )
           
