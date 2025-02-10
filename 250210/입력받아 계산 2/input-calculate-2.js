const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");
let inputIndex = 0;

const [a, b] = input[inputIndex++].split(" ").map(Number);
console.log(a * b);
