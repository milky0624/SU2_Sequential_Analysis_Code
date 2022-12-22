import os
import sys

print("")
print("")
print(" ----------------------------------------------------------- ")
print("|                                                           |")
print("| Producer : Jin Young Kim                                  |")
print("| Production Date : 2022. 12. 11                            |")
print("|                                                           |")
print("| Befor you use this code,                                  |")
print("| If it is known that the file was not directly received    |")
print("| by the producer, it will punch.                           |")
print("|                                                           |")
print("| If you have any questions, please contact us via email    |")
print("| e-mail : rlawlsdud0624011129@gmail.com                    |")
print("|                                                           |")
print(" ----------------------------------------------------------- ")
print("")
print("")

CORE_NO = input("How to use Core : ")
CORE_NO = CORE_NO

print("")

START_CASE_NO = input("Start Case Number : ")
START_CASE_NO = START_CASE_NO
END_CASE_NO = input("End Case Number : ")
END_CASE_NO = END_CASE_NO

print("")
print("")
print(" ----------------------------------------------------------- ")
print("")
print( "CPU Core of Analysis : " + CORE_NO)
print("Start Case : Case_" + START_CASE_NO + ".cfg")
print("End Case : Case_" + END_CASE_NO + ".cfg")
print("")
print(" ----------------------------------------------------------- ")
print("")


#NEW_CODE = "mpiexec -n " + CORE_NO + " " + "SU2_CFD.exe" + " " + "Case_" + str(i) + ".cfg"

for i in range(int(START_CASE_NO), int(END_CASE_NO) +1):
    NEW_CODE = "mpiexec -n " + CORE_NO + " " + "SU2_CFD.exe" + " " + "Case_" + str(i) + ".cfg > Case_" + str(i) + ".txt"
    print(NEW_CODE)

    os.system(NEW_CODE)

    print("")
    print("__________________________________Case_" + str(i) + "_____Finish")
    print("")
    print("")
    print("|  Inner_Iter|   Time(sec)|    rms[Rho]|   rms[RhoE]|          CL|          CD|         CMx|         CMy|         CMz|   rms[RhoU]|   rms[RhoV]|")

    f = open("Case_" + str(i) + ".txt", 'r')
    f = f.read().split("\n")

    for a in range(-36, -1):
        print(f[int(a)])