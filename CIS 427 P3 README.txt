README
by Drew Barlow
https://github.com/Drew-Barlow/CIS-427-P3.git
--------------------------------
Program build / run:
Build: Server and client programs were made in Visual Studio 2019 as seperate programs.
Clone the Main branch from the repository into Visual Studio.
--------------------------------
Run: Open the file named "cis 427 server.sln" in Visual Studio. Then start the server by selecting "start debugging" (F5).
Next open the file "cis_427_client.sln" in another Visual Studio instance. Start the client by selecting "start debugging" (F5). Repeat this step to have mulitple clients.
End the client or server by pressing shift+F5 or the red stop button in their respective programs.
--------------------------------
Commands:
SOLVE
MESSAGE
LIST
SHUTDOWN
LOGOUT
--------------------------------
Bugs:
1. After the user logs in, the server will not display the "SUCCESS" message.
2. After the user logs out and any user that logins in after will not see the server message "SUCCESS" again.
3. After the client logs out, then logs back again, then sends the SHUTDOWN command to the server, the server throws an exception (WinError 10038) and crashes the server.
4. After the server crashes, the client stays running.
5. After the client logs in and sends SHUTDOWN to the server, the client will end but not the server.
6. After an incorrect login, no error message is sent or recieved and the client ends.
7. After entering the SOLVE command, the client will end.
8. After entering the LIST command, the client will end.
9. SOLVE function not fully complete and implemented (client and server side).
10. LIST function not fully complete and implemented (client and server side).
11. MESSAGE function not fully complete and implemented (client and server side).
--------------------------------
Client Outputs:
--------------------------------
Server connection established!
LOGIN root root22
SOLVE
MESSAGE
LIST
SHUTDOWN
LOGOUT
Enter a command: SOLVE
SOLVE -c 4
Press any key to continue . . .
--------------------------------
Server connection established!
LOGIN root root22
SOLVE
MESSAGE
LIST
SHUTDOWN
LOGOUT
Enter a command: LIST
Press any key to continue . . .
--------------------------------
Server connection established!
LOGIN root root22
SOLVE
MESSAGE
LIST
SHUTDOWN
LOGOUT
Enter a command: SHUTDOWN
Press any key to continue . . .
-------------------------------
Server connection established!
LOGIN root root22
SOLVE
MESSAGE
LIST
SHUTDOWN
LOGOUT
Enter a command: LOGOUT
LOGIN root root22
SOLVE
MESSAGE
LIST
SHUTDOWN
LOGOUT
Enter a command:
-------------------------------
Server connection established!
LOGIN root root22
SOLVE
MESSAGE
LIST
SHUTDOWN
LOGOUT
Enter a command: MESSAGE
-all Hello all
Press any key to continue . . .
