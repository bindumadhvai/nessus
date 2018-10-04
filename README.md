Prerequisites:
     Install Nessus on your local machine and start the service.
     Browse https://localhost:8834/ and create a user with all the privilages as admin.

Create Keys:
      To create scans from API we need access_key and secret_key which are generated in the UI itself.
      To generate API keys:
          1) Go to setting -> users 
          2) Click on admin privilaged user
          3) Go to API keys and click on Generate
      NOTE: copy the keys and store them safely.

Create keys file:
      Create a file called keys in the same folder and copy the access_key and sceret_key 
      First line should contain access_key 
      second line should contain secret_key

Create Policy:
      Create a custom policy with all the required features and also give the admin credentials of the target machines while creating a policy itself. Note down the policy details like policy_id & uuid so that they can be used in the further steps.
      To get policy_id & uuid(tmplate_uuid) you can use this command :
         -> curl -H "X-ApiKeys: accessKey=access_key; secretKey=secret_key" -k https://localhost:8834/policies

Create Target file
       Create a file named targets in which give ur targets to be scanned.
       Give comma seperated target ip's which should be created as one scan or give the targets each one in seperate line to create seperate scan for each one of them.

To Create Scan:
      To Creat a scan we need 
           1) Keys - access and secret key
           2) policy id and uuid (template_uuid)
           3) folder_id - Folders are nothing but MyScans , AllScans and  Trash. Deafult folder_id for MyScans is '3'
			  check for the folders in the UI or to get the folder data in cli try this command 
                                curl -H "X-ApiKeys: accessKey=access_key; secretKey=secret_key" -k https://localhost:8834/folders
           4) scanner_id - Scanner is agent which is used for scanning.
                           we can get the scanner id from the UI or if you want the scanner data through cli try this command                                          curl -H "X-ApiKeys: accessKey=access_key; secretKey=secret_key" -k https://localhost:8834/scanners
           5) targets
                  
           NOTE : Replace your scanner_id , policy_id , folder_id in scan_runner.py

All the scanid's , target list and date&time of creation of scan are stored in a file called running and targets file will be truncated

To get Scan Status: 
       To get status of the created scans we need 
           1) username - username with admin privilages
           2) password - password of that user
           3) Create a file called credentials and place this line in that {"username":"username","password":"password"} 
           
Scan_status.py will check the scan status for each and every entry in the file called running using scan_id and later running file will be truncated.

NOTE : Successful targets will be placed in successful_targets file and failed targets will be placed in targets file so we can again create or scedule a scan for those targets.
