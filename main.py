import create_scan
import check_status
import time
import download_reports
# Calling create scan function to create scans
#print "calling create_scan function" 
#create_scan.create_scan()

# Waiting for Ten mins to complete the scan
#time.sleep(300)

# Calling the Check status function
#print "calling scan status check function"
#check_status.check_status()

#Calling the download_reports function to download the reports for the successful scans
download_reports.download_reports()
print "All the Scans are completed successfully"
