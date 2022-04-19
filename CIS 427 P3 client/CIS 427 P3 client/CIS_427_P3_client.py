
#Drew Barlow
import socket

PORT_NUM = 6810
NUM_BYTES = 1024
HEADER = 64
DISCONNECTED = "USER DISCONNECTED"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), PORT_NUM))

message = client_socket.recv(NUM_BYTES)
message = message.decode("utf-8")

# Function to send the data to the server that needs to solved
def solve():
    user = input("SOLVE ")
    client_socket.send(bytes(user, "utf-8"))

# Function that sends the serer the list command
def list():
    client_socket.send(bytes("LIST", "utf-8"))


# Function that sends the server the shutdown command
def shutdown():
    client_socket.send(bytes("SHUTDOWN","utf-8"))


# Function that tells the server the user is logging out
def logout():
    client_socket.send(bytes("LOGOUT","utf-8"))
    login()

# Function to send messages to the server and other clients
def send():
    msg = input().encode("utf-8")
    sendMsg = str(msg).encode("utf-8")
    client_socket.send(sendMsg)
   
print(message)
# Function to display commands that the user can use
def menu():
    print("SOLVE")
    print("MESSAGE")
    print("LIST")
    print("SHUTDOWN")
    print("LOGOUT")

    command = input("Enter a command: ")

    if command == "SOLVE":
       solve()
       
    elif command == "MESSAGE":
        send()

    elif command == "LIST":
        pass

    elif command == "SHUTDOWN":
        shutdown()
        
    elif command == "LOGOUT":
        logout()
    else:
        client_socket.send(bytes("300 invalid command. Please try again: ", "utf-8"))

# Function to send which user is logging in to the server
def login():
    user = input("LOGIN ")
    if user == "root root22":
        client_socket.send(bytes("root root22", "utf-8"))
        menu()
        
    elif user == "john john22":
        client_socket.send(bytes("john john22", "utf-8"))
        menu()
       
    elif user == "sally sally22":
        client_socket.send(bytes("sally sally22", "utf-8"))
        menu()

    elif user == "qiang qiang22":
        client_socket.send(bytes("qiang qiang22", "utf-8"))
        menu()
    else:
        client_socket.send(bytes(user, "utf-8"))
        error = client_socket.recv(NUM_BYTES)
        error = error.decode("utf-8")
login()
