#34:f6:4b:35:97:b5
import optparse
import subprocess
import re
import time
def ifconfig():
	ifconfig_results=subprocess.check_output(["ifconfig",opt.interface])
	mac_address_controller=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_results)
	if mac_address_controller:
		print "Old MAC => " , mac_address_controller.group(0)
	else:
		print "[-] Program can't read MAC "
def main(interface,new_mac):
	print "[+] " + interface + "'s MAC adress is cahanging to " + new_mac 
	subprocess.call(["ifconfig" , interface , "down"])
	subprocess.call(["ifconfig" , interface , "hw" , "ether" ,new_mac])
	subprocess.call(["ifconfig" , interface , "up"])
	subprocess.call(["ifconfig" , interface])

p=optparse.OptionParser()
p.add_option("-i","--interface", dest="interface", help="Type Interface")
p.add_option("-m","--mac", dest="new_mac", help="Type Your New MAC Address")
(opt,arg)=p.parse_args()
ifconfig()
time.sleep(5)
main(opt.interface,opt.new_mac)
