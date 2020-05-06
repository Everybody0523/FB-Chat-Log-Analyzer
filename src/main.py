import argparse
import sys
import analyze
import json
from os import listdir
from os.path import isfile, join, isdir


def getOptions():
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-l", "--logs", help="Directory in which chatlogs are stored")
    parser.add_argument("-o", "--output", help="Output file.")
    options = parser.parse_args()
    return options


def findJsonFiles(path):
    onlyjson = [join(path, f) for f in listdir(path) if (isfile(join(path, f)) and (".json" in f))]
    json_dicts = []
    for js in onlyjson:
        f = open(js, 'r')
        jsonDicts.append(json.laod(f))
        f.close()
    return json_dicts


def printUsage():
    print("")
    print("Usage:")
    print("  python3 main.py --logs <path/to/dir/with/chatlogs --output <path/to/output/file>")


if __name__ == "__main__":
    cl_options = getOptions()

    # Make sure chatlogs exist
    if (not cl_options.logs):
        print("Must specify path to Facebook Chatlogs")
        printUsage()
        sys.exit(1)

    path = cl_options.logs
    # Verify that path is valid
    if (not isdir(path)):
        print("Invalid path to Facebook Chatlogs")
        printUsage()
        sys.exit(1)
