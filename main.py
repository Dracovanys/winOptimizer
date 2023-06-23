import os
from datetime import datetime
from windows_toasts import WindowsToaster, ToastText1

wintoaster = WindowsToaster('Windows Optimizer')
toast = ToastText1()

def log(target: str, message: str, notify: bool = False):
    if notify:
        toast.SetBody(message)
        wintoaster.show_toast(toast)
    log = f'[{datetime.today().day}/{datetime.today().month}/{datetime.today().year} {datetime.today().hour}:{datetime.today().minute}:{datetime.today().second}][{target}] {message}'
    print(log)
    with open('log.txt', 'a') as file:
        file.write(log + '\n')

def deleteFile(path: str):
    try:
        os.remove(path)
        log('MAIN', f'File deleted: {path}')
    except FileNotFoundError:
        deleteFolder(path)
    except PermissionError:
        log('MAIN', f'File skipped: {path}')

def deleteFolder(path: str):
    try:
        os.rmdir(path)
        print('MAIN', f'Folder deleted: {path}')
    except PermissionError:
        print('MAIN', f'Folder skipped: {path}')

windowsTemp_path = "C:\\Windows\\Temp"
appDataTemp_path = "C:\\Users\\mat_d\\AppData\\Local\\Temp"
prefetch_path = "C:\\Windows\\Prefetch"

# Notifying cleaning start
log('MAIN', 'Start cleaning!', notify=True)

# Cleaning Windows Temp folder
log('MAIN', 'Windows Temp folder cleaning started.')
for file in os.listdir(windowsTemp_path):
    deleteFile(windowsTemp_path + '\\' + file)
log('MAIN', 'Windows Temp folder cleaning finished.')

# Cleaning AppData Temp folder
log('MAIN', 'AppData Temp folder cleaning started.')
for file in os.listdir(appDataTemp_path):
    deleteFile(appDataTemp_path + '\\' + file)
log('MAIN', 'AppData Temp folder cleaning finished.')

# Cleaning Prefetch folder
log('MAIN', 'Prefetch folder cleaning started.')
for file in os.listdir(prefetch_path):
    deleteFile(prefetch_path + '\\' + file)
log('MAIN', 'Prefetch folder cleaning finished.')

# Notifying cleaning finish
log('MAIN', 'All cleaning finished!', notify=True)
