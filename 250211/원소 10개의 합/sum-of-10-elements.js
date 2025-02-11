const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\s+/);
const numbers = input.map(Number);

const result = numbers.reduce((acc, cur) => {
    return acc + cur;
}, 0);
console.log(result);
