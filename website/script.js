const btn = document.getElementById("theme-btn");
btn.addEventListener("click", function () {
    document.body.classList.toggle("dark");
});

document.getElementById("copytext").addEventListener("click", () => writeClipboardText("git.euler2718@gmail.com"));

async function writeClipboardText(text) {
    try {
        await navigator.clipboard.writeText(text);
    } catch (error) {
        console.error(error.message);
    }
}