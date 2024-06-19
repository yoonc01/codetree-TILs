const fs = require("fs");
let arr = fs.readFileSync(0).toString().trim().split(/\s+/);
arr.reverse()
console.log(arr.join(""));