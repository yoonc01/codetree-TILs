const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n");

function getNextLine(input) {
    let inputIdx = 0;
    return function() {
        return input[inputIdx].split(/\s+/);
    }
}

const nextLine = getNextLine(input);

const [n] = nextLine().map(Number);
const arr = nextLine().map(Number);

for (let i = 0; i < n; i++)
    arr[i] = Math.abs(arr[i]);

console.log(arr.join(" "));