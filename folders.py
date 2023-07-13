# import os
# a = r"//10.70.10.10/DepTech/АРХИВ/Электронный архив/"
# for it in os.listdir(a):
#     # os.rename(it, it[0:7])
#     print(it)
#     os.rename(os.path.join(a, it),
#             os.path.join(a, it[:7]))
#     print(it)
# # Проверка на совпадение папок в архиве
# a = r"//10.70.10.10/DepTech/АРХИВ/Электронный архив/"
# b = os.listdir(a)
# for i in range(len(b)):
#     if b[i][0:7] == b[i-1][0:7]:
#         print(b[i])
