#!/usr/bin/env node
const fs = require("fs");
const readline = require("readline");

let set = new Set();
let answer = 0;

const reader = readline.createInterface({
  input: fs.createReadStream("./input_06.txt", "utf8"),
});

reader.on("line", (line) => {
  if (line.length === 0) {
    answer += set.size;
    set.clear();
  }

  line.split('').forEach((person) => set.add(person));
});

reader.on("close", () => {
  answer += set.size; // last group
  console.log(answer);
});
