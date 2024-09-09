"use strict";

$(document).ready(function () {
    // =====================================================================
    // navbar variables
    const $nav = $(".mobile-nav");
    const $navMenuBtn = $(".nav-menu-btn");
    const $navCloseBtn = $(".nav-close-btn");

    // navToggle function
    const navToggleFunc = function () {
        $nav.toggleClass("active");
    };

    $navMenuBtn.on("click", navToggleFunc);
    $navCloseBtn.on("click", navToggleFunc);

    // =====================================================================
    // theme toggle variables
    const $themeBtn = $(".theme-btn");

    // Load the saved theme from localStorage
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
        $("body").addClass(savedTheme);
        $themeBtn.addClass(
            savedTheme === "light-theme" ? "light-theme" : "dark-theme"
        );
    }

    $themeBtn.on("click", function () {
        // Toggle `light-theme` & `dark-theme` class on `body`
        $("body").toggleClass("light-theme dark-theme");

        // Toggle classes on all `theme-btn`
        $themeBtn.toggleClass("light dark");

        // Save the current theme to localStorage
        const currentTheme = $("body").hasClass("light-theme")
            ? "light-theme"
            : "dark-theme";
        localStorage.setItem("theme", currentTheme);
    });

    // =====================================================================
    // footer
    const fullyear = new Date().getFullYear();
    $("footer .year").text(fullyear);
});

// // =====================================================================

// "use strict";
// // =====================================================================
// // navbar variables
// const nav = document.querySelector(".mobile-nav");
// const navMenuBtn = document.querySelector(".nav-menu-btn");
// const navCloseBtn = document.querySelector(".nav-close-btn");

// // navToggle function
// const navToggleFunc = function () {
//     nav.classList.toggle("active");
// };

// navMenuBtn.addEventListener("click", navToggleFunc);
// navCloseBtn.addEventListener("click", navToggleFunc);

// // =====================================================================
// // theme toggle variables
// const themeBtn = document.querySelectorAll(".theme-btn");

// for (let i = 0; i < themeBtn.length; i++) {
//     themeBtn[i].addEventListener("click", function () {
//         // toggle `light-theme` & `dark-theme` class from `body`
//         // when clicked `theme-btn`
//         document.body.classList.toggle("light-theme");
//         document.body.classList.toggle("dark-theme");

//         for (let i = 0; i < themeBtn.length; i++) {
//             // When the `theme-btn` is clicked,
//             // it toggles classes between `light` & `dark` for all `theme-btn`.
//             themeBtn[i].classList.toggle("light");
//             themeBtn[i].classList.toggle("dark");
//         }
//     });
// }

// // =====================================================================
// // footer
// let fullyear = new Date().getFullYear();
// let footeryear = document.querySelector("footer .year");
// footeryear.textContent = fullyear;
