from apps_and_urls_tracker import focus_tracker
from dashboard import dashboard
from multiprocessing import Process

name = ""
username = ""

def start_both(name, username):
    dashboard_process = Process(target=dashboard, args=(name, username,))
    tracker_process = Process(target=focus_tracker)
    
    dashboard_process.start()
    tracker_process.start()
    dashboard_process.join()
    tracker_process.join()
    print('dashboard_processpid')
    print(dashboard_process.pid)
    with open('process_data.txt', 'w') as file:
        file.write(f"{dashboard_process.pid} \n {tracker_process.pid}")

def terminate_processes():
    global dashboard_process
    global tracker_process
    
    dashboard_process.terminate()
    tracker_process.terminate()
