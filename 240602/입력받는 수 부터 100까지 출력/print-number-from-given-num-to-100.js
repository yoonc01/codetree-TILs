const fs = require("fs");

let input = Number(fs.readFileSync(0).toString().trim());
let result = "";

for (let i = input; i < 101; i++)
    result = result + (i + " ");

console.log(result);