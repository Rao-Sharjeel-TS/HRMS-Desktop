from win32gui import GetForegroundWindow
import psutil
import time
import win32process
from getRunningApps import get_active_window_title, get_running_processes
from takeScreenshot import take_screenshot
import json
# from get_browser_history import get_history_last_seconds
from datetime import datetime

LAST_APPS = []
CLOSED = []
TIME_INTERVAL = 10 #time interval in seconds after which screenshot and json will be created and API will be called.

def save_to_file(filename, json_data):
    with open(f"jsons/{filename}", 'w') as f:
        json.dump(json_data, f, indent=4)
    print(f"JSON saved {filename}")
    print(f"Saved at {json_data}")

def make_json(process_time, dns_list, websites):

    global LAST_APPS

    focused_apps_list = list(process_time.keys())
    focused_apps_list_renamed = [app.lower() for app in focused_apps_list]

    background_apps_list = get_running_processes()
    background_apps_list_renamed = [app.split(" ")[-1].lower() for app in background_apps_list]
    background_apps_list_renamed = background_apps_list_renamed

    unused_apps = [app for app in background_apps_list_renamed if app not in focused_apps_list_renamed]
    unused_apps_zeros = [0] * len(unused_apps)
    unused_apps_dict = dict(zip(unused_apps, unused_apps_zeros))
    
    focused_keys = list(process_time.keys())
    focused_times = list(process_time.values())

    data = {}
    # data["current_app"] = get_active_window_title()

    focused_keys += websites
    closed = list(set(LAST_APPS) - set(focused_keys))
    start = list(set(focused_keys) - set(LAST_APPS))
    focused_keys += LAST_APPS

    data_list = []
    for i in range(len(focused_keys)):
        data_list.append({'app_name': focused_keys[i]})

    data['focused_apps'] = data_list
    # data["background_apps"] = background_apps_list_renamed

    json_dict = {}
    json_dict["current_time"] = str(datetime.now())
    json_dict['data'] = data

    json_obj = json.dumps(json_dict, indent=4)
    print(json_obj)
    return json_obj
    LAST_APPS = focused_keys


def focus_tracker():
    
    process_time={}
    timestamp = {}
    websites = []
    
    user_id = "234"
    counter = 0
    iteration = 0

    while True:
        try:
            current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
        except:
            current_app = "undefined"
        
        tab, is_chrome = get_active_window_title()
        if is_chrome:
            websites.append(tab)
            
        timestamp[current_app] = int(time.time())
        time.sleep(1)
        
        if current_app not in process_time.keys():
            process_time[current_app] = 0
        process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
        counter += 1
        
        if counter == TIME_INTERVAL: # 5th second data as interval is set to 5

            json_obj = make_json(process_time, [], list(set(websites)))

            counter = 0
            iteration += 1
            process_time={}
            timestamp = {}
            websites = []

# focus_tracker()