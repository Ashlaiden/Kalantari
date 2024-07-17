class CartClass {
    constructor(order) {
      this.order = order;
      this.created = new Date().getTime();
      this.AddItemURL = '/cart/item/add/';
      this.ChangeCountURL = '/cart/change/count/';
      this.DeleteItemURL = '/cart/item/delete/';
    }
    add() {
        const add_url = this.AddItemURL;
        // this.csrfmiddlewaretoken = document.getElementById('add-to-cart').children.namedItem('csrfmiddlewaretoken').value;
        const fd = new FormData();
        fd.append('csrfmiddlewaretoken', this.csrfmiddlewaretoken);
        fd.append('uid', this.uid);
        axios.post(add_url, fd)
        .then(response => {
            if (response.data.status === 'ok') {
              document.getElementById('add-to-cart').classList.add('hidden');
              if (response.data.full === 'true') {
                document.getElementById('product-cart-stat').insertAdjacentHTML('afterend', 
                `<div id="in-cart-container" class="in-cart-container">
                <div id="in-cart" class="in-cart">
                    <button type="button" id="decrease-or-delete" onclick="cart.delete()" class="in-cart-delete"><i class="fa-solid fa-trash-can"></i></button>
                    <div class="count">
                        <section id="count">1</section>
                        <span id="full">حداکثر</span>
                    </div>
                    <button type="button" id="increase disabled" onclick="cart.increase()">+</button>
                </div>
            </div>`
                );
              } else {
                document.getElementById('product-cart-stat').insertAdjacentHTML('afterend', 
                `<div id="in-cart-container" class="in-cart-container">
                <div id="in-cart" class="in-cart">
                    <button type="button" id="decrease-or-delete" onclick="cart.delete()" class="in-cart-delete"><i class="fa-solid fa-trash-can"></i></button>
                    <div class="count">
                        <section id="count">1</section>
                    </div>
                    <button type="button" id="increase" onclick="cart.increase()">+</button>
                </div>
            </div>`
                );
              }
              document.getElementById('product-cart-stat').remove();
              if (document.getElementById('cart-menu-empty')) {
                document.getElementById('cart-menu-empty').remove();
              }
              var d = response.data.detail
              document.getElementById('cart-user-menu-section-list').insertAdjacentHTML('beforeend', 
              `<li id="menu-${d.uid}" class="menu-cart-item">
              <a href="${d.product_url}" style="text-decoration: none; color: inherit">
                  <img src="${d.image_url}" alt="${d.title}">
              </a>
              <span>${d.title}</span>
              <span id="cart-menu-count-${d.uid}">${d.count}</span>
              <span>${d.price}</span>
              <form id="form-menu-${d.uid}" action="">
                  <input name="csrfmiddlewaretoken" type="hidden" value="${this.csrfmiddlewaretoken}"/>
                  <button type="button" name="delete-item" onclick="removeitemfromcart(${d.uid})"><i class="fa-solid fa-xmark"></i></button>
              </form>
          </li>`
              );
            }
            document.getElementById('continue-in-cart').classList.remove('disabled');
            update_order_info()
          })
          .catch(error => {
            Loger.ServerError();
          });
      }
    increase() {
      const increase_url = this.ChangeCountURL;
      // this.csrfmiddlewaretoken = document.getElementById(`increase-${id}`).children.namedItem('csrfmiddlewaretoken').value;
      const fd = new FormData();
      fd.append('csrfmiddlewaretoken', this.csrfmiddlewaretoken);
      fd.append('uid', this.uid);
      fd.append('action', '+');
      axios.post(increase_url, fd)
      .then(response => {

          if (response.data.status === 'ok') {
            document.getElementById(`decrease-or-delete`).classList.remove('in-cart-delete');
            document.getElementById(`decrease-or-delete`).innerHTML = '-';
            document.getElementById(`decrease-or-delete`).onclick = cart.decrease.bind(this);
            if (response.data.max === 'true') {
              document.getElementById('count').insertAdjacentHTML('afterend', '<span id="max">حداکثر</span>')
              document.getElementById('increase').classList.add('disabled');
            }
            document.getElementById(`count`).innerText = response.data.count;
            document.getElementById(`cart-menu-count-${response.data.detail.uid}`).innerHTML = response.data.count;
          }
          update_order_info()
        })
        .catch(error => {
          Loger.ServerError();
        });
    }
    decrease() {
      const decrease_url = this.ChangeCountURL;
      // this.csrfmiddlewaretoken = document.getElementById(`decrease-${id}`).children.namedItem('csrfmiddlewaretoken').value;
      const fd = new FormData();
      fd.append('csrfmiddlewaretoken', this.csrfmiddlewaretoken);
      fd.append('uid', this.uid);
      fd.append('action', '-');
      axios.post(decrease_url, fd)
      .then(response => {
          if (response.data.status === 'ok') {
            if (response.data.count == 1) {
              document.getElementById(`decrease-or-delete`).classList.add('in-cart-delete');
              document.getElementById(`decrease-or-delete`).innerHTML = '<i class="fa-solid fa-trash-can"></i>';
              document.getElementById(`decrease-or-delete`).onclick = this.delete.bind(this);
              if (response.data.max === 'false' && document.getElementById('max')) {
                document.getElementById('max').remove();
              }
            }
            document.getElementById('increase').classList.remove('disabled');
            // document.getElementById('full').remove();
            document.getElementById(`count`).innerText = response.data.count;
            document.getElementById(`cart-menu-count-${response.data.detail.uid}`).innerHTML = response.data.count;
            if (response.data.max === 'false' && document.getElementById('max')) {
              document.getElementById('max').remove();
            }
          }
          update_order_info()
        })
        .catch(error => {
          Loger.ServerError();
        });
    }
    delete() {
      const delete_item_url = this.DeleteItemURL;
      // this.csrfmiddlewaretoken = document.getElementById(`delete-${id}`).children.namedItem('csrfmiddlewaretoken').value;
      const fd = new FormData();
      fd.append('csrfmiddlewaretoken', this.csrfmiddlewaretoken);
      fd.append('uid', this.uid);
      axios.post(delete_item_url, fd)
      .then(response => {
          if (response.data.status === 'ok') {
            document.getElementById('in-cart-container').remove();
            document.getElementById('prop').insertAdjacentHTML('afterend', 
              `<div id="product-cart-stat" class="button">
                <form id="add-to-cart">
                  <button class="add-to-order-btn" onclick="cart.add()" type="button" onclick="cart.add()">افزودن به سبد خرید</button>
                </form>
              </div>`
            );
            document.getElementById(`menu-${response.data.detail.uid}`).remove();
            var cartList = document.getElementById('cart-user-menu-section-list')
            if (cartList.children.length === 0) {
              cartList.innerHTML = '<li id="cart-menu-empty" class="nothing">هیچ کالایی در سبد خرید شما وجود ندارد.</li>';
              document.getElementById('continue-in-cart').classList.add('disabled');
            }
          }
          update_order_info()
        })
        .catch(error => {
          Loger.ServerError();
        });
    }
}
// ----------------------------------------------
const cart = new CartClass('create');
var detail_page = true;

