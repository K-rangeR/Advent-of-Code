#!/usr/bin/env perl
use strict;
use warnings;
use Digest::MD5 qw(md5 md5_hex);

my $id = "cxdnnyjw";
my $i = 0;
my $count = 0;
my @pwd = ("", "", "", "", "", "", "", "");
my @invalid = ("8", "9", "a", "b", "c", "d", "e", "f");

while ($count < 8) {
  my $digest = md5_hex($id . $i);
  if (substr($digest, 0, 5) eq "00000") {
    my $pos = substr($digest, 5, 1);
    my $char = substr($digest, 6, 1);
    if (grep(/^$pos$/, @invalid)) {
      $i++;
      next;
    }
    if ($pwd[$pos] eq "") {
      $pwd[$pos] = $char;
      $count++;
    }
  }
  $i++;
}

my $answer = join "", @pwd;
print "Password: $answer\n";
