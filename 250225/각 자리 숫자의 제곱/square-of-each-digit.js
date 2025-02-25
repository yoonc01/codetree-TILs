const fs = require("fs");

const n = Number(fs.readFileSync(0, "utf8").trim());

function getSquareTotal(n) {
    if (n < 10)
        return n * n;
    const r = n % 10;
    return getSquareTotal(Math.floor(n / 10)) + r * r;
}

console.log(getSquareTotal(n));