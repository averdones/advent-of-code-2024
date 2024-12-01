# read input.txt
with open('Day 01 - Historian Hysteria/input.txt', 'r') as file:
    list1 = []
    list2 = []

    for line in file:
        elem1, elem2 = line.split()
        list1.append(int(elem1))
        list2.append(int(elem2))

#### Part 1
def calculate_sorted_distances(list1: list[int], list2: list[int]) -> int:
    list1 = sorted(list1)
    list2 = sorted(list2)

    distances = []
    for i in range(len(list1)):
        distance = abs(list1[i] - list2[i])
        distances.append(distance)

    return sum(distances)

print(calculate_sorted_distances(list1, list2))


#### Part 2

def create_counter(lst: list[int]) -> dict[int, int]:
    counter = {}
    for i in range(len(lst)):
        if (elem := lst[i]) in counter:
            counter[elem] += 1
        else:
            counter[elem] = 1

    return counter


def create_similarity_score(list1: list[int], list2: list[int]) -> int:
    score = 0
    counter_list2 = create_counter(list2)
    for elem in list1:
        counts = counter_list2.get(elem, 0)
        score += elem * counts

    return score


print(create_similarity_score(list1, list2))
