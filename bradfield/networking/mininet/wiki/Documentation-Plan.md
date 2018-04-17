### Mininet Documentation Plan/Projects

What should be done to improve the documentation and make it easier for people use, develop for, and contribute to Mininet?

### Mininet 2.0.0 Documentation

Mininet has an expanding base of documentation, available at
https://github.com/mininet/mininet/wiki/Documentation

### Documentation Futures

There are a variety of excellent and useful things which can and should be done to improve the Mininet documentation. In this section, I describe several obvious and potentially highly beneficial documentation project ideas.

#### Updated OpenFlow Tutorial

Perhaps the most important documentation update is to update the OpenFlow tutorial to use Mininet 2.0 rather than the older Mininet 1.0 and its associated tutorial VM. This will integrate the OpenFlow tutorial into the Mininet learning progression and also bring additional users (and eventually developers) into the Mininet 2.0 fold.

#### High-quality/extended documentation

Mininet/OpenFlow book: start by writing on-line; PDF download for iPad/reader; print version? (O’Reilly, but better quality???)

We would like to develop high-quality documentation for the entire Mininet system as well as OpenFlow, the controller frameworks, and the entire SDN ecosystem. Ideally we should produce something of "Adele Goldberg" (after her landmark Smalltalk-80 book(s)) or "Hennessy and Patterson" quality (as per CAQA and the EE108b textbook) rather than "O'Reilly" quality. However, an advantage of on-line documentation is that we can produce initial documentation quickly and then steadily improve and enhance it over time. A book could be developed initially in html and PDF format for easy distribution.

#### Introductory API and architecture documentation

The Introduction to Mininet is an important step towards explaining how the Mininet API is designed and intended to be used. However, there is currently no documentation that explains the overall rationale for the API and explicitly explains the high-level (Topo), medium-level (Node, Link, LinkTo(), etc.) and low-level (mininet.util) APIs.

#### Example-focused documentation

Mininet comes with a good selection of useful example code in the `examples/` directory. Unfortunately few people seem to take advantage of this code, and many people ask questions on the mailing list indicating they not only don't understand the code, but they haven't even read it or tried to understand it, and they don't even have any idea of how to run it! Although cluelessness is eternal, we can certainly leverage the existing examples by writing prose to explain their rationale, design, and usage. This would create a series of modular lessons which would help not only to understand the examples and the problems they are trying to solve, but also the rationale usage of the Mininet API and some finer aspects of SDN and OpenFlow which seem to escape many.

#### `make doc` should build all documentation(?)

It would be terrific if `make doc` not only built the Python API documentation and man pages, but created PDFs of the documentation on the web site. However, we need to think of the best way of handling this - should the documentation source be part of the Mininet source or the web site source? Does it make sense to change the Mininet source every time the documentation changes?

#### Documentation should be available for download

At the very least, the PDF/html API documentation should be available for downloading and offline reading without having to type "make doc". Note in CS244 we found that many (most?) students were confused by both Python docstrings and having to type make doc, but they had no trouble understanding a link to the html documentation or a PDF.

#### Merge CS244 Piazza into FAQ

A large amount of useful content was generated last year on Piazza.com as part of the projects for CS244, which all used Mininet. CS244 is being taught again right now and additional content is being added to Piazza. Ideally the high-quality and/or useful content from Piazza should be merged into the FAQ or other Mininet documentation.

#### Make CS244 crawlable

One possibility is that we may be able to work with Piazza to extract the CS244 content and make it available online, or perhaps to anonymize last year's posts and make it crawlable on Piazza.

#### Stackoverflow for questions?

http://stackoverflow.com works great for Python - there is a large critical mass of information, a large community of users who contribute that information, and that information is well-indexed by Google. It may be possible, given enough interest and content, to create a Mininet space on stackexchange.com.

#### Videos

Some time ago, Brandon and I wrote a basic script for a simple Mininet overview/demo. In many cases, potential Mininet users seem to ask questions indicating a basic non-understanding of what Mininet is or what it can do. Introductory videos or screencasts could potentialliy help some people get over this hurdle.

#### Collaborate with POX/Murphy on tutorials

There may be leverage working with a controller framework such as POX for combined tutorials that explain the basics of using OpenFlow by implementing simple controllers. It would be great to have something that goes beyond the existing OpenFlow tutorial and teaches people how to do a variety of interesting and cool things that aren't simple L2 or L3 forwarding.

#### Leverage CS144 course and materials (and vice-versa)

Mininet is replacing VNS, and TY has already added the CS144 projects, formerly in VNS, in Mininet form to the Mininet wiki (see above.) We may be able to figure out a way to use/leverage these assignments - and indeed the entire online CS144 course - to help bring people up to speed on the basics of networking as well as Mininet itself. In many cases, questions asked on mininet-discuss indicate a basic lack of understanding of networking and CS in general, and CS144 and related materials could help. Note the CS144 assignments are SDN-like (they involve creating a software router) but they do not use OpenFlow. Note that demos like the buffer bloat demo (which CS244 students worked on and which was also used as an in-class lab in CS144) are a huge opportunity for Mininet both in terms of classroom education and network education for the masses on the internet.

#### Magazine articles and tutorials?

It may be possible to kill multiple birds with one stone by writing a series of tutorials for publication in magazines, for example publications like Usenix's ;login:, Linux Journal, or even CACM or IEEE Computer. In addition to training users and informing people about Mininet (and raising the profile of the project), the material could be integrated into the Mininet documentation and web site.

#### Easy documentation for “users” to use out of the box

Some users seem uninterested in writing scripts in Python and prefer to use Mininet simply as a command-line tool using the built-in functionality. Perhaps we can offer better support for these "users" as well as a path to turning them into smarter, more expert users who can use Python.


