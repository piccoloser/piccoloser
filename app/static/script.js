function yearsSince(x) {
    let date = new Date(x);
    let cDate = Date.now();
    
    let mDiff = cDate - date.getTime();
    let ageDate = new Date(mDiff);
    let year = ageDate.getUTCFullYear();
    
    return year - 1970;
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