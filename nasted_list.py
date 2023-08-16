records = []
score_list = []
name_list = []


#get name and score
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])

print('records: ', records)

#get score list
for i in records:
    name_list.append(i[0])
    score_list.append(i[1])
    
sorted_score_list = sorted(score_list)
print('sorted list: ', sorted_score_list)
    
sort_alphabetic = sorted(name_list)
print('alphabatic sort: ', sort_alphabetic)

for i in sorted_score_list:
    if sorted_score_list.count(sorted_score_list[1]) > 1:
        pass
    
for j in records:
    if sorted_score_list[1] in j:
        lowest_scorer = j[0]
print('second lowest scorer name: ', lowest_scorer)




