Last login: Mon Dec 19 10:39:08 on ttys002
Sumithas-MacBook-Air:~ sumitha$ ssh -l 92065 23.253.20.67
92065@23.253.20.67's password: 
Welcome to Ubuntu 14.04.2 LTS (GNU/Linux 3.13.0-58-generic x86_64)

 * Documentation:  https://help.ubuntu.com/
New release '16.04.1 LTS' available.
Run 'do-release-upgrade' to upgrade to it.

Last login: Thu Dec 22 18:07:37 2016 from c-50-156-90-56.hsd1.ca.comcast.net
$ cd P1
$ ls
Linda.py  readme.txt  Server.py
$ vim Linda.py
$ vim Server.py









import socket
import sys
from threading import Thread
import os


# Creating nets and tuples files
netsFile = '/tmp/92065/linda/nets'
tuplesFile = '/tmp/92065/linda/tuples'

# Create directory with chmod 777 if it does not exist
# Create netsFile with chmod 666 if it does not exist
if not os.path.exists(netsFile):
    os.mkdir('/tmp/92065')
    os.chmod('/tmp/92065',0777)
    os.mkdir('/tmp/92065/linda')
    os.chmod('/tmp/92065/linda',0777)
    with open('/tmp/92065/linda/nets','wt') as netsFile:
        os.chmod('/tmp/92065/linda/nets',0666)
        netsFile.close()

# Create tuplesFile with chmod 666 if it does not exist
if not os.path.exists(tuplesFile):
    with open('/tmp/92065/linda/tuples','wt') as tuplesFile:
        os.chmod('/tmp/92065/linda/tuples',0666)
        tuplesFile.close()

Tuples = {0:('a',1,2.0),1:(2,5),2:('sum',8)}
n = 3
file = open('/tmp/92065/linda/tuples','a')
for i in range(0,n):
    file.write('\n' +str( Tuples[i]))
file.close()

#Function to find Local IP address
def getLocalIp():
    sock_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_fd.connect(("google.com",80))
    local_ip = sock_fd.getsockname()[0]
    sock_fd.close()
    return local_ip

# Find local ip address
local_ip = getLocalIp()

#Creating a server socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Binding the socket to available port number
server_socket.bind((local_ip,0))
ip = str(server_socket.getsockname()[0])
port = str(server_socket.getsockname()[1])
print(ip + " at port number: " + port)


while True:
    #Listen for all the incoming connections
    server_socket.listen(2)
    print("Server is running.....")
    conn,addr = server_socket.accept()
    Buff = conn.recv(2048)
    file = open('/tmp/92065/linda/nets','a')
    file.write('\n' + Buff)
    file.close()
    while True:

        Buff = conn.recv(2048)
        #out command
        if Buff == "out":
            Buff = conn.recv(2048)
            file = open('/tmp/92065/linda/tuples','w')
            print("\n\nTuple Space")
            Tuples.update({n: Buff})
            for i in Tuples:
                print(Tuples[i])
                file.write('\n' + str(Tuples[i]))
            conn.send("Put tuple " + Buff + "on " + local_ip)
            n = n+1
            file.close()
        #read command
        if Buff == "rd":
            Buff = conn.recv(2048)
            file = open('/tmp/92065/linda/tuples','w')
            print("\n\nTuple Space")
            for i in Tuples:
                print(Tuples[i])
                file.write('\n' + str(Tuples[i]))
                if(str(Buff) == str(Tuples[i])):
                    conn.send("Read operation: " + Buff + " available in Tuple Space")
            file.close()

        #in command
        if Buff == "in_":
            Buff = conn.recv(2048)
            file = open('/tmp/92065/linda/tuples','w')
            print("\n\nTuple Space")
            for i in Tuples:
                if(str(Buff) == str(Tuples[i])):
                    conn.send("Get tuple " + Buff + "on " + local_ip)
                    del_tuple_key = i

            del Tuples[del_tuple_key]
            for i in Tuples:
                print(Tuples[i])
                file.write('\n' + str(Tuples[i]))
            file.close()














