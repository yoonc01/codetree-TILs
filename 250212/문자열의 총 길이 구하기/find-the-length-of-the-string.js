const fs = require("fs");
const strings = fs.readFileSync(0).toString().trim().split(/\s+/);

const ans = strings.reduce((acc, cur) => {
    return acc + cur.length;
}, 0);
console.log(ans);