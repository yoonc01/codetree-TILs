const fs = require("fs");

const n = Number(fs.readFileSync(0, "utf8"))

function untilOne(n) {
    if (n == 1)
        return 0;
    if (n % 2 == 0)
        return untilOne(Math.floor(n / 2)) + 1;
    return untilOne(Math.floor(n / 3)) + 1;
}

console.log(untilOne(n));
