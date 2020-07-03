import sys,getopt
import datetime
import time
import os
import random
sys.setrecursionlimit(50000000)

def InputData(filename_input):
    dirname = filename_input.replace("\\","*").replace("/","*")
    Check_dir = "*" in dirname
    Check_file = ".txt" in filename_input
    if Check_dir == True:
        Dir_input = filename_input
    else:
        Dir_input = "./benchmark/" + filename_input
    if Check_file == True:
        Dir_input = Dir_input
    else:
        Dir_input = Dir_input + ".txt"
    # print(Dir_input)
    datafile = open(Dir_input,"r")
    Data_input = datafile.read().replace("A=<","").replace("B=<","").replace(",>","")
    Data_input_A = Data_input.split("\n")[0].replace(",","")
    Data_input_B = Data_input.split("\n")[1].replace(",","")
    return Data_input_A, Data_input_B

def Bottom_Up(Data_input_A,Data_input_B):
    data = [Data_input_A,Data_input_B]
    substrs = lambda x: {x[i:i+j] for i in range(len(x)) for j in range(len(x) - i + 1)}
    data_value = substrs(data[0])
    for val in data[1:]:
        data_value.intersection_update(substrs(val))
    Data_Max_List = list(filter(lambda y: len(y) == len(max(data_value, key=len)),data_value))
    return Data_Max_List

def main(argv):
    print("Start")
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"t/bf:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('Error - Please run again: Hw3_P76087081.py -t/-b -f <inputfile> -o <outputfile>')
        sys.exit(2)
    # print(opts)
    if len(opts) != 3:
        print ('Error - Please run again: Hw3_P76087081.py -t/-b -f <inputfile> -o <outputfile>')
        sys.exit(2)
    filetype = opts[0][0]
    filename_input = opts[1][1]
    filename_output = opts[2][1]
    return filetype,filename_input,filename_output


def Top_Down_at_both_start (str1, str2):
    if 0 == len(str1) or 0 == len(str2) or str1[0] != str2[0]:
        return ''
    else:
        return str1[0] + Top_Down_at_both_start(str1[1:], str2[1:])

def Top_Down_at_first_start (str1, str2):
    
    if 0 == len(str2):
        return ''
    else:
        answer1 = Top_Down_at_both_start (str1, str2)
        answer2 = Top_Down_at_first_start (str1, str2[1:])
        if len(answer1) < len(answer2): 
            data = answer2
        else: 
            data = answer1
        data_value.append(data)
        return  data

def Top_Down(str1, str2):
    if 0 == len(str1):
        return ''
    else:
        answer1 = Top_Down_at_first_start (str1, str2)
        answer2 = Top_Down(str1[1:], str2)
        if len(answer1) < len(answer2): 
            data = answer2
        else: 
            data = answer1
        data_value.append(data)
        return  data

def OutData(Data_Max_List,filename_ouput,filetype,Starttime):
    dirname = filename_ouput.replace("\\","*").replace("/","*")
    Dir_output = "./output/" + dirname.split("*")[-1]
    if filetype == "-b":
        Dir_output = Dir_output.replace(".txt","_bo.txt")
    else:
        Dir_output = Dir_output.replace(".txt","_to.txt")
    Fisnishtime = datetime.datetime.now() - Starttime
    datafile = open(Dir_output,"w")
    text = """Runtime: %s 
            \nCheck up times: %s 
            \nCommon sequence: %s""" %(str(Fisnishtime),str(Fisnishtime),str(Data_Max_List))
    datafile.write(text)
    datafile.close()
    print("Run time: %s" %str(Fisnishtime))
    print("Common sequence: %s"%str(Data_Max_List))
    # print("Check up times:: %s" %str(Fisnishtime))


Starttime = datetime.datetime.now()
data_value =[]
# Check parameter
filetype,filename_input,filename_ouput = main(sys.argv[1:])
# Processing data 
Data_input_A,Data_input_B = InputData(filename_input)
if filetype == "-b": 
    Data_Max_List = Bottom_Up(Data_input_A,Data_input_B)
elif filetype == "-t": 
    Data_Max_List = Top_Down(Data_input_A,Data_input_B) 
    Data_Max_List = list(filter(lambda y: len(y) == len(max(set(data_value), key=len)),set(data_value)))
# Processing Output
OutData(Data_Max_List,filename_ouput,filetype,Starttime)

    

    