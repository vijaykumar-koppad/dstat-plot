#!/usr/bin/python

import os
import sys
import csv
import argparse
from dstatplotlib import *
sys.path.append(os.getcwd())


def segregate(entry, parsed_list, dstat_dict):
    '''
    Parsing the csv file.
    '''
    if entry == "system" or entry == "epoch":

        if parsed_list[0][0] == "time" or parsed_list[0][0] == "epoch":
            '''
            poping the first element of the first row
            which will be monitor paramete, here it is time
            '''
            mptime = parsed_list[0].pop(0)
            dstat_dict['time'] = []

            for row in parsed_list[1:]:
                dstat_dict['time'].append(row.pop(0))
        else:
            dstat_dict[entry] = {}
            # system intrupts
            mpint = parsed_list[0].pop(0)
            # system context switches
            mpcsw = parsed_list[0].pop(0)
            dstat_dict[entry][mpint] = []
            dstat_dict[entry][mpcsw] = []

            for row in parsed_list[1:]:
                dstat_dict[entry][mpint].append(row.pop(0))
                dstat_dict[entry][mpcsw].append(row.pop(0))

    elif "cpu" in entry:

        if entry == "cpu usage":
            '''
            support for --cpu24
            '''
            dstat_dict[entry] = {}
            # Fieds for cpu usage "usr","sys","idl"
            fields = parsed_list[0][:3]

            for i in range(3):
                para = parsed_list[0].pop(0)
                dstat_dict[entry][para] = []

            for row in parsed_list[1:]:
                for para in fields:
                    dstat_dict[entry][para].append(row.pop(0))
        else:
            dstat_dict[entry] = {}
            '''
            Fieds for cpu usage "usr","sys","idl","wai","hiq","siq"
            '''
            fields = parsed_list[0][:6]

            for i in range(6):
                para = parsed_list[0].pop(0)
                dstat_dict[entry][para] = []

            for row in parsed_list[1:]:
                for para in fields:
                    dstat_dict[entry][para].append(row.pop(0))

    elif "dsk" in entry:
        dstat_dict[entry] = {}
        # Fieds for dsk io  "read","write"
        fields = parsed_list[0][:2]

        for i in range(2):
            para = parsed_list[0].pop(0)
            dstat_dict[entry][para] = []

        for row in parsed_list[1:]:
            for para in fields:
                dstat_dict[entry][para].append(row.pop(0))

    elif "net" in entry:
        dstat_dict[entry] = {}
        # Fieds for network io "recv","send"
        fields = parsed_list[0][:2]

        for i in range(2):
            para = parsed_list[0].pop(0)
            dstat_dict[entry][para] = []

        for row in parsed_list[1:]:
            for para in fields:
                dstat_dict[entry][para].append(row.pop(0))

    elif entry == "paging":
        '''
        Fieds for page stat  "page in","page out"
        '''
        dstat_dict[entry] = {}
        fields = parsed_list[0][:2]

        for i in range(2):
            para = parsed_list[0].pop(0)
            dstat_dict[entry][para] = []

        for row in parsed_list[1:]:
            for para in fields:
                dstat_dict[entry][para].append(row.pop(0))

    elif entry == "load avg":
        dstat_dict[entry] = {}
        # Fieds for load average  "1m","5m","15m"
        fields = parsed_list[0][:3]

        for i in range(3):
            para = parsed_list[0].pop(0)
            dstat_dict[entry][para] = []

        for row in parsed_list[1:]:
            for para in fields:
                dstat_dict[entry][para].append(row.pop(0))

    elif entry == "memory usage":
        dstat_dict[entry] = {}
        # Fieds for memory usage "used","buff","cach","free"
        fields = parsed_list[0][:4]

        for i in range(4):
            para = parsed_list[0].pop(0)
            dstat_dict[entry][para] = []

        for row in parsed_list[1:]:
            for para in fields:
                dstat_dict[entry][para].append(row.pop(0))

    elif "io" in entry:
        dstat_dict[entry] = {}
        # Fieds for io requests  "read" and "write" requests
        fields = parsed_list[0][:2]

        for i in range(2):
            para = parsed_list[0].pop(0)
            dstat_dict[entry][para] = []

        for row in parsed_list[1:]:
            for para in fields:
                dstat_dict[entry][para].append(row.pop(0))

    elif entry == "procs":
        dstat_dict[entry] = {}
        # Fieds for process stats "run" "blk" and "new"
        fields = parsed_list[0][:3]

        for i in range(3):
            para = parsed_list[0].pop(0)
            dstat_dict[entry][para] = []

        for row in parsed_list[1:]:
            for para in fields:
                dstat_dict[entry][para].append(row.pop(0))

    elif "ipc" in entry:
        '''
        Fieds for ipc stats message queue, semaphores,
        and  shared memory
        '''
        dstat_dict[entry] = {}
        fields = parsed_list[0][:3]

        for i in range(3):
            para = parsed_list[0].pop(0)
            dstat_dict[entry][para] = []

        for row in parsed_list[1:]:
            for para in fields:
                dstat_dict[entry][para].append(row.pop(0))

    elif entry == "virtual memory":
        '''
        Fieds for vm stats "hard pagefaults, soft pagefaults,
        allocated, free"
        '''
        dstat_dict[entry] = {}
        fields = parsed_list[0][:4]

        for i in range(4):
            para = parsed_list[0].pop(0)
            dstat_dict[entry][para] = []

        for row in parsed_list[1:]:
            for para in fields:
                dstat_dict[entry][para].append(row.pop(0))

    elif entry == "file locks":
        '''
        Fieds for file lock stats (posix, flock, read, write)
        '''
        dstat_dict[entry] = {}
        fields = parsed_list[0][:4]

        for i in range(4):
            para = parsed_list[0].pop(0)
            dstat_dict[entry][para] = []

        for row in parsed_list[1:]:
            for para in fields:
                dstat_dict[entry][para].append(row.pop(0))

    elif entry == "tcp sockets":
        '''
        Fieds for tcp sockets (listen, established, syn,
        time_wait, close)
        '''
        dstat_dict[entry] = {}
        fields = parsed_list[0][:5]

        for i in range(5):
            para = parsed_list[0].pop(0)
            dstat_dict[entry][para] = []

        for row in parsed_list[1:]:
            for para in fields:
                dstat_dict[entry][para].append(row.pop(0))

    elif entry == "udp":
        '''
        Fieds for udp stats  (listen, active)
        '''
        dstat_dict[entry] = {}
        fields = parsed_list[0][:2]

        for i in range(2):
            para = parsed_list[0].pop(0)
            dstat_dict[entry][para] = []

        for row in parsed_list[1:]:
            for para in fields:
                dstat_dict[entry][para].append(row.pop(0))

    elif entry == "filesystem":
        '''
        Fieds for filesystem stats (open files, inodes)
        '''
        dstat_dict[entry] = {}
        fields = parsed_list[0][:2]

        for i in range(2):
            para = parsed_list[0].pop(0)
            dstat_dict[entry][para] = []

        for row in parsed_list[1:]:
            for para in fields:
                dstat_dict[entry][para].append(row.pop(0))

    return dstat_dict


