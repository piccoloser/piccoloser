function yearsSince(x) {
    let date = new Date(x);
    let cDate = Date.now();
    
    let mDiff = cDate - date.getTime();
    let ageDate = new Date(mDiff);
    let year = ageDate.getUTCFullYear();
    
    return year - 1970;
}

function topLinks() {
    for (const link of document.querySelectorAll(".top-link")) {
        link.innerHTML = "\u21a5"
        link.addEventListener("click", () => {
            window.scrollTo(0, 0);
            history.pushState(
                "",
                document.title,
                window.location.pathname
                + window.location.search
            );
        });
    }
}   

function closeMessageLinks() {
    for (const link of document.querySelectorAll(".message-close")) {
        link.addEventListener("click", () => {
            link.parentElement.style.display = "none";
        });
    }
}

function toggleNavigation() {
    let nav = document.getElementById("toggle-nav-button");

    
}

const vars = {
    myAge: yearsSince("10/30/1999"),
    yearsCoding: yearsSince("4/1/2012"),
};

for (const k of Object.keys(vars)) {
    for (const item of document.getElementsByClassName(k)) {
        item.innerHTML = vars[k];
    }
}

topLinks();
closeMessageLinks();