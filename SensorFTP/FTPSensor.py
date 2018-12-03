import ftplib
from time import time

FTP_HOST = "10.100.79.162"
FTP_USERNAME = "jllpz"
FTP_PASSWORD = "cieloandrea1"

ftp = None

def doSubScanning(ftp, dir_path):
    print(dir_path)
    ftp.cwd(dir_path)
    subdirectory_content = ftp.nlst()
    files = len(subdirectory_content)
    file_number = 0

    if (files > 0):
        for directory in subdirectory_content:
            print("Scanning directory/file: " + directory)
            if "." not in directory:
                file_number = file_number + doSubScanning(ftp, dir_path + "/" + directory + "/")
            else:
                file_number = file_number + 1
    return file_number


def doServerScanning(ftp):
    root_directory_content = ftp.nlst()
    file_number = 0

    print("Scanning: Server Root Directory")
    for directory in root_directory_content:
        print("Scanning directory/file: " + directory)
        if "." not in directory:
            file_number = file_number + doSubScanning(ftp, "/" + directory + "/")
        else:
            file_number = file_number + 1
    return  file_number


if __name__ == '__main__':
    start = time()
    # Connect to host, default port
    ftp = ftplib.FTP(FTP_HOST)

    # Do login
    ftp.login(FTP_USERNAME, FTP_PASSWORD)

    # Get welcome message from server
    print(ftp.getwelcome())
    end = time()

    print("FTP response time: (%.2f seconds)", (end-start))

    # Doing Sensor FTP Server File Count
    print(doServerScanning(ftp))

    # Quitting FTP Server Connection
    ftp.quit()
