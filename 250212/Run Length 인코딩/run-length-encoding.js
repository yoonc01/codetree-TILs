const fs = require("fs");

const string = fs.readFileSync(0).toString().trim();

let idx = 0;
const n = string.length;
let result = "";

while (idx < n) {
    let char = string[idx];
    let count = 0;
    while (idx < n && char == string[idx]) {
        idx++;
        count++;
    }
    result = result + char + count;
}

console.log(result.length);
console.log(result);
