const fs = require("fs");
const inputs = fs.readFileSync(0).toString().trim().split("\n");

for (let line of inputs) {
    const [a, b] = line.split(" ").map(Number);
    console.log(a * b);    
}