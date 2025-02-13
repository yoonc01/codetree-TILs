const fs = require("fs");

const input = fs.readFileSync(0, "utf-8").trim().split(/\s+/);

const [inputString, targetString] = input;

console.log(inputString.indexOf(targetString));