import subprocess
import sys

testcase = sys.argv[1]
output = sys.argv[2]

comp = True

f = open(output)
outstr = f.read().strip().split()
f.close()

try:
    compiling = subprocess.check_output("gcc /app/golden_ticket.c -o /app/golden_ticket", shell=True)
except:
    comp = False
    print("fail")

if comp:
    try:
        cmd = subprocess.check_output(f"cat {testcase} | /app/golden_ticket", shell=True).decode().strip().split()
        if cmd==outstr:
            print("pass")
        else:
            print("fail")
    except:
        print("fail")
