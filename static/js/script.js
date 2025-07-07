// ===== Notes Manager JS =====

// ✅ Show a success flash message temporarily
function showFlashMessage(message) {
    const flash = document.createElement("div");
    flash.className = "flash";
    flash.innerText = message;
    document.body.appendChild(flash);

    setTimeout(() => {
        flash.remove();
    }, 2500);
}

// ✅ Confirm before deleting a task
function confirmDelete(taskName) {
    return confirm(`Are you sure you want to delete "${taskName}"?`);
}

// ✅ Animate splash fade-out (optional)
document.addEventListener('DOMContentLoaded', function () {
    const splash = document.querySelector('.splash');
    if (splash) {
        setTimeout(() => {
            splash.classList.add('fade-out');
        }, 2000);
    }
});
