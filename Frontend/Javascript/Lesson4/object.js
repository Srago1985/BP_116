const person = {
    name: "John",
    surname: "Doe",
    age: 30,
    city: "New York",
    fullName: function() {
        return `${this.name} ${this.surname}`;
    }
}

person.age = 31; // Update age
person.country = "USA"; // Add country
console.log(person.fullName()); // Output: John Doe
console.log(person);
person["profession"] = "Developer"; // Add profession using bracket notation
console.log(person["profession"]); // Output: Developer
let key = "city";
console.log(person[key]); // Output: New York
for (let prop in person) {
    console.log(`${prop}: ${person[prop]}`);
}
delete person["city"]; // Delete city
console.log(person);

function showFields(obj, fields) {
    for (let i = 0; i < fields.length; i++) {
        console.log(person[fields[i]]);
    }
}

showFields(person, ["name", "age", "country"]);

//Constructor

function Car(brand, model, year) {
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.getInfo = function() {
        return `${this.brand} ${this.model} (${this.year})`;
    }
}

const Corolla = new Car("Toyota", "Corolla", 2020);
const Civic = new Car("Honda", "Civic", 2019);
console.log(Corolla.getInfo()); // Output: Toyota Corolla (2020)
console.log(Civic.getInfo()); // Output: Honda Civic (2019)

const cars = [Corolla, Civic, new Car("Ford", "Focus", 2018)];
for (let i = 0; i < cars.length; i++) {
    console.log(cars[i].getInfo());
}