const fs = require("fs");

let numbers = fs.readFileSync(0).toString().trim().split('\n');
for (let number of numbers)
    console.log(Number(number) + 2);

