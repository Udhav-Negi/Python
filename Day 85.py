import argparse

parser = argparse.ArgumentParser()

# Add command line arguments 
parser.add_argument("url", help="Url of the file to download")
parser.add_argument("output", help="by which name do you want to save your file")

# Parse the arguments 
args = parser.parse_args()

# Use the arguments in your code 
# print(args.arg1)
# print(args.arg2)
print(args.url)
print(args.output)