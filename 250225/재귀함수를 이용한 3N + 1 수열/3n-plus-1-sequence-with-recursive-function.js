const fs = require("fs");

const n = Number(fs.readFileSync(0, "utf8"));

function count(n) {
    if (n == 0)
        return 0;
    if (n % 2 == 0)
        return count(Math.floor(n / 2)) + 1;
    return count(3 * n + 1) + 1; 
}

console.log(count(n));