records = []

# Get name and score
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])

# Find the second lowest score
second_lowest_score = sorted(set(score for name, score in records))[1]

# Get names with the second lowest score
sorted_names = sorted(name for name, score in records if score == second_lowest_score)

# Print the sorted names
for name in sorted_names:
    print(name)


''' Test Code '''
# records = []
# score_list = []
# name_list = []


# #get name and score
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     records.append([name,score])

# print('records: ', records)

# #get score list
# for i in records:
#     name_list.append(i[0])
#     score_list.append(i[1])

# print('name list: ', name_list)
# print('score list: ', score_list)
    
# sorted_score_list = sorted(score_list)
# print('sorted list: ', sorted_score_list)
    
# sort_name = []
# if sorted_score_list.count(sorted_score_list[1]) > 1:
#     for i in records:
#         if sorted_score_list[1] in i:
#             sort_name.append(i[0])
#     print('sort names: ', sort_name)
#     for j in sorted(sort_name):
#         print(j)
# else:
#     for j in records:
#         if sorted_score_list[1] in j:
#             print(j[0])



