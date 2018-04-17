by Cody Burkard

* [Cluster Edition Vision](#vision)
* [When Should I use Cluster Edition?](#when)
* [Setting up a Cluster](#setup)
* [How to Run Cluster Edition](#run)
* [Placement Algorithms](#placement)
* [How does it Work?](#how)
* [Troubleshooting](#issues)

<a name=vision></a>

Cluster Edition Vision
--------------------------

Running Mininet on a single machine is fully capable of emulating networks of hundreds of nodes. However, what if we want to emulate a massive network of thousands of nodes? A single machine may not have the resources required to support all of the nodes - and the link bandwidth between those nodes - in a massive network. 

By distributing Mininet nodes and links over a cluster of servers, we can utilize the resources of each machine, and easily scale our system to support larger networks as well as networks with more computation and communication bandwidth than can be achieved with a single Mininet server.

**Warning! Prototype!**

We believe that mainline Mininet will benefit greatly from cluster support, but this implementation of Cluster Edition is currently an experimental prototype, which is why we are shipping it as an example. Please try it out and let us know what you think at the Mininet mailing list!

If you need a more mature alternative for running Mininet on a cluster, you may wish to look at Philip Wette's excellent [MaxiNet](http://www.cs.uni-paderborn.de/?id=maxinet).

<a name=when></a>

When to use Cluster Edition
---------------------------

Any experiment that may be run on standard Mininet may be run with cluster edition. However, you may need to make some minor changes to your code (for example if you have your own custom `Node` subclasses), and you may also find that performance changes (for example increased delay) for links that span multiple servers. 

It is intended to be usable a variety of situations or environments, such as a temporary single use scenario on a few laptops or on a dedicated testbed that will run many experiments. We support either case, and would love to hear about any uses you have come up with!

<a name=setup></a>

Setting up your Cluster
-----------------------

Cluster Edition has a few requirements to make it work properly. Here we cover these basic requirements: 

* **Network Connection:** This should be obvious, but each machine should be able to communicate with the other machines in the cluster. This could be on a local network, or even over the internet.
* **Mininet on each Machine:** Each machine in the cluster must have mininet installed
* **Common Username:** Each machine in the cluster must have a common username. We recommend setting up a `mininet` user (though you can call it whatever you like) on each machine.
* **Password-less `sudo`:** Each machine in the cluster must be set up with password-less sudo for the common username. This should be easy to set up. Simply append `username ALL=NOPASSWD: ALL` to `/etc/sudoers` using the command `visudo`.
* **Password-less `ssh` access:** Each machine must be able to communicate with every other machine in the cluster via `ssh` without being asked for a password. This means we need to populate our  `~/.ssh/authorized_keys` file with the public keys of each machine, and our `~/.ssh/known_hosts` file with the hosts keys of each machine. There are a few ways to do this, but it can be very tedious. This is why we have created a script to set up ssh access for you. It is located in `mininet/util` and is called `clustersetup.sh`. The script operates in two modes; persistent and temporary. 
    * **Temporary Setup with `clustersetup.sh`:** This is the default mode. You will be prompted to enter the password of each machine once, then the setup will be complete. This script works by creating a temporary `.ssh` directory on each machine, populating it with common `known_hosts` and `authorized_keys` files, and mounting the directory over the original `.ssh` directory. There is also a cleanup option for temporary setup, which will unmount and delete the temporary `.ssh` directory on each remote machine.
        * Simply invoke `./clustersetup.sh` with the hostnames or ip addresses of each machine in the cluster as arguments:
`$ ./clustersetup.sh clusterhost1 clusterhost2`
```
    ***authenticating to:
    clusterhost1
    clusterhost2
    *** Setting up temporary SSH configuration between all nodes
    ***creating temporary ssh directory
    ***creating key pair
    ***mounting temporary ssh directory
    ***copying public key to clusterhost1
    The authenticity of host 'clusterhost1 (192.168.56.101)' can't be established.
    ECDSA key fingerprint is 32:fa:bc:de:bc:5d:32:9f:7a:26:23:23:76:f3:e0:93.
    Are you sure you want to continue connecting (yes/no)? yes
    mininet@clusterhost1's password:
    ***mounting remote temporary ssh directory for cluster1
    ***copying key pair to clusterhost1
    id_rsa
    100% 1679     1.6KB/s   00:00    
    id_rsa.pub
    100%  401     0.4KB/s   00:00    
    ***copying public key to clusterhost2
    The authenticity of host 'clusterhost2 (192.168.56.102)' can't be established.
    ECDSA key fingerprint is 32:fa:bc:de:bc:5d:32:9f:7a:26:23:23:76:f3:e0:93.
    Are you sure you want to continue connecting (yes/no)? yes
    mininet@clusterhost2's password: 
    ***mounting remote temporary ssh directory for clusterhost2
    ***copying key pair to clusterhost2
    id_rsa
    100% 1679     1.6KB/s   00:00    
    id_rsa.pub
    100%  401     0.4KB/s   00:00    
    ***copying known_hosts to clusterhost1
    known_hosts
    100%  888     0.9KB/s   00:00    
    ***copying known_hosts to clusterhost2
    known_hosts
    100%  888     0.9KB/s   00:00    
    
    ***Finished temporary setup. When you are done with your cluster
       session, tear down the SSH connections with
       ./clustersetup.sh -c clusterhost1 clusterhost2

```

* To clean up afterwards:

`$ ./clustersetup.sh -c clusterhost1 clusterhost2`
```
    ***cleaning up clusterhost1
    ***cleaning up clusterhost2
    ***unmounting local directories
    ***removing temporary ssh directory
    done!

```

* **Persistent Setup with clustersetup.sh:** This type of setup may be helpful for a permanent cluster setup, where you always want to be authenticated via `ssh`. This setup will create a common public key and propagate it throughout the cluster, allowing all hosts to authenticate to each other. There is no cleanup option for this mode, as it is purposed for a permanent cluster. 

`./clustersetup.sh -p clusterhost1 clusterhost2`

<a name=run></a>

Running Mininet Cluster Edition
-------------------------------

Once an environment has been set up, it is easy to start up mininet over a cluster by invoking mininet with the --cluster option, passing in hostnames or ip addresses as arguments. **NOTE:** You also must specify the `-E` option with `sudo` (or specify `env_keep` in `/etc/sudoers`) for cluster edition to work properly. Starting up a tree topology on your machine and two other hosts should look like this:

`$ sudo -E mn --topo tree,3,3 --cluster localhost,cluster1,cluster2`
```
    *** WARNING: Experimental cluster mode!
    *** Using RemoteHost, RemoteOVSSwitch, RemoteLink
    *** Checking servers
    cluster1 cluster2 
    *** Placing nodes
    h1:None h2:None h3:None h4:None h5:None h6:None h7:None h8:None h9:None h10:cluster1 h11:cluster1 h12:cluster1 h13:cluster1 h14:cluster1 h15:cluster1 h16:cluster1 h17:cluster1 h18:cluster1 h19:cluster2 h20:cluster2 h21:cluster2 h22:cluster2 h23:cluster2 h24:cluster2 h25:cluster2 h26:cluster2 h27:cluster2 s1:None s2:None s3:None s4:None s5:None s6:cluster1 s7:cluster1 s8:cluster1 s9:cluster1 s10:cluster2 s11:cluster2 s12:cluster2 s13:cluster2 
    *** Creating network
    *** Adding controller
    *** Adding hosts:
    h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 
    *** Adding switches:
    s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 
    *** Adding links:
    (h1, s3) (h2, s3) (h3, s3) (h4, s4) (h5, s4) (h6, s4) (h7, s5) (h8, s5) (h9, s5) (h10, s7) (h11, s7) (h12, s7) (h13, s8) (h14, s8) (h15, s8) (h16, s9) (h17, s9) (h18, s9) (h19, s11) (h20, s11) (h21, s11) (h22, s12) (h23, s12) (h24, s12) (h25, s13) (h26, s13) (h27, s13) (s1, s2) (s1, s6) (s1, s10) (s2, s3) (s2, s4) (s2, s5) (s6, s7) (s6, s8) (s6, s9) (s10, s11) (s10, s12) (s10, s13) 
    *** Configuring hosts
    h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 
    *** Starting controller
    *** Starting 13 switches
    s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 
    *** Starting CLI:
    mininet> h1 ping -c 1 h2
    PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
    64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=7.57 ms

    --- 10.0.0.2 ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 7.574/7.574/7.574/0.000 ms
    mininet> 
```


The API for cluster edition does not change at all, except that you pass in a list of hostnames as a parameter for `MininetCluster`. To see this, check out `mininet/examples/clusterdemo.py`.

<a name=placement></a>

Pluggable Node Placement Algorithms
-----------------------------------

One question you may have is "How do I know where each host will be located?" `mn --cluster...` also accepts a `--placement` argument, which allows you to choose an algorithm for your cluster to use when placing nodes.

By default, Mininet uses the built-in `SwitchBinPlacer` algorithm. This algorithm places switches and controllers into evenly-sized bins/blocks based on the size of your cluster, and tries to place hosts on the same server as their corresponding switches. This can be explicitly selected using `--placement block`.

Another built-in algorithm is `RandomPlacer` (invoked using `--placement random`) which randomly places switches and hosts across the cluster. This results in many more cross-server tunnels, and can  be useful for testing.

You may either use one of the built in placement algorithms, or you may create your own by creating your own `Placer` subclass!

<!--- to-do: elaborate on different placement algorithms, and show example of creating placement algorithm -->

<a name=how></a>

How does Cluster Edition Work?
------------------------------

The difference between Cluster Edition and standard Mininet comes down to the communication between nodes, and the creation of nodes.

* *Communication between nodes:* In standard Mininet, there are no remote nodes, so each link is created with a virtual ethernet pair. However, in Cluster Edition, we must communicate with remote nodes on each machine. In this case, `ssh` tunnels replace virtual ethernet pairs when communicating between nodes on different machines. In the future, we plan to add additional tunnel types such as GRE tunnels.

* *Creation of Nodes:* During startup, only one instance of mininet is created on an arbitrary machine in the cluster. This machine creates its own local nodes, and also creates remote nodes via (shared) `ssh` connections to remote Mininet servers. The commands that are run on each machine resemble the same commands that are run during local node startup, but are run through an `ssh` connection to the remote server. This means there are no remote node daemons, and only one mininet instance running across the cluster.

<a name=issues></a>

Common Issues and Solutions
---------------------------

* `channel 22: open failed: administratively prohibited: open failed` <br>
`mux_client_request_session: session request failed: Session open refused by peer`: <br>
If this is seen in switch and link creation, your sshd configuration does not allow enough simultaneous sessions. This can be fixed by adding `MaxSessions 1024` to `/etc/ssh/sshd_config`.

* `channel 0: open failed: administratively prohibited: open failed`: <br>
If you see this in link creation, you need to append `PermitTunnel yes` to `/etc/ssh/sshd_config`