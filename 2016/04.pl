#!/usr/bin/env perl
use strict;
use warnings;

sub decrypt {
  my ($cipher, $id) = @_;
  my %alphabet = (
    0 => 0, 'a' => 1, 'b' => 2, 'c' => 3, 'd' => 4, 'e' => 5, 'f' => 6, 'g' => 7,
    'h' => 8, 'i' => 9, 'j' => 10, 'k' => 11, 'l' => 12, 'm' => 13, 'n' => 14,
    'o' => 15, 'p' => 16, 'q' => 17, 'r' => 18, 's' => 19, 't' => 20, 'u' => 21,
    'v' => 22, 'w'=>23, 'x' => 24, 'y' => 25, 'z' => 26
  );
  my @letters = sort(keys(%alphabet));

  my $result = "";
  foreach my $letter (split //, $cipher) {
    if ($letter ne "-") {
      my $idx = ($alphabet{$letter} + $id) % 26;
      $result .= $letters[$idx];
    } else {
      $result .= " ";
    }
  }

  return $result;
}

open my $input, "<", "04_input.txt" or die "Can't open input file";

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
  if ($top5 eq $checksum) {
    my $room = decrypt($name, $id);    
    print "$room: $id\n";
  }
}

close $input;
