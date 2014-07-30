#!/usr/bin/python
#-*- coding: utf-8 -*-
# author: nullne
# Email: co.nullne@gmail.com
# TODO:
#


import os
import requests
import tarfile
from datetime import datetime, date, timedelta
import sys
import subprocess
import logging

############# config field #############

# log filename to be analyse
EXTRACT_LOG_NAME = "ssl_access_log"
URL = 'http://10.66.128.186/tcms/httpd/'
# possible value could be: DAY, WEEK, MONTH
TYPE = 'DAY'


############# config field #############

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
PATH = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
def download_file(url):
    local_filename = os.path.join(PATH, 'runtime', url.split('/')[-1])
    #local_filename = './runtime/' + url.split('/')[-1]
    r = requests.get(url, stream=True)
    if r.status_code != 200:
        print 'status code: ', r.status_code
        print 'Please check out the configs. Bye'
        sys.exit(1)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
            f.flush()
    return local_filename

def specific_file(members):
    for tarinfo in members:
        if os.path.splitext(tarinfo.name)[0] == EXTRACT_LOG_NAME:
            yield tarinfo

def extract(filename, delete=False):
    tar = tarfile.open(filename)
    tar.extractall(members=specific_file(tar), path=os.path.join(PATH, 'runtime'))
    tar.close
    if delete:
        os.remove(filename)

def get_filename():
    """
    maybe you should modify this function with different filename
    """
    log_prefix = 'tcms.log_'
    today = date.today()
    log_date = '{:02d}'.format(today.month) + '{:02d}'.format(today.day)
    log_compress_format = 'tgz'
    log_filename = log_prefix + log_date + '-0001.' + log_compress_format
    return log_filename

def get_end_date():
    yesterday = date.today() - timedelta(days=1)
    if TYPE == 'DAY':
        return '{:02d}'.format(yesterday.day) + '/' + MONTHS[yesterday.month - 1] + '/' + str(yesterday.year)
    elif TYPE == 'WEEK':
        return '{:02d}'.format(yesterday.day) + '/' + MONTHS[yesterday.month - 1] + '/' + str(yesterday.year)
    elif TYPE == 'MONTH':
        today = date.today()
        last_month = date(day=1, month=today.month, year=today.year) - timedelta(days=1)
        return '{:02d}'.format(last_month.day) + '/' + MONTHS[last_month.month - 1] + '/' + str(last_month.year)
    else:
        pass

def get_start_date():
    if TYPE == 'DAY':
        yesterday = date.today() - timedelta(days=1)
        return '{:02d}'.format(yesterday.day) + '/' + MONTHS[yesterday.month - 1] + '/' + str(yesterday.year)
    elif TYPE == 'WEEK':
        lastweek = date.today() - timedelta(days=7)
        return '{:02d}'.format(lastweek.day) + '/' + MONTHS[lastweek.month - 1] + '/' + str(lastweek.year)
    elif TYPE == 'MONTH':
        today = date.today()
        last_month = date(day=1, month=today.month, year=today.year) - timedelta(days=1)
        ret = date(day=1, month=last_month.month, year=last_month.year)
        return '{:02d}'.format(ret.day) + '/' + MONTHS[ret.month - 1] + '/' + str(ret.year)
    else:
        pass

                    

def main():
    """
    only work fine with the follwing url, and can be modified to work with other url easily
    http://10.66.128.186/tcms/httpd/
    """

    if '-v' in sys.argv[1:] or '--verbose' in sys.argv[1:]:
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    else:
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)

  
    log_filename = get_filename()

    logging.info('Downloading file...')
    download_file(URL+log_filename)
    logging.info('extracting file...')
    extract(os.path.join(PATH, 'runtime', log_filename), True)

    start_date = get_start_date()
    end_date = get_end_date()

    logging.info('preprocessing the log file...')
    project_path = os.path.abspath(os.path.join(PATH, os.path.pardir))
    res = subprocess.check_output([os.path.join(project_path, 'logPreprocess', 'preprocess.py'), os.path.join(PATH, 'runtime', 'ssl_access_log'), '-c', os.path.join(project_path, 'logPreprocess', 'tcms.cfg')], )
    logging.info('generating and storing the results...')
    ret = subprocess.check_output([os.path.join(project_path, 'logAnalysis', 'tinylogan.py'), os.path.join(PATH, 'runtime', 'res_ssl_access_log'), '-a', '-S', '--start-date', start_date, '--end-date', end_date], )

    logging.info('Complete!')





if __name__ == '__main__':
    main()
