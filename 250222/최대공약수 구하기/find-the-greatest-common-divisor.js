const fs = require("fs");

const [a, b] = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

function gcd(a, b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

console.log(gcd(a, b));