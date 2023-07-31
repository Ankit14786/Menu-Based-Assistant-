#--------------------------------------Main Program Started -----------------------------------------------------------------------------------#
import os
import time
import getpass

for Set_P in "pass":
	os.system("tput bold")
	os.system("tput setaf 5")
	keylog=getpass.getpass("\t Enter your Credentials : ")
	if keylog == "Test1234":
		time.sleep(2)
		print("***********************************")
		print(" Lets Explore the Features ......")
		print("#----------------------------------------#")
	else:	
		os.system("tput setaf 9")
		print("#---------Please Enter Correct Credentinals to continue----------#")
		os.system("tput sgr0")
		continue
	while True:
		os.system("clear")
		os.system("tput sgr0")
		os.system("tput bold 0")
		os.system("tput smso 0")
		os.system("tput setaf 0")
		print("\t\t\t1. Containerization.......") 
		os.system("tput sgr0")
		os.system("tput bold 2")
		os.system("tput smso 2")
		os.system("tput setaf 2")
		print("\t\t\t2. Linux and Storage Setup ....")
		os.system("tput sgr0")
		os.system("tput bold 3")
		os.system("tput smso 3")
		os.system("tput setaf 3")
		print("\t\t\t3. Web Environment setup .......")
		os.system("tput sgr0")
		os.system("tput bold 6")	
		os.system("tput smso 6")
		os.system("tput setaf 6")
		
		print("\t\t\t4. exit .....See You Later .....")
		
		os.system("tput sgr0")
		os.system("tput bold ")
		os.system("tput setaf 27")
		i=input("\n Enter Your Requirements:- ")
		os.system("tput sgr0 ")
		
		
		if int(i)=="1":
			Containerization() 
		elif i=="2":
			Linux_As_Assistent()
		elif i=="3":
			Web_Environment_setup()
		elif i=="4":
			exit()
		else:
			os.system("tput sgr0")
			os.system("tput bold")
			os.system("tput setaf 9")
			print('\n\n\t\t\tPlease select valid choice number .......')
			input("\n\t\t\tPress ENTER to go to main menu ")

#-----------------------------------------Module Deployed -----------------------------------------#

def Linux_As_Assistent():

	import os
	import time
	os.system("clear")
	os.system("tput smso 5")
	os.system("tput bold 4")
	os.system("tput setaf 4")
	print("\n\n\t\t\t  Welcome to Linux Assistent menu ....Please enter your choice  ")
	os.system("tput sgr 0 ")
		
	while True:

		os.system("tput setaf 3")
		print("\n1.Press 1 : Run Commands and print output ")
		print("2.Press 2 :   Apply Partition of your choice ")
		print("3.Press 3 :  LVM Support ")
		print("4.Press 4 :  Mounted disk details")
		print("5.Press 5 : List of VG's")
		print("6.Press 6 : Yum Initial Setup ")
		print("7.Press 7 : Go to main menu")
		print("8.Press 8 : Quit")

		os.system("tput setaf 5")
		a=input("\nEnter your input :  ")

		if a=="1":
			while True:
				os.system("tput setaf 6")
				command=input("\nGive me a command to execute  : ")
				os.system("tput setaf 7")
				os.system(command)
				os.system("tput setaf 2")
				#command=input("\nDo you want to run more command Y/N:- ")
				if (command=="exit"): 
					break
	
		elif a=="2":
			os.system("tput setaf 7")
			os.system("fdisk -l")
			os.system("tput setaf 3")
			b=input("\tPlease enter details : disk name : ")
			os.system("fdisk {}".format(b))
			time.sleep(2)
		
			os.system("tput setaf 3")
			print("\n\n Change inode table or Format the selected partition ")
			os.system("mkfs.ext4 {}".format(b))
			os.system("tput setaf 2")
			print("Mission Accomplished : Successfully Triggered ")
			time.sleep(2)

			os.system("tput setaf 3")	
			d=input("\n\n Mounting : Create a folder to link :-")
			os.system("mkdir /{}".format(d))
			os.system("tput setaf 2")
			print("Mission Accomplished : Folder created ")
			time.sleep(2)
		
			os.system("\n\nfdisk -l")
			os.system("tput setaf 3")
			m=input("\t Mount The folder , Please provide your disk details ")
			os.system("mount {} {} ".format(m,d))
			os.system("tput setaf 2")
			print("Mission Accomplished : Mounted ")
			time.sleep(2)

		elif a=="3":
			os.system("\n\nfdisk -l")
			os.system("tput setaf 3")
			print("Provide the both disks name :-")
			i=input("pvcreate ")
			j=input("pvcreate ")
			os.system("pvcreate {} {}".format(i,j))
			os.system("tput setaf 2")
			print("Mission Accomplished:  Physical Volume  created")
			time.sleep(2)
			
			os.system("tput setaf 3")
			print("\n\n Create Volume group as per your requiremnt ")
			VG_Name=input("Group Name Required  :-")
			os.system("vgcreate {} {} {}".format(VG_Name,i,j))
			os.system("tput setaf 2")
			print("Mission Accomplished : VG Created ")
			time.sleep(2)
				
			os.system("tput setaf 3")
			print("\n\nType a size of lv you want to set")
			Size_1=input(" Size(in GiB) -  ")
			Name=input("Type Name -")
			os.system("lvcreate --size {}GB --name {} {}".format(Size_1,Name,VG_Name))
			os.system("tput setaf 2")
			print("Misiion Accomplished :  lv created")
			time.sleep(2)
			
			os.system("tput setaf 3")		
			print("\n\nFormat the lv")
			os.system("mkfs.ext4 /dev/{}/{}".format(VG_Name,Name))
			os.system("tput setaf 2")
			print("Successfully Formatted")
			time.sleep(2)

			print("\n\nBefore the mounting please create Directory")
			p=input("mkdir ")
			os.system("mkdir {}".format(p))
			os.system("tput setaf 2")
			print("Directory created")
			time.sleep(2)

			print("\n\nMount your Directory")
			os.system("mount /dev/{}/{} /{}".format(l,o,p))
			os.system("tput setaf 2")
			print("Successfully Mounted please check with df -h command ")
			print("\n Back to the menu")
			os.system("tput setaf 7")

		elif a=="4":
			os.system("df -h")

		elif a=="5":
			os.system("vgdisplay")

		elif a=="6":
			os.system("yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")

		elif a=="7":
			break

		elif a=="8":
			os.system("tput setaf 7")
			print("Better Luck next time ..")
			time.sleep(2)
			exit()

		else:
			input("Invalid detail enterd")
			continue
			
			
