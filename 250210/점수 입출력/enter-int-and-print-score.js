const fs = require("fs")
const numbers = fs.readFileSync(0).toString().trim().split("\n");

for (let number of numbers)
    console.log(`Your score is ${number} point.`)
