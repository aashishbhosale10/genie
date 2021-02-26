from genie.conf import Genie
import csv

testbed = Genie.init("testbed.yaml")

for device in testbed.devices:
        device = testbed.devices[device]
        #print(device) # will print the device type

device.connect()
Version = device.parse("show version")
print(Version) #provide dictionary for sh version output
#print(Version["version"]["version"]) # will provide the version details for the router
#print(Version["version"]["uptime"]) # will provide details of device uptime

Alpha = "Version.csv"
Header = ["device","Version","uptime"]

with open(Alpha,"w") as f:
        writer = csv.DictWriter(f,Header)
        writer.writeheader()

        for Version, version in Version.items():
                writer.writerow({"device": device.hostname,
                                 "Version": version["version"],
                                 "uptime" : version["uptime"]})

device.disconnect()
