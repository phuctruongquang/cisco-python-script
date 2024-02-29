from netmiko import ConnectHandler
import datetime

#Path to file -> ip_list.txt
f = open("C:\\Users\\QuangPhuc\\PythonBackupCisco\\ip_list.txt", "r")
iplist = f.read().split("\n")
print(iplist)

deviceList = []

for ip in iplist:
    SW = {
     "device_type" : "cisco_s300",
     "ip" : ip,
     "username" : "admin",
     "password" : "@bcd1235!"
    }
    deviceList.append(SW)

for device in deviceList:
    try :
     #SSH to device
     net_conncet = ConnectHandler(**device)
     #Get running config
     config = net_conncet.send_command("show run")
     #Get file name
     hostname = net_conncet.send_command("show run | include hostname").split(" ")[1]
     today = str(datetime.date.today())
     fileName = hostname + "_" + today
     #Write config to file
     f = open("C:\\Users\\QuangPhuc\\PythonBackupCisco\\" + fileName,"w", encoding="utf-8")
     f.write(config)
     f.close()
     #Write log
     f = open("C:\\Users\\QuangPhuc\\PythonBackupCisco\\backup.log", "a")
     f.write("Successfully backup configuration of device " + device["ip"] + " at " + str(datetime.datetime.now()) + "\n")
     f.close()
    except :
     #Write log
     f = open("C:\\Users\\QuangPhuc\\PythonBackupCisco\\backup.log", "a")
     f.write("The is a problem with device " + device["ip"] + " at " + str(datetime.datetime.now()) + "\n")
     f.close()