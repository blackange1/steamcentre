document.addEventListener('DOMContentLoaded', function(){
    const print = (obj) => {
        console.log(obj)
    }

    let elementBody = document.getElementById('body');
    let a = document.createElement('a');
    a.id = 'scroll__up'
    a.href = '#body'
    a.classList = 'scroll__up'
    a.setAttribute('uk-scroll', '')

    let div = document.createElement('div')
    div.setAttribute('uk-icon', 'icon: chevron-up; ratio: 1.5')
    
    a.appendChild(div)
    elementBody.appendChild(a)

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

//    // render footerYear
   function renderYear() {
   let footerEnd = document.getElementById('year');
   let date = new Date();
   footerEnd.innerText = '2020 - ' + date.getFullYear().toString();
   }

   renderYear()

//    //menu
//    let subMenuHeadline = document.getElementsByClassName('sub_menu_headline')
//    for (let el of subMenuHeadline) {
//    el.onclick = function () {
//        el.nextElementSibling.classList.toggle('visible')
//    }
//    }
// alert(document.getElementById('body'))
}, false);
