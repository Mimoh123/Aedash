"use strict";

const sun = document.querySelector(".sun");
const moon = document.querySelector(".moon");
const doc = document.getElementsByTagName("body")[0];

const userTheme = localStorage.getItem("theme");

const iconToggle = () => {
  moon.classList.toggle("hidden");
  sun.classList.toggle("hidden");
};

const themeCheck = () => {
  if (userTheme === "dark" || !userTheme) {
    document.documentElement.classList.add("dark");
    localStorage.setItem("theme", "dark");
    moon.classList.add("hidden");
    return;
  } else {
    sun.classList.add("hidden");
  }
};

const themeSwitch = () => {
  if (document.documentElement.classList.contains("dark")) {
    document.documentElement.classList.remove("dark");
    localStorage.setItem("theme", "light");
    iconToggle();
    return;
  } else {
    document.documentElement.classList.add("dark");
    localStorage.setItem("theme", "dark");
    iconToggle();
  }
};

//call theme switch on click
sun.addEventListener("click", function () {
  themeSwitch();
});
moon.addEventListener("click", function () {
  themeSwitch();
});
themeCheck();

const toggler = document.querySelectorAll(".toggle");
const sidebar = document.querySelector(".sidebar-container");
const searchToggle = document.querySelector(".search-toggle");
const sidebarSearch = document.querySelector(".sidebar-search");
const foc_elem = document.querySelector(".focus");

toggler.forEach((elem) => {
  elem.addEventListener("click", () => {
    sidebar.classList.toggle("hidden");
  });
});
searchToggle.addEventListener("click", () => {
  foc_elem.focus();
  sidebar.classList.toggle("hidden");
});
// live search
// live search
// live search
// live search

const search = `{&#x27;Python for Everybody&#x27;: &#x27;/2022/8/12/python-for-everybody/&#x27;, &#x27;This is an advanced post by aadarsh&#x27;: &#x27;/2022/8/12/this-is-an-advanced-post-by-aadarsh/&#x27;, &#x27;Captain America&#x27;: &#x27;/2022/8/9/captain-america/&#x27;, &#x27;Thor Ragnarok&#x27;: &#x27;/2022/8/9/thor-ragnarok/&#x27;, &#x27;Loki season 2&#x27;: &#x27;/2022/7/26/loki-season-2/&#x27;, &#x27;Iron Man&#x27;: &#x27;/2022/7/26/iron-man/&#x27;, &#x27;Youtube first blog page&#x27;: &#x27;/2022/7/26/youtube-first-blog-page/&#x27;, &#x27;This is the second post in the page&#x27;: &#x27;/2022/7/26/this-is-the-second-post-in-the-page/&#x27;}`;

const data = search;

const dt = JSON.parse(data.replace(/&#x27;/g, '"'));
const d = JSON.stringify(dt);

const rdata = Object.keys(dt);

const input = document.querySelectorAll("#search_here");

const box = document.querySelectorAll(".s-results");

let filteredArr = [];
input.forEach((input_elem) => {
  input_elem.addEventListener("keyup", (e) => {
    document.querySelector(".overlay").style.display = "block";
    box.forEach((box_elem) => {
      box_elem.innerHTML = "";
      filteredArr = rdata.filter((elem) =>
        elem.toLowerCase().includes(e.target.value.toLowerCase())
      );
      box_elem.classList.remove("hidden");

      if (filteredArr.length > 0) {
        for (let i = 0; i < 6; i++) {
          box_elem.innerHTML += `<a href=${
            dt[filteredArr[i]]
          }><p class= ' searchList dark:text-white text-white  p-2'  style = "">${
            filteredArr[i].slice(0, 25) + "..."
          }</p></a>`;
        }
      } else {
        box_elem.innerHTML = `<p class= 'searchList dark:text-white text-white0 p-2'  >No result</p>`;
      }
    });
  });
});
const doc_e = document.documentElement;
doc_e.addEventListener("click", function (e) {
  box.forEach((elem) => {
    elem.classList.add("hidden");
    document.querySelector(".overlay").style.display = "none";
  });
});

const search_item = document.querySelectorAll(".search_item");
console.log(search_item);
search_item.forEach(function (elem) {
  elem.addEventListener("click", function () {
    console.log(search_item);
  });
});

// const replyBtn = document.querySelectorAll('.reply-btn')
// const cancelBtn = document.querySelectorAll('.cancel-btn');
// const replyBox = document.querySelector('')

// replyBtn.forEach(function(elem){
//   elem.addEventListener('click',function(){
//     console.log(this)
   
//   })
// })
const replyBtn = document.querySelectorAll(".reply-btn");
const cancelBtn = document.querySelectorAll(".cancel-btn");
const allReplies = document.querySelectorAll(".view-reply");
const allRepliesBox = document.querySelector(".all-replies-box");

const replyBox = document.querySelectorAll(".reply-form");

replyBtn.forEach(function (elem) {
  elem.addEventListener("click", function () {
    // this.parentElement.lastElementChild.classList.remove('hidden')
    this.nextElementSibling.firstElementChild.classList.remove("hidden");
    elem.classList.add("hidden");
    cancelBtn.forEach(function (elem1) {
      elem1.classList.remove("hidden");
    });
  });
});

cancelBtn.forEach(function (elem3) {
  elem3.addEventListener("click", function () {
    // this.parentElement.lastElementChild.classList.add('hidden')
    elem3.classList.add("hidden");
    this.classList.add("hidden");
    replyBox.forEach(function (elem4) {
      elem4.classList.add("hidden");
      replyBtn.forEach(function (elem) {
        elem.classList.remove("hidden");
      });
    });

    //this.parentElement.firstElementChild.classList.remove('hidden')

    //Reply btn
    this.parentElement.parentElement.parentElement.parentElement.parentElement.firstElementChild.classList.remove(
      "hidden"
    );
  });
});
allReplies.forEach(function (elem) {
  elem.addEventListener("click", function () {
    console.log(elem.nextElementSibling);
    elem.nextElementSibling.classList.toggle("hidden");
  });
});