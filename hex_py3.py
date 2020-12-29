#Run with python 2.7  and 3.9
##############################################################
################Acest program este facut de catre bekli23 ####
################Nu copii-a ###################################

#print ("To stop the script execution type CTRL-C")
#print "__________________________________________________\n"

#time.sleep(1.5)    # Pause 5.5 seconds






start_str = input('Start of range: ')
end_str = input('End of range: ')
filename = input('Output filename: ')

start = int(start_str, 16)
end = int(end_str, 16)

with open(filename, 'w') as f:
    for i in range(start, end+1):
        f.write('{:064x}\n'.format(i))