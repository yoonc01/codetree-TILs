function getNextLine(input) {
    let inputIdx = 0;
    return function () {
        return input[inputIdx++].split(/\s+/);
    };
}

function swap(strArray, a, b) {
    a = Number(a) - 1;
    b = Number(b) - 1;
        let temp = strArray[a];
        strArray[a] = strArray[b];
        strArray[b] = temp;
}

function change(strArray, a, b) {
    for (let i = 0; i < strArray.length; i++) {
        if (strArray[i] === a) strArray[i] = b;
    }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n");
const nextLine = getNextLine(input);

let [s, q] = nextLine();
q = Number(q);
let strArray = [...s];

const output = [];

while (q--) {
    const [cmd, a, b] = nextLine();
    if (cmd === "1") {
        swap(strArray, a, b);
    } else {
        change(strArray, a, b);
    }
    output.push(strArray.join(""));
}

console.log(output.join("\n"));
