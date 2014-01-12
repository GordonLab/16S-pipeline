#!/usr/bin/python                                                                                                                                                                             
# Authors: Sathish Subramanian subramanians@wusm.wustl.edu
                                                                                              
import sys,os
import warnings

username = str(os.getlogin())

# Location of reads from Illumina Run provided as first argument
readsfile = str(sys.argv[1]) 
print ("\nFiles located in folder "+readsfile+" have been specified to be processed\n")

"""                                                                                                                                                                                                                                       
Need to add code to verify reads 1, 2 and 3 are present and are the only files in the folder??                                                                                                                                             Need to add usage to make that clear                                                                                                                                                                                                       """

# Creation of a tmp folder if one does not exist
if not os.path.exists("/home/comp/jglab/"+username+"/tmp"):
   os.makedirs("/home/comp/jglab/"+username+"/tmp")
   print ("No tmp folder detected under home directory, so created directory for future use /home/comp/jglab/"+username+"/tmp\n")

# Ungzip reads 1 through 3 into tmp folder
#os.system("for f in "+readsfile+"*.gz; do   STEM=$(basename \"${f}\" .gz);   gunzip -c \"${f}\" > /home/comp/jglab/sathish/tmp/\"${STEM}\"; done")

print ("Fastq files are unzipped, now beginning to trim and overlap R1 and R3") 
