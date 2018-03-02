numbers = [int(n) for n in raw_input('Enter numbers').split()]
maps = [int(n) for n in raw_input('Enter mappings').split()]
while numbers != maps:
    for i in range(0,len(numbers)-1):
        for j in range(0,len(maps)-1):
            #print j
            if numbers[i] not in maps:
                #print "executing"
                del numbers[i]
                del maps[i]
print maps
