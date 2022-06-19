import multiprocessing
import time
import zipfile

import requests
import schedule

import program


def download_file(url: str):
    """This function downloads and extracts the update.zip file.

    Args:
        url (str): The url of the api.
    """
    response = requests.get(url + '/download')
    if response.status_code == 200:
        # download the file
        with open('update.zip', 'wb') as f:
            f.write(response.content)

        with zipfile.ZipFile('update.zip', 'r') as zip_ref:
            zip_ref.extractall()


def update_program(url: str, current_version: int, p: multiprocessing.Process):
    """This function checks if there is an update available, if there is, it downloads it and restarts the program.

    Args:
        url (str): The url of the api.
        current_version (int): The current version of the program.
        p (multiprocessing.Process): The process of the program.
    """
    print('Checking for updates...')
    response = requests.get(url + '/version')
    if response.status_code == 200:
        latest_version = response.json()['version']
        if latest_version != current_version:
            current_version = latest_version
            download_file(url)
            p.terminate()
            p.join()
            schedule.clear()
            print(schedule.jobs)
            main(current_version)


def main(current_version: int):
    """This function starts the program.

    Args:
        current_version (int): The current version of the program.
    """
    url = 'http://localhost:5000/api'
    p = multiprocessing.Process(target=program.main, args=(current_version,))
    schedule.every(10).seconds.do(update_program, url, current_version, p)
    print(schedule.jobs)

    p.start()


def schedule_check():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main(1)
    schedule_check()
