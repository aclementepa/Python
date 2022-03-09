import dns.resolver

# finnding 'A' Record
result = dns.resolver.query('tutorialspoint.com', 'A')
for ipval in result:
    print('IP', ipval.to_text())

# finding cname value
result = dns.resolver.query('mail.google.com', 'CNAME')
for cnameval in result:
    print('cname target address: ', cnameval.target)

# finding mx record
result = dns.resolver.query('google.com', 'MX')
for exdata in result:
    print('MX Record: ', exdata.exchange)