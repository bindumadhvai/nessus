import urllib3
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time
from nessus import API
import os
from shutil import copyfile

def scan_status( scanid,target_list,targets ):
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
  print scanid
  success = open("successful_targets","a+")
  success_id = open("successful_id","a+")
  failed = open("targets","a+")

  tokenurl = "https://172.16.7.20:8834/session"
  Headers = {
             'Content-Type': 'application/json'
  }

  credentials_file = open("credentials","r")  
  Data =  credentials_file.readline().strip() 
  token = requests.post(tokenurl,verify=False,headers=Headers,data=Data)
  token=token.json()
  scanurl = "https://localhost:8834/scans/" + str(scanid)      
  headers = {
        'X-Cookie': "token="+token["token"]
  }
  results = requests.get(scanurl,verify=False,headers=headers)
  results=results.json()
  if len(results['hosts'])>0: 
       if len(target_list) == len(results["hosts"]):
             success.write(str(targets)+"\n")
             success_id.write(scanid+"\n")
       else: 
          id_count= "false"
          for ip in target_list:
              flag = "false"
              for count in range(len(results["hosts"])):
                  if str(ip) == str(results["hosts"][count]):
                       flag = "true"
              if flag == "true":
                  print "scan is success for " + str(ip)
                  success.write(str(ip)+",")
                  if id_count == "false":
                      success_id.write(scanid+"\n")
                      id_count = "true"
              else:
                  print "scan is failed for " + str(ip)
                  failed.write(str(ip)+",")
  else :
     failed.write(str(targets)+"\n")
