const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(/\s+/).map(Number);
let sum = 0;

for (let elem of input)
    sum = sum + elem;

console.log(sum);