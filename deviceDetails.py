#!/usr/local/bin/python

#import requests
import math


body = "<?xml version=\"1.0\" encoding=\"utf-8\"?> \
<soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\"> \
  <soap:Body> \
    <GetAllItemInfo xmlns=\"http://webservices.airista.com/XpertTracker\"> \
      <Username>admin</Username> \
      <Password>admin</Password> \
      <ItemList>18</ItemList> \
    </GetAllItemInfo> \
  </soap:Body> \
</soap:Envelope>"

url = "http://10.127.25.169/uvs/xws/xperttrackerwebservice/xperttrackerwebservice.asmx?op=GetAllItemInfo"

headers = {'content-type': 'text/xml'}

#response = requests.post(url,data=body,headers=headers)

'''print response.content
print dir(response)
print response
'''

print dir(math)