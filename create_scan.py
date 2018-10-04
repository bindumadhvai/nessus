import scan_runner

def create_scan():
  
  # Opening targets file to read the targets line by line
  with open('targets') as filePointer:
      target_id = filePointer.readline()
      while target_id:
         
         # Reamoving the extra spaces at the end of the target_id
         target_id = target_id.strip()
         
         # Sending the target_id to scan_runner to create scan for that id
         scan_runner.scan_runner( target_id )
         
         # Reading the next line of the targets file and iterate if present
         target_id = filePointer.readline()
  
  # Opening the targets file and removing the targets list
  filePointer = open("targets","w+")
  filePointer.truncate(0)
  # Closing the file
  filePointer.close()