def generate_dstat_dict(csvfile):
    '''
    This function generate a dictinary having all the values with
    respective keys, which can be used to plot or any other purposes.
    '''
    dstat_dict = {}  # Initialising dictionary for all the parameter

    paramtrs = ["system", "total cpu usage", "dsk/total", "net/total",
                "paging", "load avg", "memory usage", "io/total", "procs",
                "ipc", "virtual memory", "file locks", "tcp sockets", "udp",
                "filesystem"]
    parsed_list = []
    csvreader = csv.reader(file(csvfile))
    for row in csvreader:
        parsed_list.append(row)

    dstat_dict['host'] = parsed_list[2][1]
    dstat_cmd = parsed_list[3][1]
    head_list = parsed_list[5]
    parsed_list = parsed_list[6:]
    for entry in head_list:
        if entry in paramtrs or "cpu" in entry or "dsk" in entry \
            or "net" in entry:
            dstat_dict = segregate(entry, parsed_list, dstat_dict)
        elif entry != '':
            print "ha ha :D"
            print "%s is not supported " % entry

    return dstat_dict


def main():

    parser = argparse.ArgumentParser(formatter_class=argparse.
                                     ArgumentDefaultsHelpFormatter)
    parser.add_argument("csvfile", help="csvfile output from dstat")
    
    args = parser.parse_args()
    dstat_dict = generate_dstat_dict(args.csvfile)
    
    plot_cpu_usr_sys(dstat_dict)


if __name__ == '__main__':
    main()
