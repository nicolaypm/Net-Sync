# this function will import sniffer_file from the src directory
import src.sniffer_file
import src.dos.Spaning_tree
import src.vlan.VLAN_Jumping

# this function prints the command that the user can execute
print("""
[*] sniff # this will sniff the traffic over the 2 devices that are targeted
[*] spaning tree # this will make the spaning tree think that it has a better way to the router
[*] vlan jumping # this will let the user sniff the traffic over the odder vlans
      """)

# this function starts the main process
def Start_main():

    # this function will give the user a choice between commands
    User_input = input("Enter the command you want to use >>> ")
    
    # this function will start the sniff process
    if User_input == 'sniff':
        src.sniffer_file.Sniffer()
        # after the sniff process go back to the main process
        Start_main()
        
    # this function will start the dos_spaning_tree process
    elif User_input == 'spaning tree':
        src.dos.Spaning_tree.dos_spaning_tree()
        # after the packet has been sent go back to the main process
        Start_main()
        
    # this function will start the Vlan_jumping process
    elif User_input == 'vlan jumping':
        src.vlan.VLAN_Jumping.Vlan_jumping()
        # after the packet has been sent go back to the main process
        Start_main()
    # if the user inputs something wrong
    else:
        Start_main()

# this function will loop back to the main process
Start_main()