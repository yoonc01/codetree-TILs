const fs = require("fs");
const str = fs.readFileSync(0, "utf8").trim();

const strArray = str.split("");

strArray[1] = 'a';
strArray[strArray.length - 2] = 'a';

console.log(strArray.join(""));