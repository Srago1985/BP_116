let a = 10;
console.log(a); // 10
console.log(typeof a); // "number"
a = String(a); // '' + a
console.log(a);
console.log(typeof a); // "string"
a = '42';
console.log(a);
console.log(typeof a);
a = Number(a); // +a
console.log(a);
console.log(typeof a);
a = undefined;
console.log(a);
console.log(typeof a);
a = null;
console.log(a);
console.log(typeof a);

let res = true + false / 5 - null;
console.log(res);
console.log(typeof res);

a = 0;
a = Boolean(a);
console.log(a); // false
console.log(typeof a);
a = '';
a = Boolean(a);
console.log(a); // false
console.log(typeof a);
a = ' ';
a = Boolean(a);
console.log(a); // true
console.log(typeof a);
a = Infinity;
a = Boolean(a);
console.log(a); // true
console.log(typeof a);