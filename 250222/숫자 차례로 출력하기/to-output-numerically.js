function recursive_up(s, e) {
    if (s == e) {
        process.stdout.write(`${s}\n`);
        return;
    }
    process.stdout.write(`${s} `);
    recursive_up(s + 1, e);
}

function recursive_down(s, e) {
    if (s == e) {
        process.stdout.write(`${s}\n`);
        return;
    }
    process.stdout.write(`${s} `);
    recursive_down(s - 1, e);
}

const fs = require("fs");
const n = Number(fs.readFileSync(0, "utf8").trim());
recursive_up(1, n);
recursive_down(n, 1);