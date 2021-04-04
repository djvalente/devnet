
from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="192.168.118.134",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

# The configuration update is always enclosed in a “config” XML element that includes a tree of XML elements that require update. 
# Change Hostname
netconf_data1 = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>NEWHOSTNAME</hostname>
  </native>
</config>
"""

# Create a loopback address

netconf_data2 = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>101</name>
    <description>TEST1</description>
    <ip>
     <address>
      <primary>
       <address>100.100.100.100</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_data2)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
