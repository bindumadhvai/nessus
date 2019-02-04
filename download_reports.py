import urllib3
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time
from nessus import API

def download_reports():
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


  # Reading access_key and secret_key from a file called keys.
  keys = open("keys","r")
  Access_key = keys.readline()
  Secret_key = keys.readline()

  keys.close()

  # Removing the spaces at the end using strip function.
  Access_key =  Access_key.strip()
  Secret_key =  Secret_key.strip()
  
# Headers used for the requests 
  Headers = {
           'Content-Type': 'application/json',
           'X-ApiKeys': "accessKey=" + Access_key + "; secretKey=" + Secret_key
  }
  
# Reading the id's of success scanned id's line by line and downloading the report
# Opening the file called success to read id's
  with open('successful_id') as filepointer:
    scanned_id_line = filepointer.readline()
    while scanned_id_line:
       
       # Removing trailing spaces and spliting the row contents into columns 
       scanned_id_line = scanned_id_line.strip()
       scanned_id= scanned_id_line.split("\t",1)
       scanid= scanned_id[0]
       
       # Exporting the scanid and checking whether their is any file existed or not
       scanurl = "https://x.x.x.x:8834/scans/" + str(scanid) + "/export"
       print scanid
       scanpld = '{"format":"nessus"}'
       results = requests.post(scanurl,verify=False,headers=Headers,data=scanpld)
       results=results.json()
       
       # Checking for the file exsistence 
       if 'file' not in results: 
           print "not a valid id"
       if 'file' in results:
          # If file is existed , check for the status of the file.
          scanreq = json.loads(json.dumps(results, indent=2, sort_keys=True))
          filestat = requests.get(scanurl +"/"+ str(scanreq["file"]) + "/status", verify=False, headers=Headers, data=json.dumps(scanreq["token"]))
          filestat = filestat.json()
          count = 0
          
          # If file status is loading then we need to wait till the file status return ready as it's state .This loop will wait for 20 mins to get the file state ready and checks the status for every 3 seconds
          while filestat['status'] == 'loading':
                  print "Your report is being prepared  " + str(count) + "/400"
                  # Waiting for 3 seconds and checking for the file status again
                  time.sleep(3)
                  filestat = requests.get(scanurl+"/" + str(scanreq["file"]) + "/status",verify=False, headers=Headers, data=json.dumps(scanreq["token"]))
                  filestat = filestat.json()
                  # Increasing the count so that it helps in counting the time of waiting
                  count +=1  
                   
                  # If count > 400 that means waited for 20 mins to get the file status as ready but still it is not.
                  if count > 400:
                      print "Your file has not been prepared after 20 minutes. Please try again"
                      break
                  continue
          
          # If file status is ready it is indicating that file is ready for the download 
          if filestat['status'] == 'ready':
              print str(scanid)+" -  sucess"
              # Requesting for the file content
              download_result=requests.get(scanurl +"/"+ str(scanreq["file"]) + "/download", verify=False, headers=Headers, data=json.dumps(scanreq["token"]),allow_redirects=True)
              # OPening the file with the scanid name and writing the content of the request into that.
              open(scanid,'w+').write(download_result.content)
       # Reading the next line of the success file to repeat the process.
       scanned_id_line=filepointer.readline()
  
  file_pointer = open("successful_id","w+")
  file_pointer.truncate(0)
  file_pointer.close()

