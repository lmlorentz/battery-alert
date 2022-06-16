import os

with open("/sys/class/power_supply/BAT1/status", "r") as status:
        for line in status:
            fsw = line.split()
            if fsw:
               sr = (fsw[0])

with open("/sys/class/power_supply/BAT1/capacity", "r") as capacity:
        for line in capacity:
            fcw = line.split()
            if fcw:
               cr = (fcw[0])
print(cr)
print(sr)

if (sr == 'Discharging' and cr == '10'):
    print('Sending warning')
    os.system('notify-send --urgency critical "Warning: Battery is low!" "Connect the charger"')

    
if (sr == 'Discharging' and cr == '5'):
    print('Sending warning 2')
    os.system('notify-send --urgency critical "Warning: Battery is very low!" "Connect the charger fast"')

    
if (sr == 'Charging' and cr == '100'):
    print('Sending warning 3')
    os.system('notify-send --urgency normal "Warning: Battery is full" "You can remove the charger now"')
