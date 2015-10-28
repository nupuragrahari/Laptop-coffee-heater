import subprocess
p = subprocess.Popen(['cat', '/sys/class/power_supply/BAT1/current_now'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err=p.communicate()
print out
p1 = subprocess.Popen(['cat', '/sys/class/power_supply/BAT1/voltage_now'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err=p1.communicate()
print out
p2 = subprocess.Popen(['cat', '/sys/class/power_supply/BAT1/present'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err=p2.communicate()
print out