import marshal,os


logo = ('''\033[1;97m
    ______                            __ 
   / ____/___  ____________  ______  / /_
  / __/ / __ \/ ___/ ___/ / / / __ \/ __/
 / /___/ / / / /__/ /  / /_/ / /_/ / /_  
/_____/_/ /_/\___/_/   \__, / .___/\__/  
                      /____/_/           
''')
os.system("clear")
print (logo)

kun = input('\033[1;97m(+) input your file : ')
fileopen = open(kun, 'rb').read()
a = compile(fileopen, 'dg', 'exec')
m = marshal.dumps(a)
s = repr(m)
c = input ("\033[1;97m(+) output file : ")
d = open(c, 'w').write('# Encrypt by Pahrul\n# Github : https://github.com/P4HRUL\n\nimport marshal\nexec(marshal.loads(' + s + '))')

print ("\n\033[1;97m(+) selesai...")
print ('\033[1;97m(+) file tersimpan di : ' + c)
print ("")