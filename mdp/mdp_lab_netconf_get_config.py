
from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="192.168.184.128",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

# Imprimir a running config em XML
netconf_reply = m.get_config(source="running")
print( xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )


# #Filtrar o Output
# netconf_filter = """
# <filter>
#     <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
# </filter>
# """
# netconf_reply = m.get_config(source="running", filter=netconf_filter)
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


