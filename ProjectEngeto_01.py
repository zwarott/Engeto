'''
ProjectEngeto_01.py: The first project to Engeto Online Python Academy

Author: Tomáš Zvardoň
Email: zvardont@seznam.cz
Discord: Tomáš Z.#3385
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

registred_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
separator = "-" * 40

if registred_users.get(input_user_name := input("username: ")) == input("password: "):
    print(separator, f"Welcome to app, {input_user_name}.", "We have 3 texts to be analyzed.", separator, sep="\n")
else:
    print("Unregistred user, terminating the program...")
    quit()

text_words = list()
selected_text = int(input("Enter a number btw. 1 and 3 to select: "))
if selected_text in (1, 2, 3):
    for words in TEXTS[selected_text - 1].split():
        clean_words = ''.join(filter(str.isalnum, words))
        text_words.append(clean_words)
else:
    print("Wrong number, terminating the program...")
    quit()
print(separator)

words_count = dict()
for words in text_words:
    if words not in words_count:
        words_count[words] = 1
    else:
        words_count[words] += 1

words_sum = sum(words for words in words_count.values())
print(f"There are {words_sum} words in the selected text.")

words_titlecase = [words for words in text_words if words.istitle()]
print(f"There are {len(words_titlecase)} titlecase words.")

words_uppercase = [words for words in text_words if words.isupper() and words.isalpha()]
print(f"There are {len(words_uppercase)} uppercase words.")

words_lowercase = [words for words in text_words if words.islower()]
print(f"There are {len(words_lowercase)} lowercase words.")

numeric_strings = [words for words in text_words if words.isnumeric()]
print(f"There are {len(numeric_strings)} numeric strings.")

sum_numbers = sum(int(numbers) for numbers in numeric_strings)
print(f"The sum of all the numbers: {sum_numbers}.", separator, sep="\n")

print("LEN|     OCCURRENCES     |NR.", separator, sep="\n")

words_len_count = {}
for word in text_words:
    words_len_count[len(word)] = words_len_count.setdefault(len(word), 0) + 1

for key, value in sorted(words_len_count.items()):
    nr = str(key).rjust(3)
    occurrences = "*" * value
    len_sep = "|".rjust(22 - value)

    print(f"{nr}|{occurrences}{len_sep}{value}")
