// Show loading animation when the page starts loading
document.addEventListener('DOMContentLoaded', function () {
    showLoadingAnimation();
  });
  
  // Function to show the loading animation
  function showLoadingAnimation() {
    const preloader = document.getElementById("preloader");
    preloader.classList.remove("hide-preloader");  
  }
  
  // Function to hide the loading animation
  function hideLoadingAnimation() {
    const preloader = document.getElementById("preloader");
    preloader.classList.add("hide-preloader");  
  }
  
  // Example: Hide loading animation after some process (e.g., after content is loaded)
  // You can call hideLoadingAnimation() at the end of your asynchronous process.
  // setTimeout is used as an example; replace it with your actual logic.
//   setTimeout(function () {
//     hideLoadingAnimation();
//   }, 2000); // Hide after 2 seconds (replace with your actual process time)
  
  window.addEventListener("load", function () {
    hideLoadingAnimation()     
  });


