from socket import socket, AF_INET, SOCK_DGRAM
import sys

def subDict(dict1, dict2):
    dict_temp = dict(dict1)
    for key in dict2:
        del dict_temp[key]
    return dict_temp

ip = sys.argv[2]
port_num = int(sys.argv[1])
file_name = sys.argv[3]

s = socket(AF_INET, SOCK_DGRAM)
s.settimeout(1)
file = open(file_name, "rb")

id = 1
dict1 = {}
while True:
    data = file.read(98)
    if data == b'':
        break
    id_bytes = id.to_bytes(2, 'little')
    data = id_bytes + data
    dict1[id] = data
    id += 1

SIZE_OF_DICT = len(dict1)

for id in range(1, SIZE_OF_DICT + 1):
    s.sendto(dict1[id], (ip, port_num))

dict2 = {}
dict3 = {}
while len(dict1) != len(dict2):
    while True:
        try:
            data, addr = s.recvfrom(1024)
            dict2[int.from_bytes(data[:2], "little")] = data[2:]
        except:
            break
    dict3 = subDict(dict1, dict2)
    for key in dict3:
        s.sendto(dict3[key], (ip, port_num))

for key in sorted(dict1.keys()):
    print(dict1[key][2:].decode(), end='')
file.close()
s.close()




# id = 1
# dict = {}
# while True:
#     data = file.read(98)
#     if data == b'':
#         break
#     id_bytes = id.to_bytes(2, 'little')
#     data = id_bytes + data
#     dict[id] = data
#     id += 1
#
# SIZE_OF_DICT = len(dict)
# id = 1
#
# while id < SIZE_OF_DICT + 1:
#     s.sendto(dict[id], (ip, port_num))
#     try:
#         data, addr = s.recvfrom(1024)
#         if int.from_bytes(data[:2], "little") == id:
#             id += 1
#             print(data[2:].decode(), end='')
#         else:
#             continue
#     except:
#         continue
