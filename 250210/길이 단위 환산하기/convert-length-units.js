const fs = require("fs")

const numbers = fs.readFileSync(0).toString().trim().split("\n");

for (let number of numbers) {
    console.log(`${(30.48 * number).toFixed(1)}`);
}