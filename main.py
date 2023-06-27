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
    with open(f'{os.path.dirname(os.path.realpath(__file__))}\\log.txt', 'a') as file:
        file.write(log.replace("\n", " ") + '\n')

def deleteFile(path: str):
    try:
        os.remove(path)
        log('MAIN', f'File deleted: {path}')
        return True
    except FileNotFoundError:
        return deleteFolder(path)
    except PermissionError:
        log('MAIN', f'File skipped: {path}')
        return False

def deleteFolder(path: str):
    try:
        os.rmdir(path)
        print('MAIN', f'Folder deleted: {path}')
        return True
    except PermissionError:
        print('MAIN', f'Folder skipped: {path}')
        return False

windowsTemp_path = "C:\\Windows\\Temp"
appDataTemp_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp"
prefetch_path = "C:\\Windows\\Prefetch"

# Start delete counter
delete_count = 0

# Cleaning Windows Temp folder
log('MAIN', 'Windows Temp folder cleaning started.')
for file in os.listdir(windowsTemp_path):
    if deleteFile(windowsTemp_path + '\\' + file):
        delete_count += 1
log('MAIN', 'Windows Temp folder cleaning finished.')

# Cleaning AppData Temp folder
log('MAIN', 'AppData Temp folder cleaning started.')
for file in os.listdir(appDataTemp_path):
    if deleteFile(appDataTemp_path + '\\' + file):
        delete_count += 1
log('MAIN', 'AppData Temp folder cleaning finished.')

# Cleaning Prefetch folder
log('MAIN', 'Prefetch folder cleaning started.')
for file in os.listdir(prefetch_path):
    if deleteFile(prefetch_path + '\\' + file):
        delete_count += 1
log('MAIN', 'Prefetch folder cleaning finished.')

# Notifying cleaning finish
log('MAIN', f'All cleaning finished!\nTemp files deleted: {delete_count}', notify=True)
