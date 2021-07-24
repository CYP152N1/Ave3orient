# Import
import os
import sys
import csv
import sys
import time
import numpy as np
import argparse
# Import

# Header
now = time.ctime()
cnvtime = time.strptime(now)
print("------------")
print(time.strftime("%Y/%m/%d %H:%M", cnvtime))
print("Start:"+str(sys.argv))
print("Ver.4_(2021.Jan.03)")
print("by Hiroki Onoda, YCU")
print("------------")
print("The program solve orientation problem by control the weighting of data")
print("------------")
# Header

# Argument & Help
parser = argparse.ArgumentParser(description='Solve orientation problem by weighting.')
parser.add_argument('-i', default='run_data.star', help='Relative path of input file; ex) run_data.star (def.); ex2) Extract/job243/particles.star ')
parser.add_argument('-o', default='ave', help='Subscript of output file name; ex) ave (def.) ')
parser.add_argument('-n', default=20790, help='Target number of each orientation bin; (pi/18)^2_410bins; ex) 20790 (def.) =2*3*5*7*9*11')

args = parser.parse_args()


# Argument & Help

#l----------------------------------------------l
#l           Valiable information               l
#l----------------------------------------------l


# Average No. of particles in each orientation-bin (pie/18)^2, finally.
Aim=int(args.n)
print("Average No. of particles in each bin")
print("Finally: "+str(Aim))
print("Default: 20790 (= 2*3*5*7*9*11)")
print("Predicted total No. of particles: "+str(Aim*410))
print("")

# The name of input file (.star)
datasi=args.i[:-5]
print("Input  :"+datasi+".star")


# The name of output file (.star)
dataso=args.o
print("Output :"+datasi+"_"+dataso+str(Aim)+".star")


#l-----------------------------------------------l
#l           Valiable information                l
#l-----------------------------------------------l

datas=datasi+".star"
datao=datasi+"_"+dataso+str(Aim)+".star"
print("------------")

def read():
    cpass=os.getcwd()
    global xno
    global yno
    global nno
    global xano
    global yano
    global cno
    global rotno
    global tiltno
    global psino
    xno=0
    yno=1
    xano=""
    yano=""
    nno=999
    cno=2
    with open(cpass+"/"+datas, mode='r') as f:
        for line in f:
            if line[0:15] == "_rlnCoordinateX":
                print(line)
                xno=int(float(line[17:].strip()))-1
            elif line[0:15] == "_rlnCoordinateY":
                print(line)
                yno=int(float(line[17:].strip()))-1
            elif line[0:18] == "_rlnMicrographName":
                print(line)
                nno=int(float(line[20:].strip()))-1
            elif line[0:16] == "_rlnOriginXAngst":
                print(line)
                xano=int(float(line[18:].strip()))-1
            elif line[0:16] == "_rlnOriginYAngst":
                print(line)
                yano=int(float(line[18:].strip()))-1
            elif line[0:15] == "_rlnClassNumber":
                print(line)
                cno=int(float(line[17:].strip()))-1
            elif line[0:12] == "_rlnAngleRot":
                print(line)
                rotno=int(float(line[14:].strip()))-1
            elif line[0:13] == "_rlnAngleTilt":
                print(line)
                tiltno=int(float(line[15:].strip()))-1
            elif line[0:12] == "_rlnAnglePsi":
                print(line)
                psino=int(float(line[14:].strip()))-1
            elif line[0:11] == "_rlnOriginX": # for previous Relion (ver. 3.0.8)
                print(line)
                xano=int(float(line[13:].strip()))-1
            elif line[0:11] == "_rlnOriginY": # for previous Relion (ver. 3.0.8)
                print(line)
                yano=int(float(line[13:].strip()))-1
            pass
        pass
    print("------------")
    print("xno="+str(xno)+" yno="+str(yno)+" xano="+str(xano)+" yano="+str(yano))
    print("nno="+str(nno)+" cno="+str(cno))
    print("rotno="+str(rotno)+" tiltno="+str(tiltno)+" psino="+str(psino))
    print("------------")
    print("FIN_header")
    now = time.ctime()
    cnvtime = time.strptime(now)
    print(time.strftime("%Y/%m/%d %H:%M", cnvtime))
    pass


