document.addEventListener('DOMContentLoaded', () => {
    // Navigation Toggle for Mobile
    const toggleBtn = document.querySelector('.mobile-toggle');
    const navLinks = document.getElementById('nav-links');
    const navItems = document.querySelectorAll('.nav-links a.nav-item');
    const sections = document.querySelectorAll('section[id]');
    const heroImage = document.querySelector('.hero-bg img');

    if(toggleBtn && navLinks) {
        toggleBtn.addEventListener('click', () => {
            const isExpanded = toggleBtn.getAttribute('aria-expanded') === 'true';
            toggleBtn.setAttribute('aria-expanded', !isExpanded);
            navLinks.classList.toggle('active');
            toggleBtn.classList.toggle('active');
        });
    }

    // Close mobile menu when clicking a link
    const links = document.querySelectorAll('.nav-links a');
    links.forEach(link => {
        link.addEventListener('click', () => {
            if (navLinks && toggleBtn) {
                navLinks.classList.remove('active');
                toggleBtn.classList.remove('active');
                toggleBtn.setAttribute('aria-expanded', 'false');
            }
        });
    });

    // Header Scroll Effect
    const header = document.getElementById('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 40) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        // Subtle parallax depth on hero background image
        if (heroImage && window.scrollY < window.innerHeight) {
            const offset = window.scrollY * 0.15;
            heroImage.style.transform = `scale(1.04) translateY(${offset}px)`;
        }
    });

    // Active navigation link based on current section in viewport
    const setActiveNavLink = () => {
        let currentId = 'home';
        const offset = 140;

        sections.forEach(section => {
            const sectionTop = section.offsetTop - offset;
            const sectionBottom = sectionTop + section.offsetHeight;
            if (window.scrollY >= sectionTop && window.scrollY < sectionBottom) {
                currentId = section.getAttribute('id');
            }
        });

        navItems.forEach(item => {
            const target = item.getAttribute('href')?.replace('#', '');
            item.classList.toggle('active', target === currentId);
        });
    };

    window.addEventListener('scroll', setActiveNavLink);
    setActiveNavLink();

    // Smooth Scrolling for Anchor Links (Accessibility improvements)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if(targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if(targetElement) {
                e.preventDefault();
                const headerOffset = 80; // Adjust for sticky header
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
  
                window.scrollTo({
                     top: offsetPosition,
                     behavior: "smooth"
                });
                
                // Set focus for accessibility
                targetElement.setAttribute('tabindex', '-1');
                targetElement.focus();
            }
        });
    });

    // Reveal animation for sections/cards on scroll
    const revealTargets = document.querySelectorAll(
        '.section-title, .about-grid, .mission-card, .objective-item, .program-card, .stat-box, .timeline-item, .cta .container'
    );

    revealTargets.forEach((el) => el.classList.add('reveal'));

    const observer = new IntersectionObserver(
        (entries, obs) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    obs.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.05, rootMargin: '0px 0px -50px 0px' }
    );

    revealTargets.forEach((el) => observer.observe(el));
});