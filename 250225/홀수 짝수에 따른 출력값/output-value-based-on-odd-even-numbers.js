const fs = require("fs");
const n = Number(fs.readFileSync(0, "utf8"));

function recursive(n) {
    if (n < 2)
        return n;
    return recursive(n - 2) + n;
}

console.log(recursive(n));