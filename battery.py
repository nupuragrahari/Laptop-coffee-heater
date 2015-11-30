import subprocess
import serial

s = serial.Serial('/dev/tty.usbmodem1411', 9600, timeout=5)
p = subprocess.Popen(['cat', '/sys/class/power_supply/BAT1/current_now'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err=p.communicate()
print out
p1 = subprocess.Popen(['cat', '/sys/class/power_supply/BAT1/voltage_now'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err=p1.communicate()
print out
p2 = subprocess.Popen(['cat', '/sys/class/power_supply/BAT1/present'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err=p2.communicate()
print out
p3 = subprocess.Popen(['cat', '/sys/class/power_supply/BAT1/capacity'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
bat_level,err=p3.communicate()
print bat_level
if bat_level < 80:
  s.write(1)
else:
  s.write(0)
  