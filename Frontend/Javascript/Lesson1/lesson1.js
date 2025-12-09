console.log("Hello, World!");
console.log("Welcome to Lesson 1 of JavaScript!");

let admin, name;
name = "John";
admin = name;
console.log(admin); // will show "John"

let planet = "Earth";
let visitor = "Guest";

const BIRTHDAY = "01.01.2000";
const age = 25;

let name2 = "Ilya";

console.log( `hello ${1}` ); // ?

console.log( `hello ${"name"}` ); // ?

console.log( `hello ${name2}` ); // ?

let userName = prompt("What is your name?", "Guest");
alert(`Hello, ${userName}!`);

let isNumberLucky = (num) => {
    let strNum = num.toString();
    let evenSum = 0;
    let oddSum = 0;

    for (let i = 0; i < strNum.length; i++) {
        if (i % 2 === 0) {
            evenSum += parseInt(strNum[i]);
        } else {
            oddSum += parseInt(strNum[i]);
        }
    }
    return evenSum === oddSum;
}

function luckyNumber(num) {
    let sum = 0;
    while (num!==0) {
        sum = num % 10 - sum;
        num = (num - num % 10) / 10;
    }
    return sum === 0;
    // +-(d0-d1+d2-d3+d4-d5...) if sum=0 -> lucky
}