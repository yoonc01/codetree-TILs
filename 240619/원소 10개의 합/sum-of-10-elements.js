const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(/\s+/).map(Number);
let sum = 0;

input.forEach((val) => {
    sum = sum + val;
})

console.log(sum);