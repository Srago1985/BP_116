let library = JSON.parse(localStorage.getItem('library')) || []; //read library from localStorage
library = library.map(book => new Book(book.isbn, book.title, book.author, book.year));

const button = document.createElement('button');//create button
button.innerText = 'Добавить книги';
button.addEventListener('click', addBooks);
document.body.appendChild(button);

if (library.length > 0) printLibrary();//print library if it is not empty

function addBooks() {
    //check input data and add new books to library
    while (true) {
        let inputData = prompt('Enter book data (isbn,title,author,year) separated by commas');
        if (inputData === null || inputData === '') break;
        const parts = inputData.split(',');
        if (parts.length !== 4 || parts.some(p => p.trim() === '')) {
            alert('Неверный формат. Введите данные в формате: isbn,title,author,year');
            continue;
        }
        const [isbn, title, author, year] = parts.map(p => p.trim());
        if (!isbn || !title || !author || !year) {
            alert('Все поля должны быть заполнены');
            continue;
        }
        if (isNaN(+year)) {
            alert('Год должен быть числом');
            continue;
        }
        if (findBook(library, isbn) !== -1) {
            alert('Книга с таким ISBN уже существует');
            continue;
        }
        library.push(new Book(isbn, title, author, year));
        localStorage.setItem('library', JSON.stringify(library));//save updated library to localStorage
    }
    printLibrary();
}


function printLibrary() {
    //print all books from library as a numbered list    
    let root = document.getElementById('root');
    if (!root) {
        root = document.createElement('div');
        root.id = 'root';
        document.body.appendChild(root);
    } else {
        root.innerHTML = '';
    } //if user clicks "Add books" multiple times, update existing list
    const ol = document.createElement('ol');
    for (let i = 0; i < library.length; i++) {
        const li = document.createElement('li');
        li.innerText = library[i].toString();
        ol.appendChild(li);
    }
    root.appendChild(ol);    
}

function findBook(library, isbn) {
    //check if a book with the given ISBN exists in the library
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

