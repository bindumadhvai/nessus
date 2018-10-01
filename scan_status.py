import urllib3
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time
from nessus import API
import os
from shutil import copyfile

def scan_status():
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
  success = open("successful_targets","a+")
  failed = open("targets","a+")

  tokenurl = "https://172.16.7.20:8834/session"
  Headers = {
             'Content-Type': 'application/json'
  }

  Data = '{"username":"admin","password":"admin"}'
  token = requests.post(tokenurl,verify=False,headers=Headers,data=Data)
  token=token.json()

  with open('running') as file_pointer:
      scanned_targets = file_pointer.readline()
      while scanned_targets:
       
         scanned_targets = scanned_targets.strip()
         scanned_target_list= scanned_targets.split("\t",2)
         targets = scanned_target_list[1]
         target_list = targets.split(",",100)
         scanid = scanned_target_list[0]
         print scanid
         scanurl = "https://localhost:8834/scans/" + str(scanid)      
         headers = {
             'X-Cookie': "token="+token["token"]
         }
         results = requests.get(scanurl,verify=False,headers=headers)
         results=results.json()
         if len(results['hosts'])>0: 
             if len(target_list) == len(results["hosts"]):
                success.write(str(targets)+"\n")
             else: 
                for ip in target_list:
                    flag = "false"
                    for count in range(len(results["hosts"])):
                        if str(ip) == str(results["hosts"][count]):
                            flag = "true"
                    if flag == "true":
                        success.write(str(ip)+",")
                    else:
                        failed.write(str(ip)+",")
         else :
             failed.write(str(targets)+"\n")
         scanned_targets = file_pointer.readline()
  
  file_pointer = open("running","w+")
  file_pointer.truncate(0)
  file_pointer.close()
