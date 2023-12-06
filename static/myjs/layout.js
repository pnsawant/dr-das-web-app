
// Current Year Code
document.addEventListener("DOMContentLoaded", function () {
    // Get the current year
    var currentYear = new Date().getFullYear();
    // Display the current year in the element with id "currentYear"
    document.getElementById("currentYear").textContent = currentYear;
});


// Scroll To Top
//Get the button
let mybutton = document.getElementById("btn-back-to-top");
// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
    scrollFunction();
};
function scrollFunction() {
    if (
        document.body.scrollTop > 178 ||
        document.documentElement.scrollTop > 178
    ) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);
function backToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}