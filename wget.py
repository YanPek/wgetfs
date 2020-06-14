from os import system
import sys
try: from colorama import Fore
except:
    system("pip install colorama")
    from colorama import Fore
	
path = ""
site = ""
def main(site, path):
    if path[-1:] != "/":
        path += "/"
    try: 
        system("pkg install wget -y")
        if path != "/":
            system(f"wget --mirror -p --convert-links -p {path} {site}")
        elif path == "/":
            system(f"wget --mirror -p --convert-links {site}")
    except:
        print("Error")
	
if __name__ == "__main__":
    if len(sys.argv) == 1:
        site = input(Fore.RED+"Url: ")
        path = input("Path: ")
        print(Fore.GREEN+"Installing..."+Fore.RESET)
        main(site, path)
    elif len(sys.argv) == 2 and sys.argv[1] == "-h":
    	print(Fore.GREEN+'''
-s - Site [https://site.com]
-p - Path [/sites/]
-h - Help

Usage:
python wget.py -s https://site.com -p /sites/
or
python wget.py -s https://site.com
or
python wget.py -h
or
python wget.py'''+Fore.RESET)
    elif len(sys.argv) == 3 and sys.argv[1] == "-s":
        main(sys.argv[2], "")
    elif len(sys.argv) == 5 and sys.argv[1] == "-s" and sys.argv[3] == "-p":
        main(sys.argv[2], sys.argv[4])
    else:
        print(Fore.GREEN+'''
-s - Site [https://site.com]
-p - Path [/sites/]
-h - Help

Usage:
python wget.py -s https://site.com -p /sites/
or
python wget.py -s https://site.com
or
python wget.py -h
or
python wget.py'''+Fore.RESET)