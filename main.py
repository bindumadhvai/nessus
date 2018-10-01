import scan_runner
import scan_status
import os
import time
#import targets

while os.stat("targets").st_size != 0:
    scan_runner.scan_runner()
    print "created scans"
    time.sleep(600)
    filePointer = open("targets","w+")
    filePointer.truncate(0)
    # Closing the file
    filePointer.close()
    print "checking status for created scans"
    scan_status.scan_status()
print "All the Scans are completed successfully"
