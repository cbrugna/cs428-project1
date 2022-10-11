# Binghamton University: CS428 2022 Fall

## Project-1: Web Server

### SUMMARY

[Provide a short description of your program's functionality, no more than a couple sentences]: 

webserver1.py is a webserver built with socket programming and TCP connections in Python. this webserver serves a simple
HelloWorld.html file that simply outputs "Hello World." If anything but http://[local_ip_adress]/HelloWorld.html is
entered into a webbrower, the web server will return a 404 Not Found. webserver2.py does the same thing, but is multithreaded
so that more than one request can be served at a time.

### NOTES, KNOWN BUGS, AND/OR INCOMPLETE PARTS

[Add any notes you have here and/or any parts of the project you were not able to complete]: 

No parts that we were not able to complete. The webservers worked and served the file when tested. 

### REFERENCES

[List any outside resources used]: 

https://docs.python.org/2.7/howto/sockets.html?highlight=socket
- Used to help understand socket programming. 

### INSTRUCTIONS

[Provide clear and complete step-by-step instructions on how to run and test your project]: #
1. Enter the directory containing webserver1.py and webserver2.py
2. To run either server type "python webserver1.py" or "python webserver2.py"
3. Open your browser and enter this into the : http://128.238.251.26:960/HelloWorld.html 
   where the IP address is the address of the host running the server. On Mac, this can be found
   by navigating to system preferences > network. We chose port 960, so use port 960. 
4. The "HelloWorld.html" file should be displayed on your browser. If any other file not present on the server is requested, the server will return a 404 Not Found error. 

### SUBMISSION

I have done this assignment completely on my own. I have not copied it, nor have I given my solution to anyone else. I understand that if I am involved in plagiarism or cheating I will have to sign an official form that I have cheated and that this form will be stored in my official university record. I also understand that I will receive a grade of "0" for the involved assignment and my grade will be reduced by one level (e.g., from "A" to "A-" or from "B+" to "B") for my first offense, and that I will receive a grade of "F" for the course for any additional offense of any kind.

By signing my name below and submitting the project, I confirm the above statement is true and that I have followed the course guidelines and policies.

Submission date: October 10, 2022

Team member 1 name: Casey Brugna

Team member 2 name: Armaan Gill
