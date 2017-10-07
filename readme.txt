
Readme

The P1 consists of two .py files.

1. Server.py
2.Linda.py

Server.py does the folowwing :
- Creates a server socket and runs server in the background.
- Creates /tmp/92065/linda/nets and /tmp/92065/linda/tuples and stores the host connections and the tuple space respectively
- Creates a Global Tuples Space with 3 Tuples.
- Server also displays the Tuple space after the execution of each command.

Linda.py does the following:
- Waits for a user input with Linda> prompt.
- Starts client thread when the user gives add <ip> <port> command and connects with the address.
-Once the Connection is established, it waits in Linda> prompt waiting for out and rd commands.
-out('abc',1,2) puts the tuple in Tuple Space
-rd(2,5) reads the tuple if the tuple is present in tuple space, else blocks.
-in_(2,5) reads the tuple if it is available and then deletes it from the tuple space.
-out,rd and in can be executed repeatedly.
-Tuple Space can be read from /tmp/92065/linda/tuples

Server runs on both machines.
Linda can run on any machine and makes connection based on the address given through add command.


PS : in() command is implemented as in_() as I could not define 'in' function since 'in' is a keyword in Python
