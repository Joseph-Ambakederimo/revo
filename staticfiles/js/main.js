document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navContent = document.querySelector('.nav-content');
  
    mobileMenuBtn.addEventListener('click', function() {
      mobileMenuBtn.classList.toggle('active');
      navContent.classList.toggle('active');
    });
  
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
      if (!navContent.contains(event.target) && !mobileMenuBtn.contains(event.target)) {
        mobileMenuBtn.classList.remove('active');
        navContent.classList.remove('active');
      }
    });
  });