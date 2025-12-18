const createBox = () => {
    const box = document.createElement('div');
    box.style.width = '400px';
    box.style.height = '400px';
    box.style.backgroundColor = 'lightblue';
    box.style.position = 'relative';
    document.body.appendChild(box);
    return box;
}

const innerBox = () => {
    const innerBox = document.createElement('div');
    innerBox.style.width = '50px';
    innerBox.style.height = '50px';
    innerBox.style.backgroundColor = 'red';
    innerBox.style.position = 'absolute';
    innerBox.style.top = '0px';
    innerBox.style.left = '0px';
    return innerBox;
}

const animateBox = () => {
    const outerBox = createBox();
    const innerBoxElement = innerBox();
    outerBox.appendChild(innerBoxElement);
    const style = document.createElement('style');
    style.textContent = `
        @keyframes moveBox {
            from {
                top: 0px;
                left: 0px;
            }
            to {
                top: 350px;
                left: 350px;
            }
        }
        .animate {
            animation: moveBox 5s ease-in-out forwards alternate infinite;
        }
    `;
    document.head.appendChild(style);    
    innerBoxElement.classList.add('animate');
}

animateBox();