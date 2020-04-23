#import simplejson 
#import BeautifulSoup
import urllib2
import time
import sys
import datetime
import glob
import os.path
#from bs4  import BeautifulSoup
from datetime import datetime as dt
import subprocess 
import shutil
global filestart 

global old_stdout

#strhmhoodicrcl = 'https://www.google.co.in/maps/dir/T+K+Reddy+Layout,+Annaiah+Reddy+Layout,+Bengaluru,+Karnataka/Hoodi+Circle,+Krishnarajapura,+Bengaluru,+Karnataka/@12.9939173,77.6829301,14z/data=!4m14!4m13!1m5!1m1!1s0x3bae10d5064f3e6d:0x84eb0cebc4387e!2m2!1d77.656118!2d13.0178419!1m5!1m1!1s0x3bae11968501ba95:0x31d127d154c62de0!2m2!1d77.7161007!2d12.9922218!3e0?hl=en'

strhmhoodicrcl =  'https://www.google.co.in/maps/dir/T+K+Reddy+Layout,+Annaiah+Reddy+Layout,+Bengaluru,+Karnataka/12.9920048,77.7153534/@13.0057344,77.6693396,14z/data=!4m9!4m8!1m5!1m1!1s0x3bae10d5064f3e6d:0x84eb0cebc4387e!2m2!1d77.656118!2d13.0178419!1m0!3e0?hl=en%27'

strhoodisapl = 'https://www.google.co.in/maps/dir/Hoodi+Circle,+Krishnarajapura,+Bengaluru,+Karnataka/SAP+Labs+India+Private+Limited,+EPIP+Zone,+Bengaluru,+Karnataka/@12.9843733,77.7077343,16z/data=!4m14!4m13!1m5!1m1!1s0x3bae11968501ba95:0x31d127d154c62de0!2m2!1d77.7161007!2d12.9922218!1m5!1m1!1s0x3bae0dfe634d7e11:0x6a217aa6cb2f5b6!2m2!1d77.7155203!2d12.9792418!3e0?hl=en'

strsapltowns = 'https://www.google.co.in/maps/dir/SAP+Labs+India+Private+Limited,+EPIP+Zone,+Bengaluru,+Karnataka/WNS,+Plot+8A,+RMZ+Centennial,+Kundalahalli+Main+Road,,+Whitefield,+Bengaluru,+Karnataka+560048/@12.9770256,77.7119831,17z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x3bae0dfe634d7e11:0x6a217aa6cb2f5b6!2m2!1d77.7155203!2d12.9792418!1m5!1m1!1s0x3bae1188797b7c53:0xe5179457e234372e!2m2!1d77.7112032!2d12.975107!3e0?hl=en'

##def logfilename():
##     dayofwk =   dt.today().weekday()
##     monthofwk = dt.today().month
##     date = dt.today().day
##     txtfile = str(dayofwk) + str(monthofwk) + str(date) + ".log"
##     old_stdout = sys.stdout
##     log_file = open(txtfile,"w")
##     sys.stdout = log_file
##     return old_stdout, log_file




##class="widget-pan
##e-section-directions-trip clearfix selected" role="option" vet="14905" ved="0ahUKEwj87ObGtKvOAhVBMI8KHbifAVEQ-CQIBigCMAA" tabindex="-1" jstrack="xh6lV_zxI8HgvAS4v4aIBQ"
##data-trip-index="0" jstcache="604"> <div aria-label="  Driving  " role="img" jstcache="389" class="widget-pane-section-directions-trip-travel-mode-icon drive" jsan="7.wi
##dget-pane-section-directions-trip-travel-mode-icon,7.drive,0.aria-label,0.role"> </div> <div jstcache="390" class="widget-pane-section-directions-trip-description"> <div
## jstcache="391"> <div class="widget-pane-section-directions-trip-numbers"> dget-pane-section-directions-trip clearfix selected<div jstcache="396" class="widget-pane-sect
##ion-directions-trip-duration delay-light" jsan="7.widget-pane-section-directions-trip-duration,7.delay-light"> <span jstcache="397">8 min</span> <span jstcache="398" sty
##le="display:none"> typically <span jstcache="399"></span> </span> </div> <div class="widget-pane-section-directions-trip-distance widget-pane-section-directions-



