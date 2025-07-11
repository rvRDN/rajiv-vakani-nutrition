// animations.js

document.addEventListener('DOMContentLoaded', function() {
    // --- Scroll-Triggered Animations Logic ---
    const animatedElements = document.querySelectorAll('.animate-on-scroll');

    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.left >= 0 &&
            rect.bottom >= 0 &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    function handleScrollAnimations() {
        animatedElements.forEach(el => {
            if (isElementInViewport(el)) {
                el.classList.add('is-visible');
            }
        });
    }

    // Initial check for animations on page load
    handleScrollAnimations();

    // Listen for scroll events for animations
    window.addEventListener('scroll', handleScrollAnimations);


    // --- Smooth Scrolling to Anchors Logic ---
    // Select all anchor links that point to IDs on the same page
    // This targets links starting with '#' that are not just '#' alone
    document.querySelectorAll('a[href^="#"]:not([href="#"])').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault(); // Prevent the default jump behavior

            const targetId = this.getAttribute('href'); // Get the ID from the href (e.g., "#about-me")
            const targetElement = document.querySelector(targetId); // Find the element with that ID

            if (targetElement) {
                // Use smooth scroll behavior
                window.scrollTo({
                    top: targetElement.offsetTop, // Scroll to the top of the target element
                    behavior: 'smooth' // Enable smooth scrolling
                });

                // Optional: For accessibility and URL consistency, update the URL hash
                // without causing a jump. This is often done after the scroll completes.
                // However, for simplicity and immediate effect, we'll just do the scroll.
            }
        });
    });
});
