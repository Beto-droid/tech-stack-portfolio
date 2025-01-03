function toggleDescription(slideIndex) {
    const carousel = new bootstrap.Carousel(document.getElementById('appCarousel'));
    carousel.to(slideIndex);
}

// For card, overlay toggle.
// click, show overlay go to app.
// Also hide before that the go to app.
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

// For more about
document.getElementById("learnMoreBtn").addEventListener("click", function(event) {
    event.preventDefault();
    document.getElementById("Content").scrollIntoView({ behavior: "smooth" });
});