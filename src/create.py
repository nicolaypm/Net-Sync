# This function import scapy so that we can create a package
from scapy.all import *

# This function organizes the code so that we can search for commands more easily
def Create_package():
    # This function will let the user specify the src IP address
    User_input_src = input('Enter the IP address of the SRC >>> ')
    # This function will let the user specify the dst IP address
    User_input_dst = input('Enter the IP address of the DST >>> ')
    
    # This function will let the program use the IP command
    ip = scapy.IP()
    
    # This function will let the program know that IP src is ecualled to User_input_src
    ip.src = User_input_src
    # This function will let the program know that IP dst is ecualled to User_input_dst
    ip.dst = User_input_dst
    
    # This function sends the package that we have just created
    send(ip.summary)
    