// calculate how long it's been since a date
function yearsSince(x) {
    let date = new Date(x);
    let cDate = Date.now();
    
    let mDiff = cDate - date.getTime();
    let ageDate = new Date(mDiff);
    let year = ageDate.getUTCFullYear();
    
    return year - 1970;
}

// add scroll-to-top function to top links
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

// add close button (x) to flash messages
function closeMessageLinks() {
    for (const link of document.querySelectorAll(".message-close")) {
        link.addEventListener("click", () => {
            link.parentElement.style.display = "none";
        });
    }
}

// toggle navigation menu height (mobile)
function toggleNavigation() {
    let nav = document.getElementById("site-navigation");

    if (nav.style.height.search("0") >= 0 || nav.style.height == "") {
        nav.style.height = "3rem";
    } else {
        nav.style.height = "0";
    }
}

// used in yearsSince
const vars = {
    myAge: yearsSince("10/30/1999"),
    yearsCoding: yearsSince("4/1/2012"),
};

// auto-fills specified items with value from yearsSince(var)
for (const k of Object.keys(vars)) {
    for (const item of document.getElementsByClassName(k)) {
        item.innerHTML = vars[k];
    }
}

// add padding for mobile toggle-nav-button
function toggleNavButtonPadding() {
    if (document.body.scrollHeight > window.innerHeight) {
        document.body.style.paddingBottom = "65px";
    } else {
        document.body.style.paddingBottom = "0";
    }
}

// make sure site-navigation is lined up correctly
function alignSiteNavigation() {
    if (window.innerWidth >= 685) {
        document.getElementById("site-navigation")
            .style.height = "3rem";
    } else {
        document.getElementById("site-navigation")
            .style.height = "0";
    }
}

// make sure everything is lined up as the user resizes their browser
window.addEventListener("resize", () => {
    alignSiteNavigation()
    toggleNavButtonPadding()
});


// make sure everything is lined up when the page loads
window.addEventListener("load", () => {
    toggleNavButtonPadding()
});

topLinks();
closeMessageLinks();