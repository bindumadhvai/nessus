import scan_status

def check_status():
   # Opening the file running as reading line by line
   with open('running') as filePointer:
      scanned_targets = filePointer.readline()
      while scanned_targets:
         
         # Removing the ending spaces after reading each line
         scanned_targets = scanned_targets.strip()
         
         # seperating the scan id , targets list and date&time as columns
         scanned_target_list= scanned_targets.split("\t",2)
           
         # Targets list in each line is stored in targets
         targets = scanned_target_list[1]
         
         # splitting targets based on commas into a list
         target_list = targets.split(",",100)
         
         # Getting scan id from sccaned_target_list
         scanid = scanned_target_list[0]
         
         # Sending the scan id to scan_status
         scan_status.scan_status( scanid,target_list,targets )
         
         # Reading next line and iterating if present
         scanned_targets = filePointer.readline()
   
   # Opening running file and deleting the data
   file_pointer = open("running","w+")
   file_pointer.truncate(0)
   file_pointer.close()
