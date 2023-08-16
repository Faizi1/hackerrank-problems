words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

past_tense = []
for i in words:
    if i[-1] == 'e':
        past_tense.append(i+'d')
    else:
        past_tense.append(i+'ed')
print(past_tense)