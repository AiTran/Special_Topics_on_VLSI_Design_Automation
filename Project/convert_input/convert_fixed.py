import numpy as np
import csv

# # FolderImage = "./inputs_0.dat/"
# # ListImage = [f for f in os.listdir(FolderImage) if f.endswith(".bmp")]
# def to_fixed(f,e):
    
#     a = f* (2**e)
#     b = int(round(a))
#     if a < 0:
#         # next three lines turns b into it's 2's complement.
#         b = abs(b)
#         b = ~b
#         b = b + 1

def tohex(val, nbits):
    convert  =   hex((val + (1 << nbits)) % (1 << nbits))
    return str(convert).zfill(6).replace("0x","")

f1 = open("./inputs_0.dat", "r")
lst_out = []
for i in f1.read().split("\n"):
    if (i):
        # print(i)
        lst_out.append(tohex(int(i), 16) )
        # print (tohex(int(i), 16))
print (lst_out)

with open("./inputs_0.hex", "wb") as f2:
    a = "\n".join(lst_out)
    f2.write(str.encode(a))
f1.close()
