const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split(" ");
let [a, b] = input.map(Number)

console.log(a + b);
console.log(a - b);
console.log(parseInt(a / b));
console.log(a % b);