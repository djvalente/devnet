
from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.118.134",
    port=22,
    username="cisco",
    password="Cisco123!"
)

def get_config():
    print("Sending 'sh ip int brief'.")
    output = sshCli.send_command("show ip int brief")
    print("IP interface status and configuration:\n{}\n".format(output))

def new_interface():
    config_commands = [
        "int loopback 1",
        "ip address 2.2.2.2 255.255.255.0",
        "description WHATEVER"
    ]
    output = sshCli.send_config_set(config_commands)
    print("IP interface status and configuration:\n{}\n".format(output))

get_config()
new_interface()
