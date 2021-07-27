from flask import Flask 
import logging 
from datetime import datetime


app=Flask(__name__)

@app.route('/api',methods = ['GET'])



def api():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S:%f")
    logging.info(current_time)
    
    return{
        
        'CurrentTime': current_time,
        'Sensor1':23,
        'Sensor2':253,
    }
