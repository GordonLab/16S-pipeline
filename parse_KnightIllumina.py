#!/usr/bin/python                                                                                                                                                                             
# Authors: Sathish Subramanian subramanians@wusm.wustl.edu; Joseph Planer
                                                                                              
import sys,os
import warnings

readfile = open(sys.argv[1],"r")
barcodefile = open(sys.argv[2],"r")


if not os.path.exists("interm"):
    os.makedirs("interm")

a = ("sed '2~4 s/.$//' "+str(sys.argv[2])+" > interm/trimmed_barcodes.txt")

b = ("grep \"^@HWI\" "+ str(sys.argv[1])+" | sed 's/^.//' > interm/header_reads.txt")

c = ("grep \"^@HWI\" "+ str(sys.argv[2])+" | sed 's/^.//' > interm/header_barcodes.txt")

print ("\nFound intersection of headers between barcode file merged file\n")

d = ("sort -u interm/header_reads.txt > interm/sorted_headers.txt")
e = ("sort -u interm/header_barcodes.txt > interm/sorted_barcodes.txt")

print ("Sorted headers\n")

f = ("comm -12 interm/sorted_headers.txt interm/sorted_barcodes.txt > interm/common_headers.txt")

g = ("filter_fasta.py -f "+sys.argv[1]+" -s interm/common_headers.txt -o interm/filt_reads.fastq")
h = ("filter_fasta.py -f "+sys.argv[2]+" -s interm/common_headers.txt -o interm/filt_barcodes.fastq")

print ("Filtered out reads from barcode and overlapped fragments\n")

i = (" cat interm/filt_reads.fastq | paste - - - - | sort -k1,1 -t \" \" | tr \"\\t\" "" \"\\n\" > "+(sys.argv[1]).split(".fastq")[0]+"_processed.fastq")
j = (" cat interm/filt_barcodes.fastq | paste - - - - | sort -k1,1 -t \" \" | tr \"\\t\" "" \"\\n\" > "+(sys.argv[2]).split(".fastq")[0]+"_processed.fastq")


os.system(a)
os.system(b)
os.system(c)
os.system(d)
os.system(e)
os.system(f)
os.system(g)
os.system(h)
os.system(i)
os.system(j)


