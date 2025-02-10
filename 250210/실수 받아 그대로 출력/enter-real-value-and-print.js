const fs = require("fs");
const numbers = fs.readFileSync(0).toString().trim().split("\n");

for (let number of numbers) {
    number = Number(number);
    console.log(number.toFixed(2));
}
