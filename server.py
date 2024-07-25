import signal
import socket
import os

banner = """
██     ██  ██████  ███    ██ ██   ██  █████
██     ██ ██  ████ ████   ██ ██  ██  ██   ██
██  █  ██ ██ ██ ██ ██ ██  ██ █████   ███████
██ ███ ██ ████  ██ ██  ██ ██ ██  ██  ██   ██
 ███ ███   ██████  ██   ████ ██   ██ ██   ██
"""
st_connection = False

def start_server(port, host='127.0.0.1'):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port)) 
    server.listen(1)
    print("[i] waiting for connection")
    client, address = server.accept()
    st_connection = True

    while(st_connection):
        agent_resp = client.recv(4096).decode('utf-8')
        print(f"agent@{address[0]} > {agent_resp}\n")
        command = input("command > ")
        client.send(command.encode('utf-8'))

def error(*args):
    msg = '[!] '
    if not args:
        msg += "error"
    msg += ''.join(args)
    print('\n'+msg)
    exit(1)

def help():
    print("[*] wonka commands:\n")
    print("[help] show this menu")
    print("[start] > start server")
    print("[show] > view the current configuration")
    print("[exit] > exit the program\n")

def brk(signum, frame):
    error("ctrl+c pressed stopping execution")

signal.signal(signal.SIGINT, brk)
print(banner)
help()

while True:
    opt = str(input("wonka > "))
    match opt:
        case "exit":
            opt = str(input("you want to exit? Y/n "))
            if (opt.lower()) == "y" or opt == "":
                exit(0)
        case "start":
            start_server(port=3030)
        case "show":
            print("[:)] working here")
        case "help":
            help()
        case _:
            print("[!] unknown command")
