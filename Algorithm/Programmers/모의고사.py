def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    first_count = 0
    second_count = 0
    third_count = 0

    for index, answer in enumerate(answers):
        if answer == first[index%len(first)]:
            first_count += 1
        if answer == second[index % len(second)]:
            second_count += 1
        if answer == third[index%len(third)]:
            third_count += 1

    count_dict = {1:first_count, 2:second_count, 3:third_count}
    top_score = max(count_dict.values())
    result = [student for student, score in count_dict.items() if score == top_score]

    return result