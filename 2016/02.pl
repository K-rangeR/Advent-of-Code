#!/usr/bin/env perl
use strict;
use warnings;

open(my $input, '<', '02_input.txt') or die 'Cannot open input file';

my @pad = (
  [0, 0, 1, 0, 0],
  [0, 2, 3, 4, 0],
  [5, 6, 7, 8, 9],
  [0,10, 11,12,0],
  [0, 0, 13, 0, 0]
);

my %map = (10 => 'A', 11 => 'B', 12 => 'C', 13 => 'D');

my $row = 2;
my $column = 0;

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
      $row = ($row != 0 and $pad[$row-1][$column] != 0) ? $row-1 : $row;
    } elsif ($char eq "D") {
      $row = ($row != 4 and $pad[$row+1][$column] != 0) ? $row+1 : $row;
    } elsif ($char eq "R") {
      $column = ($column != 4 and $pad[$row][$column+1] != 0) ? $column+1 : $column;
    } elsif ($char eq "L") {
      $column = ($column != 0 and $pad[$row][$column-1] != 0) ? $column-1 : $column;
    }
  }

  my $result = 0;
  if ($pad[$row][$column] >= 1 and $pad[$row][$column] <= 9) {
    $result = $pad[$row][$column];
  } else {
    $result = $map{$pad[$row][$column]};
  }

  push @code, $result;
}

print(join("", @code));
