<!-- %META:TOPICINFO{author="BobLantz" date="1305074404" format="1.1" version="1.7"}% -->
<!-- %META:TOPICPARENT{name="Mininet"}% -->
<!-- Use our custom page layout:
* Set VIEW_TEMPLATE = [MininetView](MininetView)
-->


Mininet Futures
----------------

Mininet is under active development, and we hope to add a variety of useful features and expansions. This page will detail a few of the things we have been thinking about.

If there are specific features which you want or wish to implement, please open up an issue in github and/or a pull request!


### Bandwidth Limiting

*CPU and Link bandwidth limiting is included in Mininet 2.0!*

### Mininet: Cluster Edition

From the beginning of the Mininet project, we have been planning to expand Mininet to work on a cluster of PCs. In order to do this, we will extend Node() with a remote proxy class which will enable control of remote nodes. Additionally, tunneling will be provided to wire together nodes on multiple systems. An infrastructure for creating, controlling, monitoring and shutting down a Mininet cluster will also need to be developed.

It should be possible to emulate a Stanford University-size network (25,000 nodes or so) with Mininet.


### Multiple OS Support

Currently we rely on Linux features for process-based virtualization. It should be possible to use the features of other operating systems, for example Solaris Containers or !FreeBSD Jails to allow Mininet to run on those systems as well. Mac OS X is also an appealing target, although getting the virtual network infrastructure in place is likely to be challenging.


### Composable Topologies

Originally I had intended for topologies to be composable, so you could make a ring of trees, a tree of grids, etc.. This may still be a useful feature to add.



### Patch cables/panel and wire/link simulation

It should be easy to add a patch cable program that just forwards packets between interfaces. This would allow us to make a virtual patch panel and change how nodes are connected (or disconnected) without perturbing their underlying interfaces, and could even support simple link modeling - e.g. simulating packet loss or delay.. It's more efficient to just use veth pairs, but if you need the additional capabilities then the virtual cable would enable them.

The API already supports running arbitrary programs (e.g. wire simulators) in a node, but a high level API supporting link simulators (e.g. automatically instantiating and connecting them) would be more convenient. A simple wire simulator (e.g. supporting delay, drop, and some model of packet loss) could be provided. 