function book_mark() {
  const url = '/favorite/bookmark/';
  const fd = new FormData();
  fd.append('csrfmiddlewaretoken', cart.csrfmiddlewaretoken);
  fd.append('uid', cart.uid);
  axios.post(url, fd)
  .then(response => {
    if (response.data.status === 'ok') {
      var bookmark = document.getElementById('bookmark');
      if (response.data.message === 'added') {
        bookmark.classList.remove('fa-regular');
        bookmark.classList.add('fa-solid');
        var data = response.data.detail
        if (document.getElementById('favorite-menu-empty')) {
          document.getElementById('favorite-menu-empty').remove();
          document.getElementById('all-favorites').classList.remove('disabled');
        }
        document.getElementById('favorite-user-menu-section-list').insertAdjacentHTML('beforeend', 
          `<li id="menu-favorite-${data.uid}" class="menu-favorite-item">
          <a href="${data.product_url}" style="text-decoration: none; color: inherit;display: flex;flex-direction: row;">
              <img src="${data.image_url}" alt="${data.title}">
              <section class="item-menu-des">
                  <span>${data.title}</span>
                  <div class="item-uid">کد کالا: ${data.uid}</div>
              </section>
          </a>
          <button type="button" name="delete-item" onclick="book_mark()"><i class="fa-solid fa-xmark"></i></button>
      </li>`
        )
      } else if (response.data.message === 'removed') {
        bookmark.classList.remove('fa-solid');
        bookmark.classList.add('fa-regular');
        document.getElementById(`menu-favorite-${cart.uid}`).remove();
        if (document.getElementById('favorite-user-menu-section-list').children.length === 0) {
          document.getElementById('favorite-user-menu-section-list').innerHTML = '<li id="favorite-menu-empty" class="nothing">هیچ کالایی در علاقه مندی ها وجود ندار.</li>';
          document.getElementById('all-favorites').classList.add('disabled');
        }
      }
    }
  })
  .catch(error => {
    Loger.ServerError();
  });
}


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
  