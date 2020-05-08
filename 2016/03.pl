#!/usr/bin/env perl
use strict;
use warnings;

sub is_triangle {
  my ($a, $b, $c) = @_;

  if (($a + $b) <= $c) {
    return 0;
  }

  if (($a + $c) <= $b) {
    return 0;
  }

  if (($b + $c) <= $a) {
    return 0;
  }

  return 1;
}

open my $input, "<", "03_input.txt" or die "Can't open input file";

my $count = 0;
while (<$input>) {
  $_ =~ s/^\s+|\s+$//g;
  my @triangle = split " ", $_;
  $count += (is_triangle(@triangle)) ? 1 : 0;
}

print "Answer: $count\n";
close $input;
