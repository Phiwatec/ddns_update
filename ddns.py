
import requests
ipUrl='http://checkip.dyndns.com/'
url='YourUpdateURL'
# See DynDNS v2 protocol by dyndns.org
resp=requests.get(ipUrl).text
resp=resp.split(':')
resp=resp[1]
resp=resp.split('<')
resp=resp[0]
ip=resp[1:]
print('Your IP is: '+ip)

r = requests.get(url+ip)
print('Response from DynDNS Service')
print(r.text)
