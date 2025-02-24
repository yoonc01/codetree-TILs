const fs = require("fs");

const n = Number(fs.readFileSync(0, "utf8").trim());

function printCountDown(n) {
    if (n == 0)
        return;
    process.stdout.write(n + " ");
    printCountDown(n - 1);
}

function printCountUp(n) {
    if (n == 0)
        return;
    printCountUp(n - 1);
    process.stdout.write(n + " ");
}

function printCnt(n) {
    printCountDown(n);
    printCountUp(n);
}

printCnt(n);