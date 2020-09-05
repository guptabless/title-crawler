import argparse, sys
import bcolors
import os

def banner():
    print("""
                    
                ████████╗██╗████████╗██╗░░░░░███████╗░░░░░░░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗██╗░░░░░███████╗██████╗░
                ╚══██╔══╝██║╚══██╔══╝██║░░░░░██╔════╝░░░░░░██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██║░░░░░██╔════╝██╔══██╗
                ░░░██║░░░██║░░░██║░░░██║░░░░░█████╗░░█████╗██║░░╚═╝██████╔╝███████║░╚██╗████╗██╔╝██║░░░░░█████╗░░██████╔╝
                ░░░██║░░░██║░░░██║░░░██║░░░░░██╔══╝░░╚════╝██║░░██╗██╔══██╗██╔══██║░░████╔═████║░██║░░░░░██╔══╝░░██╔══██╗
                ░░░██║░░░██║░░░██║░░░███████╗███████╗░░░░░░╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░██║
                ░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝░░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░╚═╝
                                                                                                              Code by NG          
          """)
if(len(sys.argv)>1):
    banner()
    if(sys.argv[1] != 'l'):
     try:
        input_location = sys.argv[2]
        if(os.path.exists(input_location) == True):
           print(bcolors.BITALIC + "Testing for Website Title")

           input_file = open(input_location, "r")
           input_file_line = input_file.readlines()
           for input_url in input_file_line:
                try:
                    url = input_url.strip()
                    parser = argparse.ArgumentParser()
                    parser.add_argument('-l', required=True)
                    args = parser.parse_args()
                    input_text = requests.get(url)
                    input_soup = BeautifulSoup(input_text.text, 'html.parser')
                    for title in input_soup.findAll('title'):
                      if(requests.get(url).status_code == 200):
                              print(bcolors.OKMSG + title.text)
                except:
                      print(bcolors.ERRMSG + 'This is not valid URL ' + url)

        elif(os.path.exists(input_location) == False):
         print(bcolors.BITALIC + "Testing for Website Title")
         try:
            input_header = requests.get(input_location)
            parser = argparse.ArgumentParser()
            parser.add_argument('-l',required = True)
            args = parser.parse_args()

            print(bcolors.BITALIC + "Testing for Website Title")
            input_text = requests.get(input_location)
            input_soup = BeautifulSoup(input_text.text, 'html.parser')
            for title in input_soup.findAll('title'):
                print(bcolors.OKMSG + title.text)
         except:
             print(bcolors.ERRMSG + 'This is not a valid URL')
     except:
         print('Please enter python title.py -l < location of word file >')
    elif((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: title.py [-h] -l location ' '\n' 'OPTIONS:' '\n' '-h,--help    '
                           'show this help message and exit' '\n''-l Location,   --location Location')
else:
  banner()
  print(bcolors.ERR + 'Please select atleast 1 option from -l or -h, with a valid domain name')
