import socket

sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = input("Insert IP: ")
edp = int(input("Insert the least port value: "))
ebp = int(input("Insert the greatest port value: "))


for port in range(edp,ebp+1):
    try:
        sc.connect((ip.port))
        print("{}. port is open")
        exit(0)
    except:
        pass
print("your ports are safe :)")
