def solution(list, num):
    values = dict()
    for i, a in enumerate(list):
        b = num - a

        if b in values:
            return[values[b], i]

        values[a]=i

    return[]

numbers = [0, 21, 78, 19, 90, 13]

print(solution(numbers, 21))
print(solution(numbers, 25))


#Time Complexity: O(n)
