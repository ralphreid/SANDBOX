The following instructions will guide you through how to set up the environment for the [[programming assignments|Assignments]]. The first set of instructions is for working with a local machine or VM running Ubuntu. We also provide an Amazon EC2 AMI image with everything set up for people would like to run the lab on EC2 (ami-96139ba6, Oregon Region). You can find instructions on how to use an EC2 AMI image below. **(Note: We strongly encourage you to use EC2 AMI image, since you can avoid version problems as POX/Mininet are open source projects and will continue to evolve.)**

## Using Your Own Ubuntu Machine or VM
### Install Needed Tools
```no-highlight
sudo apt-get update
sudo apt-get install -y git vim-nox python-setuptools python-all-dev flex bison traceroute
```
### Install Mininet
```no-highlight
cd ~
git clone git://github.com/mininet/mininet
cd mininet
./util/install.sh -fnv
```

Note: older versions of the assignments required you to check out an older version of Mininet before running ```install.sh```, but this should no longer be necessary:
```
git checkout remotes/origin/class/cs244
./util/install.sh -fnv
...
```

### Install POX
```no-highlight
cd ~
git clone http://github.com/noxrepo/pox
```

### Install ltprotocol 
```no-highlight
cd ~
git clone git://github.com/dound/ltprotocol.git
cd ltprotocol 
sudo python setup.py install
```

## Using Amazon EC2

The assignments only require a t1.micro instance, for which Amazon provides 750 free usage hours per month.  

### Launch an Instance with the provided AMI Image
* Go to [AWS Console](https://console.aws.amazon.com)
* Switch to "Oregon" region, you can do so by pull down the region menu on the upper-right corner. The default is N. Virginia. 
* Click on "Launch an instance", then choose "Classic Wizard"
* On the "Community AMIs", search for "ami-96139ba6". You should see an image with the Manifest of "Mininet_assignments". 
* Select the image, then keep clicking "Continue" on the next few page, until the page ask you to select your key pairs. 
* Choose the key pair you would like to login to your EC2 instance, then click on "Continue". 
* At the final page, you can find an "Launch" button. Click it and you are done!
* Go to "Security Groups", select "default", then click on "Inbound" tab.
* Select "SSH" from "Create a new rule" drop down.
* Click "Add Rule" then "Apply Rule Changes"
* Then use your key pair to login to your EC2 instance.
```no-highlight
> ssh -Y -i <Your KeyPair> ubuntu@<your EC2 domain name>
```

The Image contains the starter code for all the assignments. 