def Web_Environment_setup():

	from os import system
	import subprocess as sp
	from time import sleep
	system("clear")
	os.system("tput smso 5")
	os.system("tput bold 4")
	os.system("tput setaf 4")
	print("\t\t .....Web Environment Readiness Program ....\n")
	
	while True :
	   
	    os.system("tput sgr0")
	    system("tput setaf 6")
	    print("\n\n1. Enter 1 to :  Install Software ")
	    print("#--- Enter 2 to : Create Web pages ")
	    print("#----Enter 3 to : Start your Services to deliver results")
	    print("#----Enter 4 to : Stop the Environment ")
	    print("#----Enter 5 to : Go To Main Menu ")
	    print("#----Enter 6 to : Quit ")

	    system("tput setaf 3")
	    ch = int(input("\n Enter your selcted requirement code  : "))

	    if ch==1 : 
	        x = sp.getstatusoutput("rpm -q httpd")
	        if x[0] != 0 :
	            system("yum install httpd")
	            sleep(2)
	        else : 
	            system("tput setaf 2")
	            print("\n Nothing Required to do install ")
	            sleep(2)

	    elif ch==2 :
	        system("tput setaf 3")
	        Website_Page1 = input("\n Create your html document for browser : ")
	        system(f"vim /var/www/html/{Website_Page1}")
	        system("tput setaf 2")
	        print("\n Created your first page ")
	        sleep(2)

	    elif ch==3 :
	        system("tput setaf 2")
	        system("systemctl start httpd")
	        print("\n Strated your Environment ")
	        sleep(2)

	    elif ch==4 :
	        system("tput setaf 2")
	        system("systemctl stop httpd")
	        print("\n Environment Stopped by user ")
	        sleep(2)

	    elif ch==5 :
	        break

	    elif ch==6 :
	     	system("tput setaf 3")
	     	print(" Exit ")
	     	system("tput sgr0")
	     	exit()
	     	
	        
	    else :
	        system("tput setaf 1")
	        print("\nIncorrect Option selcted \n select appropriate ption count ")
	        sleep(2)




