#!/usr/bin/Python3
#A script to bruteforce (Zip, Rar, 7z) password protected archives.(only use in terminal)
#script by:https://github.com/TaherOuerfelli/ZipRip
import os
import patoolib
import pyzipper

from threading import Thread
import subprocess
#init colors for windows
if os.name == 'nt':
    import colorama
    colorama.init()


#function to clear the console
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(os.name 'posix')
    else:
        _ = os.system('clear')


#function to check path existance
def path_exists(path):
    return os.path.exists(path)
#function to check file existance
def file_exists(file):
    return os.path.exists(file) and os.path.isfile(file)

#function to get file type
def getType(file):
    if file.endswith(".rar"):
        return "rar"
    elif file.endswith(".zip"):
        return "zip"
    elif file.endswith(".7z"):
        return "7z"
    else:
        return "bad"

#verify archive file input
def verify_file(file):
    if(file == ""):
        return False
    if (file_exists(file)):
        if(getType(file)=="bad"):
            print("\t\033[31m[!] \033[37mArchive has to end with (.zip /.rar /.7z )")
            return False
        else:
            return True
    else:
        print("\t\033[31m[!] \033[37mFile does not exist.")
        return False
#verify extract path input
def verify_path(path):
    if(path == " "):
        return False
    if(path == ""):
        return True
    if (path_exists(path)):
            return True
    else:
        print("\t\033[31m[!] \033[37mPath does not exist.")
        return False


#verify wordlist file input
def verify_file_w(file):
    if(file == ""):
        return False
    if (file_exists(file)):
        if(not wordlist.endswith(".txt")):
            print("\t\033[31m[!] \033[37mWordlist has to end with (.txt)")
            return False
        else:
            return True
    else:
        print("\t\033[31m[!] \033[37mFile does not exist.")
        return False

