#!//usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp


form=cgi.FieldStorage()
cmd=form.getvalue("x")

x=(cmd.lower())
print("HERE'S YOUR RESULT......")
print()

	
if "date" in x:
	date=sp.getoutput("date")
	print(date)
elif "time" in x:
	a=sp.getoutput(" date +%r")
	print(a)
elif "calender" in x:
	cal=sp.getoutput(" cal")
	print(cal)
elif ("ip" in x) or (" ip address" in x):
	a=sp.getoutput("ifconfig")
	print(a)
elif ("active ports" in x) or ("ports" in x):
	a=sp.getoutput(" netstat -tnlp")
	print(a)
elif ("space" in x) or ("disc" in x) or ("hard disk" in x) or ("amount" in x):
	a=sp.getoutput(" df -h")
	print(a)
elif ("webserver" in x) or ("status" in x) or ("server" in x) or ("apache" in x):
	a=sp.getoutput( "systemctl status httpd")
	print(a)
elif ("selinux" in x):
	a=sp.getoutput("getenforce")
	print(a)
elif ("yum" in x) or ("list" in x) or ("module" in x):
	a=sp.getoutput("yum module list")
	print(a)
elif ("package" in x) or ("firefox" in x):
	a=sp.getoutput("sudo yum whatprovides firefox")
	print(a)
elif ("ping" in x) or ("google" in x):
	a=sp.getoutput("sudo ping www.google.com")
	print(a)
elif (("check" in x) or ("verify" in x)) and ("docker" in x):
	a=sp.getoutput("sudo rpm -q docker-ce")
	print(a)
elif (("install" in x) or ("download" in x) or ("configure" in x)) and ("docker" in x):
	a=sp.getoutput("sudo yum install docker-ce --nobest -y") 
	print(a)
elif (("start" in x) or ("launch" in x)) and ("docker" in x):
	a=sp.getoutput("sudo systemctl start docker")
	print(a)
elif (("list" in x) or ("how many" in x) or ("show" in x)) and ("docker containers" in x):
	a=sp.getoutput("sudo docker ps")
	print(a)
elif (("list" in x) or ("how many" in x) or ("show" in x)) and ("docker images" in x):
	a=sp.getoutput("sudo docker images")
	print(a)
elif (("list" in x) or ("how many" in x) ("show" in x)) and (("file" in x) or ("folder" in x)):
	a=sp.getoutput("sudols")
	print(a)
elif (("check" in x) or ("verify" in x)) and (("jdk" in x) or ("java" in x)):
	a=sp.getoutput("sudo rpm -q jdk1.8")
	print(a)
elif (("check" in x) or ("verify" in x)) and ("hadoop" in x):
	a=sp.getoutput("sudo rpm -q hadoop")
	print(a)
elif (("setup" in x) or ("install" in x) or ("download" in x) or ("configure" in x)) and (("java" in x) or ("jdk")):
	a=sp.getoutput("sudo rpm -ivh jdk-8u171-linux-x64.rpm")
	print(a)
elif (("setup" in x) or ("install" in x) or ("download" in x) or ("configure" in x)) and ("hadoop"):
	a=sp.getoutput("sudo rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
	print(a)
elif ("create" in x) and (("directory" in x) or ("folder" in x)):
	a=sp.getoutput("sudo mkdir"+fold)
	print(a)
elif ("download" in x) or ("install" in x) or ("ping3" in x):
	a=sp.getoutput("sudo yum install ping3 -y")
	print(a)
elif ("create" in x) or ("file" in x):
	a=sp.getoutput("sudo touch file1")
	print(a)
else:
	print("please elaborate your statement...")

	
