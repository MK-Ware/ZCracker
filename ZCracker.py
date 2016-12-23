#ZIP password cracker written in python by MCoury AKA python-scripter
import zipfile as zf
from unrar import rarfile as rf
import pickle
from itertools import product
import os
import sys


class CrackZip:
    '''a CrackZip object
    Use: mission = ZCracker.CrackZip(path to the file you want to attack,
    *optional*path where you want the contents saved)
         mission.dict_attack()
    or:  mission.brute_attack()'''

    def __init__(self, file_path=None, target_path=None):
        self.file_path = file_path
        self.target_path = target_path
        self.space_selector = {1: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 2: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 3: 'abcdefghijklmnopqrstuvwxyz', 4: '0123456789', 5: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 6: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 7: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 8: 'abcdefghijklmnopqrstuvwxyz0123456789', 9: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 10: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 11: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 12: 'abcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 13: '0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 14: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 15: 'abcdefghijklmnopqrstuvwxyz0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'}

    def dict_attack(self, dict_path=r'pass_dict.pickle', save=True):
        '''Starts a dictionary attack on the target file
        takes 2 optional arguments, dict_path,
        which allows th user to look in a custom dictionary,
        and save defaults to True and if set to False,
        the found password won't be saved as a txt file'''

        if not (save == True or save == False):
            raise ValueError ('save must be either True or False!')

        with open(r'' + dict_path, 'rb') as dict_f:
            content = pickle.load(dict_f)

        z = zf.ZipFile(self.file_path)

        found = []

        if self.target_path:
            print('Working...')
            for pas in content:
                b = str.encode(pas)
                try:
                    z.extractall(path=self.target_path, pwd=b)
                except Exception:
                    pass
                else:
                    found.append(pas)
                    break
        else:
            print('Working...')
            for pas in content:
                b = str.encode(pas)
                try:
                    z.extractall(pwd=b)
                except Exception:
                    pass
                else:
                    found.append(pas)
                    break

        if found:
            if save:
                with open(self.file_path + r'_pass.txt', 'w') as pfile:
                    pfile.write(pas)
            return found[0]

        if not found:
            return None

    def brute_attack(self, min_length=4, max_length=8, space_n=3, save=True):
        '''Starts a Brute-Force attack on the target file
        takes 3 optional arguments,
        min_length=4 the minimum length of the password,
        max_length=8 the maximum length of the password,
        space_n=3 a number related to the characters of the password,
        call the selector() method for more details on space_n argument,
        and save defaults to True and if set to False,
        the found password won't be saved as a txt file'''

        if not (save == True or save == False):
            raise ValueError ('save must be either True or False!')

        space = self.space_selector[space_n]

        z = zf.ZipFile(self.file_path)

        found = []

        if self.target_path:
            print('Working...')
            for length in range(min_length, max_length + 1):
                attempts = product(space, repeat=length)
                for pas in attempts:
                    pas = ''.join(pas)
                    b = str.encode(pas)
                    try:
                        z.extractall(path=self.target_path, pwd=b)
                    except Exception:
                        pass
                    else:
                        found.append(pas)
                        break
        else:
            print('Working...')
            for length in range(min_length, max_length + 1):
                attempts = product(space, repeat=length)
                for pas in attempts:
                    pas = ''.join(pas)
                    b = str.encode(pas)
                    try:
                        z.extractall(pwd=b)
                    except Exception:
                        pass
                    else:
                        found.append(pas)
                        break

        if found:
            if save:
                with open(self.file_path + r'_pass.txt', 'w') as pfile:
                    pfile.write(pas)
            return found[0]

        if not found:
            return None


class CrackRar:

    def __init__(self, file_path=None, target_path=None):
        self.file_path = file_path
        self.target_path = target_path
        self.space_selector = {1: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 2: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 3: 'abcdefghijklmnopqrstuvwxyz', 4: '0123456789', 5: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 6: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 7: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 8: 'abcdefghijklmnopqrstuvwxyz0123456789', 9: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 10: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 11: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 12: 'abcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 13: '0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 14: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 15: 'abcdefghijklmnopqrstuvwxyz0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'}

    def dict_attack(self, dict_path=r'pass_dict.pickle', save=True):
        '''Starts a dictionary attack on the target file
        takes 2 optional arguments, dict_path,
        which allows th user to look in a custom dictionary,
        and save defaults to True and if set to False,
        the found password won't be saved as a txt file'''

        if not (save == True or save == False):
            raise ValueError ('save must be either True or False!')

        with open(r'' + dict_path, 'rb') as dict_f:
            content = pickle.load(dict_f)

        r = rf.RarFile(self.file_path)

        found = []

        if self.target_path:
            print('Working...')
            for pas in content:
                try:
                    r.extractall(path=self.target_path, pwd=pas)
                except Exception:
                    pass
                else:
                    found.append(pas)
                    break
        else:
            print('Working...')
            for pas in content:
                try:
                    r.extractall(pwd=pas)
                except Exception:
                    pass
                else:
                    found.append(pas)
                    break

        if found:
            if save:
                with open(self.file_path + r'_pass.txt', 'w') as pfile:
                    pfile.write(pas)
            return found[0]

        if not found:
            return None

    def brute_attack(self, min_length=4, max_length=8, space_n=3, save=True):
        '''Starts a Brute-Force attack on the target file
        takes 3 optional arguments,
        min_length=4 the minimum length of the password,
        max_length=8 the maximum length of the password,
        space_n=3 a number related to the characters of the password,
        call the selector() method for more details on space_n argument,
        and save defaults to True and if set to False,
        the found password won't be saved as a txt file'''

        if not (save == True or save == False):
            raise ValueError ('save must be either True or False!')

        space = self.space_selector[space_n]

        r = rf.RarFile(self.file_path)

        found = []

        if self.target_path:
            print('Working...')
            for length in range(min_length, max_length + 1):
                attempts = product(space, repeat=length)
                for pas in attempts:
                    pas = ''.join(pas)
                    try:
                        r.extractall(path=self.target_path, pwd=pas)
                    except Exception:
                        pass
                    else:
                        found.append(pas)
                        break
        else:
            print('Working...')
            for length in range(min_length, max_length + 1):
                attempts = product(space, repeat=length)
                for pas in attempts:
                    pas = ''.join(pas)
                    try:
                        r.extractall(pwd=pas)
                    except Exception:
                        pass
                    else:
                        found.append(pas)
                        break

        if found:
            if save:
                with open(self.file_path + r'_pass.txt', 'w') as pfile:
                    pfile.write(pas)
            return found[0]

        if not found:
            return None

def selector(self):
    '''Lets the user take a look at the characters
    used in brute-force attacks'''

    return self.space_selector

def gen_dict(txt_path=None, target_name='pass_dict2.pickle', separator='\n'):
    '''For performance related reasons, this module requires the dictionary list
    to be saved in a pickle file. Use this function to convert a .txt password
    dictionary to pickle'''

    if os.path.exists(r'' + target_name):
        sys.exit('Target file already exists! Rename or move it to avoid losing your data...')

    with open(r'' + txt_path) as src:
        pwds = src.readlines()

    for i in range(len(pwds)):
        pwds[i] = pwds[i].strip(separator)

    with open(r'' + target_name, 'wb') as tgt:
        pickle.dump(pwds, tgt)

    return 'The given dictionary has been saved as pickle successfully!'