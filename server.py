import socket

HOST = '104.155.146.62'
PORT = 25565 # ;)
PASS = 'redacted'
FLAG = 'redacted'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connection from', addr)
            conn.sendall('Password: '.encode('ascii'))
            conn.settimeout(10)
            try:
                password = conn.recv(1024).decode('ascii').strip()
            except:
                conn.sendall('\n'.encode('ascii'))
                continue
            if password == PASS:
                conn.sendall((FLAG + '\n').encode('ascii'))
                print('Flag Delivered')
            else:
                print('Bad Password:', repr(password))
