let a;
let b;

let res = b/a;
if (isNaN(res)) {
    console.log("solution is any number");
} else if (!isFinite(res)) {
    console.log("no solution");
} else {
    console.log("Result is " + res);
}