const fs = require("fs");
const str = fs.readFileSync(0, "utf8").trim();

/* 
* 아래와 같이 split을 써도 되지만 spread 문법을 써도 됨
* const strArray = str.split("");
*/

const [...strArray] = str;

strArray[1] = 'a';
strArray[strArray.length - 2] = 'a';

console.log(strArray.join(""));