fout = open('my_mood', 'w')
print(fout)

line1 = '我很开心\n'
fout.write(line1)

line2 = '我很燃\n'
fout.write(line2)

line3 = '我想当开心的脱口秀演员\n'
fout.write(line3)

'''
When you are done writing, you have to close the file to make sure that the last
bit of data is physically written to the disk so it will not be lost if the power goes
off.
'''
fout.close()
