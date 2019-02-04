# ComputeEngine

Simple method transfer server/client.
This is intended for personal/inhouse use, network security is being worked on, but NOT in place yet. Client has full control of what it can run (including malicious code!).

It allows a client to write a function and then run it remotely, to avoid local running costs.
You can use any machine (that has Python installed) and due to the small footprint it's perfectly suited to run on older machines and TinyCore like Os'.

There are (currently) no checks on anything from whether a module is installed on the server to little/big endian kind of issues.
Keep this in mind when designing functions.

NOTE: Client function(s) must be able to be marshalled (so be careful with recursiveness and dependencies).
