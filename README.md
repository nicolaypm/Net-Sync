# Net-Sync

Net-Sync is an open-source network testing tool for ethical hacking. 

- Net-Sync is based on Scapy.  
- Sniff and collect packets over a network. 
- DOS spaning tree via Net-Sync.
- VLAN Jumping via Net-Sync.
- And meny more.

## Install Net-Sync

first we need to install scapy and to do this manually use the following command
```bash
pip install scapy
```

to clone the repository we need to use the following command
```bash
git clone https://github.com/nicolaypm/Net-Sync.git
```

cd to the directory Net-Sync
```bash
cd Net-Sync
```

start the program alle we need to do is run the following command
```bash
sudo python3 main.py
```
## Usage
- to sniff and collect packets over a network. we to Enter the sniff option and then specify how many packets we want to collect.
- DOS Spaning Tree, we need to Enter the Spaning Tree option and then specify the MAC address of the Spaning Tree
- VLAN Jumping, this will let the attacker see the traffic over odder VLANs. 
## Contributing
Pull requsts are welcome. For major changes, please open issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Code
**main.py**
![main]!(https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&t=seti&wt=none&l=python&width=680&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=2x&wm=false&code=%2523%2520this%2520function%2520will%2520import%2520sniffer_file%2520from%2520the%2520src%2520directory%250Aimport%2520src.sniffer_file%250Aimport%2520src.dos.Spaning_tree%250Aimport%2520src.vlan.VLAN_Jumping%250A%250A%2523%2520this%2520function%2520prints%2520the%2520command%2520that%2520the%2520user%2520can%2520execute%250Aprint%28%2522%2522%2522%250A%255B*%255D%2520sniff%2520%2523%2520this%2520will%2520sniff%2520the%2520traffic%2520over%2520the%25202%2520devices%2520that%2520are%2520targeted%250A%255B*%255D%2520spaning%2520tree%2520%2523%2520this%2520will%2520make%2520the%2520spaning%2520tree%2520think%2520that%2520it%2520has%2520a%2520better%2520way%2520to%2520the%2520router%250A%255B*%255D%2520vlan%2520jumping%2520%2523%2520this%2520will%2520let%2520the%2520user%2520sniff%2520the%2520traffic%2520over%2520the%2520odder%2520vlans%250A%2520%2520%2520%2520%2520%2520%2522%2522%2522%29%250A%250A%2523%2520this%2520function%2520starts%2520the%2520main%2520process%250Adef%2520Start_main%28%29%253A%250A%250A%2520%2520%2520%2520%2523%2520this%2520function%2520will%2520give%2520the%2520user%2520a%2520choice%2520between%2520commands%250A%2520%2520%2520%2520User_input%2520%253D%2520input%28%2522Enter%2520the%2520command%2520you%2520want%2520to%2520use%2520%253E%253E%253E%2520%2522%29%250A%2520%2520%2520%2520%250A%2520%2520%2520%2520%2523%2520this%2520function%2520will%2520start%2520the%2520sniff%2520process%250A%2520%2520%2520%2520if%2520User_input%2520%253D%253D%2520%27sniff%27%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520src.sniffer_file.Sniffer%28%29%250A%2520%2520%2520%2520%2520%2520%2520%2520%2523%2520after%2520the%2520sniff%2520process%2520go%2520back%2520to%2520the%2520main%2520process%250A%2520%2520%2520%2520%2520%2520%2520%2520Start_main%28%29%250A%2520%2520%2520%2520%2520%2520%2520%2520%250A%2520%2520%2520%2520%2523%2520this%2520function%2520will%2520start%2520the%2520dos_spaning_tree%2520process%250A%2520%2520%2520%2520elif%2520User_input%2520%253D%253D%2520%27spaning%2520tree%27%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520src.dos.Spaning_tree.dos_spaning_tree%28%29%250A%2520%2520%2520%2520%2520%2520%2520%2520%2523%2520after%2520the%2520packet%2520has%2520been%2520sent%2520go%2520back%2520to%2520the%2520main%2520process%250A%2520%2520%2520%2520%2520%2520%2520%2520Start_main%28%29%250A%2520%2520%2520%2520%2520%2520%2520%2520%250A%2520%2520%2520%2520%2523%2520this%2520function%2520will%2520start%2520the%2520Vlan_jumping%2520process%250A%2520%2520%2520%2520elif%2520User_input%2520%253D%253D%2520%27vlan%2520jumping%27%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520src.vlan.VLAN_Jumping.Vlan_jumping%28%29%250A%2520%2520%2520%2520%2520%2520%2520%2520%2523%2520after%2520the%2520packet%2520has%2520been%2520sent%2520go%2520back%2520to%2520the%2520main%2520process%250A%2520%2520%2520%2520%2520%2520%2520%2520Start_main%28%29%250A%2520%2520%2520%2520%2523%2520if%2520the%2520user%2520inputs%2520something%2520wrong%250A%2520%2520%2520%2520else%253A%250A%2520%2520%2520%2520%2520%2520%2520%2520Start_main%28%29%250A%250A%2523%2520this%2520function%2520will%2520loop%2520back%2520to%2520the%2520main%2520process%250AStart_main%28%29)
## License
thenerds.xyz
