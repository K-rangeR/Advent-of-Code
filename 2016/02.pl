#!/usr/bin/env perl
use strict;
use warnings;

open(my $input, '<', '02_input.txt') or die 'Cannot open input file';

my @pad = ([1,2,3],[4,5,6],[7,8,9]);
my @num_at = (1,1); # 5
my @code = ();

my @instrs;
while (<$input>) {
  chomp;
  push @instrs, $_;
}

close $input;

for my $instr (@instrs) {
  for my $char (split //, $instr) {
    if ($char eq "U") {
      $num_at[0] = ($num_at[0] != 0) ? $num_at[0]-1 : 0
    } elsif ($char eq "D") {
      $num_at[0] = ($num_at[0] != 2) ? $num_at[0]+1 : 2
    } elsif ($char eq "R") {
      $num_at[1] = ($num_at[1] != 2) ? $num_at[1]+1 : 2
    } elsif ($char eq "L") {
      $num_at[1] = ($num_at[1] != 0) ? $num_at[1]-1 : 0
    }
  }
  push @code, $pad[$num_at[0]][$num_at[1]];
}

print(join("", @code));
