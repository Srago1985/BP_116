let library = JSON.parse(localStorage.getItem('library')) || []; //read library from localStorage
library = library.map(book => new Book(book.isbn, book.title, book.author, book.year));

const buttonsContainer = document.createElement('div');
buttonsContainer.style.marginBottom = '10px';
document.body.appendChild(buttonsContainer);

const button = document.createElement('button');//create button
button.innerText = 'Добавить книги';
button.addEventListener('click', addBooks);
buttonsContainer.appendChild(button);

const buttonClear = document.createElement('button');//create button to clear library
buttonClear.innerText = 'Очистить библиотеку';
buttonClear.style.marginLeft = '10px';
buttonClear.addEventListener('click', function() {
    library = [];
    localStorage.removeItem('library');
    const root = document.getElementById('root');
    if (root) root.replaceChildren();
});
buttonsContainer.appendChild(buttonClear);

document.body.addEventListener('keydown', function(event) {//add book on Enter key press
    if (event.key === 'Enter') {
        addBooks();
    }
});

if (library.length > 0) printLibrary();//print library if it is not empty

const createLabelInput = (labelText, inputId, inputMode) => {
    const label = document.createElement('label');
    label.innerText = labelText;
    label.style.display = 'flex';
    label.style.flexDirection = 'column';


    const input = document.createElement('input');
    input.id = inputId;
    input.classList.add('input-field');    
    input.type = 'text';
    input.inputMode = inputMode || 'text';    
    input.autocomplete = 'on';
    input.style.maxWidth = '200px';
    label.appendChild(input);

    return label;
};

const isbnInput = createLabelInput('ISBN: ', 'isbn', 'numeric');
document.body.appendChild(isbnInput);
const titleInput = createLabelInput('Title: ', 'title');
document.body.appendChild(titleInput);
const authorInput = createLabelInput('Author: ', 'author');
document.body.appendChild(authorInput);
const yearInput = createLabelInput('Year: ', 'year', 'numeric');
document.body.appendChild(yearInput);

function addBooks() { //check input data and add new books to library  
        const isbn = document.getElementById('isbn').value;
        const title = document.getElementById('title').value;
        const author = document.getElementById('author').value;
        const year = document.getElementById('year').value;

        if (!isbn && year >= 1970) {
            alert('Пожалуйста, введите ISBN');
            return
        }

        if (!isbn && year < 1970) {
            document.getElementById('isbn').value = 'N/A';
        }

        if (isbn && year < 1970) {
            alert('Пожалуйста, проверьте данные, ISBN не может быть указан для книг, изданных до 1970 года');
            return;
        }
        
        if (!title || !author || !year) {
            alert('Пожалуйста, заполните все поля');
            return;
        }

        if (isNaN(year) || year > new Date().getFullYear()) {
            alert('Пожалуйста, введите корректный год публикации');
            return;
        }

        if (findBook(library, isbn) !== -1) {
            alert('Книга с таким ISBN уже существует');
            return;
        }

        library.push(new Book(isbn, title, author, year));
        localStorage.setItem('library', JSON.stringify(library));//save updated library to localStorage

        //clear inputs after adding a book
        document.querySelectorAll('.input-field').forEach(input => input.value = '');
    printLibrary();
}


function printLibrary() { //print all books from library as a numbered list    
    let root = document.getElementById('root');
    if (!root) {
        root = document.createElement('div');
        root.id = 'root';
        document.body.appendChild(root);
    } //if user clicks "Add books" multiple times, update existing list
    const ol = document.createElement('ol');
    for (let i = 0; i < library.length; i++) {
        const li = document.createElement('li');
        li.innerText = library[i].toString();
        ol.appendChild(li);
    }
    root.replaceChildren(ol);
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

