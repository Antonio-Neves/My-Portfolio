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
// --- Hide form after submit ---
///
function hide_contact_form() {
    $('#contact-form').submit(function () {
        $(this).hide();
    })
}

hide_contact_form();

//
// --- Avoid page reload after submit ---
//
$(function () {
    $('#contact-form').on('submit',function (e) {

              $.ajax({
                // type: 'post',
                // url: '/',
                data: $('#contact-form').serialize(),
                success: function () {
                 alert("Thank you! Your message has been sent!");
                }
              });
          e.preventDefault();
        });
});


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
