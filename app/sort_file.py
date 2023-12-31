#!/usr/bin/python3
import pandas as pd
import sys

if len(sys.argv) < 4 :
    print("Usage : sort_file.py inputfname, outputfname sortby")
    sys.exit

infname=sys.argv[1]
outfname=sys.argv[2]
sortby=sys.argv[3]

df = pd.read_csv(infname)
df.sort_values(inplace=True, by=sortby)
df.to_csv(outfname, index=False)
