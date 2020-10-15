#users/updateIP.py
import requests
import json

def addIP(newIP, username, password):
    link = "https://blazingseollc.com/proxy/dashboard/api/ips/add/"+username+'@yopmail.com/'+password + "/" + newIP
    x = requests.get(link)
    print(x.text)
    return


def removeIP(IP, username, password):
    link = "https://blazingseollc.com/proxy/dashboard/api/ips/delete/" + username + '@yopmail.com/' + password + "/" + IP
    x = requests.get(link)
    print(x.text)
    return
