document.addEventListener("DOMContentLoaded", function () {
    const toastEl = document.getElementById('liveToast');
    const toast = new bootstrap.Toast(toastEl, {delay: 4000});
    toast.show();
});