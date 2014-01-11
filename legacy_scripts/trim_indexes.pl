#!/usr/bin/perl -w

my $primer_trimmed_file = shift;
my $index_file = shift;

die "Usage: trim_indexes.pl <primer_trimmed_file> <index_file>\n" unless $primer_trimmed_file && $index_file;

open (IN, $primer_trimmed_file) or die "can't open $primer_trimmed_file: $!\n";
open (INDEX, $index_file) or die "can't open $index_file: $!\n";

while (<IN>) {
	# read in one fastq read from the primer trimmed file
	my $header = $_;
        chomp $header;
        my $seq = <IN>;
        chomp $seq;
        my $plus = <IN>;
        chomp $plus;
        my $qual = <IN>;
        chomp $qual;

	# the reads should be sorted in the same order in both files, so we don't need to start at the top each time
	while (<INDEX>) {
		my $idx_header = $_;
        	chomp $idx_header;
        	my $idx_seq = <INDEX>;
        	chomp $idx_seq;
       		my $idx_plus = <INDEX>;
	        chomp $idx_plus;
	        my $idx_qual = <INDEX>;
	        chomp $idx_qual;
		

		if ($header eq $idx_header) {
		    print "$idx_header\n$idx_seq\n$idx_plus\n$idx_qual\n";
		    last;
		}
	}
}
close IN;
close INDEX;
