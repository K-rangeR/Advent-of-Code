#!/usr/bin/env perl
use strict;
use warnings;

open my $input, "<", "07_input.txt" or die "Can't open input file";

my $count = 1;
while (my $line = <$input>) {
  chomp $line;
  my @tokens = split /\[|\]/, $line;
  my $in_hyper = 0;
  my $found = 0;
  for (my $i = 0; $i < @tokens; $i++) {
    if ($tokens[$i] =~ /(\w)(\w)\2\1/ and $i % 2 != 0) {
      $in_hyper = 1;
    } elsif ($tokens[$i] =~ /(\w)\1\1\1/) {
      print "double\n";
    } elsif ($tokens[$i] =~ /(\w)(\w)\2\1/ and $i % 2 == 0) {
      $found = 1;
    }
  }
  if ($found and not $in_hyper) {
    $count++;
  }
}

print "Answer: $count\n";
close $input;
