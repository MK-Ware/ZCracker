#ZIP password cracker written in python by MCoury AKA python-scripter
import zipfile as zf
import pickle
from itertools import permutations as prm
import os
import sys


class CrackZip:
    '''a CrackZip object
    Use: mission = ZCracker.CrackZip(path to the file you want to attack, *optional*path where you want the contents saved)
         mission.dict_attack()
    or:  mission.brute_attack()'''

    def __init__(self, file_path=None, target_path=None):
        self.file_path = file_path
        self.target_path = target_path
        self.space_selector = {1: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 2: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 3: 'abcdefghijklmnopqrstuvwxyz', 4: '0123456789', 5: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 6: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 7: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 8: 'abcdefghijklmnopqrstuvwxyz0123456789', 9: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 10: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 11: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 12: 'abcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 13: '0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 14: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', 15: 'abcdefghijklmnopqrstuvwxyz0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'}

    def dict_attack(self, dict_path=r'pass_dict.pickle'):
        '''Starts a dictionary attack on the target file
        takes one optional argument dict_path,
        which allows th user to look in a custom dictionary'''

        with open(dict_path, 'rb') as dict_f:
            content = pickle.load(dict_f)

        z = zf.ZipFile(r'' + self.file_path)

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
                    print('Password found:', pas)
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
                    print('Password found:', pas)
                    break

        if not found:
            print('Could not find the password...')

    def brute_attack(self, min_length=4, max_length=8, space_n=3):
        '''Starts a Brute-Force attack on the target file
        takes 3 optional arguments,
        min_length=4 the minimum length of the password,
        max_length=8 the maximum length of the password,
        and space_n=3 a number related to the characters of the password,
        call the selector() method for more details on space_n argument'''

        space = self.space_selector[space_n]
        p = ''
        for i in range(min_length, max_length + 1):
            p += space

        z = zf.ZipFile(r'' + self.file_path)

        found = []

        if self.target_path:
            print('Working...')
            for pas in prm(p):
                b = str.encode(pas)
                try:
                    z.extractall(path=self.target_path, pwd=b)
                except Exception:
                    pass
                else:
                    print('Password found:', pas)
                    break
        else:
            print('Working...')
            for pas in prm(p):
                b = str.encode(pas)
                try:
                    z.extractall(pwd=b)
                except Exception:
                    pass
                else:
                    print('Password found:', pas)
                    break

        if not found:
            print('Could not find the password...')

    def selector(self):
        '''Lets the user take a look at the characters
        used in brute-force attacks'''

        for key in self.space_selector:
            print(key,':',self.space_selector[key])



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

    print('The given dictionary has been saved as pickle successfully!')