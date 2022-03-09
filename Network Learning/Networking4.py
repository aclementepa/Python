import requests as req

r = req.get('http://www.tutorialspoint.com/python/')
print(r.text)[0:300]