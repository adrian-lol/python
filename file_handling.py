import os
import pathlib
import re
import sys
from pathlib import Path

#abc
#def

def make_new_path(file_list):

    dict_p = []
    p = ''

    #string1 = re.compile(r'Documents\\')
    #string2 = re.compile(r'\\')

    for f in file_list:

        if f.is_dir():

            reltv = f.relative_to('C:\\Users\\adriano_l\\Documents\\')
            new_path = pathlib.PureWindowsPath('C:\\Users\\adriano_l\\Documents\\2016\\').joinpath(reltv)
            dict_p.append(new_path)

    return dict_p


def make_dir(paths):

    """
    Create a dir and raise an exception if the dir already exists

    :param p: Full Path of the Dir to be created - path

    """

    for p in paths:

        p = Path(p)
        try:
            Path.mkdir(p)
        except OSError as err:
            print("OS error: {0}".format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise


def get_folders_and_files_from_path(p):

    """
    Returns a list with files inside a dir

    :param p: Full Path of the Dir - path
    :returns list: List of files inside the dir - list

    """

    dirs_list = []

    for child in p.iterdir():

        dirs_list.append(child)

        #dirs_list.append(str(child))

    return dirs_list


def file_write_dirs(fo, files_list, write_files=None, recursive=None):

    if write_files is None:
        write_files = False

    if recursive is None:
        recursive = False

    for f in files_list:
        # if not regexpIsFile.search(str(f)):
        try:

            if write_files is False:
                if f.is_dir():
                    fo.write(str(f) + '\r\n')
            else:
                fo.write(str(f) + '\r\n')

            # busca subdirs

            if recursive:

                if f.is_dir():
                    sub_dirs = get_folders_and_files_from_path(f)
                    file_write_dirs(fo, sub_dirs, write_files=write_files, recursive=recursive)

        except OSError as err:
            str_error = 'OS error: ' + str(err)
            print("OS error: {0}".format(err))
            log_error(str_log=str_error)


def log_error(file_path=None, str_log=None):

    if file_path is None:
        file_path = r'C:\Users\adriano_l\Documents\Python\scripts\testes\Dir\files_error_log.txt'

    if str_log is None:
        str_log = ''

    with open(file_path, mode='a', newline='',encoding='utf-8') as fo:

        fo.write(str_log + '\r\n')


fullPath = r'C:\Users\adriano_l\Documents\Python\python-3.5.1.exe'
p = Path(r'C:\Users\adriano_l\Documents')
pLog = Path(r'C:\Users\adriano_l\Documents\Python\scripts\testes\Dir\files_error_log.txt')

# remove tmp log
if pLog.exists():
    os.remove(str(pLog))

#print(pathlib.PureWindowsPath(fullPath).name)
#print(pathlib.PureWindowsPath(fullPath).stem)
#print(pathlib.PureWindowsPath(fullPath).suffix)
#print(pathlib.PureWindowsPath(fullPath).as_posix())

regexpIsFile = re.compile('\.')

fileout = r'C:\Users\adriano_l\Documents\Python\scripts\testes\Dir\files.txt'
error_log_out = r'C:\Users\adriano_l\Documents\Python\scripts\testes\Dir\files_error_log.txt'


with open(fileout, mode='w', encoding='utf-8', newline='') as fo:

    folders_and_files_list = get_folders_and_files_from_path(p)

    file_write_dirs(fo, folders_and_files_list, write_files=True, recursive=True)

#new_path_list = make_new_path(folders_and_files_list)

#make_dir(new_path_list)
