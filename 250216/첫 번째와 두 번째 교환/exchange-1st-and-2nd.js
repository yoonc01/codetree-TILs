const fs = require("fs");

const str = fs.readFileSync(0, "utf8").trim();

const [first, second, ...rest] = str;

const result = [second, first, ...rest.map(ch => {
    if (ch == first)
        return (second);
    else if (ch == second)
        return (first);
    return (ch);
}
)].join("");

console.log(result);
