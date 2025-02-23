dictionary = {"Masha": 
            {
                "rus" : [4, 5, 4], 
                "math" : [4, 4, 4], 
                "info": [5, 5, 5],
                "biology" : [3, 3],
                "geografy": []
            },
            "Misha" : 
            {
                "rus" : [4, 3, 4, 5, 5],
                "math" : [5, 3, 4, 5, 5],
                "info" : [5, 2, 4, 4],
                "biology" : [4, 3],
                "geografy": []
            },
            "Petya":
            {
                "rus" : [5, 5, 5, 4],
                "math" : [5, 5],
                "info" : [3, 4, 5, 4, 4, 4],
                "biology" : [4, 5],
                "geografy": []
            }}

top = []
for i in range(len(dictionary[list(dictionary.keys())[0]])):
    top.append({})

for i in list(dictionary.keys()):
    print(f"Student: {i}")
    subj = 0
    for j in list(dictionary[i].keys()):
        if (len(dictionary[i][j]) != 0):
            mean_value = sum(dictionary[i][j]) / len(dictionary[i][j])
        else:
            mean_value = 0
        print(f"\tSubject: {j} -> {mean_value}")
        top[subj].update({i : mean_value})
        subj += 1
    print()

top_current = top

subj_names = list(dictionary[list(dictionary.keys())[0]].keys())
current_subject = 0

for i in top_current:
    print(f"Subject {subj_names[current_subject]}: ")

    for j in range(len(i)):
        max_name = ''
        max_mark = -1
        for k in list(i.keys()):
            if i[k] > max_mark:
                max_mark = i[k]
                max_name = k
        if (len(top_current[current_subject]) > 0):
            del top_current[current_subject][max_name]
            print(f"{max_name} -> {max_mark}")
    current_subject += 1
    print()
