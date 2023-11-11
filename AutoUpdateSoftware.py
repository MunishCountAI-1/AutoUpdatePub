from ConnectDB import Db
import datetime
import time
import pytz 


class AutoUpdate:
    
    previousTime = -1
    previousMinute = -1
    LastRollName = -1
    lastUpdateRevalution = -1
    machineStatus = 1
    IST = pytz.timezone('Asia/Kolkata') 
    startTime = str(datetime.datetime.now(IST))

  
    def SensorUpdate(self):
        query = "select roll_id from roll_details where roll_sts_id = 1"
        DbClass = Db()
        
        self.LastRollName = DbClass.getLastRollId(query)
        while 1:
            current_time = datetime.datetime.now()
            if self.previousTime==-1:
                self.previousTime = current_time
                self.previousMinute = current_time.minute
            elif current_time.second - self.previousTime.second >=3 :
                sql = "INSERT INTO rotation_details (roll_id, rotation,timestamp) VALUES (%s, %s ,%s)"
                val = (self.LastRollName , "3000" ,  str(datetime.datetime.now(self.IST)) )
                self.previousTime = current_time
                DbClass = Db()
                DbClass.giveTheUpdateQueryWithVal(sql,val)
            if self.previousMinute+1 == current_time.minute:
                self.previousMinute = -1
                self.previousTime = -1
 
    def MachineStart(self):
       
                query = "update machine_details set machine_status = %s where machinedtl_id = 1"
                val = (str(self.machineStatus))
                Db().giveTheUpdateQueryWithVal(query,val)
        
    def DefectDetails(self):
        while 1:
            current_time = datetime.datetime.now()
            if self.previousTime==-1:
                self.previousTime = current_time
                self.previousMinute = current_time.minute
            elif current_time.second - self.previousTime.second >=3 :
                query = "insert into defect_details (defecttyp_id   , file_path    ,    filename    ,    roll_id    ,    score    ,    timestamp    ,    cam_id    ,       revolution    ,    coordinate    ) values( %s,%s,%s,%s,%s,%s,%s,%s,%s)"
                key = (1,'/home/kniti/projects/knit-i/knitting-core/images/543/2023-10-18/voltcam/cam1/15/2000/','KPR1_102_543_115_cam1_2023-10-18_15:46:47.559877+05:30_2000_image.jpg',750,0.5471679, str(datetime.datetime.now(self.IST)),7,115,'[508.5899658203125, 561.7112426757812, 1274.3033447265625, 665.8640747070312]')
                Db().giveTheUpdateQueryWithVal(query,key)
                self.previousTime = current_time
            if self.previousMinute+1 == current_time.minute:
                self.previousMinute = -1
                self.previousTime = -1
        
    def AlarmStatus(self): 
        while 1:
            current_time = datetime.datetime.now()
            if self.previousTime==-1:
                self.previousTime = current_time
                self.previousMinute = current_time.minute
            elif current_time.second - self.previousTime.second >=3 :
                query = "insert into alarm_status (alarm_name        ,alarmtyp_id    ,timestamp    ,roll_id    ,defect_id    ,alarm_status) values( %s,%s,%s,%s,%s,%s)"
                key = ('defect',1,  str(datetime.datetime.now(self.IST)) ,230,8048,2)
                Db().giveTheUpdateQueryWithVal(query,key)   
                self.previousTime = current_time
            if self.previousMinute+1 == current_time.minute:
                self.previousMinute = -1
                self.previousTime = -1
        
    def rollDetails(self):
        if self.lastUpdateRevalution==-1:
            self.lastUpdateRevalution = int(Db().LastRevalution())
        while 1:
            current_time = datetime.datetime.now()
            if self.previousTime==-1:
                self.previousTime = current_time
                self.previousMinute = current_time.minute
            elif current_time.second - self.previousTime.second >=3 :
                self.lastUpdateRevalution += 1
                if self.lastUpdateRevalution > 3150:
                    query = "update roll_details set roll_sts_id = 2 where roll_sts_id = 1"
                    Db().giveTheUpdateQuery(query)
                    query = "insert into roll_details (roll_name    ,roll_start_date    ,revolution    ,roll_sts_id    ,timestamp) values( %s,%s,%s,%s,%s)"
                    key = (542 , self.startTime , 0 , 1 , str(datetime.datetime.now(self.IST)))
                    Db().giveTheUpdateQueryWithVal(query,key) 
                    self.lastUpdateRevalution = 0
                Db().UpdateRollStsTo(self.lastUpdateRevalution)
                print(self.lastUpdateRevalution)  
                self.previousTime = current_time
            if self.previousMinute+1 == current_time.minute:
                self.previousMinute = -1
                self.previousTime = -1
            
sensorAutoUpdate = AutoUpdate()
# sensorAutoUpdate.SensorUpdate()
# sensorAutoUpdate.MachineStart()
# sensorAutoUpdate.DefectDetails()
# sensorAutoUpdate.AlarmStatus()
# sensorAutoUpdate.rollDetails()
            