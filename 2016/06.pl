#!/usr/bin/env perl
use strict;
use warnings;

open my $input, "<", "06_input.txt" or die "Can't open input file";

my @char_count = ();
while (my $line = <$input>) {
  chomp $line;
  for (my $i = 0; $i < length($line); $i++) {
    my $char = substr $line, $i, 1;    
    $char_count[$i]{$char} += 1
  }
}

my $answer = "";
foreach my $hash (@char_count) {
  my %hash = %$hash;
  my $most_frequent = (sort {$hash{$a} <=> $hash{$b}} keys %hash)[0];
  $answer .= $most_frequent;
}

print "Answer: $answer\n";
close $input;
