import json
import netmiko

dev = netmiko.ConnectHandler(device)
out = dev.send_command("show run")
print(json.dumps(out))
