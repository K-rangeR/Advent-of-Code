#!/usr/bin/env perl
use strict;
use warnings;

open my $input, "<", "01_input.txt" or die "Can't open input file\n";

my $frequency = 0;
while (my $line = <$input>) {
  chomp $line;  
  $frequency += $line;
}

print "Answer: $frequency\n";
close $input;
