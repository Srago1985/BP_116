const createButton = document.createElement('button');
createButton.textContent = 'Click me';
document.body.appendChild(createButton);

const createLabel = document.createElement('label');
createLabel.textContent = 'Name: ';
document.body.appendChild(createLabel);
const createInput = document.createElement('input');
createInput.type = 'text';
createInput.label = 'Name';
createInput.placeholder = 'Enter your name';
createLabel.appendChild(createInput);
const nameStranger = () => {
    if (createInput.value === '') {
        createInput.value = 'Stranger';
    }
}

createButton.addEventListener('mouseover', () => {createButton.textContent = `Oops, don't touch me!`});
createButton.addEventListener('mouseout', () => {createButton.textContent = 'Click me';});
createButton.addEventListener('click', () => {nameStranger(); alert(`${createInput.value}! Why are you clicking me?`); createInput.value = '';});
createButton.addEventListener('contextmenu', (e) => {nameStranger(); alert(`${createInput.value}, I told you not to click me!`); e.preventDefault(); createInput.value = '';});