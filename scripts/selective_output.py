import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "../expected_output.txt")
s=set()
for a in sys.argv:
    s.add(a)
#print(s)
arr = []
try:
    temp=""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as file:
        t = 1
        for line in file:
         #   print(t,temp)
            if (line.strip() == ""):
                if((str(t) in s)):
                    arr.append(temp)
                    arr.append("\n")
                temp=""
                t=t+1
            else:
              #  print(line,end="")
                temp=temp+line
    if((str(t) in s) and (temp !="")):
        arr.append(temp)
        arr.append("\n")
    
   # print("expected output: ",arr)
    for ele in arr:
        print(ele,end="")
                
except Exception as e:
    print("Error:", e)


