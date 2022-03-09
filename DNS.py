import sys
import dns
from dns import resolver

host = sys.argv[1]

result = dns.resolver.query(host, 'A')
for ipval in result:
    print('IP', ipval.to_text())