from collections import Counter


def unique(arr):
    # return list(set(arr))
    return [i for i,j in Counter(arr).items() if j==1]

strings = ["Hare", "Krishna", "Hare", "Krishna",
  "Krishna", "Krishna", "Hare", "Hare", ":-O"
]
print(unique(strings))