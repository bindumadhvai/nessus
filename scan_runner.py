import urllib3
import requests,json
from nessus import API
import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def scan_runner( target ):
  print "running scan_runner"
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

  # Opening a file called Running to store the details of created scans.
  running_scans = open("running","a+")

  # Nessus url .
  url = "https://localhost:8834/scans"

  # Reading access_key and secret_key from a file called keys.
  keys = open("keys","r")
  Access_key = keys.readline()
  Secret_key = keys.readline()

  keys.close()
  
  # Removing the spaces at the end using strip function.
  Access_key =  Access_key.strip()
  Secret_key =  Secret_key.strip()
   
  now = datetime.datetime.now()
     
  target_id = target
      
  # my_data consists of neccessary data required to create a scan and scan is created with the name as ip address.
  my_data = '{"uuid":"ad629e16-03b6-8c1d-cef6-ef8c9dd3c658d24bd260ef5f9e66","settings":{"name":"'+target_id+'","description":"'+target_id+'","emails":"null","enabled":"true","launch":"ONETIME","launch_now":"true","folder_id":3,"policy_id":200,"scanner_id":1,"text_targets":"'+target_id+'"}}'
        
  Headers = {
              'Content-Type': 'application/json',
              'X-ApiKeys': "accessKey=" + Access_key + "; secretKey=" + Secret_key
  }
      
  response = requests.post(url,verify=False,headers=Headers,data=my_data)
        
# Converting the response data into json
  result = response.json()
  print "created and launched scan for "+ target_id
  time = str(now)
      
# Storing the scan id , ip address and time stamp in the file called running
  running_scans.write(str(result['scan']['id'])+"\t"+target_id+"\t"+time+"\n")
  return 
