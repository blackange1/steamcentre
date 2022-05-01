//render menu
// document.getElementById('mainMenu').innerHTML = menu

//render footer
// document.getElementById('mainFooter').innerHTML = footer

//render scrollUp
document.getElementById('body').innerHTML += `
    <a href="#mainMenu" id="scroll__up" class="scroll__up" uk-scroll>
        <div  uk-icon="icon: chevron-up; ratio: 1.5" ></div>
    </a>
    `

let scrollUp = document.getElementById("scroll__up")
let isShow = false
setInterval(() => {
    if (window.scrollY > 1500) {
        if (!isShow) {
            scrollUp.classList.add("show-scroll_up")
            isShow = true
        }
    } else {
        if (isShow) {
            scrollUp.classList.remove("show-scroll_up")
            isShow = false
        }
    }
}, 1000);


// render footerYear
function renderYear() {
    let footerEnd = document.getElementById('year');
    let date = new Date();
    footerEnd.innerText = '2020 - ' + date.getFullYear().toString();
}

renderYear()

//menu
let subMenuHeadline = document.getElementsByClassName('sub_menu_headline')
for (let el of subMenuHeadline) {
    el.onclick = function () {
        el.nextElementSibling.classList.toggle('visible')
    }
}

