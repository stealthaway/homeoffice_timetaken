#import simplejson 
#import BeautifulSoup
import urllib2
import time
import sys
import datetime
import os.path
from bs4  import BeautifulSoup
from datetime import datetime as dt

global filestart 

global old_stdout

strhmhoodicrcl = 'https://www.google.co.in/maps/dir/T+K+Reddy+Layout,+Annaiah+Reddy+Layout,+Bengaluru,+Karnataka/Hoodi+Circle,+Krishnarajapura,+Bengaluru,+Karnataka/@12.9939173,77.6829301,14z/data=!4m14!4m13!1m5!1m1!1s0x3bae10d5064f3e6d:0x84eb0cebc4387e!2m2!1d77.656118!2d13.0178419!1m5!1m1!1s0x3bae11968501ba95:0x31d127d154c62de0!2m2!1d77.7161007!2d12.9922218!3e0?hl=en'

strhoodisapl = 'https://www.google.co.in/maps/dir/Hoodi+Circle,+Krishnarajapura,+Bengaluru,+Karnataka/SAP+Labs+India+Private+Limited,+EPIP+Zone,+Bengaluru,+Karnataka/@12.9843733,77.7077343,16z/data=!4m14!4m13!1m5!1m1!1s0x3bae11968501ba95:0x31d127d154c62de0!2m2!1d77.7161007!2d12.9922218!1m5!1m1!1s0x3bae0dfe634d7e11:0x6a217aa6cb2f5b6!2m2!1d77.7155203!2d12.9792418!3e0?hl=en'

strsapltowns = 'https://www.google.co.in/maps/dir/SAP+Labs+India+Private+Limited,+EPIP+Zone,+Bengaluru,+Karnataka/WNS,+Plot+8A,+RMZ+Centennial,+Kundalahalli+Main+Road,,+Whitefield,+Bengaluru,+Karnataka+560048/@12.9770256,77.7119831,17z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x3bae0dfe634d7e11:0x6a217aa6cb2f5b6!2m2!1d77.7155203!2d12.9792418!1m5!1m1!1s0x3bae1188797b7c53:0xe5179457e234372e!2m2!1d77.7112032!2d12.975107!3e0?hl=en'

def logfilename():
     dayofwk =   dt.today().weekday()
     monthofwk = dt.today().month
     date = dt.today().day
     txtfile = str(dayofwk) + str(monthofwk) + str(date) + ".log"
     old_stdout = sys.stdout
     log_file = open(txtfile,"w")
     sys.stdout = log_file
     return old_stdout, log_file

def core_morn_func():
 for i in range(1):
    if i>0:
        time.sleep(1)

    soup = BeautifulSoup(urllib2.urlopen(strhmhoodicrcl).read(),"html5lib")
    txt = soup.script
    #print(txt.string)
    txt = unicode(txt.string)
    pos = txt.index("10.0 km")
    pos1 = pos + 100
    outstr = txt[pos:pos1]
    #print(outstr)
    m1pos = outstr.find('min')
    m1pos = m1pos + 3
    m2pos = outstr.find('min', m1pos)
    #print(m2pos)
    aspos = outstr.find('"', (m2pos - 4))
    #print(aspos)
    if ((int(m2pos) - int(aspos)) == 4):
      grepos = m2pos - 3
    else:
      grepos = m2pos - 2   
    #print(grepos) 
    min1 = outstr[(grepos):m2pos]  
    intmin1 = int(min1)    
    #print(intmin1)

# start next step 2
    soup1 = BeautifulSoup(urllib2.urlopen(strhoodisapl).read(),"html5lib")
    txt1 = soup1.script
    
    txt1 = unicode(txt1.string)
    pos = txt1.index("2.9 km")
    pos1 = pos + 100
    outstr = txt1[pos:pos1]
    #print(outstr)
    m1pos = outstr.find('min')
    m1pos = m1pos + 3
    m2pos = outstr.find('min', m1pos)
    #print(m2pos)
    aspos = outstr.find('"', (m2pos - 4))
    #print(aspos)
    if ((int(m2pos) - int(aspos)) == 4):
      grepos = m2pos - 3
    else:
      grepos = m2pos - 2   
    #print(grepos) 
    min2 = outstr[(grepos):m2pos]  
    intmin2 = int(min2)    

# start next step 3

    soup2 = BeautifulSoup(urllib2.urlopen(strsapltowns).read(),"html5lib")
    txt2 = soup2.script
    txt2 = unicode(txt2.string)
    pos = txt2.index("2.2 km")
    pos1 = pos + 100
    outstr = txt2[pos:pos1]
    #print(outstr)
    m1pos = outstr.find('min')
    m1pos = m1pos + 3
    m2pos = outstr.find('min', m1pos)
    #print(m2pos)
    aspos = outstr.find('"', (m2pos - 4))
    #print(aspos)
    if ((int(m2pos) - int(aspos)) == 4):
      grepos = m2pos - 3
    else:
      grepos = m2pos - 2   
    #print(grepos) 
    min3 = outstr[(grepos):m2pos]  
    intmin3 = int(min3)    


#calculate final minutes
    ret = ((intmin1 + intmin2 + intmin3))
#    print ret
    return ret




def funcmorn():
#    sys.stdout = log_file
    #if (ret == 0):
       #open file
    #   retstd, filename = logfilename()
    for i in range(60):
         if i>0:
            time.sleep(480)#5 mins 
         travelmins = core_morn_func() 
         today = datetime.date.today()
         print(travelmins,dt.now().hour,dt.now().minute)
    #return (retstd, filename)

def funceveng():

    for i in range(1):
         if i>0:
            time.sleep(4) 
         travelmins = core_morn_func()
         today = datetime.date.today()
         print(travelmins,dt.now().hour,dt.now().minute)

    #sys.stdout = var 
    #filename.close()
    return 1




def main():
   ret = 0
 #  for i in range(1):
   while True:
        dayofwk = dt.today().weekday()
        monthofwk = dt.today().month
        date = dt.today().day
        txtfile = str(dayofwk) + str(monthofwk) + str(date) + ".log"
        if dt.now().hour in range(6,11): # 6 to 11
           if(False == os.path.isfile(txtfile)):
              old_stdout = sys.stdout
              log_file = open(txtfile,"w")
              sys.stdout = log_file
           # calc-func 
              funcmorn()
        #if dt.now().hour in range(6,7): # 16, 20
            # calc - func 
        #funceveng() 
              #if(True == os.path.isfile(txtfile)):
              sys.stdout = old_stdout 
              log_file.close()
        else:
          time.sleep(10)

main()
