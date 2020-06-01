#!/usr/bin/env perl
use strict;
use warnings;

open(my $input_file, "<", "01_input.txt") or die "Can't open input file\n";

my %start = (x => 0, y => 0);
my %end = (x => 0, y => 0);
my $direction_facing = "N";

chomp(my $input = <$input_file>);
my @directions = split(/, /, $input);
foreach (@directions) {
	my ($direction, $distance) = $_ =~ /([RL]{1})(\d+)/;
	if ($direction_facing eq "N" and $direction eq "R") {
		$end{"x"} += $distance;	
		$direction_facing = "E";
	} elsif ($direction_facing eq "N" and $direction eq "L") {
		$end{"x"} -= $distance;	
		$direction_facing = "W";
	} elsif ($direction_facing eq "S" and $direction eq "R") {
		$end{"x"} -= $distance;	
		$direction_facing = "W";
	} elsif ($direction_facing eq "S" and $direction eq "L") {
		$end{"x"} += $distance;	
		$direction_facing = "E";
	} elsif ($direction_facing eq "E" and $direction eq "R") {
		$end{"y"} -= $distance;
		$direction_facing = "S";
	} elsif ($direction_facing eq "E" and $direction eq "L") {
		$end{"y"} += $distance;
		$direction_facing = "N";
	} elsif ($direction_facing eq "W" and $direction eq "R") {
		$end{"y"} += $distance;
		$direction_facing = "N";
	} elsif ($direction_facing eq "W" and $direction eq "L") {
		$end{"y"} -= $distance;
		$direction_facing = "S";
	}
}

my $answer = abs($start{"x"} - $end{"x"}) + abs($start{"y"} - $end{"y"});
print "Answer = $answer\n";

close $input_file;
