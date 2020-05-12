#!/usr/bin/env perl
use strict;
use warnings;

open my $input, "<", "07_input.txt" or die "Can't open input file";

my $count = 0;
while (my $line = <$input>) {
  chomp $line;
  my @tokens = split /\[|\]/, $line;

  my @supernet = ();
  my @hypernet = ();
  for (my $i = 0; $i < @tokens; $i++) {
    my $token = $tokens[$i];
    for (my $j = 0; $j <= length($token)-3; $j++) {
      my ($a, $b, $c) = split(//, substr($token, $j, 3));
      if ($a ne $b and $a eq $c) {
        if ($i % 2 == 0) {
          @supernet = ($a, $b); 
        } else {
          @hypernet = ($a, $b);
        }
      }
    }
    if (@supernet and @hypernet) {
      if ($supernet[0] eq $hypernet[1] and $supernet[1] eq $hypernet[0]) {
        $count++;
        @supernet = ();
        @hypernet = ();
      }
    }
  }
}

print "Answer: $count\n";
close $input;
