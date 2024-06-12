let switchMode = document.getElementById("switchMode")

switchMode.onclick = function() {
    let theme = document.getElementById("theme");

    if (theme.getAttribute("href") === "vendor/css/products.css") {
        theme.href =  "vendor/css/dark-mode.css";
    } else {
        theme.href =  "vendor/css/products.css";
    }
}