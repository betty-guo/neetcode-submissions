from typing import List

def read_integers() -> List[int]:
    list_num_str = input().split(",")
    list_num_int = []
    for num in list_num_str:
        list_num_int.append(int(num))
    return list_num_int
    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
