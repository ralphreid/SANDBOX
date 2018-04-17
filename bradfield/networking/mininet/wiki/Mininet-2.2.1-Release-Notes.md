Mininet 2.2.1 is primarily a performance enhancement and bug fix release to [[Mininet 2.2.0 | Mininet 2.2.0 Release Notes]].

### Debian and Raspberry Pi support

`install.sh -fnv` and `install.sh -a` now work out of the box on Raspbian/Debian 7.8 Wheezy, so you can easily install and run Mininet on a [Raspberry Pi](http://raspberrypi.org)! You can also install OVS 2.3.1 using "`install.sh -V 2.3.1`".


### API Changes

2.2.1 is compatible with the 2.0 API, but some minor changes have been made for performance or other reasons, and you should be aware of them since they could cause unexpected behavior.

- links not added using `addLink()` will not be cleaned up automatically in `Mininet.stop()`. Note that `sshd.py` has changed slightly to reflect this. `controlnet.py` has also changed. The symptom you may observe is that links may be left in the root namespace. They may be deleted using `mn -c` or `mininet.clean.cleanup()`

- `printPid` is now `False` by default in `Node.cmd()` and `Node.sendCmd()`

- `mininet.clean.cleanup()` has been reorganized and now uses a class.

- Some previously silent command failures may now cause exceptions due to using `errRun` rather than `quietRun`. If you encounter unexpected exceptions, you may wish to run with `setLogLevel('debug')` (or `--v debug`) to see what is going on.

- As the Linux kernel matures, it becomes less necessary to have secondary checks as to whether an operation succeeded and try again (as seen with the infamous "gave up after 3 tries" messages) so these checks (and retries) are being removed. This may expose issues which were previously hidden on older Linux kernels.

- The Ryu controller class is now named `Ryu` instead of `RYU` - the new name reflects the correct
  project name, which is not an acronym. The `--controller ryu` option is unchanged.

#### OVS Patch Links

An `OVSLink` (`--link ovs`) class has been added which implements OVS patch links. Unlike `veth` pairs, OVS Patch Links are virtual entities within OVS itself, and can potentially support much higher data rates (particularly over multiple links, probably due to OVS's flow rule optimization) as well as slightly faster startup time.

However, **OVSLinks have several serious limitations**, including the following:

1. OVS patch ports are not real Linux interfaces, so you cannot monitor them using `tcpdump` or `wireshark`.

2. OVS patch ports are not real Linux interfaces, so you cannot control their behavior using `tc`.

3. Because of the above, `OVSLink` does not support link modeling including bandwidth limits, delay modeling, or loss modeling.

4. Based on our experience so far, no more than ~64 `OVSLinks` should be used in a row. This means that a command like `mn --topo linear,64 --test iperf` will work, but `mn --topo linear,80 --test iperf` will fail.

That being said, if you want the fastest possible data rates on small-diameter networks, you may wish to try `OVSLink`. If it doesn't work, just go back to regular links.

### Notable bug fixes

- The [CPqD switch](https://github.com/CPqD/ofsoftswitch13) should now build and install on Ubuntu 14.04
- The CLI `switch` command has been fixed (though its precise semantics are still a bit obscure, as it currently causes a switch to stop or start forwarding packets while leaving its interfaces up)
- Repeatedly invoking the CLI will not cause `.mininet_history` to double in size (thanks to Rich Lane.)

### Other minor changes

- You may now specify multiple `--controller` arguments to `mn`

- `RemoteController` and `--controller remote` now accept strings of the form `IP:port` where `IP` is the remote controller IP address and `port` is the port.

- `mn --help` and the man page for `mn` now list the class names for `--host`, `--switch`, and `--controller` options. The classes themselves, along with their options, are documented on <http://api.mininet.org> . We hope to improve the documentation over time.

### Errata

Please consult the [[Mininet 2.2.0 Release Notes#errata]].