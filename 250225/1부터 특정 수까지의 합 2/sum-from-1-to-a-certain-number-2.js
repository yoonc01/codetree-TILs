const fs = require("fs");

const n = Number(fs.readFileSync(0, "utf8").trim())

function getTotal(n) {
    if (n == 1)
        return 1;
    return getTotal(n - 1) + n;
}

console.log(getTotal(n));