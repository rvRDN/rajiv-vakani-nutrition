document.addEventListener("DOMContentLoaded", function () {
  const typedText = document.getElementById("typed-text");

  const words = [
    "Future Dietitian",
    "Educator",
    "Evidence Seeker",
    "Plant-Based Thinker",
    "Mindful Eater",
    "Writer"
  ];

  const TYPING_DELAY = 100;
  const ERASING_DELAY = 50;
  const WORD_PAUSE = 1500;

  let wordIndex = 0;
  let charIndex = 0;
  let isDeleting = false;

  function type() {
    const currentWord = words[wordIndex];

    if (isDeleting) {
      typedText.textContent = currentWord.substring(0, charIndex - 1);
      charIndex--;
    } else {
      typedText.textContent = currentWord.substring(0, charIndex + 1);
      charIndex++;
    }

    if (!isDeleting && charIndex === currentWord.length) {
  setTimeout(() => {
    isDeleting = true;
    type();
  }, 1000); // Pause after typing before deleting (1 second)
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      wordIndex = (wordIndex + 1) % words.length;
      setTimeout(type, TYPING_DELAY);
    } else {
      setTimeout(type, isDeleting ? ERASING_DELAY : TYPING_DELAY);
    }
  }

  if (typedText) {
    type();
  }
});
