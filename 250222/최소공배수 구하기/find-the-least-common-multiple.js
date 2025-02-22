const fs = require("fs");

const [a, b] = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);

function gcd(a, b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

function lcm(a, b) {
    // javascript에서 몫을 구할 때는 Math.floor를 사용하는 것이 일반적임
    return Math.floor(a * b / gcd);
}

console.log(lcm(a, b));