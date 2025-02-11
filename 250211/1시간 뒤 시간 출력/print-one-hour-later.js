const fs = require("fs");
//정규 표현식 사용
const input = fs.readFileSync(0).toString().trim().split(/[\s:]+/);
const [h, m] = input;
h++;
console.log(`{h}:{m}`);