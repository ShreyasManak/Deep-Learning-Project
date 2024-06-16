import os 
for i in range(600):
    os.system(f"cp ./prop/prop0.dat prop.dat")
    os.system(f"cp ./load1/load375.dat load.dat")
    os.system("./main.e > shape")
    os.system(f"cp displacement ./disp_S/displacement_S{i}")