# this function will import sniffer_file from the src directory
import src.sniffer_file
import src.create

# this function prints the command that the user can execute
print("""
[*] sniff # this will sniff the traffic over the 2 devices that are targeted
[*] create # this will create a custom packet and send it to the targeted device
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
        
    # this function will start the create process
    elif User_input == 'create':
        src.create.Create_package()
        # after the packet has been sent go back to the main process
        Start_main()
        
    # if the user inputs something wrong
    else:
        Start_main()

# this function will loop back to the main process
Start_main()