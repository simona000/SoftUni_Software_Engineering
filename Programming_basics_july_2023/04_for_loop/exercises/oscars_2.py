actor_name = input()
points_from_academy = float(input())
count_of_jury = int(input())


for i in range(0,count_of_jury):
    jury_name = input()
    score_from_jury = float(input())

    points_from_jury_name = len(jury_name)
    current_score = (points_from_jury_name * score_from_jury) / 2
    points_from_academy += current_score

    if points_from_academy >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {points_from_academy:.1f}!')
        break
else:
    needed_score = abs(1250.5 - points_from_academy)
    print(f"Sorry, {actor_name} you need {needed_score:.1f} more!")