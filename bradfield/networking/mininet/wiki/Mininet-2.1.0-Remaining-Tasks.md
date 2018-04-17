* ~~Create S3 folder/repository for VMs (done)~~
* ~~test `debuild`~~
* ~~Try to create a build server VM (or at least an NFS server for local builds) (BL)~~
* ~~Automate `examples/` testing as much as possible (BOC)~~
* ~~Pre-announce on `mininet-discuss` for additional testing and feedback~~
* ~~Final pass (proofreading, verification, and editing) on text files (`README`, `INSTALL`, etc.)~~
* ~~Verify that Walkthrough works with 2.1.0~~
* ~~Update [[Mininet 2.1.0 Release Notes]]~~
* ~~Update api.mininet.org~~
* ~~Verify that 2.1.0rc1 works in Ubuntu Beta~~
* ~~Run automated tests again on all targets, and tag rc2 if they pass~~
* ~~Remaining manual tests~~
  * ~~Verify that `consoles.py` and `miniedit.py` work in VMs~~
  * ~~Verify that x11 command line option and `xterm` CLI command works in VMs~~
* ~~Update VM build instructions~~
* ~~Investigate test failures on vbox~~
  * ~~testLinearBandwidth (test_linearbandwidth.testLinearBandwidth)~~
  * ~~testTopo (test_simpleperf.testSimplePerf)~~
* ~~Determine upload service (e.g. bitbucket, sourceforge) and upload vm images~~
* ~~Update Download/Installation instructions for 2.1.0~~
* ~~Synchronize debian packaging w/launchpad (BL)~~
* ~~Tag 2.1.0 final before Ubuntu Final Beta Freeze (Sep. 19th) (BL)~~
* Announce on mininet.org blog and on `mininet-discuss` (BL)

### Deferred to post 2.1.0:

* Fix ovf file so that
  * virtualbox doesn't give some unknown error about missing hardware
  * the os is specified as ubuntu-$arch
* Automate VM upload from build script (BL - add function to script)
* More (quick, high-leverage) unit tests for `make test`
