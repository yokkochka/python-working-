const menubutton = document.querySelector(".menuButton");
const menu = document.querySelector(".navMenu");
const menuCloseButton = document.querySelector(".nav .menuClose");

menubutton.addEventListener("click", () => {
    menu.classList.add("isActive");
    menuCloseButton.classList.add("isActive");
});
menuCloseButton.addEventListener("click", () => {
    menu.classList.remove("isActive");
    menuCloseButton.classList.remove("isActive");
});