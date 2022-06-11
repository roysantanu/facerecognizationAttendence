import csv
import geocoder
import datetime
import os
import pandas as pd
from datetime import datetime
import time

def attendenceEntry(Ename,filename='log.csv',timethresold=60):
    st=time.time()
    fields=['Name','Date','In','Out','Location','timestamp']
    date_time=datetime.now()
    date=str(date_time).split(' ')[0]
    Intime=str(date_time).split(' ')[1]
    location=geocoder.ip('me').latlng
    location=location[0],location[1]
    if os.path.isfile(filename):
        data=pd.read_csv(filename)
        df=pd.DataFrame(data)
        #select data from dataframe based on conditions
        mask=(df['timestamp']>=st-timethresold) & (df['Name']==Ename)
        df2=df.loc[mask]
        print ('df2: ',df2)
        mask2=(df['timestamp']<=st-timethresold) & (df['Name']==Ename) & (df['Date']==date)
        df3=df.loc[mask2]
        print ('df3: ',df3)
        nameC=df2['Name'].tolist()
        nameExist=df3['Name'].tolist()
        with open (filename,'a',newline='') as csvfile:
            csvwriter=csv.writer(csvfile)
            if len(nameC)>=1:
                print ('already signed in')
                pass
            elif len(nameC)==0:
                print ('need to check the signed in status..')
                if len(nameExist)>=1:
                    if str(df3.iloc[-1]['In'])==str(0):
                        fieldValues=[Ename,date,Intime,'0',location,st]
                        csvwriter.writerow(fieldValues)
                    elif str(df3.iloc[-1]['Out'])==str(0):
                        fieldValues=[Ename,date,'0',Intime,location,st]
                        csvwriter.writerow(fieldValues)
                elif len(nameExist)==0:
                    print ('new entry')
                    fieldValues=[Ename,date,Intime,'0',location,st]
                    csvwriter.writerow(fieldValues)
            csvfile.close
    else:
        with open (filename,'w',newline='') as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow(fields)
            fieldValues=[Ename,date,Intime,'0',location,st]
            csvwriter.writerow(fieldValues)
            csvfile.close


attendenceEntry(Ename='uday')
