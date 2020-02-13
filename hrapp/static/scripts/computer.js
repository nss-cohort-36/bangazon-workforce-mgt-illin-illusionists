const infoDialog = document.querySelector(".infoDialog")
const message = document.querySelector(".infoDialog__message")
const closeDialog = document.querySelector(".closeDialog")

document.querySelector(".computer").addEventListener("click", (evt) => {
    if (evt.target.id.startsWith("delete")) {
        const id = evt.target.id.split("--")[1]
        message.innerText = `Are you sure you want to delete computer ${id}?`
        infoDialog.show()
    }
})

// Close the dialog when the close button is clicked
closeDialog.addEventListener("click", e => infoDialog.close())

// Close the dialog when the escape key is pressed
window.addEventListener("keyup", e => {
    if (e.keyCode === 27) {
        infoDialog.close()
    }
})