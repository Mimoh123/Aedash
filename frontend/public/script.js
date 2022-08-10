'use strict';

const sun = document.querySelector('.sun');
const moon  = document.querySelector('.moon')
const doc = document.getElementsByTagName('body')[0]

const userTheme = localStorage.getItem("theme")

const iconToggle = () => {
    moon.classList.toggle('hidden');
    sun.classList.toggle('hidden');
}

const themeCheck = () => {
    if (userTheme === 'dark' || (!userTheme)){
        document.documentElement.classList.add('dark')
        localStorage.setItem("theme","dark");
        moon.classList.add('hidden');
        return;
    }else{
        sun.classList.add('hidden')
    }
}


const themeSwitch = () => {
    if (document.documentElement.classList.contains("dark")){
        document.documentElement.classList.remove("dark")
        localStorage.setItem("theme","light");
        iconToggle();
        return;
    }else{
    document.documentElement.classList.add("dark")
    localStorage.setItem("theme",'dark')
    iconToggle();
    }
}

//call theme switch on click
sun.addEventListener('click',function() {
    themeSwitch();
})
moon.addEventListener('click',function() {
    themeSwitch();
})
themeCheck();

const toggler = document.querySelectorAll('.toggle')
const sidebar = document.querySelector('.sidebar-container')
const searchToggle = document.querySelector('.search-toggle')
const sidebarSearch = document.querySelector('.sidebar-search')
const foc_elem = document.querySelector('.focus')

console.log(toggler)
toggler.forEach((elem)=> {
    elem.addEventListener('click',() =>{
        console.log('click')
        sidebar.classList.toggle('hidden')
    })
})
searchToggle.addEventListener('click',()=>{
        foc_elem.focus()
        sidebar.classList.toggle('hidden')
    })
