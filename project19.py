# Python script to download and install Splunk Enterprise on Linux(Bash to python converter)
import os
import subprocess
import time

def download_splunk():
    """
    Download the Splunk Enterprise tar file
    """
    print("Download the Splunk Enterprise tar file")
    os.system("sudo rm -rf /opt/splunk*")
    os.chdir("/opt")
    os.system("sudo wget -O splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz https://download.splunk.com/products/splunk/releases/9.0.4.1/linux/splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz")

def extract_splunk():
    """
    Extract the tar file to /opt
    """
    print("Extract the tar file to /opt")
    os.system("sudo tar -zxvf splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz -C /opt")
    os.chdir("/opt/splunk/bin/")

def start_splunk():
    """
    Start Splunk Enterprise and set up the admin user and password
    """
    print("Start Splunk Enterprise and set up the admin user and password")
    os.system("sudo ./splunk start --accept-license --answer-yes --no-prompt --seed-passwd abcd1234")

def enable_boot_start():
    """
    Enable Splunk at the startup
    """
    print("Enable Splunk at the startup")
    os.system("sudo ./splunk enable boot-start")

def main():
    download_splunk()
    extract_splunk()
    start_splunk()
    enable_boot_start()
    print("Please go on the browser, access Splunk on port 8000, username: admin, password: abcd1234")
    time.sleep(4)

if __name__ == "__main__":
    main()



