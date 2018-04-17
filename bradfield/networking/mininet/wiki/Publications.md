### Papers

* Lisa Yan, Nick McKeown. *[[Learning Networking by Reproducing Research Results | https://ccronline.sigcomm.org/2017/learning-networking-by-reproducing-research-results/ ]]*.
[[ SIGCOMM CCR, April 2017 | https://ccronline.sigcomm.org/2017/the-april-2017-issue/ ]].

  Since 2012, students in Stanford's CS244 have used Mininet (primarily, as well as other systems such as Mahimahi, Emulab, and ns-2/3) to replicate published research results; this has helped to increase their own understanding, knowledge and abilities while making a valuable contribution to the field by examining and verifying results.

<!-- was: pdf/mininet-conext12.pdf -->

* Bob Lantz, Brian O'Connor. *[[ A Mininet-based Virtual Testbed for Distributed SDN Development | http://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p365.pdf ]]*. [[SIGCOMM 2015 | http://conferences.sigcomm.org/sigcomm/2015/demosessions.php ]], August 18-20, 2015, London, UK.

  This demonstration showed distributed Mininet emulation (cluster edition) as well as enhancements such as the Mininet Server node, which simplifies running unmodified Linux services on Mininet as well as self-hosting (i.e. running multiple and nested Mininet sessions.)

* Brandon Heller. *[[ Reproducible network research with high-fidelity emulation | https://stacks.stanford.edu/file/druid:zk853sv3422/heller_thesis-augmented.pdf ]]*. Ph.D. Thesis, Stanford University, 2013.

  This thesis examines how to improve the predictive performance accuracy of emulators by defining and monitoring network *invariants*, universal properties of network systems that we know must be true. This facilitates the use of emulators like Mininet for realistic and reproducible network experiments.

* Nikhil Handigol, Brandon Heller, Vimal Jeyakumar, Bob Lantz, and Nick McKeown. *[[Reproducible Network Experiments using Container-Based Emulation | http://conferences.sigcomm.org/co-next/2012/eproceedings/conext/p253.pdf]]*. [[CoNEXT 2012 | http://conferences.sigcomm.org/co-next/2012/program.html]], December 10-13, 2012, Nice, France.

  This paper advocates changing the practice of computer networking research (and CS in general),
by demonstrating *reproducible* experiments using Mininet-HiFi, aka Mininet 2.0, and includes an overview of
its design as well as experiences using Mininet to reproduce 16 published network experiments.

<!-- was: pdf/a19-lantz.pdf -->

* Bob Lantz, Brandon Heller, and Nick McKeown. *[[A Network in a Laptop: Rapid Prototyping for Software-Defined Networks | http://conferences.sigcomm.org/hotnets/2010/papers/a19-lantz.pdf]]*. [[9th ACM Workshop on Hot Topics in Networks | http://conferences.sigcomm.org/hotnets/2010/program.html]], October 20-21, 2010, Monterey, CA.

  This paper explains the basic Mininet design and workflow.


### Reproducible Network Experiments using Mininet

* <http://reproducingnetworkresearch.wordpress.com>


### Technical Reports

* [[CSTR 2012-2 Mininet performance fidelity benchmarks | http://hci.stanford.edu/cstr/reports/2012-02.pdf]]

### Presentations and Slides

* [[Mininet SOSR Software Systems Award Talk | pdf/mininet-award-sosr17.pdf ]] [(Program)](http://conferences.sigcomm.org/sosr/2017/program.html) [(Award)](http://conferences.sigcomm.org/sosr/2017/award.html) [(Slides)](pdf/mininet-award-sosr17.pdf)

  This is our invited talk at [[ SOSR 2017 | http://conferences.sigcomm.org/sosr/2017 ]], delivered after **Mininet won the [[ ACM SIGCOMM SOSR Software Systems Award | http://conferences.sigcomm.org/sosr/2017/award.html ]]!** 

  I (BL) describe how Mininet was created, leading into a discussion of why Software Research Projects are a particularly beneficial and worthwhile form of scholarship, and ending with some suggestions for how we can improve research in networking and systems, as well as some important unanswered research questions.

* [Teaching Computer Networking with Mininet](http://teaching.mininet.org) [[(Program) | http://conferences.sigcomm.org/sigcomm/2014/tutorial-mininet.php ]] [[(Slides and Materials) | SIGCOMM 2014 Tutorial: Teaching Computer Networking with Mininet]] [(teaching.mininet.org)](http://teaching.mininet.org)

  This is our tutorial from [[ SIGCOMM 2014 | http://conferences.sigcomm.org/sigcomm/2014/ ]], where we provided an introduction to Mininet and shared experiences using Mininet to tech computer networking at Stanford, Georgia Tech and MIT as well as in MOOCs (massive open online courses.)

* [Mininet: an instant Virtual Network on your Laptop](pdf/mininet-netseminar.pdf) [[(Announcement) | NetSeminar Announcement]] [(Slides)](pdf/mininet-netseminar.pdf) [(Video)](http://www.youtube.com/watch?v=90fBCO1MMTA)

  Stanford [NetSeminar](http://netseminar.stanford.edu). Bob and Brian explain why network emulation is valuable and how Mininet addresses issues of scalability, usability, and performance modeling. Includes a somewhat detailed description of how Mininet uses underlying Linux functionality to implement a convenient Python API for network emulation. The slides include interesting supplemental material as well.

* [[Mininet-HiFi: Rapid, High Fidelity SDN Prototyping | pdf/mininet-hifi-bdh2.pdf]]

  Presentation from SDN CTO Summit describing Mininet-HiFi features, which have since been integrated into   Mininet 2.0.

* [[A Network in a Laptop: Rapid Prototyping for Software Defined Networks | pdf/mininet-hotnets2010-final.pdf]]

  Brandon's presentation from Hotnets-IX (10/20/2010) explains the Mininet architecture and SDN workflow, from prototyping to hardware deployment, and includes a slide on adding performance fidelity to Mininet.

* [["Mininet: Squeezing a 1000-node OpenFlow Network onto a Laptop" | pdf/mininet-presentation-2009.pdf]]

  Bob's original presentation to the OpenFlow Software Architecture and Implementation (SWAI) working group from 11/19/2009 (with an additional slide to illustrate the kernel datapath),