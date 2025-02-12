const fs = require("fs");

const strings = fs.readFileSync(0).toString().trim().split(/\s+/);

strings.forEach((element) => {
    console.log(element);
})