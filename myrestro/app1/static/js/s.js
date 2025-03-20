// let tabcontents = document.getElementsByClassName("tab-content");
// let tablinks = document.getElementsByClassName("tab-link");

// function openlink(arg) {   
//     for (let tabcontent of tabcontents) {
//         tabcontent.classList.remove("active-tab");
//     }
//     for (let tablink of tablinks) {
//         tablink.classList.remove("active");
//     }
//     document.getElementById(arg).classList.add("active-tab");
//     event.currentTarget.classList.add("active");
// }


let tabcontents = document.getElementsByClassName("tab-content");
let tablinks = document.getElementsByClassName("tab-links");

function openlink(arg) {
    // Remove active class from all tab contents
    for (let tabcontent of tabcontents) {
        tabcontent.classList.remove("active-tab");
    }
    // Remove active class from all tab links
    for (let tablink of tablinks) {
        tablink.classList.remove("active");
    }
    // Add active class to the clicked tab content
    document.getElementById(arg).classList.add("active-tab");
    // Add active class to the clicked tab link
    this.classList.add("active");
}
