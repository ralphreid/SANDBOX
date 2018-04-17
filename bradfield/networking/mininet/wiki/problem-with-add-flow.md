Hi everyone!
I have a topology 1 switch and 3 hosts.
I tried to run in command promt:
$dpctl add-flow tcp:127.0.0.1:6634 in_port=1, actions=out_put:2
and a result is : dpctl: 'add-flow' command takes at most 2 arguments
Please tell me why!
Thanks!
