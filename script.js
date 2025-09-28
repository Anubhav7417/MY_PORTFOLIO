// Particle System
class ParticleSystem {
    constructor() {
        this.container = document.getElementById('particles-container');
        this.particles = [];
        this.createParticles();
    }

    createParticles() {
        const particleCount = 50;
        
        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle animate-particle-float';
            
            // Random properties
            const size = Math.random() * 4 + 1;
            const tx = (Math.random() - 0.5) * 200;
            const ty = (Math.random() - 0.5) * 200;
            const colors = [
                'rgba(37, 99, 235, 0.3)',   // Primary blue
                'rgba(6, 182, 212, 0.3)',   // Accent cyan
                'rgba(16, 185, 129, 0.3)',  // Success green
                'rgba(245, 158, 11, 0.3)'   // Warning amber
            ];
            const color = colors[Math.floor(Math.random() * colors.length)];
            
            particle.style.cssText = `
                width: ${size}px;
                height: ${size}px;
                background: ${color};
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                --tx: ${tx}vw;
                --ty: ${ty}vh;
                animation-duration: ${Math.random() * 15 + 10}s;
                animation-delay: ${Math.random() * 5}s;
            `;
            
            this.container.appendChild(particle);
            this.particles.push(particle);
        }
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize particle system
    new ParticleSystem();

    // Animate skill bars when they come into view
    const skillBars = document.querySelectorAll('.skill-bar');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const width = entry.target.style.width;
                entry.target.style.width = '0%';
                setTimeout(() => {
                    entry.target.style.width = width;
                }, 500);
            }
        });
    }, { threshold: 0.5 });

    skillBars.forEach(bar => {
        observer.observe(bar);
    });

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Mobile menu toggle (you can expand this functionality)
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    mobileMenuBtn.addEventListener('click', function() {
        // Add mobile menu functionality here
        console.log('Mobile menu clicked - add your menu logic here');
    });
});
