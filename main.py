# this function will import test from the src directory
import src.test

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
        src.test.sniffer()
        # after the sniff process go back to the main process
        Start_main()

# this function will loop back to the main process
Start_main()