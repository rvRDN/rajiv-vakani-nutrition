window.addEventListener("load", () => {
  const typedText = document.getElementById("typed-text");

  if (!typedText) return;

  const words = [
    "Evidence Seeker.",
    "Nutritionist.",
    "Mindful Eater.",
    "Food Educator.",
    "Plant-Forward."
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
      }, WORD_PAUSE);
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      wordIndex = (wordIndex + 1) % words.length;
      setTimeout(type, TYPING_DELAY);
    } else {
      setTimeout(type, isDeleting ? ERASING_DELAY : TYPING_DELAY);
    }
  }

  type();
});
