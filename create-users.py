#!/usr/bin/python3
# INET4031
# Tesfaldet Fesshiai
# 10/27/25
# 10/27/25

# the import modules are for system commands, regular expressions, and input handling
import os
import re
import sys


def main():
    for line in sys.stdin:
        # this skips lines that start with a #(comments in the input file)
        match = re.match("^#",line)
        #this splits each line into parts separated by colons
        fields = line.strip().split(':')

        # this skips lines tthat are comments or dont have 5 feilds
        if match or len(fields) != 5:
            continue

        # the purpose of the next three feilds is to pull out username, passoword, and full name info
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

       #it splits groups if there are multiple listed
        groups = fields[4].split(',')

        # this shows which user is being created
        print("==> Creating account for %s..." % (username))
        #this builds the command to create a new user with no password yet
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        print(cmd)
        os.system(cmd)

        #this shows that we are setting the password

        print("==> Setting the password for %s..." % (username))
       # this builds the command to set the password using the passwd command
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        print(cmd)
        os.system(cmd)

        for group in groups:
            # if the group is not '-', add the user to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
