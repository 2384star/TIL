import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l","--left",type=int)
args=parser.parse_args()
    
print(args)