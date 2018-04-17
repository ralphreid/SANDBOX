There are two places that SSL will need to be configured if SSL is to be used between the controller and the Open vSwtich.  The instructions below assume an installation of Open vSwitch using Ubuntu packages.  If you installed by alternate means, the location of the openvswitch/pki might be different.

### Open vSwtich Setup
Create all the keys and register them with Open vSwitch.

    cd /etc/openvswitch
    sudo ovs-pki req+sign sc switch
    sudo ovs-vsctl set-ssl \
        /etc/openvswitch/sc-privkey.pem \
        /etc/openvswitch/sc-cert.pem \
        /var/lib/openvswitch/pki/controllerca/cacert.pem

The above might not be the most secure way to manage the keys, but again, this is for research and experimentation.

### Open vSwtich test controller ovs-controller Setup
Create all the keys.

    cd /etc/openvswitch
    sudo ovs-pki req+sign ctl controller

### Running a Sample Test
In one window, let’s start the ovs-controller with SSL support.

    sudo ovs-controller -v pssl:6633 \
         -p /etc/openvswitch/ctl-privkey.pem \
         -c /etc/openvswitch/ctl-cert.pem \
         -C /var/lib/openvswitch/pki/switchca/cacert.pem

Next, below is a sample Mininet Python script. Run this Mininet script that creates a simple single switch topology and sets the controller to SSL.

    #!/usr/bin/python
    from mininet.net import Mininet
    from mininet.node import Controller, RemoteController
    from mininet.cli import CLI
    from mininet.log import setLogLevel, info
    
    def emptyNet():
        net = Mininet( controller=RemoteController )
        net.addController( 'c0' )
        h1 = net.addHost( 'h1' )
        h2 = net.addHost( 'h2' )
        s1 = net.addSwitch( 's1' )
        net.addLink( h1, s1 )
        net.addLink( h2, s1 )

        net.start()
        s1.cmd('ovs-vsctl set-controller s1 ssl:127.0.0.1:6633')

        CLI( net )
        net.stop()
        
    if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()

When you run the script, you will see that a PingAll test ran and passed. You can also check and see that switch is connected using SSL.

    mininet@mininet:~$ sudo ovs-vsctl show
    902d6aa3-6a0a-4708-a286-3301c8b36430
        Bridge "s1"
            Controller "ssl:127.0.0.1:6633"
                is_connected: true
            fail_mode: secure
            Port "s1"
                Interface "s1"
                    type: internal
            Port "s1-eth1"
                Interface "s1-eth1"
            Port "s1-eth2"
                Interface "s1-eth2"
        ovs_version: "2.0.1"
