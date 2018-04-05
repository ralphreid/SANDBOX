Bradfield Networking - Class 1:

I want to learn how to break down network problems and chunk down solutions.

Thing about..

1. What are the important kinds of hardware that make the Internet possible?
2. Which networking “layers” do each of these hardware components belong to? 
3. What is a “protocol” and what does it mean to layer a series of protocols? 
4. What are the major components of a protocol? 
5. Why might there be so many protocols to choose from at each layer? 
6. How do protocols from different layers work together? 
7. In class, we will focus on making the layering approach more concrete by writing a program to parse a series of HTTP packets, which are themselves embedded in a series of TCP segments (embedded in IP datagrams [embedded in Ethernet frames]).

Objectives:
1. Define crucial speed metrics
    * propagation - time it takes for packet to transit...so amount of time "on the wire" till it hits the end of the link (1/3C * DIST)
    * transmission - speed at witch can write to the wire....how fast can put data into a transport medium
    * queuing delay - speed of the routers cpu speed, routing speed, clock speed, 
    * RTT - Ping - Measure of Latency - Round Trip Time - ms
        * monitoring
        * like minimzing delay in phone call
    * Bandwidth (or Throughput) - Mega Bits per second MBits/s
2. Define critical hardware devices
    * Routers
    * Cable
    * Modem
    * Hosts
    * Switches
3. Examine the layering model of modern network
    * Why layering?
        * easier to debug
        * optimise parts for specific reasons
        * makes a climate of better inovation
    * TLS is Transport Layer which encompases TCP as an alternative
4. Review binary data parsing
    1. Global PCAP Header folowed by N packet starts with a per packet header, IP Header, TCP, HTTP Header
    2. PCAP & per packet system captures where little indian numbers & others big indian
    3. Byte is 8 Bits

CHECKOUT
- wireshark live
- how to get ipv6 address
- checkout google quick
