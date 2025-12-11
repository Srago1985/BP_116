const arr = [10, 20, 30, 40, 50];
//push
arr.push(60);
console.log(arr); // [10, 20, 30, 40, 50, 60]
//pop
const lastElement = arr.pop();
console.log(lastElement); // 60
console.log(arr); // [10, 20, 30, 40, 50]
//unshift
arr.unshift(0); 
console.log(arr); // [0, 10, 20, 30, 40, 50]
//shift
const firstElement = arr.shift();
console.log(firstElement); // 0
console.log(arr); // [10, 20, 30, 40, 50]
//splice - remove 2 elements from index 1
arr.splice(1, 2);
console.log(arr); // [10, 40, 50]
//splice - add elements at index 1
arr.splice(1, 0, 20, 30);
console.log(arr); // [10, 20, 30, 40, 50]
//concat
const newArr = arr.concat([60, 70, 80]);
console.log(newArr); // [10, 20, 30, 40, 50, 60, 70, 80]
console.log(arr); // [10, 20, 30, 40, 50]
//slice
const slicedArr = arr.slice(2, 5);
console.log(slicedArr); // [30, 40, 50] arr[5] is not included
