import sys

madlibs_file = sys.argv[1]

with open(madlibs_file) as f:
    template = f.read()

new_words = []
words = template.split()

for word in words:
  if word[0] == "{" and word[-1] == "}":
    kind = word[1:-1]
    new_word = input("Give me a {word}:".format(word=kind))
    new_words.append(new_word)
  else:
    new_words.append(word)

completed_madlibs = " ".join(new_words)
print(completed_madlibs)
