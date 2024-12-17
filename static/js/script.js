document.addEventListener('DOMContentLoaded', function () {
    const navbar = document.querySelector('.navbar');
    const heroSection = document.querySelector('.hero-image');
    const heroHeight = heroSection.offsetHeight;

    // Initialize navbar to be transparent on page load
    navbar.classList.add('transparent');

    // Function to handle navbar background change based on scroll position
    window.addEventListener('scroll', function () {
        if (window.scrollY < heroHeight) {
            navbar.classList.add('transparent');
            navbar.classList.remove('solid');
        } else {
            navbar.classList.add('solid');
            navbar.classList.remove('transparent');
        }
    });
});
