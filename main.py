import create_scan
import check_status
import time

# Calling create scan function to create scans 
create_scan.create_scan()

# Waiting for Ten mins to complete the scan
time.sleep(600)

# Calling the Check status function
check_status.check_status()
print "All the Scans are completed successfully"
