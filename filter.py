from platform import system as iden
from os import mkdir , getcwd, chdir
from os.path import isfile , isdir
from json import load , dump
from random import choice
from colorama import Fore
from sys import argv
c = Fore.CYAN
g = Fore.GREEN
w = Fore.WHITE
r = Fore.RED
if iden() != "Windows":
 from readline import parse_and_bind
 parse_and_bind('tab:complete')
def banner():
 colors = [w , r , g , c]
 print (f"""{choice(colors)}
                                    
                         __ _ _ _            
                        / _(_) | |           
                        | |_ _| | |_ ___ _ __ 
                        |  _| | | __/ _ \ '__|
                        | | | | | ||  __/ |   
                        |_| |_|_|\__\___|_|V1.0

                        Coded By : Ali Mansour
    """)
class Filiter:

    def __init__(self) :

        pass

    def del_repeat(self , name ):
        for name_ in name:
            with open(name_ , 'r')as f:
                data = set(f.readlines())
                fx = open(name_ , 'w')
                for line in data :
                    fx.write(line.rstrip() + '\n')
                fx.close()
    def dump_names(self , path):
        global all_ , f_ext , data_ext
        n = 0
        if n == 0:
            f_ext = open(f'{path}/ext.json')
            data_ext = load(f_ext)
            n += 1
        f = open("names_json.txt" , 'w')
        all_ = []
        for i in data_ext:
            all_.append(i)
            f.write(i + '\n')
        f.close()
        print (f"[+] {str(len(all_))} At names_json.txt")
    def dump_column(self , name , *all):
        pwd = getcwd()
        if not isdir("results_fetchs"):
            mkdir("results_fetchs")
        chdir(getcwd() + '//results_fetchs')
        Filiter().dump_names(pwd)
        fxx = open("not_dumped.txt" , 'a')
        for x in all_:
            try:
                if not len(x) <= 8:
                    fxx.write(x + '\n')
                else:
                    f_c = open(f"column_{x}.txt", 'w')
                    if all:
                        for file in data_ext[x]:
                            f_c.write(file + '\n')
                        f_c.close()
                    else:
                        for i in data_ext[name]:
                            f_c.write(i + '\n')
                        f_c.close()
            except Exception as e:
                print (e)
                continue
        fxx.close()
    def self_filter(  self , name_f ):
        f_ = open('blacklist.json')
        blacklist = load(f_)["blacklist"]
        f = open(name_f,'r')
        f22 = open(f'deleted_{name_f}', 'a')
        fr = open("new_filter.txt" , 'a')
        w = []
        for path in f.readlines():
            path = path.rstrip()
            for blocked in blacklist:
                if blocked in path:
                    if path not in w:
                        w.append(path)
                        f22.write(path + '\n')
            if path not in w:
                fr.write(path + '\n')
        fr.close()
        f.close()
        f22.close()

    def extract_p_e( self, nameF , dom ,spec ):
        Filiter().del_repeat([nameF])
        fx = open("parms.txt",  'a')
        fx3 = open("others.txt", 'a')
        db = {}
        with open(nameF, 'r')as f:
            for i in f.readlines():
                i = i.rstrip()
                if ("?" in i.split('/')[-1] and not i.split('/')[-1][-1] == '?') and ( '=' in i.split('/')[-1] or "%3D" in i.split('/')[-1]):
                    if "/js" in i or ".js" in i.split('/')[-1]:
                        if "js" in db:
                            db["js"].append(i)
                        else:
                            db["js"] = []
                            db["js"].append(i)
                    elif "/css" in i or ".css" in i.split('/')[-1]:
                        if "css" in db:
                            db["css"].append(i)
                        else:
                            db["css"] = []
                            db["css"].append(i)
                    else:
                        fx.write(i + '\n')
                if "." in i.split('/')[-1]:
                    if spec != []:
                        if "." + i.split('/')[-1] in spec or i.split('/')[-1] in spec:
                            if i.split('/')[-1].split('.')[-1] in db:
                                db[i.split('/')[-1].split('.')[-1]].append(i)
                            else:
                                db[i.split('/')[-1].split('.')[-1]] = []
                                db[i.split('/')[-1].split('.')[-1]].append(i)
                    else:
                        if not "=" in i.split('/')[-1] or not "?" in i.split('/')[-1]:
                            if i.split('/')[-1].split('.')[-1] in db:
                                db[i.split('/')[-1].split('.')[-1]].append(i)
                            else:
                                db[i.split('/')[-1].split('.')[-1]] = []
                                db[i.split('/')[-1].split('.')[-1]].append(i)
                else:
                    if dom.startswith("https://"):
                        dom = dom[8:]
                    if dom.startswith("http://"):
                        dom = dom[7:]
                    if "://" in i:
                        if dom in i.split("://")[1].split('/')[0]:
                            fx3.write( i + '\n' )
        with open("ext.json" , 'w')as fe:
            dump(db, fe)
        fx.close()
        fx3.close()
spec = []
banner()
if len(argv) == 1:
    print ('Usages:')
    print ("""
-d domain to avoid annoying results ( For Filteration )

-f File

-n <Number OF Functions>

-s Spec Ext to dump

Functions:

1. Filter by deleting some extentions from inserted file
2. Fetch all extenstions at inserted file
3. Dump all extenstions and split them to files
4. All OF THEM

Example:

1. ./{0} -f name.txt -n 1
2. ./{0} -f name.txt -d google.com -s js -n 2
3. ./{0} -n 3
4. ./{0} -n All -f name.txt -d google

""".format(argv[0]))
else:
    try:
        if "-d" in argv[1:]:
            domain = argv[argv.index('-d')+1]
        if "-f" in argv[1:]:
            if isfile(argv[argv.index('-f')+1].strip()):
                file = argv[argv.index('-f')+1]
            else:
                exit("[!] File Not Inserted")
        if "-n" in argv[1:]:
            number = str(argv[argv.index('-n')+1])
        if "-n" not in argv[1:]:
            exit("[!] Number Not Inserted")
        if "-s" in argv[1:]:
            spec.append(argv[argv.index('-s')+1])
        if number == '1':
            Filiter().self_filter( file )
        elif number == '2':
            if not spec:
                spec = []
            if not domain:
                exit("[!] Domain Not Inserted")
            Filiter().extract_p_e(file , domain , spec)
        elif number == '3':
            Filiter().dump_column("" , True)
        elif number.strip() == 'All':
            Filiter().self_filter( file )
            if not spec:
                spec = []
            if not domain:
                exit("[!] Domain Not Inserted")
            Filiter().extract_p_e("new_filter.txt" , domain , spec)
            Filiter().dump_column("" , True)
        else:
            exit("[!] Wrong Choiced Number")
    except (KeyboardInterrupt , EOFError):
        exit()
    except Exception as e:
        raise
