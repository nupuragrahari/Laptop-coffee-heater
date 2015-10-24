import subprocess
p = subprocess.Popen(['cat', '/sys/class/power_supply/BAT1/current_now'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err=p.communicate()
print out
