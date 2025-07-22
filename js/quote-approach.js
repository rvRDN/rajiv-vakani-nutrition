console.log('✅ quote-approach.js loaded');

const lineWrappers = document.querySelectorAll('.quote-line-wrapper');

const quoteObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const wrapper = entry.target;
      const index = parseInt(wrapper.dataset.index, 10) || 0;
      const line = wrapper.querySelector('.animated-quote-line');
      const ambient = wrapper.querySelector('.ambient');

      setTimeout(() => {
        if (line) {
          line.style.opacity = '1';
          line.style.transform = 'translateY(0)';
        }

        if (ambient) {
          ambient.style.opacity = '1';
        }
      }, index * 400); // stagger each line

      observer.unobserve(wrapper); // Only trigger once per line
    }
  });
}, { threshold: 0.4 });

// Observe each wrapper
lineWrappers.forEach(wrapper => {
  quoteObserver.observe(wrapper);
});
