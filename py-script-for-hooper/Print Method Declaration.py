import os, re, subprocess
cmd = '/usr/local/bin/class-dump'

def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

doc = Document.getCurrentDocument()
proc = doc.getCurrentProcedure()
procEntryAddress = proc.getEntryPoint()
procName = doc.getNameAtAddress(procEntryAddress)

pattern = re.compile("[\[\sa-zA-Z0-9_]+")
match = pattern.search(procName)
match = match.group(0)
pattern = re.compile("[a-zA-Z0-9_]+")
match = pattern.findall(match)
arguments = " -t "
fire = False
if len(match) > 0:
	clazz = match[0]
	fire = True
	arguments += "-c " + clazz
if len(match) > 1:
	methodFirst = match[1]
	fire = True
	arguments = arguments + " -f "+methodFirst

file = doc.getExecutableFilePath()
arguments += " "+file
result = ""
if fire:
	cmd += arguments
	print("excute cmd: "+cmd)
	for line in run_command(cmd.split()):
		result += line

#print(file)
#print(result)
#print(doc.getCurrentAddress())
#print(arguments)
#print(clazz)
#print(methodFirst)
print(result)

