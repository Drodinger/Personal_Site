c:q
onst hamburgerButton = document.querySelector(".hamburger-menu-button");
const navMenu = document.querySelector(".nav-menu");
const navLinkAboutMe = document.getElementById("nav-about-me");
const navLinkSkills = document.getElementById("nav-skills");
const navLinkProjects = document.getElementById("nav-projects");
const navLinkExperience = document.getElementById("nav-experience");
const navLinkEducation = document.getElementById("nav-education");
const navLinkHobbies = document.getElementById("nav-hobbies");

const toggleMobileNavMenu = () => {
   navMenu.classList.toggle("active"); 
}

hamburgerButton.addEventListener("click", toggleMobileNavMenu);
navLinkAboutMe.addEventListener("click", toggleMobileNavMenu);
navLinkSkills.addEventListener("click", toggleMobileNavMenu);
navLinkProjects.addEventListener("click", toggleMobileNavMenu);
navLinkExperience.addEventListener("click", toggleMobileNavMenu);
navLinkEducation.addEventListener("click", toggleMobileNavMenu);
navLinkHobbies.addEventListener("click", toggleMobileNavMenu);
