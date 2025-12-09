// const greeting = function (name) {
//     return `Hello ${name}`
// }

// const greeting = (name) => {
//     return `Hello ${name}`;
// }

const greeting = name => `Hello ${name}`;

// greeting = 42

console.log(greeting('John'));
console.log(greeting);
const greeting2 = greeting;
console.log(greeting2('Peter'));
console.log(greeting2);
console.log(typeof greeting);
console.log(typeof greeting2);
console.log('==========');
let res = pow2(2); // x = 2
console.log(res);
res = pow3(3); // x = 3
console.log(res);
res = factorial(5); // n = 5
console.log(res);
console.log('=== universalFunction ===');
res = universalFunction(2, pow3, pow2); // a = 2, fn1 = pow3, fn2 = pow2
console.log(res);
res = universalFunction(-3, x => x ** 3, x => x ** 2); // a = -3, fn1 = x => x ** 3, fn2 = x => x ** 2
console.log(res);
res = universalFunction(6, factorial, pow2); // a = 6, fn1 = factorial, fn2 = pow2
console.log(res);
res = universalFunction('0', true, false);
console.log(res);
res = universalFunction(5, a => a + 3, a => a - 3);
// a = 5, fn1 = a => a + 3, fn2 = a => a - 3
console.log(res);

// fn1, fn2 - callback functions
function universalFunction(a, fn1, fn2) { // let a, let fn1, let fn2
    if(typeof a !== 'number' || typeof fn1 !== 'function' || typeof fn2 !== 'function') {
        return 'Error';
    }
    if (a > 0) {
        return fn1(a);
    } else {
        return fn2(a);
    }
}

function pow2(x) {
    return x ** 2;
}

function pow3(x) {
    return x ** 3;
}

function factorial(n) {
    let res = 1;
    for (let i = 1; i <= n; i++) {
        res *= i;
    }
    return res;
}