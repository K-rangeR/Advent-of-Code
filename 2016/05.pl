#!/usr/bin/env perl
use strict;
use warnings;
use Digest::MD5 qw(md5 md5_hex);

my $id = "cxdnnyjw";
my $i = 0;
my $count = 0;
my $pwd = "";

while ($count < 8) {
  my $digest = md5_hex($id . $i);
  if (substr($digest, 0, 5) eq "00000") {
    $pwd .= substr($digest, 5, 1);
    $count++;
  }
  $i++;
}

print "Password: $pwd\n";
