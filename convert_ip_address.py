# Code by @AmirMotefaker

# Convert IP Address
def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address
ipaddress = ip_address("192.168.2.301")
print(ipaddress)
