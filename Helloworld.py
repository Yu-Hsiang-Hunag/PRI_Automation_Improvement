try:
    import argparse
except ImportError:
    print("Please install argparse")
try:
    import logging
except ImportError:
    print("Please install logging")
try:
    import xml.etree.ElementTree as ET # read xml
except ImportError:
    print("Please install xml.etree.ElementTree")
import os
import re
try:
    from unidiff import PatchSet # module for getting diff file information
except:
    print("Please install unidiff")
# win32com --> open excel
# try:
#     import win32com.client
# except ImportError:
#     logging.error("Please Install win32com")
#     raise ImportError

# custom libraries #
# from common import excel
from common import oempri
# from common import common

print("Import Success")
print("Hello World")

# Parser Function # This needed to modify based on the requirement
parser = argparse.ArgumentParser(description='pri_compare', formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-u', '--account', metavar="</str>", required=True)
parser.add_argument('-p', '--password', metavar="</str>", required=True)
parser.add_argument('-t', '--jira_ticket', metavar="</str>", required=True)

args = parser.parse_args()
print(args.account)
print(args.password)
print(args.jira_ticket)