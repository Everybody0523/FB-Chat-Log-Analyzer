import argparse
import sys
import analyze


def getOptions():
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-l", "--logs", help="Directory in which chatlogs are stored")
    parser.add_argument("-o", "--output", help="Output file.")
    options = parser.parse_args()
    return options


if __name__ == "__main__":
  cl_options = getOptions()
  
  # Make sure chatlogs exist
  if (not options.logs):
    print("Must specify path to Facebook Chatlogs")
    sys.exit(1)
  
  path = options.logs
  # Verify that path is valid
  if (not os.path.isdir(path)):
    print("Invalid path to Facebook Chatlogs")
    sys.exit(1)
    
