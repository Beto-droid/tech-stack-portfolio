// document.addEventListener("DOMContentLoaded", function () {
//     // Get all the scroll-hiddens.
//     const elements = document.querySelectorAll('.scroll-hidden');
//
//
//     const observer = new IntersectionObserver((entries) => {
//         entries.forEach(entry => {
//             if (entry.isIntersecting) {
//                 entry.target.classList.add('scroll-visible');
//             } else {
//                 // rehid them
//                 entry.target.classList.remove('scroll-visible')
//             }
//         });
//     });
//
//     elements.forEach(el => observer.observe(el));
// });

document.addEventListener("DOMContentLoaded", function () {
    const progressBars = document.querySelectorAll('.progress-bar');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const bar = entry.target;
            const finalWidth = bar.getAttribute('data-final-width');
            if (entry.isIntersecting) {
                bar.style.width = '0';
                setTimeout(() => {
                    bar.style.width = finalWidth;
                }, Array.from(progressBars).indexOf(bar) * 50);
            } else {
                bar.style.width = '0';
            }
        });
    }, {
        threshold: 0.5
    });

    progressBars.forEach(bar => {
        const finalWidth = bar.style.width;
        bar.setAttribute('data-final-width', finalWidth);
        bar.style.width = '0';
        observer.observe(bar);
    });
});

// document.addEventListener("DOMContentLoaded", function () {
//     // Get all the scroll-hiddens.
//     const elements = document.querySelectorAll('.card-hidden');
//
//     const observer = new IntersectionObserver((cards) => {
//         cards.forEach(card => {
//             if (card.isIntersecting) {
//                 card.target.classList.add('card-visible');
//             } else {
//                 // rehid them
//                 card.target.classList.remove('card-visible')
//             }
//         });
//     });
//
//     elements.forEach(el => observer.observe(el));
// });

function animateElementsOnScroll(elementSelector, activeClass) {
    const elements = document.querySelectorAll(elementSelector);

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entri => {
            if (entri.isIntersecting) {
                entri.target.classList.add(activeClass);
            } else {
                // rehid them
                entri.target.classList.remove(activeClass)
            }
        });
    });
    elements.forEach(el => observer.observe(el));
}

animateElementsOnScroll('.scroll-hidden', 'scroll-visible')
animateElementsOnScroll('.card-hidden', 'card-visible')
animateElementsOnScroll('.timeline-hidden', 'timeline-visible')


document.addEventListener("DOMContentLoaded", function () {
    // Get all the scroll-hiddens.
    const elements = document.querySelectorAll('.card-hidden');

    const observer = new IntersectionObserver((cards) => {
        cards.forEach(card => {
            if (card.isIntersecting) {
                card.target.classList.add('card-visible');
            } else {
                // rehid them
                card.target.classList.remove('card-visible')
            }
        });
    });

    elements.forEach(el => observer.observe(el));
});

// document.addEventListener("DOMContentLoaded", function () {
//     const progressBars = document.querySelectorAll('.progress-bar');
//     progressBars.forEach((bar, index) => {
//         const finalWidth = bar.style.width;
//         bar.style.width = '0';
//
//         setTimeout(() => {
//             bar.style.width = finalWidth;
//         }, index * 350); // change the timeout
//     });
// });