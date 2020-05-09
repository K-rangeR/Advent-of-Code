#!/usr/bin/env perl
use strict;
use warnings;

open my $input, "<", "04_input.txt" or die "Can't open input file";

my $sum = 0;
while (my $line = <$input>) {
  chomp $line;
  my ($name, $id, $checksum) = ($line =~ /([-\w]+)-(\d+)\[(\w+)\]/);

  my %count;
  foreach my $char (split //, $name) {
    if ($char ne "-") {
      $count{$char} += 1;
    }
  }

  my @keys = sort {$count{$b} <=> $count{$a} or $a cmp $b} keys(%count);
  my @top5 = @keys[0..4];
  my $top5 = join "", @top5;
  $sum += ($top5 eq $checksum) ? $id : 0;
}

print "Answer: $sum\n";
close $input;
