const fs = require("fs");

const n = Number(fs.readFileSync(0, "utf8"));

function seq(n) {
    if (n == 1)
        return 1;
    if (n == 2)
        return 2;
    return seq(Math.floor(n / 3)) + seq(n - 1);
}

console.log(seq(n));