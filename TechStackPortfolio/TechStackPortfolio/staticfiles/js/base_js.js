
// Toast for showing the menu
document.addEventListener("DOMContentLoaded", function () {
    const toastEl = document.getElementById('liveToast');
    const toast = new bootstrap.Toast(toastEl, {delay: 4000});
    toast.show();
});


//Awfully js to make modal and login and htmx work

document.body.addEventListener('htmx:afterRequest', (event) => {
    const xhr = event.detail.xhr;
    if (xhr.status === 200) {
        const responseText = xhr.responseText.trim();
        if (responseText.startsWith("{") || responseText.startsWith("[")) {
            try {
                const data = JSON.parse(responseText);
                if (data.redirect) {
                    window.location.href = data.redirect;
                }
            } catch (e) {
                console.error("Error parsing JSON response:", e);
            }
        }
    }
});