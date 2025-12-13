const library = [];


//isbn,title,author,year
let inputData = prompt('Enter book data (isbn,title,author,year) separated by commas');
while (inputData) {
    const [isbn, title, author, year] = inputData.split(',');
    if (findBook(library, isbn) === -1) {
        library.push(new Book(isbn, title, author, year));
    }
    inputData = prompt('Enter book data (isbn,title,author,year) separated by commas');
}
printLibrary(library);


function printLibrary() {
    // TODO print all books from library to console
    for (let i = 0; i < library.length; i++) {
        console.log(library[i].toString());
    }
}


function findBook(library, isbn) {
    // TODO find book by isbn and return index of it or -1 if not found
    for (let i = 0; i < library.length; i++) {
        if (library[i].isbn === isbn) {
            return i;
        }
    }
    return -1;
}


function Book(isbn, title, author, year) {
    this.isbn = isbn;
    this.title = title;
    this.author = author;
    this.year = +year;
    this.toString = function () {
        return `ISBN: ${this.isbn}; Title: ${this.title}; Author: ${this.author}; Year of publication: ${this.year};`
    }
}
