import socket

mysocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM) #built-in support for TCP sockets (like a filehandler)
mysocket.connect(('data.pr4e.org', 80)) #página a conectar y puerto del web server
cmd= 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

while True:
    data= mysocket.recv(512)  #recibe hasta 512 caracteres
    if (len(data) < 1):
        break
    print(data.decode())

mysocket.close()
