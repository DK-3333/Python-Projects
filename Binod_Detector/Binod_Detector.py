#Binod Detector Using Python
import os

def isBinod(filename):
    with open(filename,"r") as f:
        filecontent  = f.read()
    
    #Detect all forms of Binod like bInOd 
    if "binod" in filecontent.lower():
        return True
    else:
        return False 

if __name__=="__main__":
    #Listing the contents of this folder
    dir_contents = os.listdir()
    count = 0
    #print(dir_contents)

    #For each text file, detect Binod in them.
    for item in dir_contents:
        if item.endswith("txt"):
            print(f"Detecting Binod in {item}")
            flag = isBinod(item)
            if(flag):
                print(f"!!!!!!!!!!!!!Binod found in {item}!!!!!!!!!!!!!!!")
                count += 1
            else:
                print(f"Binod not found in {item}")
    print("****************Binod Detector Summary***************")
    print(f"{count} files found with Binod hidden into them.")