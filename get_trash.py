import os
import time
import getpass
import os.path


def get_downloads_path():
    user_id = getpass.getuser()
    downloads_path = '/Users/' + user_id + '/Downloads'
    return downloads_path


def get_downloads():
    all_downloads = os.listdir(get_downloads_path())
    return all_downloads


def clean():
    print('The following files were modified more than 30 days ago and will be removed:')
    for file in get_downloads():
        modify_time = os.path.getmtime(os.path.join(get_downloads_path(),file))
        days_old = (time.time() - modify_time) / 86400
        if days_old > 30:
            print(file + ' - ' + str(days_old))


clean()
