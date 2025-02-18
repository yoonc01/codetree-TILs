const fs = require("fs");

const n = Number(fs.readFileSync(0, "utf8").trim());

const printRect = n => {
    let cnt = 1;
    for (let i = 0; i < n; i++) {
        const line = [];
        for (let j = 0; j < n; j++) {
            line.push(cnt);
            cnt = cnt % 9 + 1;
        }
        console.log(line.join(" "));
    }
}

printRect(n);