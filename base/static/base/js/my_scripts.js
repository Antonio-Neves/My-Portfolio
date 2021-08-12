//
// --- Navbar ---
//
const navbar = document.getElementById("navbar");
const navbarToggle = navbar.querySelector(".navbar-toggle");
const navbarLinks = navbar.querySelector(".navbar-links");

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

navbarLinks.addEventListener("click", () => {
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
// --- Scroll to Top ---
//
const btn = $('.gototop');

$(window).scroll(function () {
    if ($(window).scrollTop() > 300) {
        btn.addClass('show');
    } else {
        btn.removeClass('show');
    }
});

btn.on('click', function (e) {
    e.preventDefault();
    $('html, body').animate({ scrollTop: 0 }, '300');
});


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
