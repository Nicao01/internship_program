# 4)
#discovering light switches
def discover_light_switch():
    light_switches = [False, False, False]


    #turning on first light switch
    light_switches[0] = not light_switches[0]

    #turning off first light switch and turning on the second one
    light_switches[0] = not light_switches[0]
    light_switches[1] = not light_switches[1]

    #finding which light switch controls which bulb
    for i, bulb in enumerate(light_switches, 1):
        if bulb:
            print(f"The {i} light switch controls the bulb.")
            break
    else:
        print("There're no light switches on")


discover_light_switch()