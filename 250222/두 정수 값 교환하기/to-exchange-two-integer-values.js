const fs = require("fs");
let [a, b] = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

function swap(a, b) {
    [a, b] = [b, a];
    return [a, b];
}

[a, b] = swap(a, b);
console.log(a, b);