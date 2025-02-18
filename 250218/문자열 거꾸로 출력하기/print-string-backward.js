const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n");

function getNextLine(input) {
    let inputIdx = 0;
    return function () {
        return input[inputIdx++];
    }
}

const nextLine = getNextLine(input);

while(true) {
    const string = nextLine();
    if (string == "END")
        break;
    console.log(string.split("").reverse().join(""));
}
