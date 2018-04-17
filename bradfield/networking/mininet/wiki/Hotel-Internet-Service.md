
"""
A super simple OpenFlow learning switch that installs rules for
each pair of L2 addresses.
"""

# These next two imports are common POX convention
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
import pox.lib.packet as pkt
from pox.lib.packet.ethernet import ethernet
from pox.lib.packet.arp import arp
from pox.lib.addresses import IPAddr, EthAddr
from pox.lib.recoco import Timer


PROXY_MAC = EthAddr("00:00:00:00:00:FE")
PROXY_IP = IPAddr("10.0.0.254")
PROXY_PORT = 9

FAKE_MAC = EthAddr("00:00:00:00:00:EE")
log = core.getLogger()


table = {}
ipTable = {}
arpTable = {}
'''
how its being stored.
ipTable: [(event.connection,MAC-addr)] = [port, IP-addr]
arpTable:[(event.connection,IP-addr)] = [port,MAC-addr]

'''
all_ports = of.OFPP_FLOOD


class ProxyService (EventMixin):

  def __init__ (self, connection):
    self.connection = connection
    self.listenTo(connection)

  def handle_request (self, packet, event, idleTimeout, hardTimeout):

    if packet.find("arp"):
      ip = packet.find("arp")
      srcIP = ip.protosrc
      dstIP = ip.protodst
    else:
      ip = packet.find("ipv4")
      srcIP = ip.srcip
      dstIP = ip.dstip

    outgoingPort, dstMAC = arpTable[dstIP]

    "Reverse rule"
    msg = of.ofp_flow_mod()
    msg.idle_timeout = idleTimeout
    msg.hard_timeout = hardTimeout
    msg.buffer_id = None

    msg.match.in_port = outgoingPort
    msg.match.dl_src = dstMAC
    msg.match.dl_dst = packet.src
    msg.match.dl_type = ethernet.IP_TYPE
    msg.match.nw_src = dstIP
    msg.match.nw_dst = srcIP

    msg.actions.append(of.ofp_action_output(port = event.port))

    self.connection.send(msg)

    "Forward rule"
    msg = of.ofp_flow_mod()
    msg.idle_timeout = idleTimeout
    msg.hard_timeout = hardTimeout
    msg.buffer_id = None
    msg.data = event.ofp # Forward the incoming packet

    msg.match.in_port = event.port
    msg.match.dl_src = packet.src
    msg.match.dl_dst = dstMAC
    msg.match.dl_type = ethernet.IP_TYPE
    msg.match.nw_src = srcIP
    msg.match.nw_dst = dstIP

    msg.actions.append(of.ofp_action_output(port = outgoingPort))

    self.connection.send(msg)

    log.info("Installing %s <-> %s" % (srcIP, dstIP))

  def handle_arp(self,event, packet):
    global table
    global arpTable

    a = packet.find("arp")
    ''' this code would only handle the arp not to proxy. 
        when arp for 
    '''
    if a.opcode == a.REQUEST:
      ipTable[packet.src] = [event.port,a.protosrc]
      arpTable[a.protosrc] = [event.port,a.hwsrc]
  
      r = pkt.arp()
      r.hwtype = a.hwtype
      r.prototype = a.prototype
      r.hwlen = a.hwlen
      r.protolen = a.protolen
      r.opcode = r.REPLY
      r.hwdst = a.hwsrc
      r.protodst = a.protosrc
      r.protosrc = a.protodst
      if a.protodst == PROXY_IP:
        print("%s is ARPing proxy." % (a.protosrc))
        r.hwsrc = PROXY_MAC
        self.handle_request(packet, event, 0, 0 ) # connect them together.
      elif a.hwsrc == PROXY_MAC:
        port , r.hwsrc = arpTable[a.protodst]
      else:
        r.hwsrc = PROXY_MAC # our gateway 
      e = pkt.ethernet(type=packet.type, src=r.hwsrc, dst=a.hwsrc)
      e.payload = r
       
      msg = of.ofp_packet_out()
      msg.data = e.pack()
      msg.actions.append(of.ofp_action_output(port = of.OFPP_IN_PORT))
      msg.in_port = event.port
      event.connection.send(msg)
      
      log.debug("%s ARPed for %s", r.protodst, r.protosrc)
  
  
  def handle_icmp(self, event, packet):

    # Reply false pings
    # Make the ping reply
    icmp = pkt.icmp()
    icmp.type = pkt.TYPE_ECHO_REPLY
    icmp.payload = packet.find("icmp").payload

    # Make the IP packet around it
    ipp = pkt.ipv4(srcip=packet.find("ipv4").dstip,dstip=packet.find("ipv4").srcip)
    ipp.protocol = ipp.ICMP_PROTOCOL
  
    # Ethernet around that...
    e = pkt.ethernet(type=packet.type, src=packet.dst, dst=packet.src)
  
    # Hook them up...
    ipp.payload = icmp
    e.payload = ipp
  
    # Send it back to the input port
    msg = of.ofp_packet_out()
    msg.actions.append(of.ofp_action_output(port = of.OFPP_IN_PORT))
    msg.data = e.pack()
    msg.in_port = event.port
    event.connection.send(msg)
    
  def _handle_PacketIn (self, event):
    packet = event.parsed
    # Learn the source
    dst_port = table.get(packet.dst)
    if packet.find("arp"):
      self.handle_arp(event,packet)
      # Reply to ARP
    if packet.find("icmp"):
      self.handle_icmp(event,packet)

    #if packet.find("udp"):

