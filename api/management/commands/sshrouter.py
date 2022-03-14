from django.core.management.base import BaseCommand, CommandError
from netmiko import ConnectHandler

class Command(BaseCommand):
    help = 'SSH to the server Run a command(ls) on the server and save its output to an external text file'

    def handle(self, *args, **options):
        print("run command")
        systemUsername = "shraddha" # your system username
        systemPassword = "1234567"  # your system passowrd
        cisco_260 = {'device_type': "linux",'ip':'127.0.0.1', 'username': systemUsername, 'password': systemPassword}
        net_connect = ConnectHandler(**cisco_260)
        output = net_connect.send_command("ls")
        #here your can change file name and file path to store any specific location
        f = open("store-cmd-output.txt", "w")
        f.write(output)
        f.close()
        net_connect.disconnect()
        print(output)
