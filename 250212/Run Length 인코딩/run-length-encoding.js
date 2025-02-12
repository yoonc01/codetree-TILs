const fs = require("fs");

const string = fs.readFileSync(0, "utf-8").trim();

let idx = 0;
const n = string.length;
const result = [];

while (idx < n) {
    const char = string[idx];
    let count = 0;

    while (idx < n && string[idx] === char) {
        idx++;
        count++;
    }

    result.push(char, count);
}

const compressedString = result.join("");
console.log(compressedString.length);
console.log(compressedString);
