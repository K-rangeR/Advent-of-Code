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

my @one; 
my @two;
my @three;

while (<$input>) {
  $_ =~ s/^\s+|\s+$//g;
  my @triangle = split " ", $_;
  push @one, $triangle[0];  
  push @two, $triangle[1];  
  push @three, $triangle[2];
}

my $count = 0;
for (my $i = 0; $i < $#one; $i+=3) {
  $count += (is_triangle($one[$i], $one[$i+1], $one[$i+2])) ? 1 : 0;  
}

for (my $i = 0; $i < $#two; $i+=3) {
  $count += (is_triangle($two[$i], $two[$i+1], $two[$i+2])) ? 1 : 0;  
}

for (my $i = 0; $i < $#three; $i+=3) {
  $count += (is_triangle($three[$i], $three[$i+1], $three[$i+2])) ? 1 : 0;  
}

print "Answer: $count\n";
close $input;
