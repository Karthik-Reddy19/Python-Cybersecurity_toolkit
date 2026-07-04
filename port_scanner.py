import socket
host=input("Enter the IP or hostname:")
ports=[65537]
for port in ports:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)
    result=sock.connect_ex((host,port))
    if result==0:
        print(f"[Open] {port}")
    else:
        print(f"[Close] {port}")
    sock.close()