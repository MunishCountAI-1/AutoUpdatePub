from datetime import datetime 
import pytz 
  
IST = pytz.timezone('Asia/Kolkata') 
print("IST in Default Format : ",  
      datetime.now(IST)) 
