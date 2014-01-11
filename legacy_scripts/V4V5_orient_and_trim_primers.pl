#!/usr/bin/perl -w

use strict;

my $in=shift;

die "Usage: V4V5_orient_and_trim_primers.pl <infile>\n" unless $in;

open (IN, $in) or die "can' t open $in: $!\n";

my $primer515   = "GTGCCAGCAGCCGCGGTAA";
my $primer515rc = "TTACCGCGGCTGCTGGCAC";


my $primer806   = "GGACTACCAGGGTATCTAAT";
my $primer806rc = "ATTAGATACCCTGGTAGTCC";


my $missed_primer = 0;
my $primer_ok = 0;

open (MISSED, ">missed.txt") or die "can't open missed.txt";

while (<IN>) {
	my $header = $_;	
	chomp $header;
	my $seq = <IN>;
	chomp $seq;

	my $seqLen = length($seq);
	my $plus = <IN>;
	chomp $plus;
	my $qual = <IN>;
	chomp $qual;
#	print "$seqLen\n";
#	next;

	my $tempSeq = $seq;

	my $have_both_primers = 0;

	# id and remove primer1
	if ($seq =~ s/^[ACGT]{0,7}$primer515//) {
		my $len_removed = $seqLen - length($seq);
		$qual = substr($qual, $len_removed);

#		print "removed $len_removed ($primer515)\n";
#		print "$tempSeq\n$seq\n\n";
#		my $tempQual = $qual;

#		print "$tempQual\n$qual\n\n";
#		my $temp2Seq = $seq;
#		my $temp2Qual = $qual;

		my $seqLen2 = length($seq);

		if ($seq =~ s/$primer806rc[ACGT]{0,7}$//) {
#			my $len_removed = $seqLen2 - length($seq);
			$qual = substr($qual, 0, length($seq));
	
#			print "removed $len_removed ($primer806rc)\n";
		#	print "$temp2Seq\n$seq\n\n";
		#	print "$temp2Qual\n$qual\n\n";

			# now have all of the pieces and they are in the correct orientation
			print "$header\n$seq\n$plus\n$qual\n";
			$have_both_primers = 1;
		}
	}
	elsif ($seq =~ s/^[ACGT]{0,7}$primer806//) {
		my $len_removed = $seqLen - length($seq);
		$qual = substr($qual, $len_removed);
		#print "removed $len_removed ($primer806)\n";
		#print "$tempSeq\n$seq\n\n";
		#my $tempQual = $qual;
#		my $temp2Seq = $seq;
#		my $temp2Qual = $qual;
		my $seqLen2 = length($seq);

		#print "$tempQual\n$qual\n\n";
		if ($seq =~ s/$primer515rc[ACGT]{0,3}$//) {
			my $len_removed = $seqLen2 - length($seq);
			$qual = substr($qual, 0, length($seq));
	#		print "removed $len_removed ($primer515rc)\n";
#			print "$temp2Seq\n$seq\n\n";
#			print "$temp2Qual\n$qual\n\n";

			# now have all of the pieces and they are in the correct orientation
			$seq = reverse_complement_IUPAC($seq);
			$qual = reverse($qual);

			print "$header\n$seq\n$plus\n$qual\n";
			$have_both_primers = 1;
#			die;
		}
	}
	if ($have_both_primers) {
		$primer_ok++;
	}
	else {
		print MISSED "MISSED: $tempSeq\n";
		$missed_primer++;
	}

#	print "$seq$qual\n";
}
close IN;


my $total_seqs = $primer_ok + $missed_primer;
printf STDERR "*****  SUMMARY  *****\nprimers detected %d (%.1f%%)\tno primer (discarded) %d (%.1f%%)\n", $primer_ok, $primer_ok/$total_seqs*100, $missed_primer, $missed_primer/$total_seqs*100;




sub reverse_complement_IUPAC {
        my $dna = shift;

	# reverse the DNA sequence
        my $revcomp = reverse($dna);

	# complement the reversed DNA sequence
        $revcomp =~ tr/ABCDGHMNRSTUVWXYabcdghmnrstuvwxy/TVGHCDKNYSAABWXRtvghcdknysaabwxr/;
        return $revcomp;
}

