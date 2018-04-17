## Contents

- [Introduction](Link-modeling-using-ns-3#introduction)  
 - [ns-3 emulation features](Link-modeling-using-ns-3#ns-3-emulation-features)  
 - [Link simulation with ns-3](Link-modeling-using-ns-3#link-simulation-with-ns-3)  
- [Details](Link-modeling-using-ns-3#details)  
 - [How to achieve communication of ns-3 process with TAP interfaces in distinct namespaces?](Link-modeling-using-ns-3#how-to-achieve-communication-of-ns-3-process-with-tap-interfaces-in-distinct-namespaces)  
 - [Architecture: single ns-3 thread or multiple processes?](Link-modeling-using-ns-3#architecture-single-ns-3-thread-or-multiple-processes)  
- [Code](Link-modeling-using-ns-3#code)  
 - [Mininet](Link-modeling-using-ns-3#mininet)  
 - [ns-3 patches](Link-modeling-using-ns-3#ns-3-patches)  
- [Usage](Link-modeling-using-ns-3#usage)  
 - [ns-3 downloading and building](Link-modeling-using-ns-3#ns-3-downloading-and-building)  
 - [Running mininet scripts](Link-modeling-using-ns-3#running-mininet-scripts) 
- [Midterm](Link-modeling-using-ns-3#midterm)  

## Introduction

### ns-3 emulation features

[ns-3](http://www.nsnam.org/) network simulator has ability to work in so called [real-time/emulation](http://www.nsnam.org/wiki/index.php/Emulation_and_Realtime_Scheduler) mode. In that mode, the simulator can exchange packets in real-time with the outside world. It means, that packets originating from simulated nodes can be processed by a real network. Another possibility is to drive a simulated network with packets from real nodes. These two options are covered by two different kinds of ns-3 modules: `FdNetDevice` and `TapBridge`.

See more:
- [Realtime](http://www.nsnam.org/docs/release/3.17/manual/singlehtml/index.html#realtime)
- [Emulation](http://www.nsnam.org/docs/release/3.17/models/singlehtml/index.html#emulation-overview)

[`FdNetDevice`](http://www.nsnam.org/docs/release/3.17/models/singlehtml/index.html#file-descriptor-netdevice) can read and write from a file descriptor, which can be associated to a network device (via raw socket). This allows ns-3 simulations to read frames from and write frames to a network device on the host. Instead of an ns-3 channel connecting ns-3 nodes, real hardware provided by the testbed can be used. This allows ns-3 applications and protocol stacks attached to a simulation node to communicate over real hardware. The primary use for this configuration is to generate repeatable experimental results in a real-world network environment that includes all of the ns-3 tracing, logging, visualization and statistics gathering tools.

    FdNetDevice case.
    Nodes are simulated, the network is real.

    +----------------------+     +-----------------------+
    |         host 1       |     |         host 2        |
    +----------------------+     +-----------------------+
    |    ns-3 simulation   |     |                       |
    +----------------------+     |         Linux         |
    |       ns-3 Node      |     |     Network Stack     |
    |  +----------------+  |     |   +----------------+  |
    |  |    ns-3 TCP    |  |     |   |       TCP      |  |
    |  +----------------+  |     |   +----------------+  |
    |  |    ns-3 IP     |  |     |   |       IP       |  |
    |  +----------------+  |     |   +----------------+  |
    |  |   FdNetDevice  |  |     |   |                |  |
    |  |    10.1.1.1    |  |     |   |                |  |
    |  +----------------+  |     |   +    ETHERNET    +  |
    |  |   raw socket   |  |     |   |                |  |
    |--+----------------+--|     |   +----------------+  |
    |       | eth0 |       |     |        | eth0 |       |
    +-------+------+-------+     +--------+------+-------+
           10.1.1.11                     10.1.1.12
               |       real network         |
               +----------------------------+

[`TapBridge`](http://www.nsnam.org/docs/release/3.17/models/singlehtml/index.html#tap-netdevice) allows a real host to participate in an ns-3 simulation as if it were one of the simulated nodes. It can be viewed as essentially an inverse configuration to the previous one. It allows host systems and virtual machines running native applications and protocol stacks to integrate with a ns-3 simulation. In this case ns-3 connects to a TAP virtual interface created on Linux host. Packets send by host to the TAP device are transmitted through the file descriptor to the ns-3 process. Next they are forwarded down by `TapBridge` to the ns-3 net device and transmitted over the ns-3 emulated channel. The typical use case for this environment is to analyse the behaviour of native applications and protocol suites in the presence of large simulated ns-3 network. 

    TapBridge case.
    Nodes are real, the network is simulated.

    +--------+
    |  Linux |
    |  host  |                    +----------+
    | ------ |                    |   ghost  |
    |  apps  |                    |   node   |
    | ------ |                    | -------- |
    |  stack |                    |          |     +----------+
    | ------ |                    |          |     |   node   |
    |  TAP   |                    |==========|     | -------- |
    | device | <----- IPC ------> |   tap    |     |    IP    |
    +--------+                    |  bridge  |     |   stack  |
                                  | -------- |     | -------- |
                                  |   ns-3   |     |   ns-3   |
                                  |   net    |     |   net    |
                                  |  device  |     |  device  |
                                  +----------+     +----------+
                                       ||               ||
                                  +---------------------------+
                                  |        ns-3 channel       |
                                  +---------------------------+


### Link simulation with ns-3

Two `TapBridge` net devices can be used to create emulated link between two TAP virtual interfaces. Two ghost nodes inside ns-3 need to be created. Each node should consist of a `TapBridge` and ns-3 net device. These net devices should be connected together by an emulated ns-3 channel. Each `TapBridge` should be connected to the proper TAP interface. These TAP interfaces can serve now as the endpoints of the emulated link.

    +--------+                                         +--------+
    |  name  |                                         |  name  |
    | space1 |                                         | space2 |
    | ------ |                                         |--------|
    |  node  |                                         |  node  |
    | ------ |                                         |--------|
    |  stack |                                         |  stack |
    | ------ |                                         |--------|
    |  TAP   |      |==========|     |==========|      |  TAP   |
    | device |<-fd->|   tap    |     |   tap    |<-fd->| device |
    +--------+      |  bridge  |     |  bridge  |      +--------+
                    | -------- |     | -------- |
                    |   ns-3   |     |   ns-3   |
                    |   net    |     |   net    |
                    |  device  |     |  device  |
                    +----------+     +----------+
                         ||               ||
                    +---------------------------+
                    |        ns-3 channel       |
                    +---------------------------+
                 |<------------------------------->|
                             ns-3 process

## Details

### How to achieve communication of ns-3 process with TAP interfaces in distinct namespaces?

The first question, which needs to be answered, is if it is possible to ns-3 process to communicate with TAP devices in two distinct network namespaces. And, if it is possible, how sequence of interface creation, connecting ns-3 to them, and moving them between namespaces should look like.

It turns out, that it is possible to establish connection between two TAP interfaces through ns-3 and maintain it after moving TAP interfaces to another namespaces. The sequence should look like the following:

1. Create tap0 interface in the root namespace.
2. Create tap1 interface in the root namespace
3. Start ns-3, connect with tap bridges to the both interfaces and establish channel between these two nodes in ns-3.
4. Move tap0 to namespace A.
5. Move tap1 to namespace B.

So, at the end, there are:
- tap0 interface in the namespace A
- tap1 interface in the namespace B
- ns-3 process in the root namespace

Finally, we get a ns-3 process which provides a communication channel between namespace A and namespace B. Tested on Linux kernels 3.5 and 3.8.

### Architecture: single ns-3 thread or multiple processes?

Let's take a look at the code of an simple ns-3 simulation in Python. It establishes a simple channel between two devices in two distinct nodes. Next, `TapBridges` are installed to each device. Each `TapBridge` bridges a ns-3 device (`SimpleNetDevice` in that case) and a system TAP device ("tap0" or "tap1" in that case). It provides possibility of communication between these two TAP interfaces through the simulated channel, just like with the schema above.

```python
import sys
import ns.core
import ns.network
import ns.csma
import ns.tap_bridge

def main(argv):

    ns.core.GlobalValue.Bind("SimulatorImplementationType", ns.core.StringValue("ns3::RealtimeSimulatorImpl"))
    ns.core.GlobalValue.Bind("ChecksumEnabled", ns.core.BooleanValue ("true"))

    node0 = ns.network.Node()
    node1 = ns.network.Node()

    simple = ns.network.SimpleChannel()

    device0 = ns.network.SimpleNetDevice()
    device0.SetChannel(simple)
    node0.AddDevice(device0)

    device1 = ns.network.SimpleNetDevice()
    device1.SetChannel(simple)
    node1.AddDevice(device1)

    tapBridge0 = ns.tap_bridge.TapBridgeHelper()
    tapBridge0.SetAttribute ("Mode", ns.core.StringValue ("UseBridge"))
    tapBridge0.SetAttribute ("DeviceName", ns.core.StringValue("tap0"))
    tapBridge0.Install (node0, device0)

    tapBridge1 = ns.tap_bridge.TapBridgeHelper()
    tapBridge1.SetAttribute ("Mode", ns.core.StringValue ("UseBridge"))
    tapBridge1.SetAttribute ("DeviceName", ns.core.StringValue("tap1"))
    tapBridge1.Install (node1, device1)

    ns.core.Simulator.Stop(ns.core.Seconds(3600))
    ns.core.Simulator.Run()

    ns.core.Simulator.Destroy()
    return 0
```

What is important to notice, is that there are some global values set. The first value, `SimulatorImplementationType`, is set to the realtime simulator type. The second one, `ChecksumEnabled`, enables checksum computation on packets inside ns-3 (by default ns-3 do not compute checksums, however, it is needed when it is going to exchange packets with the real world).

However, this is not the end of global states. After setting up and installing devices, the simulation is started with the `ns.core.Simulator.Run()`. But there is no `ns.core.Simulator` object on which this function is called. In fact, there is only one simulator singleton object in the whole ns-3 process. It maintains its own scheduler object, which thus can be only one in the entire simulation. Apart from that, ns-3 maintains single global lists of nodes and channels, to which they are appended during object construction.

Existence of the singleton simulator object implies that there can be only one running simulator thread per process. This thread has to deal with the processing of packets from all of the simulated channels. Availability of multiple cores cannot be exploited.

On the other hand, all of the ns-3 (and mininet in our case) objects stays in a single Python/mininet/ns-3 process memory space. They can call each other methods and access attributes. For example, advanced ns-3 channel settings can be set from the level of Python/mininet. Another case is updating nodes positions inside ns-3 from the mininet level, when simulating wireless channels.

Another approach is to spawn child ns-3 process for each simulated channel or link (link is a channel with only two devices connected). Each process has its own memory and maintains its own simulator, scheduler and ns-3 nodes. They can run concurrently and exploit multiple cores for simulating different channels.

This approach, however, limits flexibility: after the fork of ns-3 process mininet will be not able to access ns-3 objects. It might be considered to implement some kind of interprocess communication between mininet and ns-3 processes for a limited set of messages, particularly for position updating. However, mininet will not access full ns-3 API like in the single process approach.

As for now, **single ns-3 thread inside common Python/mininet/ns-3 process** approach was selected.

## Code

### Mininet

Development branch: http://github.com/piotrjurkiewicz/mininet/tree/ns3-integration

A list of changes to the original mininet:
* added new module `mininet.ns3` **[mininet/ns3.py]**
* minor change in `Node.addIntf()` **[mininet/node.py]**
* added ns-3 related examples **[examples/ns3/*]**

You can follow the commits here: http://github.com/piotrjurkiewicz/mininet/commits/ns3-integration

### ns-3 patches

#### TapBridge address learning patch `required` [`submitted`](http://mailman.isi.edu/pipermail/ns-developers/2013-September/011417.html)
Code: http://gist.github.com/piotrjurkiewicz/6067858  
Details: http://mailman.isi.edu/pipermail/ns-developers/2013-September/011417.html

#### TapBridge link status notification patch `required` [`submitted`](http://mailman.isi.edu/pipermail/ns-developers/2013-September/011417.html)
Code: http://gist.github.com/piotrjurkiewicz/6067864  
Details: http://mailman.isi.edu/pipermail/ns-developers/2013-September/011417.html

#### Ethernet checksum performance patch `optional` [`submitted`](http://mailman.isi.edu/pipermail/ns-developers/2013-September/011418.html)
Code: http://gist.github.com/piotrjurkiewicz/6655299  
Details: http://mailman.isi.edu/pipermail/ns-developers/2013-September/011418.html

#### WiFi Ap address setting patch `optional`
Code: http://gist.github.com/piotrjurkiewicz/6483746

#### WiFi WDS mode implementation `optional`
Code: http://gist.github.com/piotrjurkiewicz/6483675

## Usage

### ns-3 downloading and building  
1. Download ns-3 source code: http://www.nsnam.org/releases/latest
2. Unzip it: `tar xjf ns-allinone-3.*.tar.bz2`
3. Go to the directory containing ns-3: `cd ns-allinone-3.*/ns-3.*/`
4. Configure it: `./waf -d optimized --enable-sudo configure`
5. You may be prompted for sudo password while building.
6. Build: `./waf build`

### Running mininet scripts
1. Run `sudo ./waf shell` in order to let the ns-3 set appropriate environment variables.
2. Go to the directory with mininet scripts.
3. Run a mininet script, for example: `python mininet/examples/ns3/emptynet-simple.py`

## Midterm

For the time being, `mininet.ns3` module implements:

- ns-3 simulator handling: `start()`, `stop()`, `clear()`. I use global module functions and one global thread object because ns-3 simulator is a singleton object, so there can be only one simulator thread running.

- `TBIntf` - subclass of mininet's Intf: It is a TAP interface located on mininet node which is bridged with the nsDevice located on nsNode. In fact, TBIntf class is the main workhorse of the module.

- `SimpleSegment` - network segment (channel) with underlying SimpleChannel model from ns-3 (SimpleChannel is to simplest existing channel model in ns-3). Multiple nodes can connect to the segment, each time with `SimpleSegment.add()`. (see test-2.py)

- `SimpleLink` - subclass of mininet's Link and SimpleSegment. It is a SimpleSegment with only two nodes connected. Its constructor is similar to the constructor of mininet's Link, so it can be used alternately. (see test-3.py)

- `CSMASegment` and `CSMALink` - the same but for CSMA channel ns-3 model. (see test-4.py) 

Examples emptynet-simple and emptynet-csma are modifications of the original emptynet example. Added and modified lines to the original are marked. As you may see, you have to only change Link class to another and invoke mininet.ns3.start() to start the ns-3 simulator.

IMPORTANT NOTICE:
You should not create any ns-3 segments or links or add any nodes to them after calling mininet.ns3.start(). Some part of ns-3 code called during device connecting is not thread-safe and it results in segfaults.

I have prepared a Mininet virtual machine with built ns-3. Supports wired segments and links: Simple and CSMA. Download [here](https://www.dropbox.com/s/nce813ropsz16wf/midterm.zip).

1. Unzip and import machine to the VM hypervisor.
2. Start VM.
3. Go to the directory containing ns-3: `cd ns-allinone-3.17/ns-3.17/`
4. Run `sudo ./waf shell` in order to let the ns-3 set appropriate environment variables.
5. Run tests:
   - `python ../../mininet/examples/ns3/test-0.py`  
   Test starting and stopping ns-3 simulator.
   - `python ../../mininet/examples/ns3/test-1.py`  
   Usage of TBIntf mixed with ns-3 code.
   - `python ../../mininet/examples/ns3/test-2.py`  
   Usage of SimpleSegment. Three nodes connected to the one segment (channel).
   - `python ../../mininet/examples/ns3/test-3.py`  
   Usage of SimpleLink (SimpleSegment with only two nodes connected)
   - `python ../../mininet/examples/ns3/test-4.py`  
   Usage of CSMALink.
   - `python ../../mininet/examples/ns3/test-5.py`  
   Capturing packet trace for CSMALink on ns-3 device.
   - `python ../../mininet/examples/ns3/emptynet-simple.py`  
   Modification of original emptynet.py example with SimpleLink. Changed lines are marked.
   - `python ../../mininet/examples/ns3/emptynet-csma.py`  
   Modification of original emptynet.py example with CSMALink. Changed lines are marked.

