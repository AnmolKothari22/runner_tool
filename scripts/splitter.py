import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(SCRIPT_DIR, "../temp_test_file/input2.txt")
INPUT_PATH_SPLIT = os.path.join(SCRIPT_DIR, "../temp_test_file/tc_seperated")
#print(INPUT_PATH)
#print(INPUT_PATH_SPLIT)


try:
    with open(INPUT_PATH, "r", encoding="utf-8") as file:
        temp="1\n"
        file_no=1
        co=0
        for line in file:
            if (co==0) or (co==1):
                co=co+1
                continue
            if( line.strip() != ""):
              #  print("the line: ",len(line),line)
                temp=temp+line
            else:
                file_name="tc"+str(file_no)+".txt"
                FILE_TEMP_PATH= os.path.join(INPUT_PATH_SPLIT,file_name)
                #print(temp)
                #print(FILE_TEMP_PATH)
                with open(FILE_TEMP_PATH, "w", encoding="utf-8") as tc:
                    tc.write(temp)
                file_no=file_no+1
                temp="1\n"
            co=co+1

        file_name="tc"+str(file_no)+".txt"
        FILE_TEMP_PATH= os.path.join(INPUT_PATH_SPLIT,file_name)
        with open(FILE_TEMP_PATH, "w", encoding="utf-8") as tc:
            tc.write(temp)

                
except Exception as e:
    print("Error:", e)


