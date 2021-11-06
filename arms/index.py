
import time
import requests
import platform
import json

#########################################################################################
# VARIABLES OF CONFIGURATION
# FUTURE .ENV
#########################################################################################
brain = 'http://localhost:5000'
interval_send_information = 2







#########################################################################################
# APPLICATION
#########################################################################################

def getOrderMonitoring():
    return requests.get(f"{brain}/order")

def sendKeepAlive():
    data_payload = {
        "name":platform.node(),
        "operational_system": platform.platform(),
        "operational_system_version": platform.version(),
        "operational_system_processor": platform.processor(),
        "general": platform.uname(),
    }
    return requests.post(url= f"{brain}/keep_alive", data=json.dumps(data_payload), headers={'content-type': 'application/json'})


while True:
    time.sleep(interval_send_information)

    try:
        order = getOrderMonitoring().json()
    except:
        print("Erro to get order")

    if order['keep_alive'] == True:
        sendKeepAlive()