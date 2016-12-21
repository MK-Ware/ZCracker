# ZCracker

=========A zip password cracker written in Python by python-scripter==========

Example:

import ZCracker as zc

mission = zc.CrackZip('d:\lockedzip.zip')

to start a dictionary attack:

mission.dict_attack()

to start a Brute-Force attack:

mission.brute_attack()

PS: currently, brute-force attacks do not look for white-spaces in the password string and you really shouldn't try a full scale brute-force attack unless you have a supercomputer cause it can take ages.
===============================================================

If you have a custom dictionary list file you want to use instead of the included dictionary (which is advisable, since the included dict  contains words only), you can convert it to  pickle using the  gen_dict() function.

Example:

from ZCracker import gen_dict

gen_dict('dictionary.txt', 'dictionary.pickle', separator='\n')

Note that if the passwords in your dictionary.txt file  are  by anything other  a new line (which is rare), you must pass the limiter as the separator argument.

For example, of  you have a blank line between every 2  passwords:
gen_dict('dictionary.txt', 'dictionary.pickle', separator='\n\n')
=============================================================

If you have any suggestions or  if you notice any bugs, please let me know!
