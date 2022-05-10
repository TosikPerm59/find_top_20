
def find_top_20(slist):
    best_students = []
    score_set = set()
    for student in slist:
        student["total_scores"] = 0
        student["total_only_math_and_cs"] = 0
        for subject in student["scores"]:
            student["total_scores"] += student["scores"][subject]
        student["total_scores"] += student["extra_scores"]
        student["total_only_math_and_cs"] += student["scores"]["math"] + student["scores"]["computer_science"]
        score_set.add(student["total_scores"])
    count = 0
    for best_score in sorted(list(score_set))[::-1]:
        for student in slist:
            if student["total_scores"] == best_score:
                best_students.append(student)
                count += 1
            if count == 20:
                if [i["total_scores"] for i in best_students].count(best_score) < \
                  [i['total_scores'] for i in slist].count(best_score):
                    for stud in best_students:
                        if stud["total_scores"] == best_score:
                            best_students.remove(stud)
                            count -= 1
                    controversial_cand_in_slist = []
                    total_only_math_and_cs_list = []
                    for stu in slist:
                        if stu["total_scores"] == best_score:
                            controversial_cand_in_slist.append(stu)
                            total_only_math_and_cs_list.append(stu["total_only_math_and_cs"])
                    for best_sc in sorted(total_only_math_and_cs_list):
                        for st in controversial_cand_in_slist:
                            if st["total_only_math_and_cs"] == best_sc:
                                best_students.append(st)
                                count += 1
                            if count == 20:
                                break
                        if count == 20:
                            break
        if count == 20:
            break
    # print(final_score)
    for n in best_students:
        print(n["name"])


candidates = [
 {"name": "Vasya1",  "scores": {"math": 58, "russian_language": 652, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya1",  "scores": {"math": 334, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya1",  "scores": {"math": 926, "russian_language": 334, "computer_science": 34},  "extra_scores":1},
 {"name": "Vasya2",  "scores": {"math": 58, "russian_language": 662, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya2",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya2",  "scores": {"math": 926, "russian_language": 363, "computer_science": 34},  "extra_scores":1},
{"name": "Vasya3",  "scores": {"math": 58, "russian_language": 692, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya3",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya3",  "scores": {"math": 68, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
{"name": "Vasya4",  "scores": {"math": 68, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya4",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya4",  "scores": {"math": 962, "russian_language": 335, "computer_science": 34},  "extra_scores":1},
{"name": "Vasya5",  "scores": {"math": 58, "russian_language": 72, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya5",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya5",  "scores": {"math": 92, "russian_language": 33, "computer_science": 35},  "extra_scores":1},
{"name": "Vasya6",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya6",  "scores": {"math": 33, "russian_language": 865, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya6",  "scores": {"math": 92, "russian_language": 34, "computer_science": 34},  "extra_scores":1},
{"name": "Vasya7",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya7",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
 {"name": "Petya7",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores":1}
]
find_top_20(candidates)