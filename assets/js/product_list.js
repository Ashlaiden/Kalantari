// var products = document.getElementsByClassName('item');

// for (let index = 0; index < products.length + 1; index++) {
//     // const item = products[index];
//     products[index].addEventListener('mouseenter', function () {
//         const item = products[index];
//         const cover = item.children[0];
//         const hover = item.children[1];
//         cover.style.transition = 'opacity 0.3s ease-in-out';
//         hover.style.transition = 'opacity 0.3s ease-in-out';
//         hover.style.opacity = 0;

//         cover.style.opacity = 0;
//         // cover.style.visibility = 0;
//         // cover.classList.remove('covered')
//         // cover.classList.add('hovered')
//         setTimeout(function() {
//             cover.classList.add('hidden');
//             hover.classList.remove('hidden');
//             // hover.style.opacity = 0;
//         }, 300); // Delay of 300ms
//         hover.style.opacity = 1;
//         // hover.classList.remove('hovered')
//         // hover.classList.add('covered')
//         // hover.style.visibility = 1;
//     });

//     products[index].addEventListener('mouseleave', function () {
//         const item = products[index];
//         const cover = item.children[0];
//         const hover = item.children[1];
//         cover.style.transition = 'opacity 0.3s ease-in-out';
//         hover.style.transition = 'opacity 0.3s ease-in-out';
//         cover.style.opacity = 0;
//         hover.style.opacity = 1;

//         hover.style.opacity = 0;
//         // cover.style.visibility = 1;
//         // hover.classList.remove('covered')
//         // hover.classList.add('hovered')
//         setTimeout(function() {
//             hover.classList.add('hidden')
//             cover.classList.remove('hidden')
//             // cover.style.opacity = 0;
//         }, 300); // Delay of 300ms
//         // cover.classList.remove('hovered')
//         cover.style.opacity = 1;
//         // cover.classList.add('covered')
//         // hover.style.visibility = 0;
//     });
// }

// -----------------------------------------

// var products = document.getElementsByClassName('item');

// for (let index = 0; index < products.length; index++) {
//     const item = products[index];
//     // Assuming the first child is the cover and the second is the hover image
//     const cover = item.children[0];
//     const hover = item.children[1];

//     // Set initial styles for transition
//     cover.style.transition = 'opacity 0.3s ease-in-out';
//     hover.style.transition = 'opacity 0.3s ease-in-out';
//     hover.style.opacity = 0; // Start with the hover image invisible

//     item.addEventListener('mouseenter', function () {
//         // Assuming the first child is the cover and the second is the hover image
//         const cover = item.children[0];
//         const hover = item.children[1];

//         // Set initial styles for transition
//         cover.style.transition = 'opacity 0.3s ease-in-out';
//         hover.style.transition = 'opacity 0.3s ease-in-out';
//         hover.style.opacity = 0; // Start with the hover image invisible

//         cover.style.opacity = 0;
//         // cover.classList.add('hidden')
//         // hover.classList.remove('hidden')
//         hover.style.opacity = 1;
//     });

//     item.addEventListener('mouseleave', function () {
//         // Assuming the first child is the cover and the second is the hover image
//         const cover = item.children[0];
//         const hover = item.children[1];

//         // Set initial styles for transition
//         cover.style.transition = 'opacity 0.3s ease-in-out';
//         hover.style.transition = 'opacity 0.3s ease-in-out';
//         hover.style.opacity = 0; // Start with the hover image invisible

//         cover.style.opacity = 1;
//         // cover.classList.remove('hidden')
//         // hover.classList.add('hidden')
//         hover.style.opacity = 0;
//     });
// }
// -------------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', (event) => {
    // Get all the elements with the class 'product-item'
    const productItems = document.querySelectorAll('.item');
  
    // Add mouseover and mouseout event listeners to each product item
    productItems.forEach(item => {
        var dualimage = item.getAttribute('dual-image');

        if(dualimage && dualimage === 'true') {
            item.addEventListener('mouseenter', () => {
              // When the mouse is over the item, hide the cover image and show the hover image
              item.querySelector('.cover-image').style.opacity = '0';
              // item.querySelector('.cover-image').style.transform = 'rotateY(-180deg)';
              // item.querySelector('.hover-image').style.transform = 'rotateY(0deg)';
              item.querySelector('.hover-image').style.opacity = '1';
            });
        
            item.addEventListener('mouseleave', () => {
              // When the mouse is no longer over the item, show the cover image and hide the hover image
              item.querySelector('.cover-image').style.opacity = '1';
              // item.querySelector('.hover-image').style.transform = 'rotateY(-180deg)';
              // item.querySelector('.cover-image').style.transform = 'rotateY(0deg)';
              item.querySelector('.hover-image').style.opacity = '0';
            });
        }
    });
  });
function active_items_listener() {
  document.querySelectorAll('.item-link').forEach(function(link) {
    link.addEventListener('click', function(event) {
      if (event.target.parentElement.tagName.toLowerCase() === 'button') {
        copy_to_clipboard(this.href);
        event.preventDefault();
        event.stopPropagation();
      } else {
        event.preventDefault();
      }
    });
  });
}
active_items_listener();