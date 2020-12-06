#!/usr/bin/env node
const fs = require("fs");
const readline = require("readline");

let map = new Map();
let answer = 0;
let people = 0;

const reader = readline.createInterface({
  input: fs.createReadStream("./input_06.txt", "utf8"),
});

reader.on("line", (line) => {
  if (line.length === 0) {
    answer += getCount(map);
    map.clear();
    people = 0;
    return;
  }

  people++;

  line.split('').forEach((q) => {
    let cnt = map.get(q) || 0;
    map.set(q, cnt+1);
  });
});

reader.on("close", () => {
  answer += getCount(map);
  console.log(answer);
});

function getCount(map) {
    let cnt = 0;
    for ([key, value] of map) {
      if (value === people) {
        cnt++;
      }
    }
    return cnt;
}
