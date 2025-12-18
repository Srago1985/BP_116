const previousButton = document.querySelector('.btn_prev');
const nextButton = document.querySelector('.btn_next');
const image = document.querySelector('img');

const images = [
    './Images/Rouen_Cathedral_1.jpg',
    './Images/Rouen_Cathedral_2.jpg',
    './Images/Rouen_Cathedral_3.jpg',
    './Images/Rouen_Cathedral_4.jpg',
    './Images/Rouen_Cathedral_5.jpg',
    './Images/Rouen_Cathedral_6.jpg'
];

let currentImageIndex = 0;

const showNextImage = () => {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    image.src = images[currentImageIndex];
};

const showPreviousImage = () => {
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    image.src = images[currentImageIndex];
};

previousButton.addEventListener('click', showPreviousImage);
nextButton.addEventListener('click', showNextImage);



