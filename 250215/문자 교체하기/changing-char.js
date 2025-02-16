const fs = require("fs");
const [str1, str2] = fs.readFileSync(0, "utf8").trim().split(/\s+/);

console.log(str1.slice(0, 2) + str2.slice(2));