class QuotaManager(EventMixin):
  
  def __init__ (self,connection):
    self.connection = connection
    self.listenTo(connection)

  def _handle_flowstats_received (self, event):

    '''
    class ofp_flow_stats (ofp_stats_body_base):
  _MIN_LENGTH = 88
  def __init__ (self, **kw):
    self.table_id = 0
    self.match = ofp_match()
    self.duration_sec = 0
    self.duration_nsec = 0
    self.priority = OFP_DEFAULT_PRIORITY
    self.idle_timeout = 0
    self.hard_timeout = 0
    self.cookie = 0
    self.packet_count = 0
    self.byte_count = 0
    self.actions = []
    '''
    #stats = flow_stats_to_list(event.stats)
    #log.debug("FlowStatsReceived from %s: %s", dpidToStr(event.connection.dpid), stats)
    #event.stats.show()
    received = event
    received.show()
    #print(of.ofp_flow_stats.show(event.stats))


    #global src_dpid, dst_dpid, input_pkts, output_pkts
    ##print "src_dpid=", dpidToStr(src_dpid), "dst_dpid=", dpidToStr(dst_dpid)
    #for f in event.stats:
    #  if f.match.dl_type==0x0800 and f.match.nw_dst==IPAddr("192.168.123.2") and f.match.nw_tos==0x64 and event.connection.dpid==src_dpid:
    #    #print "input: ", f.byte_count, f.packet_count
    #    input_pkts = f.packet_count
    #  if f.match.dl_type==0x0800 and f.match.nw_dst==IPAddr("192.168.123.2") and f.match.nw_tos==0x64 and event.connection.dpid==dst_dpid:
    #    #print "output: ", f.byte_count, f.packet_count 
    #    output_pkts = f.packet_count
    #    if input_pkts !=0:
    #      print getTheTime(), "Path Loss Rate =", (input_pkts-output_pkts)*1.0/input_pkts*100, "%"

  def _timer_func (self):
    for connection in core.openflow._connections.values():
      connection.send(of.ofp_stats_request(body=of.ofp_flow_stats_request()))
      #connection.send(of.ofp_stats_request(body=of.ofp_port_stats_request()))
    log.debug("Sent %i flow stats request, refreshing.", len(core.openflow._connections))

  def _handle_ConnectionUp (self, event):
    Timer(5, self._timer_func, recurring=True)
    core.openflow.addListenerByName("FlowStatsReceived", self._handle_flowstats_received) 
    print("timer started")

class Proxy_Service(EventMixin):

  def __init__ (self):
    self.listenTo(core.openflow)

  def _handle_ConnectionUp (self, event):
    log.debug("Connection %s" % event.connection)
    # Put our proxy into the table.
    #print(event.connection)
    ipTable[PROXY_MAC] = [PROXY_PORT,PROXY_IP]
    arpTable[PROXY_IP] = [PROXY_PORT,PROXY_MAC]
    ProxyService(event.connection)
    #QuotaManager(event.connection)

def launch ():
  core.registerNew(Proxy_Service)