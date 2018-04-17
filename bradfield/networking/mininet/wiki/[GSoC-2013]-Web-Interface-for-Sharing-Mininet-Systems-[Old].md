## Note: This page is old and some information may be outdated, new docs is located [here](https://github.com/mininet/mininet/wiki/%5BGSoC-2013%5D-Web-Interface-for-Sharing-Mininet-Systems)

There are two main objectives: [PyPI or CPAN for Mininet](Web-Interface-for-Sharing-Mininet-Systems#pypi-or-cpan-for-mininet) and [Complete system/VM/experiment archive](Web-Interface-for-Sharing-Mininet-Systems#complete-systemvmexperiment-archive).

### Contents

* [PyPI or CPAN for Mininet](Web-Interface-for-Sharing-Mininet-Systems#pypi-or-cpan-for-mininet)
 * [Project Iteration Log](Web-Interface-for-Sharing-Mininet-Systems#project-iteration-log)
 * [Project Mentor Feedback](Web-Interface-for-Sharing-Mininet-Systems#project-mentor-feedback)
* [Complete system/VM/experiment archive](Web-Interface-for-Sharing-Mininet-Systems#complete-systemvmexperiment-archive)

---

### PyPI or CPAN for Mininet

For this part of project, we are going to use existing Python packaging system (based on `setuptools`) to package Mininet modules and build a PyPI clone just to share Mininet modules.

---

#### Project Iteration Log

#### First iteration (17 June - 5 July):
- All missing major features are added to djangopypi2:
 - User registration page
 - Package permission page
 - Package search page
- Deployed the djangopypi2 on a free micro Amazon EC2 instance running on nginx + gunicorn. VNC can be used for remote access if needed. HTTPS is used for most parts of website except those under /simple/. The certificate used for HTTPS is currently self-signed though.
- Tried out the packaging system with more complicated dependencies. The Mininet modules used are: `mininet`, `pox`, `ripl`, `riplpox`.

#### Second iteration (8 July - End of GSoC):
- [mnp](https://github.com/heryandi/mnp).
- [Direct multipart upload to S3 with automatic retry on failure](https://github.com/heryandi/flask-s3-multipart). Maybe useful for uploading VM image later.
- [User guide](https://ec2-54-218-16-158.us-west-2.compute.amazonaws.com/guide/) and [mininet-starter](https://github.com/heryandi/mininet-starter) package.
- Setup script to setup the djpp on an Ubuntu 12.04 machine.
- GitHub login integration with djangopypi2.
- Design docs.
- Documentation.
- Test cases. (Unit tests done for mnp. In-progress for djpp.)

----

#### Project Mentor Feedback

#### First Phase Feedback (BL) (... through 5 July)

Great - it looks like this is a feasible proof of concept and the basic system is up and running to some extent!!

I'm interested in a bunch of things which might help to make this a real system that we could use:

1. Replicability/movability to a different cloud

 We now have one test server running in Amazon. If I want to replicate this server elsewhere (e.g. suppose we make a private cloud for on.lab using openstack), how do I do it? Is the process automatic? Can I still use Amazon for storage and as a CDN? If so, how?  
**Heryandi**
A script to gunicorn + supervisord + nginx with proper configuration has been written, though it is not fully automatic in some steps (e.g.: sudo).
As for using Amazon only for storage/CDN, I am quite sure that it is possible with the API.
The python API is available [here](http://boto.readthedocs.org/en/latest/s3_tut.html) and it seems to me that there should be no problem on using it
**Heryandi End**

2. Help/documentation

 When people go to the site, where do they find clear instructions about how to find, download and use packages, as well as how to create new packages and upload them? Is there a walkthrough showing how one might do this?

 When people go to a project page, how do they find out about the different options for downloading and/or installing a package?

 What is the learning curve? How do we make it as quick and easy as possible for people to find, install, and run/use a module?

 Many modules have documentation. How is that integrated into the system? How/where do I go to find documentation on a particular module? If I'm installing from the command line, how do I get the documentation?  
**Heryandi**  
First 3 questions: A walkthrough has been written and put into https://ec2-54-218-16-158.us-west-2.compute.amazonaws.com/guide/.

Module documentation: There is a package page which can show the documentation as written by uploader. If this is not enough, then a link to external website can also be added.

Command line documentation issues:
- If the package is not installed yet, then the `mnp docs` command can be used to pull the docs from the website.
- If package is already installed and the packager specifically set the package to download/install the documentation as well, then it will be available on disk. I have added to the tutorial on how to do this.
**Heryandi End**

3. Scripts

 Are there scripts to make these processes as easy as possible?  
**Heryandi**
https://github.com/heryandi/mnp
**Heryandi End**

4. How do you think people should find out about the system?  
**Heryandi**
Never thought about this at all, maybe mention it in OpenFlow and Mininet tutorial?
The people in Open Networking Lab should be ["encouraged"](http://en.wikipedia.org/wiki/Eating_your_own_dog_food) to use it as well so at least someone starts using it...
**Heryandi End**

5. How are the data backed up? If everything stored on Amazon goes away, how do we recreate it?  
**Heryandi**
The setup script can be used to help recreate the server configuration.
However, for the data (users, packages etc), currently there is no backup scheme at all...
If we intend to use S3 though, there should be no issue on reliability (Note: I have never used S3, I may be wrong).
We may want to do our own periodical backup (e.g.: every 1 month) to backup the data.
**Heryandi End**

6. Bug fixes and security updates

 How are bug fixes and security updates handled? What happens when there are critical security bugs in Linux/Ubuntu/Django/etc.?  
**Heryandi**
If the bugs are in Linux/Ubuntu, it shouldn't break the code if Linux/Ubuntu is upgraded.
If it affects Python/Django though, there may need to be some changes to the code if we upgrade. The best bet is to write unit tests with decent coverage so at least the breaking changes can be identified (and fixed manually >_<) quickly. Note: Currently there is almost no unit tests in djangopypi2! Once updated, simply ssh into the server and do a git pull and then restart the server.
**Heryandi End**

#### Midterm Feedback (BL) (August 2-9, 2013)

Three of the key aspects of the system are basic functionality (it needs to do what we need and be robust/reliable/secure/functional/upgradable), reproducibility (we need to be able to create/reproduce it on whatever hosting infrastructure we end up going with, which will probably be some kind of VM service like a local or hosted cloud), and usability.

##### 1. Basic design and progress review

I'm glad to see the documentation as well as the basic functionality of the system. Demonstrating the basic functionality is obviously essential, and the scripts and documentation are critical for usability. Overall I think that the basic design is sound. So far, you have

- Installed the Django PyPI clone on an EC2 instance to test its suitability for Mininet
- Written scripts to make it easier to use the system
- Written documentation to explain how to use the scripts and the system

To reiterate, the latter two parts - scripts and documentation - are critically important to making the system usable in deployment.

One thing that we haven't done a great job so far at is reproducibility, even the basic task of maintaining an overview of the design, or a simple design document, elaborating the project vision and describing the system components. This doesn't have to be complex or lengthy - rather it should be concise and reasonably complete, much like this summary.

##### 2. Next reproducibility steps: project source code and resource storage and access

Although you have prototyped much of the functionality of the project, it is important that the the code, data, documentation, and scripts are stored somewhere (e.g. on github) so that

- They can easily be found
- They are archived and backed up to prevent loss
- Anyone can review them, comment upon them, and enhance them
- The system can be replicated on - or migrated to - different infrastructure as needed (e.g. EC2, private cloud, etc..)

We've talked briefly about this and I believe you said that you would make sure that the code, documentation, configuration scripts, user scripts, and other notes are checked in somewhere and linked from this page.

In addition to documenting and collecting what you have so far, I think that for the system to be successful we will need a mechanism or, at the very least, a fairly detailed list of the steps required for replicating the system, that is, creating a production-ready version of it on whatever infrastructure we choose for the production version.

##### 3. Next usability step suggestions: single sign on, documentation access, and discoverability

**Single (and multiple) sign-on**: Although I think it's a good idea to allow people to register for the system with simply an e-mail address, I believe that *single sign-on* is also very important for success and usability of the system. Ideally, users should have the option of signing on with their github account so that they don't need to create a new account just to create packages. Note that people who want to *use* packages don't need to authenticate themselves or create an account at all - accounts and sign-on are only required for developers who are creating packages and making them available to others. Also, a single login should be usable for both the package system and the complete system/experiment archive system.

**Discoverability**: On one hand, we should add links and vanity URLs on mininet.org to point to the system. I (BL) can take care of that. Additionally, the user scripts (command line commands) should have the ability to enumerate the packages that are available.

**Documentation access**: This is related to discoverability; it should be easy to find complete documentation for a given package, and it should ideally also be possible to examine package documentation (or at the very least get a URL for the documentation) from the user commands.

Something to think about is whether the package scripts should be integrated into the `mn` command (e.g. `mn --install`) or should be separate scripts. For now, I am thinking we should prototype separate scripts - we can always integrate them with `mn` at a later date if desired. Also it's not entirely obvious to me how much integration we want with Mininet proper, and whether we want the package system to be a dependency for Mininet or a separate system.

##### 4. Overall Project Planning

Heryandi, it looks like things are going reasonably well; if you want to comment on the additional stuff you want to work on on both projects, that would definitely be helpful. Overall of course we're going to want to time-box things and just do whatever can be completed in the time frame, but it's important to me that things are packaged and documented so that we can either deploy them as-is or can easily continue work to add the remaining features that are required to get to a stage where we can put a test system on line and open it up to some users for testing purposes. We could make that part of the GSoC plan, or that could also be done afterward if there is missing functionality, usability features, or documentation that we still need to complete. Ideally at the end of the project we'll have, at the very least, a system that can be demonstrated.

One thing that might be nice to try for might be some live demos, perhaps via a Google+ hangout or something. We'd obviously have to coordinate the time zones, but I think other Mininet developers, GSoC participants and mentors, or perhaps folks at onlab might be interested.

Additionally, I think we will want a final project writeup/wiki page, including everything that is useful or relevant, from the basic functionality and design of the system, to some explanation of its components and internals, to instruction for deployment and installation (including links to each of the components as needed), to documentation (or links to it) for package users and developers. The sooner you start this, the easier it will be I think. You might be able to reorganize a lot of the existing material on this page.

----

### Complete system/VM/experiment archive

This objective is to be able to quickly replicate experiments.

The idea is to create a place for users to submit either of these:
- Complete VM image that is ready to run the experiment.
 Pros: Pretty much guaranteed that the experiment will be able to work.
 Cons: Users will need to upload/download huge files. Storage space consumed will also be large.
- Executable script to setup all the configurations needed (e.g.: download and install some packages from apt-get or PyPI) to run the experiment.  
 Pros: Users will not need to upload/download huge files. Storage space consumed will also be smaller.  
 Cons: May not always be successful in replicating experiments because of various problems (e.g.: some packages or some version of the packages may not be available anymore, different mininet version, different version of Linux).

The item uploaded will be submitted together with a post describing the content and the instruction to replicate the experiment (like the blog posts on reproducingnetworkresearch.wordpress.com).

#### BL Comments

Some questions I think we need to think about or investigate:

Storage Issues:

* What can we use for scalable storage/CDN?
* Can/should we use S3? How much does it cost? How are credentials handled?
* What are other issues relating to VM image storage, which might require a LOT of storage?  
**Heryandi**
Storage/CDN/S3: I investigated several storage & CDN solution and it seems to me that they are pretty much the same, but only Amazon provides free tier for 1 year.  
Credentials: We need to manually configure the CORS configuration of S3. In the configuration, we can specify which domains are allowed to directly upload to the folder. We can also configure folders to be publicly readable.  
Others: Uploading the image itself is a pain because of the size... [Fixed. I have created a quick prototype to do direct multipart uploads to S3 with auto-retry on failure]
**Heryandi End**


Deployment issues

* What are the target deployment platforms?
* Can the same image be used on, say, EC2 and VirtualBox?  
**Heryandi**
Deployment platforms: Not sure what you meant by deployment platforms. VirtualBox, VMware and KVM?  
EC2 & VBox: Should be possible. For the details, [the other GSoC project](https://github.com/mininet/mininet/wiki/Mininet-network-in-a-box-and-automatic-deployment-on-ec2) seems to be directly related to this issue.
**Heryandi End**

Web front-end issues:

* Can we have a single sign-on for both packages and VM images?  
**Heryandi**
If both sites can access the same user database, I am sure that this can be done.
**Heryandi End**

User Issues:

* What are the specific foolproof steps that users will take?
* Is there a template for documentation of each system, sort of like what we had on reproducingnetworkresearch.org?
* Is there a means for users to add additional information or documentation about a system?
* How will users find out about this system?
* How will it be documented?  
**Heryandi**
Not sure about any of these...
**Heryandi End** 