#verify if unrar is available in the console (UnRar should be in PATH)
def verify_rar():
    try:
        subprocess.run(['unrar', '-v'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("\t\t\033[33m\'unrar\' \033[37mis available in the console.")
        return True
    except FileNotFoundError:
        print("\t\t\033[33m\'unrar\' \033[31mis not installed or not available in the console.(make sure \'unrar\' is in PATH)")
        return False
    except subprocess.CalledProcessError as e:
        print("\t\033[31mError:", e)
        return False

#verify if 7z is available in the console (7z should be in PATH)
def verify_7z():
    try:
        subprocess.run(['7z', '-h'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("\t\t\033[33m\'7z\' \033[37mis available in the console.")
        return True
    except FileNotFoundError:
        print("\t\t\033[33m\'7z\' \033[31mis not installed or not available in the console.(make sure \'7z\' is in PATH)")
        return False
    except subprocess.CalledProcessError as e:
        print("\t\033[31mError:", e)
        return False


#function to extract rar file with the provided password
def extract_rar(file, passwrd):
    
        global found
        try:
            if((Isthreading == False) and found == False):
                print("\t\033[35mTrying password: \033[34m"+ str(passwrd))
            elif (found == False):
                print("\t\033[35m-> \033[34m"+ str(passwrd))

            #try extracting rar file with unrar.exe
            if(extpath!=""):
                command =['unrar', 'x', '-p'+passwrd , file,extpath]
            else:
                command =['unrar', 'x', '-p'+passwrd , file]
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            found = True
            print("\t\033[32m[+] "+filetype+" file extracted. \n\tPassword = \033[1m\033[33m"+ str(passwrd)+"\033[22m\n")
                
        except Exception as e:
            #print(e)
            pass

#function to extract file using patoolib
def extract_patool(file, passwrd):
    
        global found
        try:
            if((Isthreading == False) and found == False):
                print("\t\033[35mTrying password: \033[34m"+ str(passwrd))
            elif (found == False):
                print("\t\033[35m-> \033[34m"+ str(passwrd))

            #extracting rar file with patoolib (slow)
            command = ['patool', 'extract', '--password', passwrd, file, '--outdir', extpath]
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            found = True
            print("\t\033[32m[+] "+filetype+" file extracted. \n\tPassword = \033[1m\033[33m"+ str(passwrd)+"\033[22m\n")
                
        except Exception as e:
            #print(e)
            pass

#function to extract zip file with the provided password
def extract_zip(file, passwrd):
    global found

    try:
        if((Isthreading == False) and found == False):
            print("\t\033[35mTrying password: \033[34m"+ str(passwrd))
        elif (found == False):
                print("\t\033[35m-> \033[34m"+ str(passwrd))
        #try extracting zip file using pyzipper module
        with pyzipper.AESZipFile(file) as zf:
            zf.pwd = passwrd.encode()  # Set the password
            zf.extractall(extpath)
        found = True
        print("\n\t\033[32m[+] "+filetype+" file extracted. \n\tPassword = \033[1m\033[33m"+ str(passwrd)+"\033[22m\n")

    except:
        pass

#function to extract 7z file with the provided password
def extract_7z(file, passwrd):
    
        global found
        try:
            if(found == False):
                print("\t\033[35mTrying password: \033[34m"+ str(passwrd))
            #run a subprocess using 7z in the commandline
            if(extpath!=""):
                command = ['7z', 'x', file,'-p'+passwrd,'-o'+extpath,'-y' ]
            else:
                command = ['7z', 'x', file,'-p'+passwrd,'-y' ]
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            found = True
            print("\t\033[32m[+] "+filetype+" file extracted. \n\tPassword = \033[1m\033[33m"+ str(passwrd)+"\033[22m\n")
                
        except Exception as e:
            #print(e)
            pass



def main():
        #display file type
        if(filetype == "rar"):
                print("\n\n\t\033[35mType: \033[36mRar")
        elif(filetype == "zip"):
                print("\n\n\t\033[35mType: \033[36mZip")
        elif(filetype == "7z"):
                print("\n\n\t\033[35mType: \033[36m7z")
        else:
                print("\n\033[31mFiletype unsupported.")
                exit(3)
        #display tool used
        if(tool == "rar"):
                print("\t\033[35mTool: \033[36mUnRar")
        elif(tool == "7z"):
                print("\t\033[35mTool: \033[36m7z")
        elif(tool == "patool"):
                print("\t\033[35mTool: \033[36mPatoolib")
        elif(tool == "zip"):
                print("\t\033[35mTool: \033[36mpyzipper")
        else:
                exit(4)
        if(Isthreading == True):
                print("\033[36m\tMultithreading enabled \n\t(Trying as many passwords as possible)")
        print("\033[35m\n\tTrying to extract (please wait)..")
        #open wordlist
        f = open(wordlist, "r")
        #loop through all passwords
        for i in f.readlines():
                #current password
                password = i.strip()
                
                if(found == False):
                        if (Isthreading == True):
                                #thread execution
                                if(tool == "rar"):
                                    t = Thread(target=extract_rar, args=(file, password))
                                elif(tool == "patool"):
                                    t = Thread(target=extract_patool, args=(file, password))
                                else:
                                    t = Thread(target=extract_zip, args=(file, password))
                                t.start()
                        else:
                            if(tool == "rar"):
                                extract_rar(file, password)
                            elif (tool == "7z"):
                                extract_7z(file, password)
                            elif (tool == "patool"):
                                extract_patool(file, password)
                            else:
                                extract_zip(file, password)
                else:
                        break;
        


if __name__ == '__main__':
        #Title --------------------------------#
        x='\033[33m* '
        for i in range(25):
            x +='* '
        print(x)
        print("\033[1m\tZipRip-v1 Archive BruteForce tool\033[22m\033[33m")

        print("\033[1m\n\n\t* Supported archives: \033[37mzip\033[33m,\033[37mrar\033[33m,\033[37m7z\033[22m\033[33m\n")
        print(x)
        #--------------------------------------#
                
        #password found?
        found =False
        #use all threads?
        Isthreading  = False

        #type of archive
        filetype = ""
        #tool used for extract
        tool = ""
        
        
        #file input
        file=""
        while(not verify_file(file)):
                file = input("\n\t\033[1m\033[36mArchive path :\033[33m\033[37m ")
                file = file.strip()
        #set filetype
        filetype = getType(file)

        #set tool
        if(filetype=="rar"):
            tool = "rar"
            if(not verify_rar()):
                tool = "7z"
                if(not verify_7z()):
                    tool = "patool"
                    print("\t\t\033[33m\'Patoolib\' \033[37mwill be used. (slow)")
        ########
        if(filetype=="7z"):
            tool = "7z"
            if(not verify_7z()):
                tool = "patool"
                print("\t\t\033[33m\'Patoolib\' \033[37mwill be used. (slow)")
        ########
        if(filetype=="zip"):
            tool = "zip"

        #extract path input
        extpath=" "
        while(not verify_path(extpath)):
                extpath = input("\n\t\033[1m\033[36mExtract folder path (optional) :\033[33m\033[37m ")
                extpath = extpath.strip()
                
        #wordlist input
        wordlist=""
        while(not verify_file_w(wordlist)):
                wordlist = input("\n\t\033[1m\033[36mWordlist path : \033[33m\033[37m ")
                wordlist = wordlist.strip()
                

        
        #ask for threading (extract files at the same time to speed up)
        if(tool != "7z"):
            x = input("\n\t\033[1m\033[36mUse MultiThreading? \n\t\033[31m(Warning: Running as many Subproccesses as possible, may slow down your computer) Y/N: \033[33m\033[37m ")
            if(x.upper() == "Y"):
                    Isthreading = True
        else:
            x = input("\n\t\033[1m\033[36m\'7z\' blocks multiple extract operations, multithreading is not available \n\tpress enter to continue: \033[33m\033[37m ")

        
        
        #start brute force
        clear()
        main()

        #show last message
        if(found == False and Isthreading == False):
                print("\n\t\033[31mFailed: wordlist does not contain the required password!\n")
        if (Isthreading == True):
                print("\n\t\033[35mThreading Ended.\n")
        exit(0)