#Angle Tilt
def angtil():
    cpass=os.getcwd()
    lool=""
    with open(cpass+"/"+datasi+"_"+dataso+str(Aim)+".star", mode='w') as f:
        f.write(lool)
        f.close()
        pass
    b00=0
    b0001p=0
    b0001n=0
    b0000a=0
    b01=0
    b0104p=0
    b0104n=0
    b0103p=0
    b0103n=0
    b0102p=0
    b0102n=0
    b0101p=0
    b0101n=0
    b0100a=0
    b02=0
    b0207p=0
    b0207n=0
    b0206p=0
    b0206n=0
    b0205p=0
    b0205n=0
    b0204p=0
    b0204n=0
    b0203p=0
    b0203n=0
    b0202p=0
    b0202n=0
    b0201p=0
    b0201n=0
    b0200a=0
    b03=0
    b0310a=0
    b0309p=0
    b0309n=0
    b0308p=0
    b0308n=0
    b0307p=0
    b0307n=0
    b0306p=0
    b0306n=0
    b0305p=0
    b0305n=0
    b0304p=0
    b0304n=0
    b0303p=0
    b0303n=0
    b0302p=0
    b0302n=0
    b0301p=0
    b0301n=0
    b0300a=0
    b04=0
    b0412p=0
    b0412n=0
    b0411p=0
    b0411n=0
    b0410p=0
    b0410n=0
    b0409p=0
    b0409n=0
    b0408p=0
    b0408n=0
    b0407p=0
    b0407n=0
    b0406p=0
    b0406n=0
    b0405p=0
    b0405n=0
    b0404p=0
    b0404n=0
    b0403p=0
    b0403n=0
    b0402p=0
    b0402n=0
    b0401p=0
    b0401n=0
    b0400a=0
    b05=0
    b0515a=0
    b0514p=0
    b0514n=0
    b0513p=0
    b0513n=0
    b0512p=0
    b0512n=0
    b0511p=0
    b0511n=0
    b0510p=0
    b0510n=0
    b0509p=0
    b0509n=0
    b0508p=0
    b0508n=0
    b0507p=0
    b0507n=0
    b0506p=0
    b0506n=0
    b0505p=0
    b0505n=0
    b0504p=0
    b0504n=0
    b0503p=0
    b0503n=0
    b0502p=0
    b0502n=0
    b0501p=0
    b0501n=0
    b0500a=0
    b06=0
    b0616a=0
    b0615p=0
    b0615n=0
    b0614p=0
    b0614n=0
    b0613p=0
    b0613n=0
    b0612p=0
    b0612n=0
    b0611p=0
    b0611n=0
    b0610p=0
    b0610n=0
    b0609p=0
    b0609n=0
    b0608p=0
    b0608n=0
    b0607p=0
    b0607n=0
    b0606p=0
    b0606n=0
    b0605p=0
    b0605n=0
    b0604p=0
    b0604n=0
    b0603p=0
    b0603n=0
    b0602p=0
    b0602n=0
    b0601p=0
    b0601n=0
    b0600a=0
    b07=0
    b0717p=0
    b0717n=0
    b0716p=0
    b0716n=0
    b0715p=0
    b0715n=0
    b0714p=0
    b0714n=0
    b0713p=0
    b0713n=0
    b0712p=0
    b0712n=0
    b0711p=0
    b0711n=0
    b0710p=0
    b0710n=0
    b0709p=0
    b0709n=0
    b0708p=0
    b0708n=0
    b0707p=0
    b0707n=0
    b0706p=0
    b0706n=0
    b0705p=0
    b0705n=0
    b0704p=0
    b0704n=0
    b0703p=0
    b0703n=0
    b0702p=0
    b0702n=0
    b0701p=0
    b0701n=0
    b0700a=0
    b08=0
    b0818a=0
    b0817p=0
    b0817n=0
    b0816p=0
    b0816n=0
    b0815p=0
    b0815n=0
    b0814p=0
    b0814n=0
    b0813p=0
    b0813n=0
    b0812p=0
    b0812n=0
    b0811p=0
    b0811n=0
    b0810p=0
    b0810n=0
    b0809p=0
    b0809n=0
    b0808p=0
    b0808n=0
    b0807p=0
    b0807n=0
    b0806p=0
    b0806n=0
    b0805p=0
    b0805n=0
    b0804p=0
    b0804n=0
    b0803p=0
    b0803n=0
    b0802p=0
    b0802n=0
    b0801p=0
    b0801n=0
    b0800a=0
    c00=0
    c0001p=0
    c0001n=0
    c0000a=0
    c01=0
    c0104p=0
    c0104n=0
    c0103p=0
    c0103n=0
    c0102p=0
    c0102n=0
    c0101p=0
    c0101n=0
    c0100a=0
    c02=0
    c0207p=0
    c0207n=0
    c0206p=0
    c0206n=0
    c0205p=0
    c0205n=0
    c0204p=0
    c0204n=0
    c0203p=0
    c0203n=0
    c0202p=0
    c0202n=0
    c0201p=0
    c0201n=0
    c0200a=0
    c03=0
    c0310a=0
    c0309p=0
    c0309n=0
    c0308p=0
    c0308n=0
    c0307p=0
    c0307n=0
    c0306p=0
    c0306n=0
    c0305p=0
    c0305n=0
    c0304p=0
    c0304n=0
    c0303p=0
    c0303n=0
    c0302p=0
    c0302n=0
    c0301p=0
    c0301n=0
    c0300a=0
    c04=0
    c0412p=0
    c0412n=0
    c0411p=0
    c0411n=0
    c0410p=0
    c0410n=0
    c0409p=0
    c0409n=0
    c0408p=0
    c0408n=0
    c0407p=0
    c0407n=0
    c0406p=0
    c0406n=0
    c0405p=0
    c0405n=0
    c0404p=0
    c0404n=0
    c0403p=0
    c0403n=0
    c0402p=0
    c0402n=0
    c0401p=0
    c0401n=0
    c0400a=0
    c05=0
    c0515a=0
    c0514p=0
    c0514n=0
    c0513p=0
    c0513n=0
    c0512p=0
    c0512n=0
    c0511p=0
    c0511n=0
    c0510p=0
    c0510n=0
    c0509p=0
    c0509n=0
    c0508p=0
    c0508n=0
    c0507p=0
    c0507n=0
    c0506p=0
    c0506n=0
    c0505p=0
    c0505n=0
    c0504p=0
    c0504n=0
    c0503p=0
    c0503n=0
    c0502p=0
    c0502n=0
    c0501p=0
    c0501n=0
    c0500a=0
    c06=0
    c0616a=0
    c0615p=0
    c0615n=0
    c0614p=0
    c0614n=0
    c0613p=0
    c0613n=0
    c0612p=0
    c0612n=0
    c0611p=0
    c0611n=0
    c0610p=0
    c0610n=0
    c0609p=0
    c0609n=0
    c0608p=0
    c0608n=0
    c0607p=0
    c0607n=0
    c0606p=0
    c0606n=0
    c0605p=0
    c0605n=0
    c0604p=0
    c0604n=0
    c0603p=0
    c0603n=0
    c0602p=0
    c0602n=0
    c0601p=0
    c0601n=0
    c0600a=0
    c07=0
    c0717p=0
    c0717n=0
    c0716p=0
    c0716n=0
    c0715p=0
    c0715n=0
    c0714p=0
    c0714n=0
    c0713p=0
    c0713n=0
    c0712p=0
    c0712n=0
    c0711p=0
    c0711n=0
    c0710p=0
    c0710n=0
    c0709p=0
    c0709n=0
    c0708p=0
    c0708n=0
    c0707p=0
    c0707n=0
    c0706p=0
    c0706n=0
    c0705p=0
    c0705n=0
    c0704p=0
    c0704n=0
    c0703p=0
    c0703n=0
    c0702p=0
    c0702n=0
    c0701p=0
    c0701n=0
    c0700a=0
    c08=0
    c0818a=0
    c0817p=0
    c0817n=0
    c0816p=0
    c0816n=0
    c0815p=0
    c0815n=0
    c0814p=0
    c0814n=0
    c0813p=0
    c0813n=0
    c0812p=0
    c0812n=0
    c0811p=0
    c0811n=0
    c0810p=0
    c0810n=0
    c0809p=0
    c0809n=0
    c0808p=0
    c0808n=0
    c0807p=0
    c0807n=0
    c0806p=0
    c0806n=0
    c0805p=0
    c0805n=0
    c0804p=0
    c0804n=0
    c0803p=0
    c0803n=0
    c0802p=0
    c0802n=0
    c0801p=0
    c0801n=0
    c0800a=0
    liii=""
    cccow=0
    
    print("------------")
    print("Start_counting")
    # Count No. of inital particles of each olientation angles 
    with open(cpass+"/"+datas, mode='r') as g:
        for line in g:
            
            # Progress bar
            cccow+=1
            if cccow > 99999:
                sys.stdout.write(".")
                sys.stdout.flush()
                cccow=0
                pass
            
            # Exclude header line
            if line[0] == " ":
                lrotno=""
                ltiltno=""
                lpsino=""
                til=""
                rot=""
                csvgl=line.split()
                if len(csvgl) < rotno:
                    pass
                else:
                    # Extract rotation angle & tilt angle
                    lrotno=csvgl[rotno].strip()
                    ltiltno=csvgl[tiltno].strip()
                    lpsino=csvgl[psino].strip()
                    rot=float(lrotno)
                    til=float(ltiltno)
                    # Branching by rotation angle & tilt angle
                    if til <= 10:
                        b00 +=1
                        if rot > 60:
                            b0001p +=1
                            pass
                        elif rot < -60:
                            b0001n +=1
                            pass
                        else:
                            b0000a +=1
                            pass
                        pass
                    elif til <= 20:
                        b01 +=1
                        if rot > 140:
                            b0104p +=1
                            pass
                        elif rot < -140:
                            b0104n +=1
                            pass
                        elif rot > 100:
                            b0103p +=1
                            pass
                        elif rot < -100:
                            b0103n +=1
                            pass
                        elif rot > 60:
                            b0102p +=1
                            pass
                        elif rot < -60:
                            b0102n +=1
                            pass
                        elif rot > 20:
                            b0101p +=1
                            pass
                        elif rot < -20:
                            b0101n +=1
                            pass
                        else:
                            b0100a +=1
                            pass
                        pass
                    elif til <= 30:
                        b02 +=1
                        if rot > 156:
                            b0207p +=1
                            pass
                        elif rot < -156:
                            b0207n +=1
                            pass
                        elif rot > 132:
                            b0206p +=1
                            pass
                        elif rot < -132:
                            b0206n +=1
                            pass
                        elif rot > 108:
                            b0205p +=1
                            pass
                        elif rot < -108:
                            b0205n +=1
                            pass
                        elif rot > 84:
                            b0204p +=1
                            pass
                        elif rot < -84:
                            b0204n +=1
                            pass
                        elif rot > 60:
                            b0203p +=1
                            pass
                        elif rot < -60:
                            b0203n +=1
                            pass
                        elif rot > 36:
                            b0202p +=1
                            pass
                        elif rot < -36:
                            b0202n +=1
                            pass
                        elif rot > 12:
                            b0201p +=1
                            pass
                        elif rot < -12:
                            b0201n +=1
                            pass
                        else:
                            b0200a +=1
                            pass
                        pass
                    elif til <= 40:
                        b03 +=1
                        if rot > 171:
                            b0310a +=1
                            pass
                        elif rot < -171:
                            b0310a +=1
                            pass
                        elif rot > 153:
                            b0309p +=1
                            pass
                        elif rot < -153:
                            b0309n +=1
                            pass
                        elif rot > 135:
                            b0308p +=1
                            pass
                        elif rot < -135:
                            b0308n +=1
                            pass
                        elif rot > 117:
                            b0307p +=1
                            pass
                        elif rot < -117:
                            b0307n +=1
                            pass
                        elif rot > 99:
                            b0306p +=1
                            pass
                        elif rot < -99:
                            b0306n +=1
                            pass
                        elif rot > 81:
                            b0305p +=1
                            pass
                        elif rot < -81:
                            b0305n +=1
                            pass
                        elif rot > 63:
                            b0304p +=1
                            pass
                        elif rot < -63:
                            b0304n +=1
                            pass
                        elif rot > 45:
                            b0303p +=1
                            pass
                        elif rot < -45:
                            b0303n +=1
                            pass
                        elif rot > 27:
                            b0302p +=1
                            pass
                        elif rot < -27:
                            b0302n +=1
                            pass
                        elif rot > 9:
                            b0301p +=1
                            pass
                        elif rot < -9:
                            b0301n +=1
                            pass
                        else:
                            b0300a +=1
                            pass
                    elif til <= 50:
                        b04 +=1
                        if rot > 165.6:
                            b0412p +=1
                            pass
                        elif rot < -165.6:
                            b0412n +=1
                            pass
                        elif rot > 151.2:
                            b0411p +=1
                            pass
                        elif rot < -151.2:
                            b0411n +=1
                            pass
                        elif rot > 136.8:
                            b0410p +=1
                            pass
                        elif rot < -136.8:
                            b0410n +=1
                            pass
                        elif rot > 122.4:
                            b0409p +=1
                            pass
                        elif rot < -122.4:
                            b0409n +=1
                            pass
                        elif rot > 108:
                            b0408p +=1
                            pass
                        elif rot < -108:
                            b0408n +=1
                            pass
                        elif rot > 93.6:
                            b0407p +=1
                            pass
                        elif rot < -93.6:
                            b0407n +=1
                            pass
                        elif rot > 79.2:
                            b0406p +=1
                            pass
                        elif rot < -79.2:
                            b0406n +=1
                            pass
                        elif rot > 64.8:
                            b0405p +=1
                            pass
                        elif rot < -64.8:
                            b0405n +=1
                            pass
                        elif rot > 50.4:
                            b0404p +=1
                            pass
                        elif rot < -50.4:
                            b0404n +=1
                            pass
                        elif rot > 36:
                            b0403p +=1
                            pass
                        elif rot < -36:
                            b0403n +=1
                            pass
                        elif rot > 21.6:
                            b0402p +=1
                            pass
                        elif rot < -21.6:
                            b0402n +=1
                            pass
                        elif rot > 7.2:
                            b0401p +=1
                            pass
                        elif rot < -7.2:
                            b0401n +=1
                            pass
                        else:
                            b0400a +=1
                            pass
                    elif til <= 60:
                        b05 +=1
                        if rot > 174:
                            b0515a +=1
                            pass
                        elif rot < -174:
                            b0515a +=1
                            pass
                        elif rot > 162:
                            b0514p +=1
                            pass
                        elif rot < -162:
                            b0514n +=1
                            pass
                        elif rot > 150:
                            b0513p +=1
                            pass
                        elif rot < -150:
                            b0513n +=1
                            pass
                        elif rot > 138:
                            b0512p +=1
                            pass
                        elif rot < -138:
                            b0512n +=1
                            pass
                        elif rot > 126:
                            b0511p +=1
                            pass
                        elif rot < -126:
                            b0511n +=1
                            pass
                        elif rot > 114:
                            b0510p +=1
                            pass
                        elif rot < -114:
                            b0510n +=1
                            pass
                        elif rot > 102:
                            b0509p +=1
                            pass
                        elif rot < -102:
                            b0509n +=1
                            pass
                        elif rot > 90:
                            b0508p +=1
                            pass
                        elif rot < -90:
                            b0508n +=1
                            pass
                        elif rot > 78:
                            b0507p +=1
                            pass
                        elif rot < -78:
                            b0507n +=1
                            pass
                        elif rot > 66:
                            b0506p +=1
                            pass
                        elif rot < -66:
                            b0506n +=1
                            pass
                        elif rot > 54:
                            b0505p +=1
                            pass
                        elif rot < -54:
                            b0505n +=1
                            pass
                        elif rot > 42:
                            b0504p +=1
                            pass
                        elif rot < -42:
                            b0504n +=1
                            pass
                        elif rot > 30:
                            b0503p +=1
                            pass
                        elif rot < -30:
                            b0503n +=1
                            pass
                        elif rot > 18:
                            b0502p +=1
                            pass
                        elif rot < -18:
                            b0502n +=1
                            pass
                        elif rot > 6:
                            b0501p +=1
                            pass
                        elif rot < -6:
                            b0501n +=1
                            pass
                        else:
                            b0500a +=1
                            pass
                    elif til <= 70:
                        b06 +=1
                        if rot > 174.375:
                            b0616a +=1
                            pass
                        elif rot < -174.375:
                            b0616a +=1
                            pass
                        elif rot > 163.125:
                            b0615p +=1
                            pass
                        elif rot < -163.125:
                            b0615n +=1
                            pass
                        elif rot > 151.875:
                            b0614p +=1
                            pass
                        elif rot < -151.875:
                            b0614n +=1
                            pass
                        elif rot > 140.625:
                            b0613p +=1
                            pass
                        elif rot < -140.625:
                            b0613n +=1
                            pass
                        elif rot > 129.375:
                            b0612p +=1
                            pass
                        elif rot < -129.375:
                            b0612n +=1
                            pass
                        elif rot > 118.125:
                            b0611p +=1
                            pass
                        elif rot < -118.125:
                            b0611n +=1
                            pass
                        elif rot > 106.875:
                            b0610p +=1
                            pass
                        elif rot < -106.875:
                            b0610n +=1
                            pass
                        elif rot > 95.625:
                            b0609p +=1
                            pass
                        elif rot < -95.625:
                            b0609n +=1
                            pass
                        elif rot > 84.375:
                            b0608p +=1
                            pass
                        elif rot < -84.375:
                            b0608n +=1
                            pass
                        elif rot > 73.125:
                            b0607p +=1
                            pass
                        elif rot < -73.125:
                            b0607n +=1
                            pass
                        elif rot > 61.875:
                            b0606p +=1
                            pass
                        elif rot < -61.875:
                            b0606n +=1
                            pass
                        elif rot > 50.625:
                            b0605p +=1
                            pass
                        elif rot < -50.625:
                            b0605n +=1
                            pass
                        elif rot > 39.375:
                            b0604p +=1
                            pass
                        elif rot < -39.375:
                            b0604n +=1
                            pass
                        elif rot > 28.125:
                            b0603p +=1
                            pass
                        elif rot < -28.125:
                            b0603n +=1
                            pass
                        elif rot > 16.875:
                            b0602p +=1
                            pass
                        elif rot < -16.875:
                            b0602n +=1
                            pass
                        elif rot > 5.625:
                            b0601p +=1
                            pass
                        elif rot < -5.625:
                            b0601n +=1
                            pass
                        else:
                            b0600a +=1
                            pass
                    elif til <= 80:
                        b07 +=1
                        if rot > 169.714:
                            b0717p +=1
                            pass
                        elif rot < -169.714:
                            b0717n +=1
                            pass
                        elif rot > 159.429:
                            b0716p +=1
                            pass
                        elif rot < -159.429:
                            b0716n +=1
                            pass
                        elif rot > 149.143:
                            b0715p +=1
                            pass
                        elif rot < -149.143:
                            b0715n +=1
                            pass
                        elif rot > 138.857:
                            b0714p +=1
                            pass
                        elif rot < -138.857:
                            b0714n +=1
                            pass
                        elif rot > 128.571:
                            b0713p +=1
                            pass
                        elif rot < -128.571:
                            b0713n +=1
                            pass
                        elif rot > 118.286:
                            b0712p +=1
                            pass
                        elif rot < -118.286:
                            b0712n +=1
                            pass
                        elif rot > 108:
                            b0711p +=1
                            pass
                        elif rot < -108:
                            b0711n +=1
                            pass
                        elif rot > 97.7143:
                            b0710p +=1
                            pass
                        elif rot < -97.7143:
                            b0710n +=1
                            pass
                        elif rot > 87.4286:
                            b0709p +=1
                            pass
                        elif rot < -87.4286:
                            b0709n +=1
                            pass
                        elif rot > 77.1429:
                            b0708p +=1
                            pass
                        elif rot < -77.2429:
                            b0708n +=1
                            pass
                        elif rot > 66.8571:
                            b0707p +=1
                            pass
                        elif rot < -66.8571:
                            b0707n +=1
                            pass
                        elif rot > 56.5714:
                            b0706p +=1
                            pass
                        elif rot < -56.5714:
                            b0706n +=1
                            pass
                        elif rot > 46.2857:
                            b0705p +=1
                            pass
                        elif rot < -46.2857:
                            b0705n +=1
                            pass
                        elif rot > 36:
                            b0704p +=1
                            pass
                        elif rot < -36:
                            b0704n +=1
                            pass
                        elif rot > 25.7143:
                            b0703p +=1
                            pass
                        elif rot < -25.7143:
                            b0703n +=1
                            pass
                        elif rot > 15.4286:
                            b0702p +=1
                            pass
                        elif rot < -15.4826:
                            b0702n +=1
                            pass
                        elif rot > 5.14286:
                            b0701p +=1
                            pass
                        elif rot < -5.24286:
                            b0701n +=1
                            pass
                        else:
                            b0700a +=1
                            pass
                    elif til <= 90:
                        b08 +=1
                        if rot > 175:
                            b0818a +=1
                            pass
                        elif rot < -175:
                            b0818a +=1
                            pass
                        elif rot > 165:
                            b0817p +=1
                            pass
                        elif rot < -165:
                            b0817n +=1
                            pass
                        elif rot > 155:
                            b0816p +=1
                            pass
                        elif rot < -155:
                            b0816n +=1
                            pass
                        elif rot > 145:
                            b0815p +=1
                            pass
                        elif rot < -145:
                            b0815n +=1
                            pass
                        elif rot > 135:
                            b0814p +=1
                            pass
                        elif rot < -135:
                            b0814n +=1
                            pass
                        elif rot > 125:
                            b0813p +=1
                            pass
                        elif rot < -125:
                            b0813n +=1
                            pass
                        elif rot > 115:
                            b0812p +=1
                            pass
                        elif rot < -115:
                            b0812n +=1
                            pass
                        elif rot > 105:
                            b0811p +=1
                            pass
                        elif rot < -105:
                            b0811n +=1
                            pass
                        elif rot > 95:
                            b0810p +=1
                            pass
                        elif rot < -95:
                            b0810n +=1
                            pass
                        elif rot > 85:
                            b0809p +=1
                            pass
                        elif rot < -85:
                            b0809n +=1
                            pass
                        elif rot > 75:
                            b0808p +=1
                            pass
                        elif rot < -75:
                            b0808n +=1
                            pass
                        elif rot > 65:
                            b0807p +=1
                            pass
                        elif rot < -65:
                            b0807n +=1
                            pass
                        elif rot > 55:
                            b0806p +=1
                            pass
                        elif rot < -55:
                            b0806n +=1
                            pass
                        elif rot > 45:
                            b0805p +=1
                            pass
                        elif rot < -45:
                            b0805n +=1
                            pass
                        elif rot > 35:
                            b0804p +=1
                            pass
                        elif rot < -35:
                            b0804n +=1
                            pass
                        elif rot > 25:
                            b0803p +=1
                            pass
                        elif rot < -25:
                            b0803n +=1
                            pass
                        elif rot > 15:
                            b0802p +=1
                            pass
                        elif rot < -15:
                            b0802n +=1
                            pass
                        elif rot > 5:
                            b0801p +=1
                            pass
                        elif rot < -5:
                            b0801n +=1
                            pass
                        else:
                            b0800a +=1
                            pass
                    elif til <= 100:
                        c08 +=1
                        if rot > 175:
                            c0818a +=1
                            pass
                        elif rot < -175:
                            c0818a +=1
                            pass
                        elif rot > 165:
                            c0817p +=1
                            pass
                        elif rot < -165:
                            c0817n +=1
                            pass
                        elif rot > 155:
                            c0816p +=1
                            pass
                        elif rot < -155:
                            c0816n +=1
                            pass
                        elif rot > 145:
                            c0815p +=1
                            pass
                        elif rot < -145:
                            c0815n +=1
                            pass
                        elif rot > 135:
                            c0814p +=1
                            pass
                        elif rot < -135:
                            c0814n +=1
                            pass
                        elif rot > 125:
                            c0813p +=1
                            pass
                        elif rot < -125:
                            c0813n +=1
                            pass
                        elif rot > 115:
                            c0812p +=1
                            pass
                        elif rot < -115:
                            c0812n +=1
                            pass
                        elif rot > 105:
                            c0811p +=1
                            pass
                        elif rot < -105:
                            c0811n +=1
                            pass
                        elif rot > 95:
                            c0810p +=1
                            pass
                        elif rot < -95:
                            c0810n +=1
                            pass
                        elif rot > 85:
                            c0809p +=1
                            pass
                        elif rot < -85:
                            c0809n +=1
                            pass
                        elif rot > 75:
                            c0808p +=1
                            pass
                        elif rot < -75:
                            c0808n +=1
                            pass
                        elif rot > 65:
                            c0807p +=1
                            pass
                        elif rot < -65:
                            c0807n +=1
                            pass
                        elif rot > 55:
                            c0806p +=1
                            pass
                        elif rot < -55:
                            c0806n +=1
                            pass
                        elif rot > 45:
                            c0805p +=1
                            pass
                        elif rot < -45:
                            c0805n +=1
                            pass
                        elif rot > 35:
                            c0804p +=1
                            pass
                        elif rot < -35:
                            c0804n +=1
                            pass
                        elif rot > 25:
                            c0803p +=1
                            pass
                        elif rot < -25:
                            c0803n +=1
                            pass
                        elif rot > 15:
                            c0802p +=1
                            pass
                        elif rot < -15:
                            c0802n +=1
                            pass
                        elif rot > 5:
                            c0801p +=1
                            pass
                        elif rot < -5:
                            c0801n +=1
                            pass
                        else:
                            c0800a +=1
                            pass
                    elif til <= 110:
                        c07 +=1
                        if rot > 169.714:
                            c0717p +=1
                            pass
                        elif rot < -169.714:
                            c0717n +=1
                            pass
                        elif rot > 159.429:
                            c0716p +=1
                            pass
                        elif rot < -159.429:
                            c0716n +=1
                            pass
                        elif rot > 149.143:
                            c0715p +=1
                            pass
                        elif rot < -149.143:
                            c0715n +=1
                            pass
                        elif rot > 138.857:
                            c0714p +=1
                            pass
                        elif rot < -138.857:
                            c0714n +=1
                            pass
                        elif rot > 128.571:
                            c0713p +=1
                            pass
                        elif rot < -128.571:
                            c0713n +=1
                            pass
                        elif rot > 118.286:
                            c0712p +=1
                            pass
                        elif rot < -118.286:
                            c0712n +=1
                            pass
                        elif rot > 108:
                            c0711p +=1
                            pass
                        elif rot < -108:
                            c0711n +=1
                            pass
                        elif rot > 97.7143:
                            c0710p +=1
                            pass
                        elif rot < -97.7143:
                            c0710n +=1
                            pass
                        elif rot > 87.4286:
                            c0709p +=1
                            pass
                        elif rot < -87.4286:
                            c0709n +=1
                            pass
                        elif rot > 77.1429:
                            c0708p +=1
                            pass
                        elif rot < -77.2429:
                            c0708n +=1
                            pass
                        elif rot > 66.8571:
                            c0707p +=1
                            pass
                        elif rot < -66.8571:
                            c0707n +=1
                            pass
                        elif rot > 56.5714:
                            c0706p +=1
                            pass
                        elif rot < -56.5714:
                            c0706n +=1
                            pass
                        elif rot > 46.2857:
                            c0705p +=1
                            pass
                        elif rot < -46.2857:
                            c0705n +=1
                            pass
                        elif rot > 36:
                            c0704p +=1
                            pass
                        elif rot < -36:
                            c0704n +=1
                            pass
                        elif rot > 25.7143:
                            c0703p +=1
                            pass
                        elif rot < -25.7143:
                            c0703n +=1
                            pass
                        elif rot > 15.4286:
                            c0702p +=1
                            pass
                        elif rot < -15.4826:
                            c0702n +=1
                            pass
                        elif rot > 5.14286:
                            c0701p +=1
                            pass
                        elif rot < -5.24286:
                            c0701n +=1
                            pass
                        else:
                            c0700a +=1
                            pass
                    elif til <= 120:
                        c06 +=1
                        if rot > 174.375:
                            c0616a +=1
                            pass
                        elif rot < -174.375:
                            c0616a +=1
                            pass
                        elif rot > 163.125:
                            c0615p +=1
                            pass
                        elif rot < -163.125:
                            c0615n +=1
                            pass
                        elif rot > 151.875:
                            c0614p +=1
                            pass
                        elif rot < -151.875:
                            c0614n +=1
                            pass
                        elif rot > 140.625:
                            c0613p +=1
                            pass
                        elif rot < -140.625:
                            c0613n +=1
                            pass
                        elif rot > 129.375:
                            c0612p +=1
                            pass
                        elif rot < -129.375:
                            c0612n +=1
                            pass
                        elif rot > 118.125:
                            c0611p +=1
                            pass
                        elif rot < -118.125:
                            c0611n +=1
                            pass
                        elif rot > 106.875:
                            c0610p +=1
                            pass
                        elif rot < -106.875:
                            c0610n +=1
                            pass
                        elif rot > 95.625:
                            c0609p +=1
                            pass
                        elif rot < -95.625:
                            c0609n +=1
                            pass
                        elif rot > 84.375:
                            c0608p +=1
                            pass
                        elif rot < -84.375:
                            c0608n +=1
                            pass
                        elif rot > 73.125:
                            c0607p +=1
                            pass
                        elif rot < -73.125:
                            c0607n +=1
                            pass
                        elif rot > 61.875:
                            c0606p +=1
                            pass
                        elif rot < -61.875:
                            c0606n +=1
                            pass
                        elif rot > 50.625:
                            c0605p +=1
                            pass
                        elif rot < -50.625:
                            c0605n +=1
                            pass
                        elif rot > 39.375:
                            c0604p +=1
                            pass
                        elif rot < -39.375:
                            c0604n +=1
                            pass
                        elif rot > 28.125:
                            c0603p +=1
                            pass
                        elif rot < -28.125:
                            c0603n +=1
                            pass
                        elif rot > 16.875:
                            c0602p +=1
                            pass
                        elif rot < -16.875:
                            c0602n +=1
                            pass
                        elif rot > 5.625:
                            c0601p +=1
                            pass
                        elif rot < -5.625:
                            c0601n +=1
                            pass
                        else:
                            c0600a +=1
                            pass
                    elif til <= 130:
                        c05 +=1
                        if rot > 174:
                            c0515a +=1
                            pass
                        elif rot < -174:
                            c0515a +=1
                            pass
                        elif rot > 162:
                            c0514p +=1
                            pass
                        elif rot < -162:
                            c0514n +=1
                            pass
                        elif rot > 150:
                            c0513p +=1
                            pass
                        elif rot < -150:
                            c0513n +=1
                            pass
                        elif rot > 138:
                            c0512p +=1
                            pass
                        elif rot < -138:
                            c0512n +=1
                            pass
                        elif rot > 126:
                            c0511p +=1
                            pass
                        elif rot < -126:
                            c0511n +=1
                            pass
                        elif rot > 114:
                            c0510p +=1
                            pass
                        elif rot < -114:
                            c0510n +=1
                            pass
                        elif rot > 102:
                            c0509p +=1
                            pass
                        elif rot < -102:
                            c0509n +=1
                            pass
                        elif rot > 90:
                            c0508p +=1
                            pass
                        elif rot < -90:
                            c0508n +=1
                            pass
                        elif rot > 78:
                            c0507p +=1
                            pass
                        elif rot < -78:
                            c0507n +=1
                            pass
                        elif rot > 66:
                            c0506p +=1
                            pass
                        elif rot < -66:
                            c0506n +=1
                            pass
                        elif rot > 54:
                            c0505p +=1
                            pass
                        elif rot < -54:
                            c0505n +=1
                            pass
                        elif rot > 42:
                            c0504p +=1
                            pass
                        elif rot < -42:
                            c0504n +=1
                            pass
                        elif rot > 30:
                            c0503p +=1
                            pass
                        elif rot < -30:
                            c0503n +=1
                            pass
                        elif rot > 18:
                            c0502p +=1
                            pass
                        elif rot < -18:
                            c0502n +=1
                            pass
                        elif rot > 6:
                            c0501p +=1
                            pass
                        elif rot < -6:
                            c0501n +=1
                            pass
                        else:
                            c0500a +=1
                            pass
                    elif til <= 140:
                        c04 +=1
                        if rot > 165.6:
                            c0412p +=1
                            pass
                        elif rot < -165.6:
                            c0412n +=1
                            pass
                        elif rot > 151.2:
                            c0411p +=1
                            pass
                        elif rot < -151.2:
                            c0411n +=1
                            pass
                        elif rot > 136.8:
                            c0410p +=1
                            pass
                        elif rot < -136.8:
                            c0410n +=1
                            pass
                        elif rot > 122.4:
                            c0409p +=1
                            pass
                        elif rot < -122.4:
                            c0409n +=1
                            pass
                        elif rot > 108:
                            c0408p +=1
                            pass
                        elif rot < -108:
                            c0408n +=1
                            pass
                        elif rot > 93.6:
                            c0407p +=1
                            pass
                        elif rot < -93.6:
                            c0407n +=1
                            pass
                        elif rot > 79.2:
                            c0406p +=1
                            pass
                        elif rot < -79.2:
                            c0406n +=1
                            pass
                        elif rot > 64.8:
                            c0405p +=1
                            pass
                        elif rot < -64.8:
                            c0405n +=1
                            pass
                        elif rot > 50.4:
                            c0404p +=1
                            pass
                        elif rot < -50.4:
                            c0404n +=1
                            pass
                        elif rot > 36:
                            c0403p +=1
                            pass
                        elif rot < -36:
                            c0403n +=1
                            pass
                        elif rot > 21.6:
                            c0402p +=1
                            pass
                        elif rot < -21.6:
                            c0402n +=1
                            pass
                        elif rot > 7.2:
                            c0401p +=1
                            pass
                        elif rot < -7.2:
                            c0401n +=1
                            pass
                        else:
                            c0400a +=1
                            pass
                    elif til <= 150:
                        c03 +=1
                        if rot > 171:
                            c0310a +=1
                            pass
                        elif rot < -171:
                            c0310a +=1
                            pass
                        elif rot > 153:
                            c0309p +=1
                            pass
                        elif rot < -153:
                            c0309n +=1
                            pass
                        elif rot > 135:
                            c0308p +=1
                            pass
                        elif rot < -135:
                            c0308n +=1
                            pass
                        elif rot > 117:
                            c0307p +=1
                            pass
                        elif rot < -117:
                            c0307n +=1
                            pass
                        elif rot > 99:
                            c0306p +=1
                            pass
                        elif rot < -99:
                            c0306n +=1
                            pass
                        elif rot > 81:
                            c0305p +=1
                            pass
                        elif rot < -81:
                            c0305n +=1
                            pass
                        elif rot > 63:
                            c0304p +=1
                            pass
                        elif rot < -63:
                            c0304n +=1
                            pass
                        elif rot > 45:
                            c0303p +=1
                            pass
                        elif rot < -45:
                            c0303n +=1
                            pass
                        elif rot > 27:
                            c0302p +=1
                            pass
                        elif rot < -27:
                            c0302n +=1
                            pass
                        elif rot > 9:
                            c0301p +=1
                            pass
                        elif rot < -9:
                            c0301n +=1
                            pass
                        else:
                            c0300a +=1
                            pass
                    elif til <= 160:
                        c02 +=1
                        if rot > 156:
                            c0207p +=1
                            pass
                        elif rot < -156:
                            c0207n +=1
                            pass
                        elif rot > 132:
                            c0206p +=1
                            pass
                        elif rot < -132:
                            c0206n +=1
                            pass
                        elif rot > 108:
                            c0205p +=1
                            pass
                        elif rot < -108:
                            c0205n +=1
                            pass
                        elif rot > 84:
                            c0204p +=1
                            pass
                        elif rot < -84:
                            c0204n +=1
                            pass
                        elif rot > 60:
                            c0203p +=1
                            pass
                        elif rot < -60:
                            c0203n +=1
                            pass
                        elif rot > 36:
                            c0202p +=1
                            pass
                        elif rot < -36:
                            c0202n +=1
                            pass
                        elif rot > 12:
                            c0201p +=1
                            pass
                        elif rot < -12:
                            c0201n +=1
                            pass
                        else:
                            c0200a +=1
                            pass
                    elif til <= 170:
                        c01 +=1
                        if rot > 140:
                            c0104p +=1
                            pass
                        elif rot < -140:
                            c0104n +=1
                            pass
                        elif rot > 100:
                            c0103p +=1
                            pass
                        elif rot < -100:
                            c0103n +=1
                            pass
                        elif rot > 60:
                            c0102p +=1
                            pass
                        elif rot < -60:
                            c0102n +=1
                            pass
                        elif rot > 20:
                            c0101p +=1
                            pass
                        elif rot < -20:
                            c0101n +=1
                            pass
                        else:
                            c0100a +=1
                            pass
                        pass
                    else:
                        c00 +=1
                        if rot > 60:
                            c0001p +=1
                            pass
                        elif rot < -60:
                            c0001n +=1
                            pass
                        else:
                            c0000a +=1
                            pass
                        pass
                    pass
                pass
            pass
        pass
    print("Complete.")
    print("------------")
    lil=""
    lil+=str(b0000a)+","+str(b0001p)+"\n"
    lil+=str(b0100a)+","+str(b0101p)+","+str(b0102p)+","+str(b0103p)+","+str(b0104p)+"\n"
    lil+=str(b0200a)+","+str(b0201p)+","+str(b0202p)+","+str(b0203p)+","+str(b0204p)+","+str(b0205p)+","+str(b0206p)+","+str(b0207p)+"\n"
    lil+=str(b0300a)+","+str(b0301p)+","+str(b0302p)+","+str(b0303p)+","+str(b0304p)+","+str(b0305p)+","+str(b0306p)+","+str(b0307p)+","+str(b0308p)+","+str(b0309p)+","+str(b0310a)+"\n"
    lil+=str(b0400a)+","+str(b0401p)+","+str(b0402p)+","+str(b0403p)+","+str(b0404p)+","+str(b0405p)+","+str(b0406p)+","+str(b0407p)+","+str(b0408p)+","+str(b0409p)+","+str(b0410p)+","+str(b0411p)+","+str(b0412p)+"\n"
    lil+=str(b0500a)+","+str(b0501p)+","+str(b0502p)+","+str(b0503p)+","+str(b0504p)+","+str(b0505p)+","+str(b0506p)+","+str(b0507p)+","+str(b0508p)+","+str(b0509p)+","+str(b0510p)+","+str(b0511p)+","+str(b0512p)+","+str(b0513p)+","+str(b0514p)+","+str(b0515a)+"\n"
    lil+=str(b0600a)+","+str(b0601p)+","+str(b0602p)+","+str(b0603p)+","+str(b0604p)+","+str(b0605p)+","+str(b0606p)+","+str(b0607p)+","+str(b0608p)+","+str(b0609p)+","+str(b0610p)+","+str(b0611p)+","+str(b0612p)+","+str(b0613p)+","+str(b0614p)+","+str(b0615p)+","+str(b0616a)+"\n"
    lil+=str(b0700a)+","+str(b0701p)+","+str(b0702p)+","+str(b0703p)+","+str(b0704p)+","+str(b0705p)+","+str(b0706p)+","+str(b0707p)+","+str(b0708p)+","+str(b0709p)+","+str(b0710p)+","+str(b0711p)+","+str(b0712p)+","+str(b0713p)+","+str(b0714p)+","+str(b0715p)+","+str(b0716p)+","+str(b0717p)+"\n"
    lil+=str(b0800a)+","+str(b0801p)+","+str(b0802p)+","+str(b0803p)+","+str(b0804p)+","+str(b0805p)+","+str(b0806p)+","+str(b0807p)+","+str(b0808p)+","+str(b0809p)+","+str(b0810p)+","+str(b0811p)+","+str(b0812p)+","+str(b0813p)+","+str(b0814p)+","+str(b0815p)+","+str(b0816p)+","+str(b0817p)+","+str(b0818a)+"\n"
    lil+=str(c0800a)+","+str(c0801p)+","+str(c0802p)+","+str(c0803p)+","+str(c0804p)+","+str(c0805p)+","+str(c0806p)+","+str(c0807p)+","+str(c0808p)+","+str(c0809p)+","+str(c0810p)+","+str(c0811p)+","+str(c0812p)+","+str(c0813p)+","+str(c0814p)+","+str(c0815p)+","+str(c0816p)+","+str(c0817p)+","+str(c0818a)+"\n"
    lil+=str(c0700a)+","+str(c0701p)+","+str(c0702p)+","+str(c0703p)+","+str(c0704p)+","+str(c0705p)+","+str(c0706p)+","+str(c0707p)+","+str(c0708p)+","+str(c0709p)+","+str(c0710p)+","+str(c0711p)+","+str(c0712p)+","+str(c0713p)+","+str(c0714p)+","+str(c0715p)+","+str(c0716p)+","+str(c0717p)+"\n"
    lil+=str(c0600a)+","+str(c0601p)+","+str(c0602p)+","+str(c0603p)+","+str(c0604p)+","+str(c0605p)+","+str(c0606p)+","+str(c0607p)+","+str(c0608p)+","+str(c0609p)+","+str(c0610p)+","+str(c0611p)+","+str(c0612p)+","+str(c0613p)+","+str(c0614p)+","+str(c0615p)+","+str(c0616a)+"\n"
    lil+=str(c0500a)+","+str(c0501p)+","+str(c0502p)+","+str(c0503p)+","+str(c0504p)+","+str(c0505p)+","+str(c0506p)+","+str(c0507p)+","+str(c0508p)+","+str(c0509p)+","+str(c0510p)+","+str(c0511p)+","+str(c0512p)+","+str(c0513p)+","+str(c0514p)+","+str(c0515a)+"\n"
    lil+=str(c0400a)+","+str(c0401p)+","+str(c0402p)+","+str(c0403p)+","+str(c0404p)+","+str(c0405p)+","+str(c0406p)+","+str(c0407p)+","+str(c0408p)+","+str(c0409p)+","+str(c0410p)+","+str(c0411p)+","+str(c0412p)+"\n"
    lil+=str(c0300a)+","+str(c0301p)+","+str(c0302p)+","+str(c0303p)+","+str(c0304p)+","+str(c0305p)+","+str(c0306p)+","+str(c0307p)+","+str(c0308p)+","+str(c0309p)+","+str(c0310a)+"\n"
    lil+=str(c0200a)+","+str(c0201p)+","+str(c0202p)+","+str(c0203p)+","+str(c0204p)+","+str(c0205p)+","+str(c0206p)+","+str(c0207p)+"\n"
    lil+=str(c0100a)+","+str(c0101p)+","+str(c0102p)+","+str(c0103p)+","+str(c0104p)+"\n"
    lil+=str(c0000a)+","+str(c0001p)+"\n"
    lil+="\n"
    lil+="\n"
    lil+=","+str(b0001n)+"\n"
    lil+=","+str(b0101n)+","+str(b0102n)+","+str(b0103n)+","+str(b0104n)+"\n"
    lil+=","+str(b0201n)+","+str(b0202n)+","+str(b0203n)+","+str(b0204n)+","+str(b0205n)+","+str(b0206n)+","+str(b0207n)+"\n"
    lil+=","+str(b0301n)+","+str(b0302n)+","+str(b0303n)+","+str(b0304n)+","+str(b0305n)+","+str(b0306n)+","+str(b0307n)+","+str(b0308n)+","+str(b0309n)+"\n"
    lil+=","+str(b0401n)+","+str(b0402n)+","+str(b0403n)+","+str(b0404n)+","+str(b0405n)+","+str(b0406n)+","+str(b0407n)+","+str(b0408n)+","+str(b0409n)+","+str(b0410n)+","+str(b0411n)+","+str(b0412n)+"\n"
    lil+=","+str(b0501n)+","+str(b0502n)+","+str(b0503n)+","+str(b0504n)+","+str(b0505n)+","+str(b0506n)+","+str(b0507n)+","+str(b0508n)+","+str(b0509n)+","+str(b0510n)+","+str(b0511n)+","+str(b0512n)+","+str(b0513n)+","+str(b0514n)+"\n"
    lil+=","+str(b0601n)+","+str(b0602n)+","+str(b0603n)+","+str(b0604n)+","+str(b0605n)+","+str(b0606n)+","+str(b0607n)+","+str(b0608n)+","+str(b0609n)+","+str(b0610n)+","+str(b0611n)+","+str(b0612n)+","+str(b0613n)+","+str(b0614n)+","+str(b0615n)+"\n"
    lil+=","+str(b0701n)+","+str(b0702n)+","+str(b0703n)+","+str(b0704n)+","+str(b0705n)+","+str(b0706n)+","+str(b0707n)+","+str(b0708n)+","+str(b0709n)+","+str(b0710n)+","+str(b0711n)+","+str(b0712n)+","+str(b0713n)+","+str(b0714n)+","+str(b0715n)+","+str(b0716n)+","+str(b0717n)+"\n"
    lil+=","+str(b0801n)+","+str(b0802n)+","+str(b0803n)+","+str(b0804n)+","+str(b0805n)+","+str(b0806n)+","+str(b0807n)+","+str(b0808n)+","+str(b0809n)+","+str(b0810n)+","+str(b0811n)+","+str(b0812n)+","+str(b0813n)+","+str(b0814n)+","+str(b0815n)+","+str(b0816n)+","+str(b0817n)+"\n"
    lil+=","+str(c0801n)+","+str(c0802n)+","+str(c0803n)+","+str(c0804n)+","+str(c0805n)+","+str(c0806n)+","+str(c0807n)+","+str(c0808n)+","+str(c0809n)+","+str(c0810n)+","+str(c0811n)+","+str(c0812n)+","+str(c0813n)+","+str(c0814n)+","+str(c0815n)+","+str(c0816n)+","+str(c0817n)+"\n"
    lil+=","+str(c0701n)+","+str(c0702n)+","+str(c0703n)+","+str(c0704n)+","+str(c0705n)+","+str(c0706n)+","+str(c0707n)+","+str(c0708n)+","+str(c0709n)+","+str(c0710n)+","+str(c0711n)+","+str(c0712n)+","+str(c0713n)+","+str(c0714n)+","+str(c0715n)+","+str(c0716n)+","+str(c0717n)+"\n"
    lil+=","+str(c0601n)+","+str(c0602n)+","+str(c0603n)+","+str(c0604n)+","+str(c0605n)+","+str(c0606n)+","+str(c0607n)+","+str(c0608n)+","+str(c0609n)+","+str(c0610n)+","+str(c0611n)+","+str(c0612n)+","+str(c0613n)+","+str(c0614n)+","+str(c0615n)+"\n"
    lil+=","+str(c0501n)+","+str(c0502n)+","+str(c0503n)+","+str(c0504n)+","+str(c0505n)+","+str(c0506n)+","+str(c0507n)+","+str(c0508n)+","+str(c0509n)+","+str(c0510n)+","+str(c0511n)+","+str(c0512n)+","+str(c0513n)+","+str(c0514n)+"\n"
    lil+=","+str(c0401n)+","+str(c0402n)+","+str(c0403n)+","+str(c0404n)+","+str(c0405n)+","+str(c0406n)+","+str(c0407n)+","+str(c0408n)+","+str(c0409n)+","+str(c0410n)+","+str(c0411n)+","+str(c0412n)+"\n"
    lil+=","+str(c0301n)+","+str(c0302n)+","+str(c0303n)+","+str(c0304n)+","+str(c0305n)+","+str(c0306n)+","+str(c0307n)+","+str(c0308n)+","+str(c0309n)+"\n"
    lil+=","+str(c0201n)+","+str(c0202n)+","+str(c0203n)+","+str(c0204n)+","+str(c0205n)+","+str(c0206n)+","+str(c0207n)+"\n"
    lil+=","+str(c0101n)+","+str(c0102n)+","+str(c0103n)+","+str(c0104n)+"\n"
    lil+=","+str(c0001n)+"\n"
    lil+="\n"
    with open(cpass+"/rotilt.csv", mode='w') as h:
        h.write(lil)
        h.close()
        pass
    print("Save:"+cpass+"/rotilt.csv")
    #
    lio="Before\n"
    lio+=","*17+str(b0001n)+","+str(b0000a)+","+str(b0001p)+"\n"
    lio+=","*13+str(b0104n)+","+str(b0103n)+","+str(b0102n)+","+str(b0101n)+","+str(b0100a)+","+str(b0101p)+","+str(b0102p)+","+str(b0103p)+","+str(b0104p)+"\n"
    lio+=","*11+str(b0207n)+","+str(b0206n)+","+str(b0205n)+","+str(b0204n)+","+str(b0203n)+","+str(b0202n)+","+str(b0201n)+","+str(b0200a)+","+str(b0201p)+","+str(b0202p)+","+str(b0203p)+","+str(b0204p)+","+str(b0205p)+","+str(b0206p)+","+str(b0207p)+"\n"
    lio+=","*8 +str(b0309n)+","+str(b0308n)+","+str(b0307n)+","+str(b0306n)+","+str(b0305n)+","+str(b0304n)+","+str(b0303n)+","+str(b0302n)+","+str(b0301n)+","+str(b0300a)+","+str(b0301p)+","+str(b0302p)+","+str(b0303p)+","+str(b0304p)+","+str(b0305p)+","+str(b0306p)+","+str(b0307p)+","+str(b0308p)+","+str(b0309p)+","+str(b0310a)+"\n"
    lio+=","*6 +str(b0412n)+","+str(b0411n)+","+str(b0410n)+","+str(b0409n)+","+str(b0408n)+","+str(b0407n)+","+str(b0406n)+","+str(b0405n)+","+str(b0404n)+","+str(b0403n)+","+str(b0402n)+","+str(b0401n)+","+str(b0400a)+","+str(b0401p)+","+str(b0402p)+","+str(b0403p)+","+str(b0404p)+","+str(b0405p)+","+str(b0406p)+","+str(b0407p)+","+str(b0408p)+","+str(b0409p)+","+str(b0410p)+","+str(b0411p)+","+str(b0412p)+"\n"
    lio+=","*4 +str(b0514n)+","+str(b0513n)+","+str(b0512n)+","+str(b0511n)+","+str(b0510n)+","+str(b0509n)+","+str(b0508n)+","+str(b0507n)+","+str(b0506n)+","+str(b0505n)+","+str(b0504n)+","+str(b0503n)+","+str(b0502n)+","+str(b0501n)+","+str(b0500a)+","+str(b0501p)+","+str(b0502p)+","+str(b0503p)+","+str(b0504p)+","+str(b0505p)+","+str(b0506p)+","+str(b0507p)+","+str(b0508p)+","+str(b0509p)+","+str(b0510p)+","+str(b0511p)+","+str(b0512p)+","+str(b0513p)+","+str(b0514p)+","+str(b0515a)+"\n"
    lio+=","*3 +str(b0615n)+","+str(b0614n)+","+str(b0613n)+","+str(b0612n)+","+str(b0611n)+","+str(b0610n)+","+str(b0609n)+","+str(b0608n)+","+str(b0607n)+","+str(b0606n)+","+str(b0605n)+","+str(b0604n)+","+str(b0603n)+","+str(b0602n)+","+str(b0601n)+","+str(b0600a)+","+str(b0601p)+","+str(b0602p)+","+str(b0603p)+","+str(b0604p)+","+str(b0605p)+","+str(b0606p)+","+str(b0607p)+","+str(b0608p)+","+str(b0609p)+","+str(b0610p)+","+str(b0611p)+","+str(b0612p)+","+str(b0613p)+","+str(b0614p)+","+str(b0615p)+","+str(b0616a)+"\n"
    lio+=","*1 +str(b0716n)+","+str(b0715n)+","+str(b0714n)+","+str(b0713n)+","+str(b0712n)+","+str(b0711n)+","+str(b0710n)+","+str(b0709n)+","+str(b0708n)+","+str(b0707n)+","+str(b0706n)+","+str(b0705n)+","+str(b0704n)+","+str(b0703n)+","+str(b0702n)+","+str(b0701n)+","+str(b0700a)+","+str(b0701p)+","+str(b0702p)+","+str(b0703p)+","+str(b0704p)+","+str(b0705p)+","+str(b0706p)+","+str(b0707p)+","+str(b0708p)+","+str(b0709p)+","+str(b0710p)+","+str(b0711p)+","+str(b0712p)+","+str(b0713p)+","+str(b0714p)+","+str(b0715p)+","+str(b0716p)+","+str(b0717p)+"\n"
    lio+=","*1 +str(b0817n)+","+str(b0816n)+","+str(b0815n)+","+str(b0814n)+","+str(b0813n)+","+str(b0812n)+","+str(b0811n)+","+str(b0810n)+","+str(b0809n)+","+str(b0808n)+","+str(b0807n)+","+str(b0806n)+","+str(b0805n)+","+str(b0804n)+","+str(b0803n)+","+str(b0802n)+","+str(b0801n)+","+str(b0800a)+","+str(b0801p)+","+str(b0802p)+","+str(b0803p)+","+str(b0804p)+","+str(b0805p)+","+str(b0806p)+","+str(b0807p)+","+str(b0808p)+","+str(b0809p)+","+str(b0810p)+","+str(b0811p)+","+str(b0812p)+","+str(b0813p)+","+str(b0814p)+","+str(b0815p)+","+str(b0816p)+","+str(b0817p)+","+str(b0818a)+"\n"
    lio+=","*1 +str(c0817n)+","+str(c0816n)+","+str(c0815n)+","+str(c0814n)+","+str(c0813n)+","+str(c0812n)+","+str(c0811n)+","+str(c0810n)+","+str(c0809n)+","+str(c0808n)+","+str(c0807n)+","+str(c0806n)+","+str(c0805n)+","+str(c0804n)+","+str(c0803n)+","+str(c0802n)+","+str(c0801n)+","+str(c0800a)+","+str(c0801p)+","+str(c0802p)+","+str(c0803p)+","+str(c0804p)+","+str(c0805p)+","+str(c0806p)+","+str(c0807p)+","+str(c0808p)+","+str(c0809p)+","+str(c0810p)+","+str(c0811p)+","+str(c0812p)+","+str(c0813p)+","+str(c0814p)+","+str(c0815p)+","+str(c0816p)+","+str(c0817p)+","+str(c0818a)+"\n"
    lio+=","*1 +str(c0716n)+","+str(c0715n)+","+str(c0714n)+","+str(c0713n)+","+str(c0712n)+","+str(c0711n)+","+str(c0710n)+","+str(c0709n)+","+str(c0708n)+","+str(c0707n)+","+str(c0706n)+","+str(c0705n)+","+str(c0704n)+","+str(c0703n)+","+str(c0702n)+","+str(c0701n)+","+str(c0700a)+","+str(c0701p)+","+str(c0702p)+","+str(c0703p)+","+str(c0704p)+","+str(c0705p)+","+str(c0706p)+","+str(c0707p)+","+str(c0708p)+","+str(c0709p)+","+str(c0710p)+","+str(c0711p)+","+str(c0712p)+","+str(c0713p)+","+str(c0714p)+","+str(c0715p)+","+str(c0716p)+","+str(c0717p)+"\n"
    lio+=","*3 +str(c0615n)+","+str(c0614n)+","+str(c0613n)+","+str(c0612n)+","+str(c0611n)+","+str(c0610n)+","+str(c0609n)+","+str(c0608n)+","+str(c0607n)+","+str(c0606n)+","+str(c0605n)+","+str(c0604n)+","+str(c0603n)+","+str(c0602n)+","+str(c0601n)+","+str(c0600a)+","+str(c0601p)+","+str(c0602p)+","+str(c0603p)+","+str(c0604p)+","+str(c0605p)+","+str(c0606p)+","+str(c0607p)+","+str(c0608p)+","+str(c0609p)+","+str(c0610p)+","+str(c0611p)+","+str(c0612p)+","+str(c0613p)+","+str(c0614p)+","+str(c0615p)+","+str(c0616a)+"\n"
    lio+=","*4 +str(c0514n)+","+str(c0513n)+","+str(c0512n)+","+str(c0511n)+","+str(c0510n)+","+str(c0509n)+","+str(c0508n)+","+str(c0507n)+","+str(c0506n)+","+str(c0505n)+","+str(c0504n)+","+str(c0503n)+","+str(c0502n)+","+str(c0501n)+","+str(c0500a)+","+str(c0501p)+","+str(c0502p)+","+str(c0503p)+","+str(c0504p)+","+str(c0505p)+","+str(c0506p)+","+str(c0507p)+","+str(c0508p)+","+str(c0509p)+","+str(c0510p)+","+str(c0511p)+","+str(c0512p)+","+str(c0513p)+","+str(c0514p)+","+str(c0515a)+"\n"
    lio+=","*6 +str(c0412n)+","+str(c0411n)+","+str(c0410n)+","+str(c0409n)+","+str(c0408n)+","+str(c0407n)+","+str(c0406n)+","+str(c0405n)+","+str(c0404n)+","+str(c0403n)+","+str(c0402n)+","+str(c0401n)+","+str(c0400a)+","+str(c0401p)+","+str(c0402p)+","+str(c0403p)+","+str(c0404p)+","+str(c0405p)+","+str(c0406p)+","+str(c0407p)+","+str(c0408p)+","+str(c0409p)+","+str(c0410p)+","+str(c0411p)+","+str(c0412p)+"\n"
    lio+=","*8 +str(c0309n)+","+str(c0308n)+","+str(c0307n)+","+str(c0306n)+","+str(c0305n)+","+str(c0304n)+","+str(c0303n)+","+str(c0302n)+","+str(c0301n)+","+str(c0300a)+","+str(c0301p)+","+str(c0302p)+","+str(c0303p)+","+str(c0304p)+","+str(c0305p)+","+str(c0306p)+","+str(c0307p)+","+str(c0308p)+","+str(c0309p)+","+str(c0310a)+"\n"
    lio+=","*11+str(c0207n)+","+str(c0206n)+","+str(c0205n)+","+str(c0204n)+","+str(c0203n)+","+str(c0202n)+","+str(c0201n)+","+str(c0200a)+","+str(c0201p)+","+str(c0202p)+","+str(c0203p)+","+str(c0204p)+","+str(c0205p)+","+str(c0206p)+","+str(c0207p)+"\n"
    lio+=","*13+str(c0104n)+","+str(c0103n)+","+str(c0102n)+","+str(c0101n)+","+str(c0100a)+","+str(c0101p)+","+str(c0102p)+","+str(c0103p)+","+str(c0104p)+"\n"
    lio+=","*17+str(c0001n)+","+str(c0000a)+","+str(c0001p)+"\n"
    lio+="After\n"
    lio+=","*17+str(integ(b0001n))+","+str(integ(b0000a))+","+str(integ(b0001p))+"\n"
    lio+=","*13+str(integ(b0104n))+","+str(integ(b0103n))+","+str(integ(b0102n))+","+str(integ(b0101n))+","+str(integ(b0100a))+","+str(integ(b0101p))+","+str(integ(b0102p))+","+str(integ(b0103p))+","+str(integ(b0104p))+"\n"
    lio+=","*11+str(integ(b0207n))+","+str(integ(b0206n))+","+str(integ(b0205n))+","+str(integ(b0204n))+","+str(integ(b0203n))+","+str(integ(b0202n))+","+str(integ(b0201n))+","+str(integ(b0200a))+","+str(integ(b0201p))+","+str(integ(b0202p))+","+str(integ(b0203p))+","+str(integ(b0204p))+","+str(integ(b0205p))+","+str(integ(b0206p))+","+str(integ(b0207p))+"\n"
    lio+=","*8 +str(integ(b0309n))+","+str(integ(b0308n))+","+str(integ(b0307n))+","+str(integ(b0306n))+","+str(integ(b0305n))+","+str(integ(b0304n))+","+str(integ(b0303n))+","+str(integ(b0302n))+","+str(integ(b0301n))+","+str(integ(b0300a))+","+str(integ(b0301p))+","+str(integ(b0302p))+","+str(integ(b0303p))+","+str(integ(b0304p))+","+str(integ(b0305p))+","+str(integ(b0306p))+","+str(integ(b0307p))+","+str(integ(b0308p))+","+str(integ(b0309p))+","+str(integ(b0310a))+"\n"
    lio+=","*6 +str(integ(b0412n))+","+str(integ(b0411n))+","+str(integ(b0410n))+","+str(integ(b0409n))+","+str(integ(b0408n))+","+str(integ(b0407n))+","+str(integ(b0406n))+","+str(integ(b0405n))+","+str(integ(b0404n))+","+str(integ(b0403n))+","+str(integ(b0402n))+","+str(integ(b0401n))+","+str(integ(b0400a))+","+str(integ(b0401p))+","+str(integ(b0402p))+","+str(integ(b0403p))+","+str(integ(b0404p))+","+str(integ(b0405p))+","+str(integ(b0406p))+","+str(integ(b0407p))+","+str(integ(b0408p))+","+str(integ(b0409p))+","+str(integ(b0410p))+","+str(integ(b0411p))+","+str(integ(b0412p))+"\n"
    lio+=","*4 +str(integ(b0514n))+","+str(integ(b0513n))+","+str(integ(b0512n))+","+str(integ(b0511n))+","+str(integ(b0510n))+","+str(integ(b0509n))+","+str(integ(b0508n))+","+str(integ(b0507n))+","+str(integ(b0506n))+","+str(integ(b0505n))+","+str(integ(b0504n))+","+str(integ(b0503n))+","+str(integ(b0502n))+","+str(integ(b0501n))+","+str(integ(b0500a))+","+str(integ(b0501p))+","+str(integ(b0502p))+","+str(integ(b0503p))+","+str(integ(b0504p))+","+str(integ(b0505p))+","+str(integ(b0506p))+","+str(integ(b0507p))+","+str(integ(b0508p))+","+str(integ(b0509p))+","+str(integ(b0510p))+","+str(integ(b0511p))+","+str(integ(b0512p))+","+str(integ(b0513p))+","+str(integ(b0514p))+","+str(integ(b0515a))+"\n"
    lio+=","*3 +str(integ(b0615n))+","+str(integ(b0614n))+","+str(integ(b0613n))+","+str(integ(b0612n))+","+str(integ(b0611n))+","+str(integ(b0610n))+","+str(integ(b0609n))+","+str(integ(b0608n))+","+str(integ(b0607n))+","+str(integ(b0606n))+","+str(integ(b0605n))+","+str(integ(b0604n))+","+str(integ(b0603n))+","+str(integ(b0602n))+","+str(integ(b0601n))+","+str(integ(b0600a))+","+str(integ(b0601p))+","+str(integ(b0602p))+","+str(integ(b0603p))+","+str(integ(b0604p))+","+str(integ(b0605p))+","+str(integ(b0606p))+","+str(integ(b0607p))+","+str(integ(b0608p))+","+str(integ(b0609p))+","+str(integ(b0610p))+","+str(integ(b0611p))+","+str(integ(b0612p))+","+str(integ(b0613p))+","+str(integ(b0614p))+","+str(integ(b0615p))+","+str(integ(b0616a))+"\n"
    lio+=","*1 +str(integ(b0716n))+","+str(integ(b0715n))+","+str(integ(b0714n))+","+str(integ(b0713n))+","+str(integ(b0712n))+","+str(integ(b0711n))+","+str(integ(b0710n))+","+str(integ(b0709n))+","+str(integ(b0708n))+","+str(integ(b0707n))+","+str(integ(b0706n))+","+str(integ(b0705n))+","+str(integ(b0704n))+","+str(integ(b0703n))+","+str(integ(b0702n))+","+str(integ(b0701n))+","+str(integ(b0700a))+","+str(integ(b0701p))+","+str(integ(b0702p))+","+str(integ(b0703p))+","+str(integ(b0704p))+","+str(integ(b0705p))+","+str(integ(b0706p))+","+str(integ(b0707p))+","+str(integ(b0708p))+","+str(integ(b0709p))+","+str(integ(b0710p))+","+str(integ(b0711p))+","+str(integ(b0712p))+","+str(integ(b0713p))+","+str(integ(b0714p))+","+str(integ(b0715p))+","+str(integ(b0716p))+","+str(integ(b0717p))+"\n"
    lio+=","*1 +str(integ(b0817n))+","+str(integ(b0816n))+","+str(integ(b0815n))+","+str(integ(b0814n))+","+str(integ(b0813n))+","+str(integ(b0812n))+","+str(integ(b0811n))+","+str(integ(b0810n))+","+str(integ(b0809n))+","+str(integ(b0808n))+","+str(integ(b0807n))+","+str(integ(b0806n))+","+str(integ(b0805n))+","+str(integ(b0804n))+","+str(integ(b0803n))+","+str(integ(b0802n))+","+str(integ(b0801n))+","+str(integ(b0800a))+","+str(integ(b0801p))+","+str(integ(b0802p))+","+str(integ(b0803p))+","+str(integ(b0804p))+","+str(integ(b0805p))+","+str(integ(b0806p))+","+str(integ(b0807p))+","+str(integ(b0808p))+","+str(integ(b0809p))+","+str(integ(b0810p))+","+str(integ(b0811p))+","+str(integ(b0812p))+","+str(integ(b0813p))+","+str(integ(b0814p))+","+str(integ(b0815p))+","+str(integ(b0816p))+","+str(integ(b0817p))+","+str(integ(b0818a))+"\n"
    lio+=","*1 +str(integ(c0817n))+","+str(integ(c0816n))+","+str(integ(c0815n))+","+str(integ(c0814n))+","+str(integ(c0813n))+","+str(integ(c0812n))+","+str(integ(c0811n))+","+str(integ(c0810n))+","+str(integ(c0809n))+","+str(integ(c0808n))+","+str(integ(c0807n))+","+str(integ(c0806n))+","+str(integ(c0805n))+","+str(integ(c0804n))+","+str(integ(c0803n))+","+str(integ(c0802n))+","+str(integ(c0801n))+","+str(integ(c0800a))+","+str(integ(c0801p))+","+str(integ(c0802p))+","+str(integ(c0803p))+","+str(integ(c0804p))+","+str(integ(c0805p))+","+str(integ(c0806p))+","+str(integ(c0807p))+","+str(integ(c0808p))+","+str(integ(c0809p))+","+str(integ(c0810p))+","+str(integ(c0811p))+","+str(integ(c0812p))+","+str(integ(c0813p))+","+str(integ(c0814p))+","+str(integ(c0815p))+","+str(integ(c0816p))+","+str(integ(c0817p))+","+str(integ(c0818a))+"\n"
    lio+=","*1 +str(integ(c0716n))+","+str(integ(c0715n))+","+str(integ(c0714n))+","+str(integ(c0713n))+","+str(integ(c0712n))+","+str(integ(c0711n))+","+str(integ(c0710n))+","+str(integ(c0709n))+","+str(integ(c0708n))+","+str(integ(c0707n))+","+str(integ(c0706n))+","+str(integ(c0705n))+","+str(integ(c0704n))+","+str(integ(c0703n))+","+str(integ(c0702n))+","+str(integ(c0701n))+","+str(integ(c0700a))+","+str(integ(c0701p))+","+str(integ(c0702p))+","+str(integ(c0703p))+","+str(integ(c0704p))+","+str(integ(c0705p))+","+str(integ(c0706p))+","+str(integ(c0707p))+","+str(integ(c0708p))+","+str(integ(c0709p))+","+str(integ(c0710p))+","+str(integ(c0711p))+","+str(integ(c0712p))+","+str(integ(c0713p))+","+str(integ(c0714p))+","+str(integ(c0715p))+","+str(integ(c0716p))+","+str(integ(c0717p))+"\n"
    lio+=","*3 +str(integ(c0615n))+","+str(integ(c0614n))+","+str(integ(c0613n))+","+str(integ(c0612n))+","+str(integ(c0611n))+","+str(integ(c0610n))+","+str(integ(c0609n))+","+str(integ(c0608n))+","+str(integ(c0607n))+","+str(integ(c0606n))+","+str(integ(c0605n))+","+str(integ(c0604n))+","+str(integ(c0603n))+","+str(integ(c0602n))+","+str(integ(c0601n))+","+str(integ(c0600a))+","+str(integ(c0601p))+","+str(integ(c0602p))+","+str(integ(c0603p))+","+str(integ(c0604p))+","+str(integ(c0605p))+","+str(integ(c0606p))+","+str(integ(c0607p))+","+str(integ(c0608p))+","+str(integ(c0609p))+","+str(integ(c0610p))+","+str(integ(c0611p))+","+str(integ(c0612p))+","+str(integ(c0613p))+","+str(integ(c0614p))+","+str(integ(c0615p))+","+str(integ(c0616a))+"\n"
    lio+=","*4 +str(integ(c0514n))+","+str(integ(c0513n))+","+str(integ(c0512n))+","+str(integ(c0511n))+","+str(integ(c0510n))+","+str(integ(c0509n))+","+str(integ(c0508n))+","+str(integ(c0507n))+","+str(integ(c0506n))+","+str(integ(c0505n))+","+str(integ(c0504n))+","+str(integ(c0503n))+","+str(integ(c0502n))+","+str(integ(c0501n))+","+str(integ(c0500a))+","+str(integ(c0501p))+","+str(integ(c0502p))+","+str(integ(c0503p))+","+str(integ(c0504p))+","+str(integ(c0505p))+","+str(integ(c0506p))+","+str(integ(c0507p))+","+str(integ(c0508p))+","+str(integ(c0509p))+","+str(integ(c0510p))+","+str(integ(c0511p))+","+str(integ(c0512p))+","+str(integ(c0513p))+","+str(integ(c0514p))+","+str(integ(c0515a))+"\n"
    lio+=","*6 +str(integ(c0412n))+","+str(integ(c0411n))+","+str(integ(c0410n))+","+str(integ(c0409n))+","+str(integ(c0408n))+","+str(integ(c0407n))+","+str(integ(c0406n))+","+str(integ(c0405n))+","+str(integ(c0404n))+","+str(integ(c0403n))+","+str(integ(c0402n))+","+str(integ(c0401n))+","+str(integ(c0400a))+","+str(integ(c0401p))+","+str(integ(c0402p))+","+str(integ(c0403p))+","+str(integ(c0404p))+","+str(integ(c0405p))+","+str(integ(c0406p))+","+str(integ(c0407p))+","+str(integ(c0408p))+","+str(integ(c0409p))+","+str(integ(c0410p))+","+str(integ(c0411p))+","+str(integ(c0412p))+"\n"
    lio+=","*8 +str(integ(c0309n))+","+str(integ(c0308n))+","+str(integ(c0307n))+","+str(integ(c0306n))+","+str(integ(c0305n))+","+str(integ(c0304n))+","+str(integ(c0303n))+","+str(integ(c0302n))+","+str(integ(c0301n))+","+str(integ(c0300a))+","+str(integ(c0301p))+","+str(integ(c0302p))+","+str(integ(c0303p))+","+str(integ(c0304p))+","+str(integ(c0305p))+","+str(integ(c0306p))+","+str(integ(c0307p))+","+str(integ(c0308p))+","+str(integ(c0309p))+","+str(integ(c0310a))+"\n"
    lio+=","*11+str(integ(c0207n))+","+str(integ(c0206n))+","+str(integ(c0205n))+","+str(integ(c0204n))+","+str(integ(c0203n))+","+str(integ(c0202n))+","+str(integ(c0201n))+","+str(integ(c0200a))+","+str(integ(c0201p))+","+str(integ(c0202p))+","+str(integ(c0203p))+","+str(integ(c0204p))+","+str(integ(c0205p))+","+str(integ(c0206p))+","+str(integ(c0207p))+"\n"
    lio+=","*13+str(integ(c0104n))+","+str(integ(c0103n))+","+str(integ(c0102n))+","+str(integ(c0101n))+","+str(integ(c0100a))+","+str(integ(c0101p))+","+str(integ(c0102p))+","+str(integ(c0103p))+","+str(integ(c0104p))+"\n"
    lio+=","*17+str(integ(c0001n))+","+str(integ(c0000a))+","+str(integ(c0001p))+"\n"
    lio+="Variable_name\n"
    lio+=","*17+"b0001n,b0000a,b0001p\n"
    lio+=","*13+"b0104n,b0103n,b0102n,b0101n,b0100a,b0101p,b0102p,b0103p,b0104p\n"
    lio+=","*11+"b0207n,b0206n,b0205n,b0204n,b0203n,b0202n,b0201n,b0200a,b0201p,b0202p,b0203p,b0204p,b0205p,b0206p,b0207p\n"
    lio+=","*8 +"b0309n,b0308n,b0307n,b0306n,b0305n,b0304n,b0303n,b0302n,b0301n,b0300a,b0301p,b0302p,b0303p,b0304p,b0305p,b0306p,b0307p,b0308p,b0309p,b0310a\n"
    lio+=","*6 +"b0412n,b0411n,b0410n,b0409n,b0408n,b0407n,b0406n,b0405n,b0404n,b0403n,b0402n,b0401n,b0400a,b0401p,b0402p,b0403p,b0404p,b0405p,b0406p,b0407p,b0408p,b0409p,b0410p,b0411p,b0412p\n"
    lio+=","*4 +"b0514n,b0513n,b0512n,b0511n,b0510n,b0509n,b0508n,b0507n,b0506n,b0505n,b0504n,b0503n,b0502n,b0501n,b0500a,b0501p,b0502p,b0503p,b0504p,b0505p,b0506p,b0507p,b0508p,b0509p,b0510p,b0511p,b0512p,b0513p,b0514p,b0515a\n"
    lio+=","*3 +"b0615n,b0614n,b0613n,b0612n,b0611n,b0610n,b0609n,b0608n,b0607n,b0606n,b0605n,b0604n,b0603n,b0602n,b0601n,b0600a,b0601p,b0602p,b0603p,b0604p,b0605p,b0606p,b0607p,b0608p,b0609p,b0610p,b0611p,b0612p,b0613p,b0614p,b0615p,b0616a\n"
    lio+=","*1  +"b0716n,b0715n,b0714n,b0713n,b0712n,b0711n,b0710n,b0709n,b0708n,b0707n,b0706n,b0705n,b0704n,b0703n,b0702n,b0701n,b0700a,b0701p,b0702p,b0703p,b0704p,b0705p,b0706p,b0707p,b0708p,b0709p,b0710p,b0711p,b0712p,b0713p,b0714p,b0715p,b0716p,b0717p\n"
    lio+=","*1  +"b0817n,b0816n,b0815n,b0814n,b0813n,b0812n,b0811n,b0810n,b0809n,b0808n,b0807n,b0806n,b0805n,b0804n,b0803n,b0802n,b0801n,b0800a,b0801p,b0802p,b0803p,b0804p,b0805p,b0806p,b0807p,b0808p,b0809p,b0810p,b0811p,b0812p,b0813p,b0814p,b0815p,b0816p,b0817p,b0818a\n"
    lio+=","*1  +"c0817n,c0816n,c0815n,c0814n,c0813n,c0812n,c0811n,c0810n,c0809n,c0808n,c0807n,c0806n,c0805n,c0804n,c0803n,c0802n,c0801n,c0800a,c0801p,c0802p,c0803p,c0804p,c0805p,c0806p,c0807p,c0808p,c0809p,c0810p,c0811p,c0812p,c0813p,c0814p,c0815p,c0816p,c0817p,c0818a\n"
    lio+=","*1  +"c0716n,c0715n,c0714n,c0713n,c0712n,c0711n,c0710n,c0709n,c0708n,c0707n,c0706n,c0705n,c0704n,c0703n,c0702n,c0701n,c0700a,c0701p,c0702p,c0703p,c0704p,c0705p,c0706p,c0707p,c0708p,c0709p,c0710p,c0711p,c0712p,c0713p,c0714p,c0715p,c0716p,c0717p\n"
    lio+=","*3 +"c0615n,c0614n,c0613n,c0612n,c0611n,c0610n,c0609n,c0608n,c0607n,c0606n,c0605n,c0604n,c0603n,c0602n,c0601n,c0600a,c0601p,c0602p,c0603p,c0604p,c0605p,c0606p,c0607p,c0608p,c0609p,c0610p,c0611p,c0612p,c0613p,c0614p,c0615p,c0616a\n"
    lio+=","*4 +"c0514n,c0513n,c0512n,c0511n,c0510n,c0509n,c0508n,c0507n,c0506n,c0505n,c0504n,c0503n,c0502n,c0501n,c0500a,c0501p,c0502p,c0503p,c0504p,c0505p,c0506p,c0507p,c0508p,c0509p,c0510p,c0511p,c0512p,c0513p,c0514p,c0515a\n"
    lio+=","*6 +"c0412n,c0411n,c0410n,c0409n,c0408n,c0407n,c0406n,c0405n,c0404n,c0403n,c0402n,c0401n,c0400a,c0401p,c0402p,c0403p,c0404p,c0405p,c0406p,c0407p,c0408p,c0409p,c0410p,c0411p,c0412p\n"
    lio+=","*8 +"c0309n,c0308n,c0307n,c0306n,c0305n,c0304n,c0303n,c0302n,c0301n,c0300a,c0301p,c0302p,c0303p,c0304p,c0305p,c0306p,c0307p,c0308p,c0309p,c0310a\n"
    lio+=","*11+"c0207n,c0206n,c0205n,c0204n,c0203n,c0202n,c0201n,c0200a,c0201p,c0202p,c0203p,c0204p,c0205p,c0206p,c0207p\n"
    lio+=","*13+"c0104n,c0103n,c0102n,c0101n,c0100a,c0101p,c0102p,c0103p,c0104p\n"
    lio+=","*17+"c0001n,c0000a,c0001p\n"
    lio+="Integration_No.\n"
    lio+=","*17+str(avera(b0001n))+","+str(avera(b0000a))+","+str(avera(b0001p))+"\n"
    lio+=","*13+str(avera(b0104n))+","+str(avera(b0103n))+","+str(avera(b0102n))+","+str(avera(b0101n))+","+str(avera(b0100a))+","+str(avera(b0101p))+","+str(avera(b0102p))+","+str(avera(b0103p))+","+str(avera(b0104p))+"\n"
    lio+=","*11+str(avera(b0207n))+","+str(avera(b0206n))+","+str(avera(b0205n))+","+str(avera(b0204n))+","+str(avera(b0203n))+","+str(avera(b0202n))+","+str(avera(b0201n))+","+str(avera(b0200a))+","+str(avera(b0201p))+","+str(avera(b0202p))+","+str(avera(b0203p))+","+str(avera(b0204p))+","+str(avera(b0205p))+","+str(avera(b0206p))+","+str(avera(b0207p))+"\n"
    lio+=","*8 +str(avera(b0309n))+","+str(avera(b0308n))+","+str(avera(b0307n))+","+str(avera(b0306n))+","+str(avera(b0305n))+","+str(avera(b0304n))+","+str(avera(b0303n))+","+str(avera(b0302n))+","+str(avera(b0301n))+","+str(avera(b0300a))+","+str(avera(b0301p))+","+str(avera(b0302p))+","+str(avera(b0303p))+","+str(avera(b0304p))+","+str(avera(b0305p))+","+str(avera(b0306p))+","+str(avera(b0307p))+","+str(avera(b0308p))+","+str(avera(b0309p))+","+str(avera(b0310a))+"\n"
    lio+=","*6 +str(avera(b0412n))+","+str(avera(b0411n))+","+str(avera(b0410n))+","+str(avera(b0409n))+","+str(avera(b0408n))+","+str(avera(b0407n))+","+str(avera(b0406n))+","+str(avera(b0405n))+","+str(avera(b0404n))+","+str(avera(b0403n))+","+str(avera(b0402n))+","+str(avera(b0401n))+","+str(avera(b0400a))+","+str(avera(b0401p))+","+str(avera(b0402p))+","+str(avera(b0403p))+","+str(avera(b0404p))+","+str(avera(b0405p))+","+str(avera(b0406p))+","+str(avera(b0407p))+","+str(avera(b0408p))+","+str(avera(b0409p))+","+str(avera(b0410p))+","+str(avera(b0411p))+","+str(avera(b0412p))+"\n"
    lio+=","*4 +str(avera(b0514n))+","+str(avera(b0513n))+","+str(avera(b0512n))+","+str(avera(b0511n))+","+str(avera(b0510n))+","+str(avera(b0509n))+","+str(avera(b0508n))+","+str(avera(b0507n))+","+str(avera(b0506n))+","+str(avera(b0505n))+","+str(avera(b0504n))+","+str(avera(b0503n))+","+str(avera(b0502n))+","+str(avera(b0501n))+","+str(avera(b0500a))+","+str(avera(b0501p))+","+str(avera(b0502p))+","+str(avera(b0503p))+","+str(avera(b0504p))+","+str(avera(b0505p))+","+str(avera(b0506p))+","+str(avera(b0507p))+","+str(avera(b0508p))+","+str(avera(b0509p))+","+str(avera(b0510p))+","+str(avera(b0511p))+","+str(avera(b0512p))+","+str(avera(b0513p))+","+str(avera(b0514p))+","+str(avera(b0515a))+"\n"
    lio+=","*3 +str(avera(b0615n))+","+str(avera(b0614n))+","+str(avera(b0613n))+","+str(avera(b0612n))+","+str(avera(b0611n))+","+str(avera(b0610n))+","+str(avera(b0609n))+","+str(avera(b0608n))+","+str(avera(b0607n))+","+str(avera(b0606n))+","+str(avera(b0605n))+","+str(avera(b0604n))+","+str(avera(b0603n))+","+str(avera(b0602n))+","+str(avera(b0601n))+","+str(avera(b0600a))+","+str(avera(b0601p))+","+str(avera(b0602p))+","+str(avera(b0603p))+","+str(avera(b0604p))+","+str(avera(b0605p))+","+str(avera(b0606p))+","+str(avera(b0607p))+","+str(avera(b0608p))+","+str(avera(b0609p))+","+str(avera(b0610p))+","+str(avera(b0611p))+","+str(avera(b0612p))+","+str(avera(b0613p))+","+str(avera(b0614p))+","+str(avera(b0615p))+","+str(avera(b0616a))+"\n"
    lio+=","*1 +str(avera(b0716n))+","+str(avera(b0715n))+","+str(avera(b0714n))+","+str(avera(b0713n))+","+str(avera(b0712n))+","+str(avera(b0711n))+","+str(avera(b0710n))+","+str(avera(b0709n))+","+str(avera(b0708n))+","+str(avera(b0707n))+","+str(avera(b0706n))+","+str(avera(b0705n))+","+str(avera(b0704n))+","+str(avera(b0703n))+","+str(avera(b0702n))+","+str(avera(b0701n))+","+str(avera(b0700a))+","+str(avera(b0701p))+","+str(avera(b0702p))+","+str(avera(b0703p))+","+str(avera(b0704p))+","+str(avera(b0705p))+","+str(avera(b0706p))+","+str(avera(b0707p))+","+str(avera(b0708p))+","+str(avera(b0709p))+","+str(avera(b0710p))+","+str(avera(b0711p))+","+str(avera(b0712p))+","+str(avera(b0713p))+","+str(avera(b0714p))+","+str(avera(b0715p))+","+str(avera(b0716p))+","+str(avera(b0717p))+"\n"
    lio+=","*1 +str(avera(b0817n))+","+str(avera(b0816n))+","+str(avera(b0815n))+","+str(avera(b0814n))+","+str(avera(b0813n))+","+str(avera(b0812n))+","+str(avera(b0811n))+","+str(avera(b0810n))+","+str(avera(b0809n))+","+str(avera(b0808n))+","+str(avera(b0807n))+","+str(avera(b0806n))+","+str(avera(b0805n))+","+str(avera(b0804n))+","+str(avera(b0803n))+","+str(avera(b0802n))+","+str(avera(b0801n))+","+str(avera(b0800a))+","+str(avera(b0801p))+","+str(avera(b0802p))+","+str(avera(b0803p))+","+str(avera(b0804p))+","+str(avera(b0805p))+","+str(avera(b0806p))+","+str(avera(b0807p))+","+str(avera(b0808p))+","+str(avera(b0809p))+","+str(avera(b0810p))+","+str(avera(b0811p))+","+str(avera(b0812p))+","+str(avera(b0813p))+","+str(avera(b0814p))+","+str(avera(b0815p))+","+str(avera(b0816p))+","+str(avera(b0817p))+","+str(avera(b0818a))+"\n"
    lio+=","*1 +str(avera(c0817n))+","+str(avera(c0816n))+","+str(avera(c0815n))+","+str(avera(c0814n))+","+str(avera(c0813n))+","+str(avera(c0812n))+","+str(avera(c0811n))+","+str(avera(c0810n))+","+str(avera(c0809n))+","+str(avera(c0808n))+","+str(avera(c0807n))+","+str(avera(c0806n))+","+str(avera(c0805n))+","+str(avera(c0804n))+","+str(avera(c0803n))+","+str(avera(c0802n))+","+str(avera(c0801n))+","+str(avera(c0800a))+","+str(avera(c0801p))+","+str(avera(c0802p))+","+str(avera(c0803p))+","+str(avera(c0804p))+","+str(avera(c0805p))+","+str(avera(c0806p))+","+str(avera(c0807p))+","+str(avera(c0808p))+","+str(avera(c0809p))+","+str(avera(c0810p))+","+str(avera(c0811p))+","+str(avera(c0812p))+","+str(avera(c0813p))+","+str(avera(c0814p))+","+str(avera(c0815p))+","+str(avera(c0816p))+","+str(avera(c0817p))+","+str(avera(c0818a))+"\n"
    lio+=","*1 +str(avera(c0716n))+","+str(avera(c0715n))+","+str(avera(c0714n))+","+str(avera(c0713n))+","+str(avera(c0712n))+","+str(avera(c0711n))+","+str(avera(c0710n))+","+str(avera(c0709n))+","+str(avera(c0708n))+","+str(avera(c0707n))+","+str(avera(c0706n))+","+str(avera(c0705n))+","+str(avera(c0704n))+","+str(avera(c0703n))+","+str(avera(c0702n))+","+str(avera(c0701n))+","+str(avera(c0700a))+","+str(avera(c0701p))+","+str(avera(c0702p))+","+str(avera(c0703p))+","+str(avera(c0704p))+","+str(avera(c0705p))+","+str(avera(c0706p))+","+str(avera(c0707p))+","+str(avera(c0708p))+","+str(avera(c0709p))+","+str(avera(c0710p))+","+str(avera(c0711p))+","+str(avera(c0712p))+","+str(avera(c0713p))+","+str(avera(c0714p))+","+str(avera(c0715p))+","+str(avera(c0716p))+","+str(avera(c0717p))+"\n"
    lio+=","*3 +str(avera(c0615n))+","+str(avera(c0614n))+","+str(avera(c0613n))+","+str(avera(c0612n))+","+str(avera(c0611n))+","+str(avera(c0610n))+","+str(avera(c0609n))+","+str(avera(c0608n))+","+str(avera(c0607n))+","+str(avera(c0606n))+","+str(avera(c0605n))+","+str(avera(c0604n))+","+str(avera(c0603n))+","+str(avera(c0602n))+","+str(avera(c0601n))+","+str(avera(c0600a))+","+str(avera(c0601p))+","+str(avera(c0602p))+","+str(avera(c0603p))+","+str(avera(c0604p))+","+str(avera(c0605p))+","+str(avera(c0606p))+","+str(avera(c0607p))+","+str(avera(c0608p))+","+str(avera(c0609p))+","+str(avera(c0610p))+","+str(avera(c0611p))+","+str(avera(c0612p))+","+str(avera(c0613p))+","+str(avera(c0614p))+","+str(avera(c0615p))+","+str(avera(c0616a))+"\n"
    lio+=","*4 +str(avera(c0514n))+","+str(avera(c0513n))+","+str(avera(c0512n))+","+str(avera(c0511n))+","+str(avera(c0510n))+","+str(avera(c0509n))+","+str(avera(c0508n))+","+str(avera(c0507n))+","+str(avera(c0506n))+","+str(avera(c0505n))+","+str(avera(c0504n))+","+str(avera(c0503n))+","+str(avera(c0502n))+","+str(avera(c0501n))+","+str(avera(c0500a))+","+str(avera(c0501p))+","+str(avera(c0502p))+","+str(avera(c0503p))+","+str(avera(c0504p))+","+str(avera(c0505p))+","+str(avera(c0506p))+","+str(avera(c0507p))+","+str(avera(c0508p))+","+str(avera(c0509p))+","+str(avera(c0510p))+","+str(avera(c0511p))+","+str(avera(c0512p))+","+str(avera(c0513p))+","+str(avera(c0514p))+","+str(avera(c0515a))+"\n"
    lio+=","*6 +str(avera(c0412n))+","+str(avera(c0411n))+","+str(avera(c0410n))+","+str(avera(c0409n))+","+str(avera(c0408n))+","+str(avera(c0407n))+","+str(avera(c0406n))+","+str(avera(c0405n))+","+str(avera(c0404n))+","+str(avera(c0403n))+","+str(avera(c0402n))+","+str(avera(c0401n))+","+str(avera(c0400a))+","+str(avera(c0401p))+","+str(avera(c0402p))+","+str(avera(c0403p))+","+str(avera(c0404p))+","+str(avera(c0405p))+","+str(avera(c0406p))+","+str(avera(c0407p))+","+str(avera(c0408p))+","+str(avera(c0409p))+","+str(avera(c0410p))+","+str(avera(c0411p))+","+str(avera(c0412p))+"\n"
    lio+=","*8 +str(avera(c0309n))+","+str(avera(c0308n))+","+str(avera(c0307n))+","+str(avera(c0306n))+","+str(avera(c0305n))+","+str(avera(c0304n))+","+str(avera(c0303n))+","+str(avera(c0302n))+","+str(avera(c0301n))+","+str(avera(c0300a))+","+str(avera(c0301p))+","+str(avera(c0302p))+","+str(avera(c0303p))+","+str(avera(c0304p))+","+str(avera(c0305p))+","+str(avera(c0306p))+","+str(avera(c0307p))+","+str(avera(c0308p))+","+str(avera(c0309p))+","+str(avera(c0310a))+"\n"
    lio+=","*11+str(avera(c0207n))+","+str(avera(c0206n))+","+str(avera(c0205n))+","+str(avera(c0204n))+","+str(avera(c0203n))+","+str(avera(c0202n))+","+str(avera(c0201n))+","+str(avera(c0200a))+","+str(avera(c0201p))+","+str(avera(c0202p))+","+str(avera(c0203p))+","+str(avera(c0204p))+","+str(avera(c0205p))+","+str(avera(c0206p))+","+str(avera(c0207p))+"\n"
    lio+=","*13+str(avera(c0104n))+","+str(avera(c0103n))+","+str(avera(c0102n))+","+str(avera(c0101n))+","+str(avera(c0100a))+","+str(avera(c0101p))+","+str(avera(c0102p))+","+str(avera(c0103p))+","+str(avera(c0104p))+"\n"
    lio+=","*17+str(avera(c0001n))+","+str(avera(c0000a))+","+str(avera(c0001p))+"\n"
    with open(cpass+"/rotilt_m.csv", mode='w') as h:
        h.write(lio)
        h.close()
        pass
    print("Save:"+cpass+"/rotilt_m.csv")
    lili=""
    lili+="120,85,"+str(b0001p)+"\n"
    lili+="-120,85,"+str(b0001n)+"\n"
    lili+="0,85,"+str(b0000a)+"\n"
    lili+="160,75,"+str(b0104p)+"\n"
    lili+="-160,75,"+str(b0104n)+"\n"
    lili+="120,75,"+str(b0103p)+"\n"
    lili+="-120,75,"+str(b0103n)+"\n"
    lili+="80,75,"+str(b0102p)+"\n"
    lili+="-80,75,"+str(b0102n)+"\n"
    lili+="40,75,"+str(b0101p)+"\n"
    lili+="-40,75,"+str(b0101n)+"\n"
    lili+="0,75,"+str(b0100a)+"\n"
    lili+="168,65,"+str(b0207p)+"\n"
    lili+="-168,65,"+str(b0207n)+"\n"
    lili+="144,65,"+str(b0206p)+"\n"
    lili+="-144,65,"+str(b0206n)+"\n"
    lili+="120,65,"+str(b0205p)+"\n"
    lili+="-120,65,"+str(b0205n)+"\n"
    lili+="96,65,"+str(b0204p)+"\n"
    lili+="-96,65,"+str(b0204n)+"\n"
    lili+="72,65,"+str(b0203p)+"\n"
    lili+="-72,65,"+str(b0203n)+"\n"
    lili+="48,65,"+str(b0202p)+"\n"
    lili+="-48,65,"+str(b0202n)+"\n"
    lili+="24,65,"+str(b0201p)+"\n"
    lili+="-24,65,"+str(b0201n)+"\n"
    lili+="0,65,"+str(b0200a)+"\n"
    lili+="180,55,"+str(b0310a)+"\n"
    lili+="162,55,"+str(b0309p)+"\n"
    lili+="-162,55,"+str(b0309n)+"\n"
    lili+="144,55,"+str(b0308p)+"\n"
    lili+="-144,55,"+str(b0308n)+"\n"
    lili+="126,55,"+str(b0307p)+"\n"
    lili+="-126,55,"+str(b0307n)+"\n"
    lili+="108,55,"+str(b0306p)+"\n"
    lili+="-108,55,"+str(b0306n)+"\n"
    lili+="90,55,"+str(b0305p)+"\n"
    lili+="-90,55,"+str(b0305n)+"\n"
    lili+="72,55,"+str(b0304p)+"\n"
    lili+="-72,55,"+str(b0304n)+"\n"
    lili+="54,55,"+str(b0303p)+"\n"
    lili+="-54,55,"+str(b0303n)+"\n"
    lili+="36,55,"+str(b0302p)+"\n"
    lili+="-36,55,"+str(b0302n)+"\n"
    lili+="18,55,"+str(b0301p)+"\n"
    lili+="-18,55,"+str(b0301n)+"\n"
    lili+="0,55,"+str(b0300a)+"\n"
    lili+="172.8,45,"+str(b0412p)+"\n"
    lili+="-172.8,45,"+str(b0412n)+"\n"
    lili+="158.4,45,"+str(b0411p)+"\n"
    lili+="-158.4,45,"+str(b0411n)+"\n"
    lili+="144,45,"+str(b0410p)+"\n"
    lili+="-144,45,"+str(b0410n)+"\n"
    lili+="126,45,"+str(b0409p)+"\n"
    lili+="-126,45,"+str(b0409n)+"\n"
    lili+="108,45,"+str(b0408p)+"\n"
    lili+="-108,45,"+str(b0408n)+"\n"
    lili+="96,45,"+str(b0407p)+"\n"
    lili+="-96,45,"+str(b0407n)+"\n"
    lili+="84,45,"+str(b0406p)+"\n"
    lili+="-84,45,"+str(b0406n)+"\n"
    lili+="72,45,"+str(b0405p)+"\n"
    lili+="-72,45,"+str(b0405n)+"\n"
    lili+="60,45,"+str(b0404p)+"\n"
    lili+="-60,45,"+str(b0404n)+"\n"
    lili+="48,45,"+str(b0403p)+"\n"
    lili+="-48,45,"+str(b0403n)+"\n"
    lili+="36,45,"+str(b0402p)+"\n"
    lili+="-36,45,"+str(b0402n)+"\n"
    lili+="18,45,"+str(b0401p)+"\n"
    lili+="-18,45,"+str(b0401n)+"\n"
    lili+="0,45,"+str(b0400a)+"\n"
    lili+="180,35,"+str(b0515a)+"\n"
    lili+="168,35,"+str(b0514p)+"\n"
    lili+="-168,35,"+str(b0514n)+"\n"
    lili+="156,35,"+str(b0513p)+"\n"
    lili+="-156,35,"+str(b0513n)+"\n"
    lili+="144,35,"+str(b0512p)+"\n"
    lili+="-144,35,"+str(b0512n)+"\n"
    lili+="132,35,"+str(b0511p)+"\n"
    lili+="-132.6,35,"+str(b0511n)+"\n"
    lili+="120,35,"+str(b0510p)+"\n"
    lili+="-120,35,"+str(b0510n)+"\n"
    lili+="108,35,"+str(b0509p)+"\n"
    lili+="-108,35,"+str(b0509n)+"\n"
    lili+="96,35,"+str(b0508p)+"\n"
    lili+="-96,35,"+str(b0508n)+"\n"
    lili+="84,35,"+str(b0507p)+"\n"
    lili+="-84,35,"+str(b0507n)+"\n"
    lili+="72,35,"+str(b0506p)+"\n"
    lili+="-72,35,"+str(b0506n)+"\n"
    lili+="60,35,"+str(b0505p)+"\n"
    lili+="-60,35,"+str(b0505n)+"\n"
    lili+="48,35,"+str(b0504p)+"\n"
    lili+="-48,35,"+str(b0504n)+"\n"
    lili+="36,35,"+str(b0503p)+"\n"
    lili+="-36,35,"+str(b0503n)+"\n"
    lili+="24,35,"+str(b0502p)+"\n"
    lili+="-24,35,"+str(b0502n)+"\n"
    lili+="12,35,"+str(b0501p)+"\n"
    lili+="-12,35,"+str(b0501n)+"\n"
    lili+="0,35,"+str(b0500a)+"\n"
    lili+="180,25,"+str(b0616a)+"\n"
    lili+="168.75,25,"+str(b0615p)+"\n"
    lili+="-168.75,25,"+str(b0615n)+"\n"
    lili+="157.5,25,"+str(b0614p)+"\n"
    lili+="-157.5,25,"+str(b0614n)+"\n"
    lili+="146.25,25,"+str(b0613p)+"\n"
    lili+="-146.25,25,"+str(b0613n)+"\n"
    lili+="135,25,"+str(b0612p)+"\n"
    lili+="-135,25,"+str(b0612n)+"\n"
    lili+="123.75,25,"+str(b0611p)+"\n"
    lili+="-123.75,25,"+str(b0611n)+"\n"
    lili+="112.5,25,"+str(b0610p)+"\n"
    lili+="-112.5,25,"+str(b0610n)+"\n"
    lili+="101.25,25,"+str(b0609p)+"\n"
    lili+="-101.25,25,"+str(b0609n)+"\n"
    lili+="90,25,"+str(b0608p)+"\n"
    lili+="-90,25,"+str(b0608n)+"\n"
    lili+="78.75,25,"+str(b0607p)+"\n"
    lili+="-78.75,25,"+str(b0607n)+"\n"
    lili+="67.5,25,"+str(b0606p)+"\n"
    lili+="-67.5,25,"+str(b0606n)+"\n"
    lili+="56.25,25,"+str(b0605p)+"\n"
    lili+="-56.25,25,"+str(b0605n)+"\n"
    lili+="45,25,"+str(b0604p)+"\n"
    lili+="-45,25,"+str(b0604n)+"\n"
    lili+="33.75,25,"+str(b0603p)+"\n"
    lili+="-33.75,25,"+str(b0603n)+"\n"
    lili+="22.5,25,"+str(b0602p)+"\n"
    lili+="-22.5,25,"+str(b0602n)+"\n"
    lili+="11.25,25,"+str(b0601p)+"\n"
    lili+="-11.25,25,"+str(b0601n)+"\n"
    lili+="0,25,"+str(b0600a)+"\n"
    lili+="174.857,15,"+str(b0717p)+"\n"
    lili+="-174.857,15,"+str(b0717n)+"\n"
    lili+="164.571,15,"+str(b0716p)+"\n"
    lili+="-164.571,15,"+str(b0716n)+"\n"
    lili+="154.286,15,"+str(b0715p)+"\n"
    lili+="-154.286,15,"+str(b0715n)+"\n"
    lili+="144,15,"+str(b0714p)+"\n"
    lili+="-144,15,"+str(b0714n)+"\n"
    lili+="133.714,15,"+str(b0713p)+"\n"
    lili+="-133.714,15,"+str(b0713n)+"\n"
    lili+="123.429,15,"+str(b0712p)+"\n"
    lili+="-123.429,15,"+str(b0712n)+"\n"
    lili+="113.143,15,"+str(b0711p)+"\n"
    lili+="-113.143,15,"+str(b0711n)+"\n"
    lili+="102.857,15,"+str(b0710p)+"\n"
    lili+="-102.857,15,"+str(b0710n)+"\n"
    lili+="92.5714,15,"+str(b0709p)+"\n"
    lili+="-92.5714,15,"+str(b0709n)+"\n"
    lili+="82.2857,15,"+str(b0708p)+"\n"
    lili+="-82.2857,15,"+str(b0708n)+"\n"
    lili+="72,15,"+str(b0707p)+"\n"
    lili+="-72,15,"+str(b0707n)+"\n"
    lili+="61.7143,15,"+str(b0706p)+"\n"
    lili+="-61.7143,15,"+str(b0706n)+"\n"
    lili+="51.4286,15,"+str(b0705p)+"\n"
    lili+="-51.4286,15,"+str(b0705n)+"\n"
    lili+="41.1429,15,"+str(b0704p)+"\n"
    lili+="-41.1429,15,"+str(b0704n)+"\n"
    lili+="30.8571,15,"+str(b0703p)+"\n"
    lili+="-30.8571,15,"+str(b0703n)+"\n"
    lili+="20.5714,15,"+str(b0702p)+"\n"
    lili+="-20.5714,15,"+str(b0702n)+"\n"
    lili+="10.2857,15,"+str(b0701p)+"\n"
    lili+="-10.2857,15,"+str(b0701n)+"\n"
    lili+="0,15,"+str(b0700a)+"\n"
    lili+="180,5,"+str(b0818a)+"\n"
    lili+="170,5,"+str(b0817p)+"\n"
    lili+="-170,5,"+str(b0817n)+"\n"
    lili+="160,5,"+str(b0816p)+"\n"
    lili+="-160,5,"+str(b0816n)+"\n"
    lili+="150,5,"+str(b0815p)+"\n"
    lili+="-150,5,"+str(b0815n)+"\n"
    lili+="140,5,"+str(b0814p)+"\n"
    lili+="-140,5,"+str(b0814n)+"\n"
    lili+="130,5,"+str(b0813p)+"\n"
    lili+="-130,5,"+str(b0813n)+"\n"
    lili+="120,5,"+str(b0812p)+"\n"
    lili+="-120,5,"+str(b0812n)+"\n"
    lili+="110,5,"+str(b0811p)+"\n"
    lili+="-110,5,"+str(b0811n)+"\n"
    lili+="100,5,"+str(b0810p)+"\n"
    lili+="-100,5,"+str(b0810n)+"\n"
    lili+="90,5,"+str(b0809p)+"\n"
    lili+="-90,5,"+str(b0809n)+"\n"
    lili+="80,5,"+str(b0808p)+"\n"
    lili+="-80,5,"+str(b0808n)+"\n"
    lili+="70,5,"+str(b0807p)+"\n"
    lili+="-70,5,"+str(b0807n)+"\n"
    lili+="60,5,"+str(b0806p)+"\n"
    lili+="-60,5,"+str(b0806n)+"\n"
    lili+="50,5,"+str(b0805p)+"\n"
    lili+="-50,5,"+str(b0805n)+"\n"
    lili+="40,5,"+str(b0804p)+"\n"
    lili+="-40,5,"+str(b0804n)+"\n"
    lili+="30,5,"+str(b0803p)+"\n"
    lili+="-30,5,"+str(b0803n)+"\n"
    lili+="20,5,"+str(b0802p)+"\n"
    lili+="-20,5,"+str(b0802n)+"\n"
    lili+="10,5,"+str(b0801p)+"\n"
    lili+="-10,5,"+str(b0801n)+"\n"
    lili+="0,5,"+str(b0800a)+"\n"
    #Mirror-image
    lill=""
    lill+="120,-85,"+str(c0001p)+"\n"
    lill+="-120,-85,"+str(c0001n)+"\n"
    lill+="0,-85,"+str(c0000a)+"\n"
    lill+="160,-75,"+str(c0104p)+"\n"
    lill+="-160,-75,"+str(c0104n)+"\n"
    lill+="120,-75,"+str(c0103p)+"\n"
    lill+="-120,-75,"+str(c0103n)+"\n"
    lill+="80,-75,"+str(c0102p)+"\n"
    lill+="-80,-75,"+str(c0102n)+"\n"
    lill+="40,-75,"+str(c0101p)+"\n"
    lill+="-40,-75,"+str(c0101n)+"\n"
    lill+="0,-75,"+str(c0100a)+"\n"
    lill+="168,-65,"+str(c0207p)+"\n"
    lill+="-168,-65,"+str(c0207n)+"\n"
    lill+="144,-65,"+str(c0206p)+"\n"
    lill+="-144,-65,"+str(c0206n)+"\n"
    lill+="120,-65,"+str(c0205p)+"\n"
    lill+="-120,-65,"+str(c0205n)+"\n"
    lill+="96,-65,"+str(c0204p)+"\n"
    lill+="-96,-65,"+str(c0204n)+"\n"
    lill+="72,-65,"+str(c0203p)+"\n"
    lill+="-72,-65,"+str(c0203n)+"\n"
    lill+="48,-65,"+str(c0202p)+"\n"
    lill+="-48,-65,"+str(c0202n)+"\n"
    lill+="24,-65,"+str(c0201p)+"\n"
    lill+="-24,-65,"+str(b0201n)+"\n"
    lill+="0,-65,"+str(c0200a)+"\n"
    lill+="180,-55,"+str(c0310a)+"\n"
    lill+="162,-55,"+str(c0309p)+"\n"
    lill+="-162,-55,"+str(c0309n)+"\n"
    lill+="144,-55,"+str(c0308p)+"\n"
    lill+="-144,-55,"+str(c0308n)+"\n"
    lill+="126,-55,"+str(c0307p)+"\n"
    lill+="-126,-55,"+str(c0307n)+"\n"
    lill+="108,-55,"+str(c0306p)+"\n"
    lill+="-108,-55,"+str(c0306n)+"\n"
    lill+="90,-55,"+str(c0305p)+"\n"
    lill+="-90,-55,"+str(c0305n)+"\n"
    lill+="72,-55,"+str(c0304p)+"\n"
    lill+="-72,-55,"+str(c0304n)+"\n"
    lill+="54,-55,"+str(c0303p)+"\n"
    lill+="-54,-55,"+str(c0303n)+"\n"
    lill+="36,-55,"+str(c0302p)+"\n"
    lill+="-36,-55,"+str(c0302n)+"\n"
    lill+="18,-55,"+str(c0301p)+"\n"
    lill+="-18,-55,"+str(c0301n)+"\n"
    lill+="0,-55,"+str(c0300a)+"\n"
    lill+="172.8,-45,"+str(c0412p)+"\n"
    lill+="-172.8,-45,"+str(c0412n)+"\n"
    lill+="158.4,-45,"+str(c0411p)+"\n"
    lill+="-158.4,-45,"+str(c0411n)+"\n"
    lill+="144,-45,"+str(c0410p)+"\n"
    lill+="-144,-45,"+str(c0410n)+"\n"
    lill+="126,-45,"+str(c0409p)+"\n"
    lill+="-126,-45,"+str(c0409n)+"\n"
    lill+="108,-45,"+str(c0408p)+"\n"
    lill+="-108,-45,"+str(c0408n)+"\n"
    lill+="96,-45,"+str(c0407p)+"\n"
    lill+="-96,-45,"+str(c0407n)+"\n"
    lill+="84,-45,"+str(c0406p)+"\n"
    lill+="-84,-45,"+str(c0406n)+"\n"
    lill+="72,-45,"+str(c0405p)+"\n"
    lill+="-72,-45,"+str(c0405n)+"\n"
    lill+="60,-45,"+str(c0404p)+"\n"
    lill+="-60,-45,"+str(c0404n)+"\n"
    lill+="48,-45,"+str(c0403p)+"\n"
    lill+="-48,-45,"+str(c0403n)+"\n"
    lill+="36,-45,"+str(c0402p)+"\n"
    lill+="-36,-45,"+str(c0402n)+"\n"
    lill+="18,-45,"+str(c0401p)+"\n"
    lill+="-18,-45,"+str(c0401n)+"\n"
    lill+="0,-45,"+str(c0400a)+"\n"
    lill+="180,-35,"+str(c0515a)+"\n"
    lill+="168,-35,"+str(c0514p)+"\n"
    lill+="-168,-35,"+str(c0514n)+"\n"
    lill+="156,-35,"+str(c0513p)+"\n"
    lill+="-156,-35,"+str(c0513n)+"\n"
    lill+="144,-35,"+str(c0512p)+"\n"
    lill+="-144,-35,"+str(c0512n)+"\n"
    lill+="132,-35,"+str(c0511p)+"\n"
    lill+="-132,-35,"+str(c0511n)+"\n"
    lill+="120,-35,"+str(c0510p)+"\n"
    lill+="-120,-35,"+str(c0510n)+"\n"
    lill+="108,-35,"+str(c0509p)+"\n"
    lill+="-108,-35,"+str(c0509n)+"\n"
    lill+="96,-35,"+str(c0508p)+"\n"
    lill+="-96,-35,"+str(c0508n)+"\n"
    lill+="84,-35,"+str(c0507p)+"\n"
    lill+="-84,-35,"+str(c0507n)+"\n"
    lill+="72,-35,"+str(c0506p)+"\n"
    lill+="-72,-35,"+str(c0506n)+"\n"
    lill+="60,-35,"+str(c0505p)+"\n"
    lill+="-60,-35,"+str(c0505n)+"\n"
    lill+="48,-35,"+str(c0504p)+"\n"
    lill+="-48,-35,"+str(c0504n)+"\n"
    lill+="36,-35,"+str(c0503p)+"\n"
    lill+="-36,-35,"+str(c0503n)+"\n"
    lill+="24,-35,"+str(c0502p)+"\n"
    lill+="-24,-35,"+str(c0502n)+"\n"
    lill+="12,-35,"+str(c0501p)+"\n"
    lill+="-12,-35,"+str(c0501n)+"\n"
    lill+="0,-35,"+str(c0500a)+"\n"
    lill+="180,-25,"+str(c0616a)+"\n"
    lill+="168.75,-25,"+str(c0615p)+"\n"
    lill+="-168.75,-25,"+str(c0615n)+"\n"
    lill+="157.5,-25,"+str(c0614p)+"\n"
    lill+="-157.5,-25,"+str(c0614n)+"\n"
    lill+="146.25,-25,"+str(c0613p)+"\n"
    lill+="-146.25,-25,"+str(c0613n)+"\n"
    lill+="135,-25,"+str(c0612p)+"\n"
    lill+="-135,-25,"+str(c0612n)+"\n"
    lill+="123.75,-25,"+str(c0611p)+"\n"
    lill+="-123.75,-25,"+str(c0611n)+"\n"
    lill+="112.5,-25,"+str(c0610p)+"\n"
    lill+="-112.5,-25,"+str(c0610n)+"\n"
    lill+="101.25,-25,"+str(c0609p)+"\n"
    lill+="-101.25,-25,"+str(c0609n)+"\n"
    lill+="90,-25,"+str(c0608p)+"\n"
    lill+="-90,-25,"+str(c0608n)+"\n"
    lill+="78.75,-25,"+str(c0607p)+"\n"
    lill+="-78.75,-25,"+str(c0607n)+"\n"
    lill+="67.5,-25,"+str(c0606p)+"\n"
    lill+="-67.5,-25,"+str(c0606n)+"\n"
    lill+="56.25,-25,"+str(c0605p)+"\n"
    lill+="-56.25,-25,"+str(c0605n)+"\n"
    lill+="45,-25,"+str(c0604p)+"\n"
    lill+="-45,-25,"+str(c0604n)+"\n"
    lill+="33.75,-25,"+str(c0603p)+"\n"
    lill+="-33.75,-25,"+str(c0603n)+"\n"
    lill+="22.5,-25,"+str(c0602p)+"\n"
    lill+="-22.5,-25,"+str(c0602n)+"\n"
    lill+="11.25,-25,"+str(c0601p)+"\n"
    lill+="-11.25,-25,"+str(c0601n)+"\n"
    lill+="0,-25,"+str(c0600a)+"\n"
    lill+="174.857,-15,"+str(c0717p)+"\n"
    lill+="-174.857,-15,"+str(c0717n)+"\n"
    lill+="164.571,-15,"+str(c0716p)+"\n"
    lill+="-164.571,-15,"+str(c0716n)+"\n"
    lill+="154.286,-15,"+str(c0715p)+"\n"
    lill+="-154.286,-15,"+str(c0715n)+"\n"
    lill+="144,-15,"+str(c0714p)+"\n"
    lill+="-144,-15,"+str(c0714n)+"\n"
    lill+="133.714,-15,"+str(c0713p)+"\n"
    lill+="-133.714,-15,"+str(c0713n)+"\n"
    lill+="123.429,-15,"+str(c0712p)+"\n"
    lill+="-123.429,-15,"+str(c0712n)+"\n"
    lill+="113.143,-15,"+str(c0711p)+"\n"
    lill+="-113.143,-15,"+str(c0711n)+"\n"
    lill+="102.857,-15,"+str(c0710p)+"\n"
    lill+="-102.857,-15,"+str(c0710n)+"\n"
    lill+="92.5714,-15,"+str(c0709p)+"\n"
    lill+="-92.5714,-15,"+str(c0709n)+"\n"
    lill+="82.2857,-15,"+str(c0708p)+"\n"
    lill+="-82.2857,-15,"+str(c0708n)+"\n"
    lill+="72,-15,"+str(c0707p)+"\n"
    lill+="-72,-15,"+str(c0707n)+"\n"
    lill+="61.7143,-15,"+str(c0706p)+"\n"
    lill+="-61.7143,-15,"+str(c0706n)+"\n"
    lill+="51.4286,-15,"+str(c0705p)+"\n"
    lill+="-51.4286,-15,"+str(c0705n)+"\n"
    lill+="41.1429,-15,"+str(c0704p)+"\n"
    lill+="-41.1429,-15,"+str(c0704n)+"\n"
    lill+="30.8571,-15,"+str(c0703p)+"\n"
    lill+="-30.8571,-15,"+str(c0703n)+"\n"
    lill+="20.5714,-15,"+str(c0702p)+"\n"
    lill+="-20.5714,-15,"+str(c0702n)+"\n"
    lill+="10.2857,-15,"+str(c0701p)+"\n"
    lill+="-10.2857,-15,"+str(c0701n)+"\n"
    lill+="0,-15,"+str(c0700a)+"\n"
    lill+="180,-5,"+str(c0818a)+"\n"
    lill+="170,-5,"+str(c0817p)+"\n"
    lill+="-170,-5,"+str(c0817n)+"\n"
    lill+="160,-5,"+str(c0816p)+"\n"
    lill+="-160,-5,"+str(c0816n)+"\n"
    lill+="150,-5,"+str(c0815p)+"\n"
    lill+="-150,-5,"+str(c0815n)+"\n"
    lill+="140,-5,"+str(c0814p)+"\n"
    lill+="-140,-5,"+str(c0814n)+"\n"
    lill+="130,-5,"+str(c0813p)+"\n"
    lill+="-130,-5,"+str(c0813n)+"\n"
    lill+="120,-5,"+str(c0812p)+"\n"
    lill+="-120,-5,"+str(c0812n)+"\n"
    lill+="110,-5,"+str(c0811p)+"\n"
    lill+="-110,-5,"+str(c0811n)+"\n"
    lill+="100,-5,"+str(c0810p)+"\n"
    lill+="-100,-5,"+str(c0810n)+"\n"
    lill+="90,-5,"+str(c0809p)+"\n"
    lill+="-90,-5,"+str(c0809n)+"\n"
    lill+="80,-5,"+str(c0808p)+"\n"
    lill+="-80,-5,"+str(c0808n)+"\n"
    lill+="70,-5,"+str(c0807p)+"\n"
    lill+="-70,-5,"+str(c0807n)+"\n"
    lill+="60,-5,"+str(c0806p)+"\n"
    lill+="-60,-5,"+str(c0806n)+"\n"
    lill+="50,-5,"+str(c0805p)+"\n"
    lill+="-50,-5,"+str(c0805n)+"\n"
    lill+="40,-5,"+str(c0804p)+"\n"
    lill+="-40,-5,"+str(c0804n)+"\n"
    lill+="30,-5,"+str(c0803p)+"\n"
    lill+="-30,-5,"+str(c0803n)+"\n"
    lill+="20,-5,"+str(c0802p)+"\n"
    lill+="-20,-5,"+str(c0802n)+"\n"
    lill+="10,-5,"+str(c0801p)+"\n"
    lill+="-10,-5,"+str(c0801n)+"\n"
    lill+="0,-5,"+str(c0800a)+"\n"
    with open(cpass+"/rotilt2.csv", mode='w') as h:
        h.write(lili)
        h.write(lill)
        h.close()
        pass
    print("Save:"+cpass+"/rotilt2.csv")

    
    print("------------")
    now = time.ctime()
    cnvtime = time.strptime(now)
    print(time.strftime("%Y/%m/%d %H:%M", cnvtime))
    print("------------")
    global twooo
    global thooo
    global siooo
    global llll
    global lnel
    lloo=""
    llll=""
    loll=""
    olll=""
    onel=""
    lllo=""
    twooo=0
    thooo=0
    siooo=0
    ww=0
    cw=0
    cow=0
    coww=0
    cowww=0
    t00=time.time()
    t01=time.time()
    
    #Data separation
    with open(cpass+"/"+datas, mode='r') as g:
        for line in g:
            #Progress bar
            cowww+=1
            coww+=1
            cow+=1
            cw+=1
            ww+=1
            lnel=line
            if ww > 99:
                ww=0
                lloo+=llll
                llll=""
            if cw > 999:
                cw=0
                lllo+=lloo
                lloo=""
            if cow > 9999:
                sys.stdout.write(".")
                sys.stdout.flush()
                cow=0
                loll+=lllo
                lllo=""
            if coww > 99999:
                t02=time.time()
                print(str(cowww)+"/"+str(round(t02-t01, 1))+"s")
                t01=time.time()
                with open(cpass+"/"+datasi+"_"+dataso+str(Aim)+".star", mode='a') as f:
                    f.write(loll)
                    f.close()
                    pass
                coww=0
                loll=""
                pass
            #Progress bar
            if not line[0] == " ":
                with open(cpass+"/"+datasi+"_"+dataso+str(Aim)+".star", mode='a') as f:
                    f.write(line)
                    f.close()
                    pass
                pass
            if line[0] == " ": # Exclude header line
                lrotno=""
                ltiltno=""
                lpsino=""
                til=""
                rot=""
                csvgl=line.split()
                if len(csvgl) < rotno: # Exclude header line
                    with open(cpass+"/"+datasi+"_"+dataso+str(Aim)+".star", mode='a') as f:
                        f.write(line)
                        f.close()
                        pass
                    pass
                else:
                    # Extract olientation information
                    lrotno=csvgl[rotno].strip()
                    ltiltno=csvgl[tiltno].strip()
                    lpsino=csvgl[psino].strip()
                    rot=float(lrotno)
                    til=float(ltiltno)
                    
                    # Branching by rotation angle & tilt angle
                    if til <= 10:
                        if rot > 60:
                            aver(b0001p)
                            pass
                        elif rot < -60:
                            aver(b0001n)
                            pass
                        else:
                            aver(b0000a)
                            pass
                        pass
                    elif til <= 20:
                        if rot > 140:
                            aver(b0104p)
                            pass
                        elif rot < -140:
                            aver(b0104n)
                            pass
                        elif rot > 100:
                            aver(b0103p)
                            pass
                        elif rot < -100:
                            aver(b0103n)
                            pass
                        elif rot > 60:
                            aver(b0102p)
                            pass
                        elif rot < -60:
                            aver(b0102n)
                            pass
                        elif rot > 20:
                            aver(b0101p)
                            pass
                        elif rot < -20:
                            aver(b0101n)
                            pass
                        else:
                            aver(b0100a)
                            pass
                        pass
                    elif til <= 30:
                        if rot > 156:
                            aver(b0207p)
                            pass
                        elif rot < -156:
                            aver(b0207n)
                            pass
                        elif rot > 132:
                            aver(b0206p)
                            pass
                        elif rot < -132:
                            aver(b0206n)
                            pass
                        elif rot > 108:
                            aver(b0205p)
                            pass
                        elif rot < -108:
                            aver(b0205n)
                            pass
                        elif rot > 84:
                            aver(b0204p)
                            pass
                        elif rot < -84:
                            aver(b0204n)
                            pass
                        elif rot > 60:
                            aver(b0203p)
                            pass
                        elif rot < -60:
                            aver(b0203n)
                            pass
                        elif rot > 36:
                            aver(b0202p)
                            pass
                        elif rot < -36:
                            aver(b0202n)
                            pass
                        elif rot > 12:
                            aver(b0201p)
                            pass
                        elif rot < -12:
                            aver(b0201n)
                            pass
                        else:
                            aver(b0200a)
                            pass
                        pass
                    elif til <= 40:
                        if rot > 171:
                            aver(b0310a)
                            pass
                        elif rot < -171:
                            aver(b0310a)
                            pass
                        elif rot > 153:
                            aver(b0309p)
                            pass
                        elif rot < -153:
                            aver(b0309n)
                            pass
                        elif rot > 135:
                            aver(b0308p)
                            pass
                        elif rot < -135:
                            aver(b0308n)
                            pass
                        elif rot > 117:
                            aver(b0307p)
                            pass
                        elif rot < -117:
                            aver(b0307n)
                            pass
                        elif rot > 99:
                            aver(b0306p)
                            pass
                        elif rot < -99:
                            aver(b0306n)
                            pass
                        elif rot > 81:
                            aver(b0305p)
                            pass
                        elif rot < -81:
                            aver(b0305n)
                            pass
                        elif rot > 63:
                            aver(b0304p)
                            pass
                        elif rot < -63:
                            aver(b0304n)
                            pass
                        elif rot > 45:
                            aver(b0303p)
                            pass
                        elif rot < -45:
                            aver(b0303n)
                            pass
                        elif rot > 27:
                            aver(b0302p)
                            pass
                        elif rot < -27:
                            aver(b0302n)
                            pass
                        elif rot > 9:
                            aver(b0301p)
                            pass
                        elif rot < -9:
                            aver(b0301n)
                            pass
                        else:
                            aver(b0300a)
                            pass
                    elif til <= 50:
                        if rot > 165.6:
                            aver(b0412p)
                            pass
                        elif rot < -165.6:
                            aver(b0412n)
                            pass
                        elif rot > 151.2:
                            aver(b0411p)
                            pass
                        elif rot < -151.2:
                            aver(b0411n)
                            pass
                        elif rot > 136.8:
                            aver(b0410p)
                            pass
                        elif rot < -136.8:
                            aver(b0410n)
                            pass
                        elif rot > 122.4:
                            aver(b0409p)
                            pass
                        elif rot < -122.4:
                            aver(b0409n)
                            pass
                        elif rot > 108:
                            aver(b0408p)
                            pass
                        elif rot < -108:
                            aver(b0408n)
                            pass
                        elif rot > 93.6:
                            aver(b0407p)
                            pass
                        elif rot < -93.6:
                            aver(b0407n)
                            pass
                        elif rot > 79.2:
                            aver(b0406p)
                            pass
                        elif rot < -79.2:
                            aver(b0406n)
                            pass
                        elif rot > 64.8:
                            aver(b0405p)
                            pass
                        elif rot < -64.8:
                            aver(b0405n)
                            pass
                        elif rot > 50.4:
                            aver(b0404p)
                            pass
                        elif rot < -50.4:
                            aver(b0404n)
                            pass
                        elif rot > 36:
                            aver(b0403p)
                            pass
                        elif rot < -36:
                            aver(b0403n)
                            pass
                        elif rot > 21.6:
                            aver(b0402p)
                            pass
                        elif rot < -21.6:
                            aver(b0402n)
                            pass
                        elif rot > 7.2:
                            aver(b0401p)
                            pass
                        elif rot < -7.2:
                            aver(b0401n)
                            pass
                        else:
                            aver(b0400a)
                            pass
                    elif til <= 60:
                        if rot > 174:
                            aver(b0515a)
                            pass
                        elif rot < -174:
                            aver(b0515a)
                            pass
                        elif rot > 162:
                            aver(b0514p)
                            pass
                        elif rot < -162:
                            aver(b0514n)
                            pass
                        elif rot > 150:
                            aver(b0513p)
                            pass
                        elif rot < -150:
                            aver(b0513n)
                            pass
                        elif rot > 138:
                            aver(b0512p)
                            pass
                        elif rot < -138:
                            aver(b0512n)
                            pass
                        elif rot > 126:
                            aver(b0511p)
                            pass
                        elif rot < -126:
                            aver(b0511n)
                            pass
                        elif rot > 114:
                            aver(b0510p)
                            pass
                        elif rot < -114:
                            aver(b0510n)
                            pass
                        elif rot > 102:
                            aver(b0509p)
                            pass
                        elif rot < -102:
                            aver(b0509n)
                            pass
                        elif rot > 90:
                            aver(b0508p)
                            pass
                        elif rot < -90:
                            aver(b0508n)
                            pass
                        elif rot > 78:
                            aver(b0507p)
                            pass
                        elif rot < -78:
                            aver(b0507n)
                            pass
                        elif rot > 66:
                            aver(b0506p)
                            pass
                        elif rot < -66:
                            aver(b0506n)
                            pass
                        elif rot > 54:
                            aver(b0505p)
                            pass
                        elif rot < -54:
                            aver(b0505n)
                            pass
                        elif rot > 42:
                            aver(b0504p)
                            pass
                        elif rot < -42:
                            aver(b0504n)
                            pass
                        elif rot > 30:
                            aver(b0503p)
                            pass
                        elif rot < -30:
                            aver(b0503n)
                            pass
                        elif rot > 18:
                            aver(b0502p)
                            pass
                        elif rot < -18:
                            aver(b0502n)
                            pass
                        elif rot > 6:
                            aver(b0501p)
                            pass
                        elif rot < -6:
                            aver(b0501n)
                            pass
                        else:
                            aver(b0500a)
                            pass
                    elif til <= 70:
                        if rot > 174.375:
                            aver(b0616a)
                            pass
                        elif rot < -174.375:
                            aver(b0616a)
                            pass
                        elif rot > 163.125:
                            aver(b0615p)
                            pass
                        elif rot < -163.125:
                            aver(b0615n)
                            pass
                        elif rot > 151.875:
                            aver(b0614p)
                            pass
                        elif rot < -151.875:
                            aver(b0614n)
                            pass
                        elif rot > 140.625:
                            aver(b0613p)
                            pass
                        elif rot < -140.625:
                            aver(b0613n)
                            pass
                        elif rot > 129.375:
                            aver(b0612p)
                            pass
                        elif rot < -129.375:
                            aver(b0612n)
                            pass
                        elif rot > 118.125:
                            aver(b0611p)
                            pass
                        elif rot < -118.125:
                            aver(b0611n)
                            pass
                        elif rot > 106.875:
                            aver(b0610p)
                            pass
                        elif rot < -106.875:
                            aver(b0610n)
                            pass
                        elif rot > 95.625:
                            aver(b0609p)
                            pass
                        elif rot < -95.625:
                            aver(b0609n)
                            pass
                        elif rot > 84.375:
                            aver(b0608p)
                            pass
                        elif rot < -84.375:
                            aver(b0608n)
                            pass
                        elif rot > 73.125:
                            aver(b0607p)
                            pass
                        elif rot < -73.125:
                            aver(b0607n)
                            pass
                        elif rot > 61.875:
                            aver(b0606p)
                            pass
                        elif rot < -61.875:
                            aver(b0606n)
                            pass
                        elif rot > 50.625:
                            aver(b0605p)
                            pass
                        elif rot < -50.625:
                            aver(b0605n)
                            pass
                        elif rot > 39.375:
                            aver(b0604p)
                            pass
                        elif rot < -39.375:
                            aver(b0604n)
                            pass
                        elif rot > 28.125:
                            aver(b0603p)
                            pass
                        elif rot < -28.125:
                            aver(b0603n)
                            pass
                        elif rot > 16.875:
                            aver(b0602p)
                            pass
                        elif rot < -16.875:
                            aver(b0602n)
                            pass
                        elif rot > 5.625:
                            aver(b0601p)
                            pass
                        elif rot < -5.625:
                            aver(b0601n)
                            pass
                        else:
                            aver(b0600a)
                            pass
                    elif til <= 80:
                        if rot > 169.714:
                            aver(b0717p)
                            pass
                        elif rot < -169.714:
                            aver(b0717n)
                            pass
                        elif rot > 159.429:
                            aver(b0716p)
                            pass
                        elif rot < -159.429:
                            aver(b0716n)
                            pass
                        elif rot > 149.143:
                            aver(b0715p)
                            pass
                        elif rot < -149.143:
                            aver(b0715n)
                            pass
                        elif rot > 138.857:
                            aver(b0714p)
                            pass
                        elif rot < -138.857:
                            aver(b0714n)
                            pass
                        elif rot > 128.571:
                            aver(b0713p)
                            pass
                        elif rot < -128.571:
                            aver(b0713n)
                            pass
                        elif rot > 118.286:
                            aver(b0712p)
                            pass
                        elif rot < -118.286:
                            aver(b0712n)
                            pass
                        elif rot > 108:
                            aver(b0711p)
                            pass
                        elif rot < -108:
                            aver(b0711n)
                            pass
                        elif rot > 97.7143:
                            aver(b0710p)
                            pass
                        elif rot < -97.7143:
                            aver(b0710n)
                            pass
                        elif rot > 87.4286:
                            aver(b0709p)
                            pass
                        elif rot < -87.4286:
                            aver(b0709n)
                            pass
                        elif rot > 77.1429:
                            aver(b0708p)
                            pass
                        elif rot < -77.2429:
                            aver(b0708n)
                            pass
                        elif rot > 66.8571:
                            aver(b0707p)
                            pass
                        elif rot < -66.8571:
                            aver(b0707n)
                            pass
                        elif rot > 56.5714:
                            aver(b0706p)
                            pass
                        elif rot < -56.5714:
                            aver(b0706n)
                            pass
                        elif rot > 46.2857:
                            aver(b0705p)
                            pass
                        elif rot < -46.2857:
                            aver(b0705n)
                            pass
                        elif rot > 36:
                            aver(b0704p)
                            pass
                        elif rot < -36:
                            aver(b0704n)
                            pass
                        elif rot > 25.7143:
                            aver(b0703p)
                            pass
                        elif rot < -25.7143:
                            aver(b0703n)
                            pass
                        elif rot > 15.4286:
                            aver(b0702p)
                            pass
                        elif rot < -15.4826:
                            aver(b0702n)
                            pass
                        elif rot > 5.14286:
                            aver(b0701p)
                            pass
                        elif rot < -5.24286:
                            aver(b0701n)
                            pass
                        else:
                            aver(b0700a)
                            pass
                    elif til <= 90:
                        if rot > 175:
                            aver(b0818a)
                            pass
                        elif rot < -175:
                            aver(b0818a)
                            pass
                        elif rot > 165:
                            aver(b0817p)
                            pass
                        elif rot < -165:
                            aver(b0817n)
                            pass
                        elif rot > 155:
                            aver(b0816p)
                            pass
                        elif rot < -155:
                            aver(b0816n)
                            pass
                        elif rot > 145:
                            aver(b0815p)
                            pass
                        elif rot < -145:
                            aver(b0815n)
                            pass
                        elif rot > 135:
                            aver(b0814p)
                            pass
                        elif rot < -135:
                            aver(b0814n)
                            pass
                        elif rot > 125:
                            aver(b0813p)
                            pass
                        elif rot < -125:
                            aver(b0813n)
                            pass
                        elif rot > 115:
                            aver(b0812p)
                            pass
                        elif rot < -115:
                            aver(b0812n)
                            pass
                        elif rot > 105:
                            aver(b0811p)
                            pass
                        elif rot < -105:
                            aver(b0811n)
                            pass
                        elif rot > 95:
                            aver(b0810p)
                            pass
                        elif rot < -95:
                            aver(b0810n)
                            pass
                        elif rot > 85:
                            aver(b0809p)
                            pass
                        elif rot < -85:
                            aver(b0809n)
                            pass
                        elif rot > 75:
                            aver(b0808p)
                            pass
                        elif rot < -75:
                            aver(b0808n)
                            pass
                        elif rot > 65:
                            aver(b0807p)
                            pass
                        elif rot < -65:
                            aver(b0807n)
                            pass
                        elif rot > 55:
                            aver(b0806p)
                            pass
                        elif rot < -55:
                            aver(b0806n)
                            pass
                        elif rot > 45:
                            aver(b0805p)
                            pass
                        elif rot < -45:
                            aver(b0805n)
                            pass
                        elif rot > 35:
                            aver(b0804p)
                            pass
                        elif rot < -35:
                            aver(b0804n)
                            pass
                        elif rot > 25:
                            aver(b0803p)
                            pass
                        elif rot < -25:
                            aver(b0803n)
                            pass
                        elif rot > 15:
                            aver(b0802p)
                            pass
                        elif rot < -15:
                            aver(b0802n)
                            pass
                        elif rot > 5:
                            aver(b0801p)
                            pass
                        elif rot < -5:
                            aver(b0801n)
                            pass
                        else:
                            aver(b0800a)
                            pass
                    elif til <= 100:
                        if rot > 175:
                            aver(c0818a)
                            pass
                        elif rot < -175:
                            aver(c0818a)
                            pass
                        elif rot > 165:
                            aver(c0817p)
                            pass
                        elif rot < -165:
                            aver(c0817n)
                            pass
                        elif rot > 155:
                            aver(c0816p)
                            pass
                        elif rot < -155:
                            aver(c0816n)
                            pass
                        elif rot > 145:
                            aver(c0815p)
                            pass
                        elif rot < -145:
                            aver(c0815n)
                            pass
                        elif rot > 135:
                            aver(c0814p)
                            pass
                        elif rot < -135:
                            aver(c0814n)
                            pass
                        elif rot > 125:
                            aver(c0813p)
                            pass
                        elif rot < -125:
                            aver(c0813n)
                            pass
                        elif rot > 115:
                            aver(c0812p)
                            pass
                        elif rot < -115:
                            aver(c0812n)
                            pass
                        elif rot > 105:
                            aver(c0811p)
                            pass
                        elif rot < -105:
                            aver(c0811n)
                            pass
                        elif rot > 95:
                            aver(c0810p)
                            pass
                        elif rot < -95:
                            aver(c0810n)
                            pass
                        elif rot > 85:
                            aver(c0809p)
                            pass
                        elif rot < -85:
                            aver(c0809n)
                            pass
                        elif rot > 75:
                            aver(c0808p)
                            pass
                        elif rot < -75:
                            aver(c0808n)
                            pass
                        elif rot > 65:
                            aver(c0807p)
                            pass
                        elif rot < -65:
                            aver(c0807n)
                            pass
                        elif rot > 55:
                            aver(c0806p)
                            pass
                        elif rot < -55:
                            aver(c0806n)
                            pass
                        elif rot > 45:
                            aver(c0805p)
                            pass
                        elif rot < -45:
                            aver(c0805n)
                            pass
                        elif rot > 35:
                            aver(c0804p)
                            pass
                        elif rot < -35:
                            aver(c0804n)
                            pass
                        elif rot > 25:
                            aver(c0803p)
                            pass
                        elif rot < -25:
                            aver(c0803n)
                            pass
                        elif rot > 15:
                            aver(c0802p)
                            pass
                        elif rot < -15:
                            aver(c0802n)
                            pass
                        elif rot > 5:
                            aver(c0801p)
                            pass
                        elif rot < -5:
                            aver(c0801n)
                            pass
                        else:
                            aver(c0800a)
                            pass
                    elif til <= 110:
                        if rot > 169.714:
                            aver(c0717p)
                            pass
                        elif rot < -169.714:
                            aver(c0717n)
                            pass
                        elif rot > 159.429:
                            aver(c0716p)
                            pass
                        elif rot < -159.429:
                            aver(c0716n)
                            pass
                        elif rot > 149.143:
                            aver(c0715p)
                            pass
                        elif rot < -149.143:
                            aver(c0715n)
                            pass
                        elif rot > 138.857:
                            aver(c0714p)
                            pass
                        elif rot < -138.857:
                            aver(c0714n)
                            pass
                        elif rot > 128.571:
                            aver(c0713p)
                            pass
                        elif rot < -128.571:
                            aver(c0713n)
                            pass
                        elif rot > 118.286:
                            aver(c0712p)
                            pass
                        elif rot < -118.286:
                            aver(c0712n)
                            pass
                        elif rot > 108:
                            aver(c0711p)
                            pass
                        elif rot < -108:
                            aver(c0711n)
                            pass
                        elif rot > 97.7143:
                            aver(c0710p)
                            pass
                        elif rot < -97.7143:
                            aver(c0710n)
                            pass
                        elif rot > 87.4286:
                            aver(c0709p)
                            pass
                        elif rot < -87.4286:
                            aver(c0709n)
                            pass
                        elif rot > 77.1429:
                            aver(c0708p)
                            pass
                        elif rot < -77.2429:
                            aver(c0708n)
                            pass
                        elif rot > 66.8571:
                            aver(c0707p)
                            pass
                        elif rot < -66.8571:
                            aver(c0707n)
                            pass
                        elif rot > 56.5714:
                            aver(c0706p)
                            pass
                        elif rot < -56.5714:
                            aver(c0706n)
                            pass
                        elif rot > 46.2857:
                            aver(c0705p)
                            pass
                        elif rot < -46.2857:
                            aver(c0705n)
                            pass
                        elif rot > 36:
                            aver(c0704p)
                            pass
                        elif rot < -36:
                            aver(c0704n)
                            pass
                        elif rot > 25.7143:
                            aver(c0703p)
                            pass
                        elif rot < -25.7143:
                            aver(c0703n)
                            pass
                        elif rot > 15.4286:
                            aver(c0702p)
                            pass
                        elif rot < -15.4826:
                            aver(c0702n)
                            pass
                        elif rot > 5.14286:
                            aver(c0701p)
                            pass
                        elif rot < -5.24286:
                            aver(c0701n)
                            pass
                        else:
                            aver(c0700a)
                            pass
                    elif til <= 120:
                        if rot > 174.375:
                            aver(c0616a)
                            pass
                        elif rot < -174.375:
                            aver(c0616a)
                            pass
                        elif rot > 163.125:
                            aver(c0615p)
                            pass
                        elif rot < -163.125:
                            aver(c0615n)
                            pass
                        elif rot > 151.875:
                            aver(c0614p)
                            pass
                        elif rot < -151.875:
                            aver(c0614n)
                            pass
                        elif rot > 140.625:
                            aver(c0613p)
                            pass
                        elif rot < -140.625:
                            aver(c0613n)
                            pass
                        elif rot > 129.375:
                            aver(c0612p)
                            pass
                        elif rot < -129.375:
                            aver(c0612n)
                            pass
                        elif rot > 118.125:
                            aver(c0611p)
                            pass
                        elif rot < -118.125:
                            aver(c0611n)
                            pass
                        elif rot > 106.875:
                            aver(c0610p)
                            pass
                        elif rot < -106.875:
                            aver(c0610n)
                            pass
                        elif rot > 95.625:
                            aver(c0609p)
                            pass
                        elif rot < -95.625:
                            aver(c0609n)
                            pass
                        elif rot > 84.375:
                            aver(c0608p)
                            pass
                        elif rot < -84.375:
                            aver(c0608n)
                            pass
                        elif rot > 73.125:
                            aver(c0607p)
                            pass
                        elif rot < -73.125:
                            aver(c0607n)
                            pass
                        elif rot > 61.875:
                            aver(c0606p)
                            pass
                        elif rot < -61.875:
                            aver(c0606n)
                            pass
                        elif rot > 50.625:
                            aver(c0605p)
                            pass
                        elif rot < -50.625:
                            aver(c0605n)
                            pass
                        elif rot > 39.375:
                            aver(c0604p)
                            pass
                        elif rot < -39.375:
                            aver(c0604n)
                            pass
                        elif rot > 28.125:
                            aver(c0603p)
                            pass
                        elif rot < -28.125:
                            aver(c0603n)
                            pass
                        elif rot > 16.875:
                            aver(c0602p)
                            pass
                        elif rot < -16.875:
                            aver(c0602n)
                            pass
                        elif rot > 5.625:
                            aver(c0601p)
                            pass
                        elif rot < -5.625:
                            aver(c0601n)
                            pass
                        else:
                            aver(c0600a)
                            pass
                    elif til <= 130:
                        if rot > 174:
                            aver(c0515a)
                            pass
                        elif rot < -174:
                            aver(c0515a)
                            pass
                        elif rot > 162:
                            aver(c0514p)
                            pass
                        elif rot < -162:
                            aver(c0514n)
                            pass
                        elif rot > 150:
                            aver(c0513p)
                            pass
                        elif rot < -150:
                            aver(c0513n)
                            pass
                        elif rot > 138:
                            aver(c0512p)
                            pass
                        elif rot < -138:
                            aver(c0512n)
                            pass
                        elif rot > 126:
                            aver(c0511p)
                            pass
                        elif rot < -126:
                            aver(c0511n)
                            pass
                        elif rot > 114:
                            aver(c0510p)
                            pass
                        elif rot < -114:
                            aver(c0510n)
                            pass
                        elif rot > 102:
                            aver(c0509p)
                            pass
                        elif rot < -102:
                            aver(c0509n)
                            pass
                        elif rot > 90:
                            aver(c0508p)
                            pass
                        elif rot < -90:
                            aver(c0508n)
                            pass
                        elif rot > 78:
                            aver(c0507p)
                            pass
                        elif rot < -78:
                            aver(c0507n)
                            pass
                        elif rot > 66:
                            aver(c0506p)
                            pass
                        elif rot < -66:
                            aver(c0506n)
                            pass
                        elif rot > 54:
                            aver(c0505p)
                            pass
                        elif rot < -54:
                            aver(c0505n)
                            pass
                        elif rot > 42:
                            aver(c0504p)
                            pass
                        elif rot < -42:
                            aver(c0504n)
                            pass
                        elif rot > 30:
                            aver(c0503p)
                            pass
                        elif rot < -30:
                            aver(c0503n)
                            pass
                        elif rot > 18:
                            aver(c0502p)
                            pass
                        elif rot < -18:
                            aver(c0502n)
                            pass
                        elif rot > 6:
                            aver(c0501p)
                            pass
                        elif rot < -6:
                            aver(c0501n)
                            pass
                        else:
                            aver(c0500a)
                            pass
                    elif til <= 140:
                        if rot > 165.6:
                            aver(c0412p)
                            pass
                        elif rot < -165.6:
                            aver(c0412n)
                            pass
                        elif rot > 151.2:
                            aver(c0411p)
                            pass
                        elif rot < -151.2:
                            aver(c0411n)
                            pass
                        elif rot > 136.8:
                            aver(c0410p)
                            pass
                        elif rot < -136.8:
                            aver(c0410n)
                            pass
                        elif rot > 122.4:
                            aver(c0409p)
                            pass
                        elif rot < -122.4:
                            aver(c0409n)
                            pass
                        elif rot > 108:
                            aver(c0408p)
                            pass
                        elif rot < -108:
                            aver(c0408n)
                            pass
                        elif rot > 93.6:
                            aver(c0407p)
                            pass
                        elif rot < -93.6:
                            aver(c0407n)
                            pass
                        elif rot > 79.2:
                            aver(c0406p)
                            pass
                        elif rot < -79.2:
                            aver(c0406n)
                            pass
                        elif rot > 64.8:
                            aver(c0405p)
                            pass
                        elif rot < -64.8:
                            aver(c0405n)
                            pass
                        elif rot > 50.4:
                            aver(c0404p)
                            pass
                        elif rot < -50.4:
                            aver(c0404n)
                            pass
                        elif rot > 36:
                            aver(c0403p)
                            pass
                        elif rot < -36:
                            aver(c0403n)
                            pass
                        elif rot > 21.6:
                            aver(c0402p)
                            pass
                        elif rot < -21.6:
                            aver(c0402n)
                            pass
                        elif rot > 7.2:
                            aver(c0401p)
                            pass
                        elif rot < -7.2:
                            aver(c0401n)
                            pass
                        else:
                            aver(c0400a)
                            pass
                    elif til <= 150:
                        if rot > 171:
                            aver(c0310a)
                            pass
                        elif rot < -171:
                            aver(c0310a)
                            pass
                        elif rot > 153:
                            aver(c0309p)
                            pass
                        elif rot < -153:
                            aver(c0309n)
                            pass
                        elif rot > 135:
                            aver(c0308p)
                            pass
                        elif rot < -135:
                            aver(c0308n)
                            pass
                        elif rot > 117:
                            aver(c0307p)
                            pass
                        elif rot < -117:
                            aver(c0307n)
                            pass
                        elif rot > 99:
                            aver(c0306p)
                            pass
                        elif rot < -99:
                            aver(c0306n)
                            pass
                        elif rot > 81:
                            aver(c0305p)
                            pass
                        elif rot < -81:
                            aver(c0305n)
                            pass
                        elif rot > 63:
                            aver(c0304p)
                            pass
                        elif rot < -63:
                            aver(c0304n)
                            pass
                        elif rot > 45:
                            aver(c0303p)
                            pass
                        elif rot < -45:
                            aver(c0303n)
                            pass
                        elif rot > 27:
                            aver(c0302p)
                            pass
                        elif rot < -27:
                            aver(c0302n)
                            pass
                        elif rot > 9:
                            aver(c0301p)
                            pass
                        elif rot < -9:
                            aver(c0301n)
                            pass
                        else:
                            aver(c0300a)
                            pass
                    elif til <= 160:
                        if rot > 156:
                            aver(c0207p)
                            pass
                        elif rot < -156:
                            aver(c0207n)
                            pass
                        elif rot > 132:
                            aver(c0206p)
                            pass
                        elif rot < -132:
                            aver(c0206n)
                            pass
                        elif rot > 108:
                            aver(c0205p)
                            pass
                        elif rot < -108:
                            aver(c0205n)
                            pass
                        elif rot > 84:
                            aver(c0204p)
                            pass
                        elif rot < -84:
                            aver(c0204n)
                            pass
                        elif rot > 60:
                            aver(c0203p)
                            pass
                        elif rot < -60:
                            aver(c0203n)
                            pass
                        elif rot > 36:
                            aver(c0202p)
                            pass
                        elif rot < -36:
                            aver(c0202n)
                            pass
                        elif rot > 12:
                            aver(c0201p)
                            pass
                        elif rot < -12:
                            aver(c0201n)
                            pass
                        else:
                            aver(c0200a)
                            pass
                    elif til <= 170:
                        if rot > 140:
                            aver(c0104p)
                            pass
                        elif rot < -140:
                            aver(c0104n)
                            pass
                        elif rot > 100:
                            aver(c0103p)
                            pass
                        elif rot < -100:
                            aver(c0103n)
                            pass
                        elif rot > 60:
                            aver(c0102p)
                            pass
                        elif rot < -60:
                            aver(c0102n)
                            pass
                        elif rot > 20:
                            aver(c0101p)
                            pass
                        elif rot < -20:
                            aver(c0101n)
                            pass
                        else:
                            aver(c0100a)
                            pass
                        pass
                    else:
                        if rot > 60:
                            aver(c0001p)
                            pass
                        elif rot < -60:
                            aver(c0001n)
                            pass
                        else:
                            aver(c0000a)
                            pass
                        pass
                    pass
                pass
            pass
        pass
    #Finish 
    print(str(cowww)+"lines were loaded")
    print("------------")
    now = time.ctime()
    cnvtime = time.strptime(now)
    print(time.strftime("%Y/%m/%d %H:%M", cnvtime))
    t03=time.time()
    print("Fin :Integration/"+str(round(t03-t00, 1))+"s")
    print("Save:"+cpass+"/"+datasi+"_"+dataso+str(Aim)+".star")

