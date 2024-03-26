
// window.onscroll = function() {
//     var detail = document.getElementById('detail');
//     var footer = document.getElementById('footer');
//     var offset = footer.offsetTop - window.innerHeight;
  
//     if (window.pageYOffset > offset) {
//         detail.style.position = 'absolute';
//         detail.style.bottom = '0px';
//         detail.style.left = '0px';
//         detail.style.width = '100%';
//     } else {
//         detail.style.position = 'fixed';
//         detail.style.width = '50%';
//     }
// };

// window.addEventListener('scroll', function() {
//     var detail = document.getElementById('detail');
//     var footer = document.getElementById('footer');
//     var offset = footer.offsetTop - window.innerHeight;
//     var bottom = footer.offsetTop 
  
//     if (window.pageYOffset > offset) {
//         detail.style.position = 'absolute';
//         detail.style.bottom = '0px';
//         detail.style.left = '0px';
//         detail.style.width = '100%';
//     } else {
//         detail.style.position = 'fixed';
//         detail.style.width = '50%';
//     }
// });

// function _updateDetailStyle() {
//     var detail = document.getElementById('detail');
//     var footer = document.getElementById('footer');
//     var offset = footer.offsetTop - window.innerHeight;
//     // var space = footer.offsetTop - (window.scrollY + window.innerHeight);

//     // Get the element you want to measure
//     var detailContainer = document.getElementById('detail-container');
//     // Get the dimensions of the element
//     var detailContainerRect = detailContainer.getBoundingClientRect();
//     // Get the dimensions of the viewport
//     var viewportHeight = window.innerHeight || document.documentElement.clientHeight;
//     // Calculate the space between the element and the bottom edge of the viewport
//     var spaceToBottom = viewportHeight - detailContainerRect.bottom;
//     if (spaceToBottom < 0) {
//         spaceToBottom = Math.abs(spaceToBottom);
//     }
  
//     if (window.pageYOffset > offset) {
//         detail.style.bottom = '0px';
//         detail.style.left = '0px';
//     } else {
//         detail.style.bottom = spaceToBottom + 'px';
//     }
// }

// function updateDetailStyle() {
//     var detail = document.getElementById('detail');
//     var footer = document.getElementById('footer');
//     var offset = footer.offsetTop - window.innerHeight;
//     var bottom = footer.offsetTop 
//     var top = footer.offsetTop - window.InputEvent + 80
  
//     if (window.pageYOffset >= offset) {
//         detail.style.position = 'absolute';
//         detail.style.top = top + 'px';
//         // detail.classList.add('static');
//         // detail.style.position = 'absolute';
//         // detail.style.bottom = '0px';
//         // detail.style.left = '0px';
//         // detail.style.width = '100%';
//     } else {
//         detail.style.position = 'fixed';
//         detail.style.bottom = '0px';
//         detail.style.left = '0px';
//         detail.style.width = '50%';
//         // detail.classList.remove('static');
//         // detail.style.position = 'fixed';
//         // detail.style.width = '50%';
//     }
// }

// // Initial check on page load
// updateDetailStyle();
// window.addEventListener("wheel", updateDetailStyle);
// window.addEventListener("scroll", updateDetailStyle);



// window.addEventListener("scroll", function() {
// // Get the element you want to measure
// var element = document.getElementById('detail-container');

// // Get the dimensions of the element
// var elementRect = element.getBoundingClientRect();

// // Get the dimensions of the viewport
// var viewportHeight = window.innerHeight || document.documentElement.clientHeight;

// // Calculate the space between the element and the bottom edge of the viewport
// var spaceToBottom = viewportHeight - elementRect.bottom;

// if (spaceToBottom < 0) {
//     spaceToBottom = Math.abs(spaceToBottom);
// }

// // Output the results
// console.log('Space to bottom:', spaceToBottom, 'px');
// });



// // Define the range of heights where you want to slow down scrolling
// var startHeight = document.getElementById('footer').offsetTop - 50;
// var endHeight = document.getElementById('footer').offsetTop + 50;

// // Define the scrolling speed adjustment factor within the range
// var scrollSpeedFactor = 0.05; // Adjust this value as needed (lower values slow down scrolling more)

// // Add a scroll event listener to the window
// window.addEventListener('scroll', function() {
//     // Get the current scroll position
//     var scrollTop = window.scrollY || window.pageYOffset;

//     // Check if the current scroll position is within the specified range
//     if (scrollTop >= startHeight && scrollTop <= endHeight) {
//         // Adjust the scrolling speed within the specified range
//         window.scrollTo(0, scrollTop + scrollSpeedFactor); // Increase or decrease the second argument to control the scrolling speed
//     }
// });











// // Function to animate scrolling
// function smoothScroll(startY, endY, duration) {
//     const startTime = performance.now();
  
//     function scroll() {
//       const currentTime = performance.now();
//       const timeElapsed = currentTime - startTime;
//       const progress = Math.min(timeElapsed / duration, 1);
  
//       // Calculate the current position using an easing function
//       const position = startY + (endY - startY) * easeInOutQuad(progress);
  
//       window.scrollTo(0, position);
  
//       if (timeElapsed < duration) {
//         requestAnimationFrame(scroll);
//       }
//     }
  
//     scroll();
//   }
  
//   // Easing function for a smooth effect
//   function easeInOutQuad(t) {
//     return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
//   }
  
//   // Usage example: Scroll from 500px to 1000px over 3 seconds
//   smoothScroll(document.getElementById('footer') - 100, document.getElementById('footer') + 100, 4000);
  