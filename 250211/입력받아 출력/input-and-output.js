const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");
const numbers = input.map(Number);
const [a, b] = numbers;
console.log(a, b);