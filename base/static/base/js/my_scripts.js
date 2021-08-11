// /* Preloader
//     * -------------------------------------------------- */
//     var ssPreloader = function() {
//
//         $("html").addClass('ss-preload');
//
//         $WIN.on('load', function() {
//
//             //force page scroll position to top at page refresh
//             $('html, body').animate({ scrollTop: 0 }, 'normal');
//
//             // will first fade out the loading animation
//             $("#loader").fadeOut("slow", function() {
//                 // will fade out the whole DIV that covers the website.
//                 $("#preloader").delay(300).fadeOut("slow");
//             });
//
//             // for hero content animations
//             $("html").removeClass('ss-preload');
//             $("html").addClass('ss-loaded');
//
//         });
//     };
//
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
