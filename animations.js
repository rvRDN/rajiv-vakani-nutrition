// animations.js

document.addEventListener('DOMContentLoaded', function() {
    // Select all elements that should animate on scroll
    const animatedElements = document.querySelectorAll('.animate-on-scroll');

    // Function to check if an element is in the viewport
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.left >= 0 &&
            rect.bottom >= 0 && // Check if element is above the bottom of the viewport
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    // Function to handle scroll event
    function handleScroll() {
        animatedElements.forEach(el => {
            if (isElementInViewport(el)) {
                // Add the 'is-visible' class when element enters viewport
                // This class will trigger the CSS animation
                el.classList.add('is-visible');
            }
            // Optional: If you want elements to disappear when scrolled out of view,
            // you could add an 'else { el.classList.remove('is-visible'); }'
            // but for a smooth reveal, usually we keep them visible once animated.
        });
    }

    // Initial check on page load in case elements are already in view
    handleScroll();

    // Listen for scroll events
    window.addEventListener('scroll', handleScroll);
});