# data integration
def aver(x0YZZa):
    global llll
    global line
    cocouu=0
    rrrttt=float(x0YZZa)/Aim
    if rrrttt > float(2)/3:
        llll+=lnel
        cocouu+=1
        pass
    else:
        if cocouu == 0:
            for ratiii in range(98):
                ratmin=2*ratiii+3
                ratmax=2*ratiii+5
                tiomin=float(2)/ratmin
                tiomax=float(2)/ratmax
                if rrrttt <= tiomin:
                    if rrrttt >tiomax:
                        baisuu=ratiii+2
                        llll+=lnel*baisuu
                        cocouu+=1
                        pass
                    pass
                pass
            pass
        pass
    if rrrttt <= float(2)/199:
        llll+=lnel*100
        pass
    pass

# caliculate integrate No.
def avera(x0YZZa):
    cocouu=0
    rrrttt=float(x0YZZa)/Aim
    if rrrttt > float(2)/3:
        return 1
        cocouu+=1
        pass
    else:
        if cocouu == 0:
            for ratiii in range(98):
                ratmin=2*ratiii+3
                ratmax=2*ratiii+5
                tiomin=float(2)/ratmin
                tiomax=float(2)/ratmax
                if rrrttt <= tiomin:
                    if rrrttt >tiomax:
                        return ratiii+2
                        cocouu+=1
                        pass
                    pass
                pass
            pass
        pass
    if rrrttt <= float(2)/199:
        return 100
        pass
    pass

# caluculate integrated data No.
def integ(x0YZZa):
    return avera(x0YZZa)*x0YZZa
    pass

print("------------")
read()
angtil()
print("------------")
now = time.ctime()
cnvtime = time.strptime(now)
print(time.strftime("%Y/%m/%d %H:%M", cnvtime))
print("Finish:"+str(sys.argv))
print("------------")
