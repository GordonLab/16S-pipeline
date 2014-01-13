#!/usr/bin/python                                                                                                                                                                             
# Authors: Sathish Subramanian subramanians@wusm.wustl.edu;
                                                                                              
import sys,os
import warnings
import subprocess

username = str(os.getlogin())

# Location of reads from Illumina Run provided as first argument
readsfile = str(sys.argv[1]) 
print ("\nFiles located in folder "+readsfile+" have been specified to be processed\n")

"""                                                                                                                                                                                                                                       
Need to add code to verify reads 1, 2 and 3 are present and are the only files in the folder??                                                                                                                                             
Need to add usage to make that clear                                                                                                                                                                                                       
"""

# Creation of a tmp folder if one does not exist
if not os.path.exists("/home/comp/jglab/"+username+"/tmp"):
   os.makedirs("/home/comp/jglab/"+username+"/tmp")
   print ("No tmp folder detected under home directory, so created directory for future use /home/comp/jglab/"+username+"/tmp\n")

# Ungzip reads 1 and 2 plus index read into tmp folder
decompress = subprocess.call(("for f in "+readsfile+"*.gz; do if test \"${f#*R1_001.fastq.gz*}\" != \"$f\"; then READ1=$(basename \"${f}\" .gz); echo \"Decompressing Read 1: \"${READ1}\"\";  gunzip -c \"${f}\" > /home/comp/jglab/"+username+"/tmp/\"${READ1}\"; elif test \"${f#*R2_001.fastq.gz*}\" != \"$f\"; then INDEX=$(basename \"${f}\" .gz); echo \"Decompressing Index Read: \"${INDEX}\"\";  gunzip -c \"${f}\" > /home/comp/jglab/"+username+"/tmp/\"${INDEX}\"; elif test \"${f#*R3_001.fastq.gz*}\" != \"$f\"; then READ2=$(basename \"${f}\" .gz); echo \"Decompressing Read 2: \"${READ2}\"\n\";  gunzip -c \"${f}\" > /home/comp/jglab/"+username+"/tmp/\"${READ2}\"; fi; done"), shell="FALSE")

# Need to isolate variables READ1, READ2 and INDEX

print ("Fastq files are decompressed, now beginning to trim and overlap Reads 1 and 2\n") 
