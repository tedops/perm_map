import os, sys

class bcolors:
    FAIL = '\033[91m'
    ENDC = '\033[0m'

curdir = os.getcwd()

def generate_perm_map(rootDir):
    os.chdir(rootDir)
    perm_map = {}
    for dirName, subdirList, fileList in os.walk("."):
        for fname in fileList:
            f = '{0}/{1}'.format(dirName,fname)
            if ".git" in f:
                break
            perm = oct(os.stat(f).st_mode & 0777)
            perm_map[f] = perm
    os.chdir(curdir)
    return perm_map

try:

    jgit_checkout = generate_perm_map(sys.argv[1])
    # print jgit_checkout
    git_clone = generate_perm_map(sys.argv[2])
    # print git_clone

    myset = set(jgit_checkout) & set(git_clone)

    for i in myset:
        if jgit_checkout[i] != git_clone[i]:
            print ("{0}\t{1}{2}{3}\t{4}".format(jgit_checkout[i], bcolors.FAIL, git_clone[i], bcolors.ENDC, i))

except IndexError:
    print ("ERROR: Index out of range.")
    pass
