# Import Module
import ftplib 
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'File transfer to the server(FTP)'

    def handle(self, *args, **options):
        print("run command")
        # Fill Required Information
        HOSTNAME = "ftp.dlptest.com" 
        USERNAME = "dlpuser@dlptest.com"
        PASSWORD = "eUj8GeW55SvYaswqUyDSm5v6N"
        # Connect FTP Server
        ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

        # force UTF-8 encoding
        ftp_server.encoding = "utf-8"
        
        # Enter File Name with Extension
        filename = "store-cmd-output.txt"
        
        ftp_server.storbinary(f"STOR {filename}", filename)

        # Read file in binary mode
        # with open(filename, "r") as file:
            # Command for Uploading the file "STOR filename"
            # ftp_server.storbinary(f"STOR {filename}", file)
        
        # Get list of files
        ftp_server.dir()
        
        # Close the Connection
        ftp_server.quit()

