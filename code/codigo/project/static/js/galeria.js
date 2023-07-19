const container = document.querySelector('.container')
const linkUnsplash = 'https://source.unsplash.com/random/'
const rows = 10

for(let i = 0; i < rows * 3; i++) {
    const img = document.createElement('img')
    img.src = `${linkUnsplash}${getRandomSize()}`
    container.appendChild(img)
}

console.log(getRandomSize())

function getRandomSize() {
    return `${getRandomNr()}x${getRandomNr()}`
}

function getRandomNr() {
    return Math.floor(Math.random() * 10) + 300
}