def search_in_str(data):
    #int inttxtz = 0
    searchstr1 = "widget-pane-section-directions-trip clearfix selected"
    secondsearchstr = "widget-pane-section-directions-trip-numbers"
    thirdsearchstr = "jstcache"
    ret = data.find(searchstr1);
    #print ('1st ret=', ret)
    if ret == -1:
        print('error')
        return
    #else the ret is the position of the str

    ret = data.find(secondsearchstr, ret)
    if ret == -1:
        print('error2')
        return
    #print ('2nd ret=' ,ret)
    #now get the jsccache value

    ret = data.find(thirdsearchstr, ret)
    if ret == -1:
        print('error3')
        return
    #get the value convert and form search str

    #jstcache="396"
    #print ('3rd ret=', ret)
    
    pos1 = ret + 10
    pos2 = pos1 + 3

    # this position is to get the 396 out
    txt = data[pos1:pos2]

    #print txt

    #generate the next search string

    inttxt = int(txt)

    #print inttxt

    finalsearchstr = inttxt + 1

    #print finalsearchstr

    ret = data.find(str(finalsearchstr),pos2)
    if ret == -1:
        print('error4')
        return

    #get the final value by manipulation
    #read upto min
    retx = data.find(">", ret)
    rety = data.find(" ", retx)
    retx = retx + 1
    txtz= data[retx:rety]

    #print txtz
    inttxtz = int(txtz)

    return inttxtz
    
    
    
    
    
    

def core_morn_func(url):
 ret = 0 
 for i in range(1):
    if i>0:
        time.sleep(1)

    #soup = BeautifulSoup(urllib2.urlopen(strhmhoodicrcl).read(),"html5lib")
    #txt = soup.script
    #print(txt.string)
    #txt = unicode(txt.string)
    #print txt.encode('utf-8')
    #pos = txt.index("10.0 km")
    #pos1 = pos + 100
    #outstr = txt[pos:pos1]
    #print(outstr)
    #m1pos = outstr.find('min')
    #m1pos = m1pos + 3
    #m2pos = outstr.find('min', m1pos)
    #print(m2pos)
    #aspos = outstr.find('"', (m2pos - 4))
    #print(aspos)
    #if ((int(m2pos) - int(aspos)) == 4):
    #  grepos = m2pos - 3
    #else:
    #  grepos = m2pos - 2   
    #print(grepos) 
    #min1 = outstr[(grepos):m2pos]  
    #intmin1 = int(min1)    
    #print(intmin1)
    #ret = subprocess.call(['./save_page_as','\"www.example.com\"', ' --browser', 'firefox', ' --destination', ' ./tmp'], shell=True)
    ret = subprocess.call(["./save_page_as",url, "--browser", "firefox","--destination", "./tmp2/a.html"])
    # read the file
    with open("./tmp2/a.html", "r") as myfile:
        data = myfile.read()
    #search in the string
        retmin = search_in_str(data)
       # print retmin
       # delete the files
    #subprocess.call(['rm -rf ./tmp2/*'],shell=True)
    # remove the files one by one
    #shutil.rmtree('./tmp2/
    for name in glob.glob('./tmp2/a*'):
        if os.path.isdir(name):
          shutil.rmtree(name, ignore_errors=True) 
        else:
           os.remove(name)

    time.sleep(5)
 
    return retmin



###calculate final minutes
##    ret = ((intmin1 + intmin2 + intmin3))
###    print ret
##    return ret




def funcmorn():
#    sys.stdout = log_file
    #if (ret == 0):
       #open file
    #   retstd, filename = logfilename()
    for i in range(12): # 60
         if i>0:
            time.sleep(480)#5 mins 
         acc = 0
         travelmins = core_morn_func(strhmhoodicrcl)
         acc = travelmins
         #print acc
         travelmins = core_morn_func(strhoodisapl)
         acc = acc + travelmins
         #print acc
         travelmins = core_morn_func(strsapltowns)
         acc = acc + travelmins
         #print acc
         today = datetime.date.today()
         print(acc,dt.now().hour,dt.now().minute)
         #remove the tmp files
         #subprocess.call(["pwd"])
         #subprocess.call(['mkdir tt'],shell=True)
         #subprocess.call(['rm -rf ./tmp2/*'],shell=True)
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
   hour = 0
   currfile = 0
 #  for i in range(1):
   while True:
        dayofwk = dt.today().weekday()
        monthofwk = dt.today().month
        date = dt.today().day
        txtfile = str(dayofwk) + str(monthofwk) + str(date) + ".log"
        #hour = dt.now().hour
        #funcmorn();
        if dt.now().hour in range(6,11): # 6 to 11
            if(False == os.path.isfile(txtfile)):
               if(currfile != 0):
                   currfile.close()
               old_stdout = sys.stdout
               log_file = open(txtfile,"w")
               sys.stdout = log_file #/*sujay*/
               currfile = log_file 
            funcmorn()
        #if dt.now().hour in range(6,7): # 16, 20
            # calc - func 
        #funceveng() 
              #if(True == os.path.isfile(txtfile)):
        #      sys.stdout = old_stdout 
        #      log_file.close()
        else:
            if(currfile != 0):
              currfile.close()
            time.sleep(900)

main()
