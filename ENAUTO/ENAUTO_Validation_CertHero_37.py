
from ncclient import manager
import xml.dom.minidom
import xmltodict

m = manager.connect(
    host="192.168.184.128",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

netconf_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet1</name>
        </interface>
    </interfaces>
     <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet1</name>
        </interface>
    </interfaces-state>
</filter>
"""

# netconf_reply = m.get_config(source="running", filter=netconf_filter)
netconf_reply = m.get(netconf_filter)

intf_details = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
intf_config = intf_details["interfaces"]["interface"]
intf_info = intf_details["interfaces-state"]["interface"]

print("")
print("Interface Details: ")
print(" Name: {}".format(intf_info["name"]))
# print(" Name: {}".format(intf_info["name"]["#text"]))
print(" Description: {}".format(intf_config["description"]))
print(" Type: {}".format(intf_config["type"]["#text"]))
print(" MAC Address: {}".format(intf_info["phys-address"]))
print(" Packet Input: {}".format(intf_info["statistics"]["in-unicast-pkts"]))
print(" Packet Output: {}".format(intf_info["statistics"]["out-unicast-pkts"]))
