function toggleDescription(slideIndex) {
    const carousel = new bootstrap.Carousel(document.getElementById('appCarousel'));
    carousel.to(slideIndex);
}