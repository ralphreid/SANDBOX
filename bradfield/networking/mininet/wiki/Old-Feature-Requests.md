<!-- %META:TOPICINFO{author="BobLantz" date="1305074389" format="1.1" version="1.13"}% -->
<!-- %META:TOPICPARENT{name="Mininet"}% -->
<!-- Use our custom page layout:
* Set VIEW_TEMPLATE = [MininetView](MininetView)
-->

<!-- %TOC% -->

### CLI Requests

* configurable xterm spawning, or at minimum, spawn a single xterm from the CLI
* option to daemonize run script
* add SSHD test to CLI to, say, run hostname via SSH and grab the output
* start/stop switches in order
* set/add configurable max_backoff on switches
* print dpid via nodeid function from topo?
* extract default port from openflow.h
* split --mac setting into host and switches
* add get_connected_hosts function to topo
* print average ping time from regression test


### [Doc/Install](Doc/Install) Requests

* API documentation (comment re-uglification filter + doxypy + upload to wiki)


### Code Cleanup

* clean up params in Mininet.__init__
* add ports() call to just call port() twice and return the tuple
* reconsider the functions in Node; split some into a Port object, others to a [NamespaceHost](NamespaceHost), others to [ProcessNode](ProcessNode.md)?
* check all uses of send; make as many of these into named functions as possible; should simplify porting to remote usage [Why does this help? -BL]
* [NetCLI](NetCLI)? separate out the control from creation aspects? [I say just fix the CLI, and do proxies if desired. However, we will do a CLI for cluster edition. -BL]
* dpid naming could really be redone - rename as an id, or nodeid, or something else. [I have my doubts about dpids -BL]


### Speedup Requests
* consider multithread setup and cleanup [Probably won't help, but you never know. -BL]


### Other Requests

* Add host log. Namespaces all share the same history; would be useful to a have h0.log. Not sure if this is possible. Maybe tee std output to a file, and have a separate input log?
* Increase inactivity timer to clean up debug log output with nox
* Support multiple controllers
* Support distributed operation: mix of physical and virtual ports.
* ensure controller is dead at the start?
* Generalize the Port object; enable non-config or already-configured ports. Plus add up/down methods.
