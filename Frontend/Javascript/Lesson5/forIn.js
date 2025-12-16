const person = {
    firstName: 'John',
    lastName: 'Doe',
    age: 25,
    fullName: function () {
        return `${this.firstName} ${this.lastName}`;
    }
}

for (let key in person) {
    if (typeof person[key] === 'function') {
        console.log(`${key} -> ${person[key]()}`);
    } else {
        console.log(`${key} -> ${person[key]}`);
    }
}