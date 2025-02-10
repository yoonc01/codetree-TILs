const fs = require("fs");
input = fs.readFileSync(0).toString().trim().split("\n");
numbers = input.map(Number);

const [a, b] = numbers;
console.log(a * b);