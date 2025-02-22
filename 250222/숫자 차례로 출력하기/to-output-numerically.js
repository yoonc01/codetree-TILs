function up(n) {
    if (n == 0)
        return;
    up(n - 1);
    process.stdout.write(n + " ");
}

function down(n) {
    if (n == 0)
        return;
    process.stdout.write(n + " ");
    down(n - 1);
}

const fs = require("fs");
const n = Number(fs.readFileSync(0).toString().trim());

up(n);
console.log();
down(n);