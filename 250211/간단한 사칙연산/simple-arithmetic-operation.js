const fs = require("fs");

const [a, b] = fs.readFileSync(0).toString().trim().split(/\s+/).map(Number);

console.log(a + b);
console.log(a - b);
console.log(parseInt(a / b));
console.log(a % b);