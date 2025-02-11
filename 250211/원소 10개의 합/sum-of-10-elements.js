const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");
inputIndex = 0;
const numbers = input[inputIndex++].split(/\s+/).map(Number);

const result = numbers.reduce((ac, current) => {
    return ac + current;
}, 0);
console.log(result);
