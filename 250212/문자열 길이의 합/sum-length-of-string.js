const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");
let inputIndex = 0;

const n = parseInt(input[inputIndex++]);
let totalLen = 0;
let startsWithA = 0;

for (let i = 0; i < n; i++) {
    let str = input[inputIndex++];
    if (str[0] == 'a')
        startsWithA++;
    totalLen = totalLen + str.length;
}

console.log(totalLen, startsWithA);