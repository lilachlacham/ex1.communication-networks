import socket
import sys

port = int(sys.argv[1])
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', port))
#s.settimeout(1)

msg_dict = {}
current_id = 1

while True:
    data, addr = s.recvfrom(1024)
    s.sendto(data, addr)
    recv_id = int.from_bytes(data[:2], "little")
    if recv_id not in msg_dict:
        msg_dict[recv_id] = data
        if recv_id == current_id:
            print(data[2:].decode(), end='')
            current_id += 1
            while True:
                if current_id in msg_dict:
                    print(msg_dict[current_id][2:].decode(), end='')
                    current_id += 1
                else:
                    break







# dict = {}
# id =0
#
# while True:
#     try:
#         data, addr = s.recvfrom(1024)
#         recv_id = int.from_bytes(data[:2], "little")
#         if recv_id == id + 1:
#             id+=1
#             dict.update({id: data})
#             print(data[2:].decode(), end='')
#             s.sendto(data, addr)
#         else:
#             s.sendto(dict[recv_id], addr)
#     except:
#         continue