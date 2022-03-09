import ipaddress

print(ipaddress.ip_address(u'192.168.0.255'))
# print(ipaddress.ip_address(u'192.168.0.256'))

print (ipaddress.ip_address(u'FFFF:9999:2:FDE:257:0:2FAE:112D'))
#invalid IPV6 address
# print (ipaddress.ip_address(u'FFFF:10000:2:FDE:257:0:2FAE:112D'))

print(type(ipaddress.ip_address(u'192.168.0.255')))
print(type(ipaddress.ip_address(u'2001:db8::')))

print(ipaddress.ip_address(u'192.168.0.255').reverse_pointer)

print(ipaddress.ip_network(u'192.168.0.0/28'))

# add or subtract
print (ipaddress.IPv4Address(u'192.168.0.2')+1)

print (ipaddress.IPv4Address(u'192.168.0.253')-3)

# Increases the previous octet by value 1.
print (ipaddress.IPv4Address(u'192.168.10.253')+3)

# Throws Value error
# print (ipaddress.IPv4Address(u'255.255.255.255')+1)