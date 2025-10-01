# import random
#
# file_name = "mes.txt"
# with open(file_name, "w") as file:
#     for _ in range(100):
#         random.randint(1, 100)
#                 number =
#         random.randint(1,1000)
# file.write(str(number)+ '\n')

import random
numbers=[random.randint(1, 100) for _ in range(100) ]
with open("mes.txt", "w") as f:
    for num in numbers:
        f.write(str(num)+ "\n")

import

