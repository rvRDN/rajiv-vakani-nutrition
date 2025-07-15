// animations.js

document.addEventListener('DOMContentLoaded', function() {
    // --- Scroll-Triggered Animations Logic (using IntersectionObserver) ---
    // Select both sections with 'animate-on-scroll' and individual 'upcoming-item' elements
    // The 'upcoming-item' elements will now be observed directly for animation
    const animateOnScrollElements = document.querySelectorAll('.animate-on-scroll, .upcoming-item');

    const observerOptions = {
        root: null, // relative to the viewport
        rootMargin: '0px',
        threshold: 0.1 // percentage of element visible to trigger
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show'); // Use 'show' class for visibility
                observer.unobserve(entry.target); // Stop observing once animated
            }
        });
    }, observerOptions);

    animateOnScrollElements.forEach(element => {
        observer.observe(element);
    });

    // --- Smooth Scrolling to Anchors Logic (from your original file) ---
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