def Containerization():

	import os
	os.system("clear")
	os.system("tput smso 5")
	os.system("tput setaf 3")
	print("\n\n\t\t\t Setup your Conatinerized Application  ")
	os.system("tput sgr 0 ") 

	while True:
		os.system("tput setaf 4")
		#os.system("tput smul 4")
		print("""
		1.  Enter 1 To : Fetch images from Dockerhub if available.
		2.  Enter 2 To : Get  Docker image.
		3.  Enter 3 To : Availaible Images .
		4.  Enter 4 To : Containers List .
		5.  Enter 5 To : Launch a Container .
		6.  Enter 6 To : Stopped container List .
		7.  Enter 7 To : Launch container and attach .
		8.  Enter 8 To : Delete container.
		9.  Enter 9 To : Delete docker  images.
		10. Enter 10 To: Go to main menu.
		11. Enter 11 To: Quit .
		""")
		
		os.system("tput sgr0")
		os.system("tput bold")	
		os.system("tput setaf 5")
		x=input("\n Type your selected code : ")
		os.system("clear")
		if x=="1":
			os.system("tput sgr0")	
			os.system("tput setaf 6")
			docker_image=input("\n Please type image you want to fetch :- ")
			os.system("docker search {}".format(docker_image))
			os.system("tput sgr0")			
			os.system("tput bold")
			os.system("tput setaf 4")
			input("\n\t\t Enter Button ")
			os.system("tput sgr0")


		
		elif x=="2":
			os.system("tput sgr0")	
			os.system("tput setaf 6")
			z=input("\n Type Image Name you want to download:- ")	
			os.system("docker pull {}:latest".format(z))					
			os.system("tput sgr0")			
			os.system("tput bold")
			os.system("tput setaf 4")
			input("\n\t\t Enter Button")
			os.system("tput sgr0")


		elif x=="3":
			os.system("tput sgr0")	
			os.system("docker images")
			os.system("tput sgr0")			
			os.system("tput bold")
			os.system("tput setaf 4")
			input("\n\t\t Enter button ")
			os.system("tput sgr0")


			

		elif x=="4":
			os.system("tput sgr0")	
			os.system("docker ps")
			os.system("tput sgr0")			
			os.system("tput bold")
			os.system("tput setaf 4")
			input("\n\t\t Enter Button ")
			os.system("tput sgr0")


		elif x=="5":
			os.system("tput sgr0")	
			os.system("docker images")
			ISO_IMAGE_USED_TO_LAUNCH=input("\n Type Image name which you want to use to launch a container :- ")
			COMNTAINER_NAME=input("\n Type name you want to give to your containe :- ")	
			os.system("docker run -it --name {}  {}:latest".format(COMNTAINER_NAME,ISO_IMAGE_USED_TO_LAUNCH))
			os.system("tput sgr0")			
			os.system("tput bold")
			os.system("tput setaf 4")
			input("\n\t\t Enter ")
			os.system("tput sgr0")



		elif x=="6":
			os.system("tput sgr0")	
			os.system("docker ps -a")
			os.system("tput sgr0")
			os.system("tput bold")
			os.system("tput setaf 4")
			input("\n\t\t Enter Button ")
			os.system("tput sgr0")

		

		elif x=="7":
			os.system("tput sgr0")	
			os.system("docker ps -a")
			Start_Container=input("\n Type Name of container you want to start :- ")
	#----To start conatiner	
    	os.system("docker start {}".format(Start_Container))
   #-----To Attach Container 
			os.system("docker attach {}".format(Start_Container))

		elif x=="8":
			while True:
				os.system("tput sgr0")	
				os.system("tput smul 3")
				os.system("tput setaf 3")
				print("\n1. Enter  1 To : Remove one container.")
				print("2.   Enter  2 To : Remove all container.")
				print("3.   Enter  3 To : Go to main menu.")
				print("4.   Enter  4 To : Exit.")

				os.system("tput sgr0")	
				os.system("tput setaf 6")
				a=input("Enter your choice:- ")
				if a=="1":
					os.system("tput sgr0")	
					os.system("docker ps -a")
					os.system("tput setaf 5")
					x=input("\nType container id or name you want to remove :- ")
					os.system("docker rm {}".format(x))
					os.system("docker ps -a")
					os.system("tput sgr0")
					os.system("tput bold")
					os.system("tput setaf 4")
					input("\n\t\t Enter Button ")
					os.system("tput sgr0")
				
				elif a=="2":
					os.system("tput sgr0")	
					os.system("docker ps -a")
					os.system("docker rm `docker ps -a -q`")
					os.system("docker ps -a")
					os.system("tput sgr0")
					os.system("tput bold")
					os.system("tput setaf 4")
					input("\n\t\t Enter Button ")
					os.system("tput sgr0")

				
				elif a=="3":
					break

				elif a=="4":
					exit()
				
				else:
					print("\n\t\t Invalid Choice ")



		elif x=="9":
			os.system("tput sgr0")	
			os.system("docker images")
			img=input("\n Your Image Name :- ")
			os.system("docker rmi -f {}".format(img))
			os.system("docker images")
			os.system("tput sgr0")			
			os.system("tput bold")
			os.system("tput setaf 4")
			input("\n\t\t Enter Button ")
			os.system("tput sgr0")
		

		elif x=="10":
			break

		elif x=="11":
			exit()







