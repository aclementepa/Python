# port 445 used for network file share

import os
import sys
import re
import psutil

import numbers
import subprocess

try:
    from subprocess import DEVNULL
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')

def get_open_files(*pids):
    for pid in pids:
        if not isinstance(pid, numbers.Integral):
            raise ValueError('invalid PID')
    files = set()
    for pid in pids:
        try:
            out = subprocess.check_output(['lsof', '-wXFn', '+p', str(pid)],
                    stderr=DEVNULL)
        except:
            pass
        else:
            lines = out.strip().split('\n')
            for line in lines:
                # Skip sockets, pipes, etc.:
                if line.startswith('n') and line[1] == '/':
                    files.add(line[1:])
    return list(files)

def get_pids_open(*files):
    for f in files:
        if not isinstance(f, basestring):
            raise ValueError('invalid file name %s' % f)
    pids = set()
    try:
        out = subprocess.check_output(['lsof', '+wt']+list(files),
                stderr=DEVNULL)
    except Exception as e:
        out = str(e.output)
    if not out.strip():
        return []
    lines = out.strip().split('\n')
    for line in lines:
        pids.add(int(line))
    return list(pids)

output = open('output.txt', 'a')
output.write('\n')
fileList = []
shareList = open(sys.argv[1])
eachShare = shareList.readlines()
for shares in eachShare:
    path = shares.rstrip('\r\n')
    print('\nWalking directory ' + path + '\n')
    for root, subFolders, files in os.walk(path):
        #print 'Indexing ' + root + '\n'
        for file in files:
            fileList.append(os.path.join(root,file))
            # print('Found ' + root + file)
keywords = open(sys.argv[2])
searchTerm = keywords.readlines()
output.write('=== Directories or file names matching search criteria ===\n')
for term in searchTerm:
    strip = term.rstrip('\r\n')
    if any(strip in s for s in fileList):
        matching = [s for s in fileList if strip in s]
        for item in matching:
            output.write('\n' + item)
output.close()


# output.write('\n\n=== Files matching search criteria ===\n\n')
# for term in searchTerm:
#     strip = term.strip('\r\n')
#     for item in fileList:
#         print('Searching file ' + item + ' for term ' + term)
#         searchFile = open(item, 'rb')
#         for line in searchFile:
#             if re.search(strip, line, re.IGNORECASE):
#                 output.write('found ' + strip + ' in file ' + item + '\n')
#                 break
#         searchFile.close()

pidList = get_pids_open(fileList)
for pids in pidList:
    print(pids)
