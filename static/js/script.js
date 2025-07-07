// Confirm before deleting a file
function confirmDelete(filename) {
    const confirmDelete = confirm(`Are you sure you want to delete "${filename}"?`);
    if (confirmDelete) {
        window.location.href = `/delete/${filename}`;
    }
}

// Toast message on file upload (if added in backend later)
document.addEventListener("DOMContentLoaded", () => {
    const toast = document.getElementById("toast-message");
    if (toast) {
        toast.classList.add("show");
        setTimeout(() => {
            toast.classList.remove("show");
        }, 3000);
    }
});

// Optional: Toggle dark/light mode
function toggleTheme() {
    document.body.classList.toggle("light-theme");
}

// Smooth scroll for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
