dicts_lists = [
    {
        "Name": "James",
        "Age": 21,
    },
    {
        "Name": "May",
        "Age": 14,
    },
    {
        "Name": "Katy",
        "Age": 23,
    },
]

# There are different ways to sort that list
# 1- Using the sort/ sorted function based on the age
# dicts_lists.sort(key=lambda item: item.get("Age"))

# 2- Using itemgetter module based on name
from operator import itemgetter

f = itemgetter("Name")
dicts_lists.sort(key=f)

print(dicts_lists)

import pandas as pd

df = pd.DataFrame(dicts_lists)
print(df.sort_values(by="Age"))

df.head(2)

df.replace(21, 888)
