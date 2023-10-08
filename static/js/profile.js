let profileBtn = document.querySelector(".profile_btn");
let profileDetails = document.querySelector(".profile_details");
let downIcon = document.querySelector(".profile_icon");

profileBtn.addEventListener("click", () => {
  profileDetails.classList.toggle("profileNone");
  profileBtn.classList.toggle("profileRadius");
  if (downIcon.classList.contains("fa-chevron-down")) {
    downIcon.classList.remove("fa-chevron-down");
    downIcon.classList.add("fa-chevron-up");
  } else {
    downIcon.classList.remove("fa-chevron-up");
    downIcon.classList.add("fa-chevron-down");
  }
});
