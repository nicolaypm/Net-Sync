# This function import scapy so that we can use the sniff command
from scapy.all import *

# This function organizes the code so that we can search for commands more easily
def Sniffer():
    # This function gives the user a choice of how many times he or she likes to sniff
    User_input = int(input('Enter how many times you want to sniff, infinite enter 0 >>> '))
    # This function sniffs all the packages that are available over the network
    Packet_sniffer = sniff(count = User_input)
    # This function will print out all the packages that are available over the network
    print(Packet_sniffer)