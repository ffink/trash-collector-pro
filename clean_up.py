import os
import time
import getpass
import os.path
import shutil


def get_downloads_path():
    user_id = getpass.getuser()
    downloads_path = '/Users/' + user_id + '/Downloads'
    return downloads_path


def get_downloads():
    all_downloads = os.listdir(get_downloads_path())
    return all_downloads


def clean():
    print('The following downloads were last modified over 30 days ago and will be removed:')
    for file in get_downloads():
        modify_time = os.path.getmtime(os.path.join(get_downloads_path(),file))
        days_old = (time.time() - modify_time) / 86400
        if days_old > 30:
            print(file + ' | ' + str(round(days_old,1)) + ' days ago.')
    response = raw_input("Confirm delete? (y/n) ")
    if response == 'y' or response == 'yes':
        for file in get_downloads():
            if os.path.isfile(os.path.join(get_downloads_path(),file)) == True:
                modify_time = os.path.getmtime(os.path.join(get_downloads_path(),file))
                days_old = (time.time() - modify_time) / 86400
                if days_old > 30:
                    os.remove(os.path.join(get_downloads_path(),file))
            elif os.path.isfile(os.path.join(get_downloads_path(),file)) == False:
                modify_time = os.path.getmtime(os.path.join(get_downloads_path(),file))
                days_old = (time.time() - modify_time) / 86400
                if days_old > 30:
                    directory_response = raw_input('Warning: ' + file + ' is a directory. All contents will be deleted. Confirm? (y/n) ')
                    if directory_response == 'y' or directory_response == 'yes':
                        shutil.rmtree(os.path.join(get_downloads_path(),file))
                    elif directory_response == 'n' or directory_response == 'no':
                        print('Directory will not be removed.')
                    else:
                        print('Invalid entry. Directory will not be removed.')
    elif response == 'n' or response == 'no':
        print('Aborted.')
    else:
        print('Invalid response. Process aborted.')


clean()
