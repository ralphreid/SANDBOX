## Expected results:
 Example code, documentation, and tutorials for automatically discovering and recreating a hardware topology in Mininet.

## Plan
To have a component in each controller(POX, Floodlight) that generates a mininet python file for the physical topology.


## Procedure
* Create a module in controller which collects the following information:

> Host: IP + MAC

> Switch: MAC

> Link: each end's MAC + port no(if possible)

* Using the above information and mininet API, create mininet python file for physical topology.

<i>BL Comments: This sounds good to me. I know I'm not mentoring you officially, but I think that you will want to make a wiki page that explains how to install and use your system, perhaps with instructions and a walkthrough as well as API documentation for people who want to integrate your module into their POX/Floodlight controller. I recommend making it as simple as possible for someone to make use of your mininet topology creation module -> for example it should be as easy as downloading and running a script and then getting a custom topology file which can be used directly from the mininet command line or from another script. Also regarding your plan, I think the best plan is to try to get something which you could demo, at least in some basic form, a couple of weeks from now (now being June 17th.)</i>

#### BL Feedback July 12th:

1. I like the idea of creating a custom topology file which can be used from the command line or in a script.
2. I don't actually know offhand how to collect topology information in pox, floodlight, etc..
3. I'd like to see a complete walkthrough showing the steps which one might take to
   - enable this functionality in an existing controller
   - find out when the topology is available
   - request that a mininet topology be generated
   - examine that generated mininet topology
   - re-invoke the controller with the new topology hosted in Mininet
4. I believe that pox, floodlight, etc. have messaging/RPC interfaces which can be used to service requests.

#### update
Walk through has been update [here](https://github.com/basavesh/gsoc13/wiki)