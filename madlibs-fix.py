import sys

madlibs_file = sys.argv[1]

with open(madlibs_file) as f:
    template = f.read()

start_plain = 0
start_question = None
new_parts = []

for (position, letter) in enumerate(template):
    if letter == '{':
        plain_part = template[start_plain:position]
        new_parts.append(plain_part)
        start_question = position+1
    elif letter == '}':
        question = template[start_question:position]
        answer = input("Give me a {word}: ".format(word=question))
        new_parts.append(answer)
        start_plain = position+1

new_parts.append(template[start_plain:])
completed_madlibs = "".join(new_parts)
print(completed_madlibs)
