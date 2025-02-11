const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\s+/);
console.log(input.reverse().join(""));
