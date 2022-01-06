console.log("Hellow World");
const form = document.querySelector('#form')
const tagImage = document.querySelector('#image')
const inputFile = document.querySelector('#file')

function renderImage(formData) {
    const file = formData.get('image')
    const image = URL.createObjectURL(file)
    tagImage.setAttribute('src', image)
}

inputFile.addEventListener('change', () => {
    const formData = new FormData(form)
    renderImage(formData)
})