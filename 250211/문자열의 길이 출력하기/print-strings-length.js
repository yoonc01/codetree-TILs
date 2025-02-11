const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");
const ans = input.reduce((acc, cur) => {
    return acc + cur.length;
    }, 0);
console.log(ans);