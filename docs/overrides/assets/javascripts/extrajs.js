// Bahala Na Python - Extra JavaScript
// This file is loaded after the theme's main JS

(function() {
  'use strict';

  // Add keyboard shortcut hints
  document.addEventListener('keydown', function(e) {
    // Ctrl+Shift+K to toggle XP tracker
    if (e.ctrlKey && e.shiftKey && e.key === 'K') {
      e.preventDefault();
      const tracker = document.getElementById('xp-tracker');
      if (tracker) {
        const isVisible = tracker.style.display !== 'none';
        tracker.style.display = isVisible ? 'none' : 'block';
      }
    }
  });

})();
