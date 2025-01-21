import csv

with open("lesson-10/homework/grades.csv", "r") as file:
    reader = csv.DictReader(file)
    all_dics_list = list(reader)


subj_score_dic = {}

for dic in all_dics_list:
    if dic['Subject'] not in subj_score_dic.keys():
        subj_score_dic[dic["Subject"]] = [int(dic["Grade"])]
    else:
        subj_score_dic[dic["Subject"]].append(int(dic["Grade"]))

for key in subj_score_dic.keys():
    subj_score_dic[key] = sum(subj_score_dic[key]) / len(subj_score_dic[key])

final_dic_list = [{"Subject": key, "Average Grade": value} for key, value in subj_score_dic.items()]
# print(final_dic_list)

with open("lesson-10/homework/average_grades.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Subject", "Average Grade"])
    writer.writeheader()
    writer.writerows(final_dic_list)