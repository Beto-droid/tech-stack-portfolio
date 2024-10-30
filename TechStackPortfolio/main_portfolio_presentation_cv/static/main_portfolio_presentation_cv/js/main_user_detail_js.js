function toggleDescription(slideIndex) {
    const carousel = new bootstrap.Carousel(document.getElementById('appCarousel'));
    carousel.to(slideIndex);
}

// For card

function toggleOverlay(button) {
    const card = button.closest('.card');
    const overlay = card.querySelector('.card-overlay');
    overlay.classList.toggle('visible');

    const titleOverlay = card.querySelector('.project-card-title');
    if (titleOverlay) {
        titleOverlay.style.display = titleOverlay.style.display === 'none' ? 'block' : 'none';
    }
    const go_to_app_button = card.querySelector('.go-to-app-button');
    go_to_app_button.classList.toggle('disabled');
}