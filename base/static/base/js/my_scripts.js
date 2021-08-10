//
// --- Navbar ---
//
const navbar = document.getElementById("navbar");
const navbarToggle = navbar.querySelector(".navbar-toggle");

function openMobileNavbar() {
  navbar.classList.add("opened");
  navbarToggle.setAttribute("aria-label", "Close navigation menu.");
}

function closeMobileNavbar() {
  navbar.classList.remove("opened");
  navbarToggle.setAttribute("aria-label", "Open navigation menu.");
}

navbarToggle.addEventListener("click", () => {
  if (navbar.classList.contains("opened")) {
    closeMobileNavbar();
  } else {
    openMobileNavbar();
  }
});

const navbarMenu = navbar.querySelector(".navbar-menu");
const navbarLinksContainer = navbar.querySelector(".navbar-links");

navbarLinksContainer.addEventListener("click", (clickEvent) => {
  clickEvent.stopPropagation();
});

navbarMenu.addEventListener("click", closeMobileNavbar);

//
// --- Animated Title ---
//
// Wrap every letter in a span
// var textWrapper = document.querySelector('.ml12');
// textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");
//
// anime.timeline({loop: true})
//   // Entry
//   .add({
//     targets: '.ml12 .letter',
//     translateX: [40,0],
//     translateZ: 0,
//     opacity: [0,1],
//     easing: "easeOutExpo",
//     duration: 1200,
//     delay: (el, i) => 500 + 30 * i
//   // Exit
//   }).add({
//     targets: '.ml12 .letter',
//     translateX: [0, 30],
//     opacity: [1,0],
//     easing: "easeInExpo",
//     duration: 1100,
//     delay: (el, i) => 100 + 30 * i
//   });

//
// --- Cokie Consent ---
//
window.cookieconsent.initialise({
  "palette": {
    "popup": {
      "background": "rgba(16,45,105, 0.6)",
      "text": "rgb(235,240,255)"
    },
    "button": {
      "background": "transparent",
      "text": "rgb(235,240,255)",
      "border": "rgb(235,240,255)"
    }
  },
  "content": {
    "dismiss": "OK"
  }
});
