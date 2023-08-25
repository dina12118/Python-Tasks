import requests

# 1.Write a code to suggest automatically activates for you 

url2 = requests.get("https://www.boredapi.com/api/activity")
print(url2.json()['activity'])
print('_________________________')

# 2.Get your public IP

url3 = requests.get("https://api.ipify.org/?format=json")
my_ip = str(url3.json()['ip'])
print(my_ip)
print('_________________________')

# 3.Get your location

url4 = requests.get("https://ipinfo.io/{}/geo".format(my_ip))
print(url4.json())
