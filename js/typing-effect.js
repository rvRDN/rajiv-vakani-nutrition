// js/typing-effect.js

document.addEventListener("DOMContentLoaded", () => {
  const words = [
    "Educator",
    "Writer",
    "Future Dietitian",
    "Evidence Seeker",
    "Plant-Based Advocate"
  ];

  let wordIndex = 0;
  let charIndex = 0;
  let typingForward = true;
  const typedElement = document.getElementById("typed-word");

  // Only proceed if the typedElement exists on the page
  if (!typedElement) {
    console.warn("Element with ID 'typed-word' not found. Typing effect will not run.");
    return;
  }

  function type() {
    const word = words[wordIndex];
    typedElement.textContent = word.substring(0, charIndex); // Update text content

    if (typingForward) {
      charIndex++;
      if (charIndex > word.length) { // Use > to allow for the word to be fully typed before pausing
        typingForward = false;
        setTimeout(type, 1200); // Pause before deleting
        return;
      }
    } else {
      charIndex--;
      if (charIndex < 0) { // Use < to ensure it fully deletes before moving to next word
        typingForward = true;
        wordIndex = (wordIndex + 1) % words.length;
        charIndex = 0; // Reset charIndex for the new word
      }
    }
    
    // Set timeout for next character, faster when deleting, slower when typing
    setTimeout(type, typingForward ? 100 : 50); 
  }

  setTimeout(type, 500); // Start typing after a short delay
});