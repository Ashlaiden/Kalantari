document.addEventListener("DOMContentLoaded", function () {
    var header = document.getElementById("main-header");
    var brand = document.getElementById('brand-name');

    // header.addEventListener("mouseover", function () {
    //     header.classList.add("header-hover");
    // });

    // header.addEventListener("mouseout", function () {
    //     header.classList.remove("header-hover");
    // });

    window.addEventListener("scroll", function () {
        if (window.scrollY > 5) {
            header.classList.add("header-hover");
            brand.classList.remove('brand-name');
        } else {
            header.classList.remove("header-hover");
            brand.classList.add('brand-name');
        }
    });

    function updateHeaderStyles() {
        if (window.scrollY > 5) {
            header.classList.add("header-hover");
            brand.classList.remove('brand-name');
        } else {
            header.classList.remove("header-hover");
            if (headerIsHovered) {
                brand.classList.remove('brand-name');
            } else {
                brand.classList.add('brand-name');
            }
        }
    }

    // Initial check on page load
    updateHeaderStyles();

    window.addEventListener("scroll", updateHeaderStyles);

});

// Get the element
var header = document.getElementById('main-header');
var brand = document.getElementById('brand-name');
var headerIsHovered = false;
// Add event listener for mouseenter (hover)
header.addEventListener('mouseenter', function() {
    headerIsHovered = true;
    brand.classList.remove('brand-name');
});
// Add event listener for mouseleave (unhover)
header.addEventListener('mouseleave', function() {
    headerIsHovered = false;
    if (window.scrollY > 1) {
        brand.classList.remove('brand-name');
    } else {
        brand.classList.add('brand-name');
    }
});
// -------------Menu---------------
document.getElementById('menu-btn').addEventListener('click', function () {
    var sidebar = document.getElementById('menu');
    var overlay = document.getElementById('overlay');

    if (sidebar.style.right !== '0px') {
        sidebar.style.right = '0';
        overlay.style.opacity = '1';
        overlay.style.visibility = 'visible';
    }
});
document.getElementById('overlay').addEventListener('click', function (event) {
    var sidebar = document.getElementById('menu');
    var overlay = document.getElementById('overlay');

    if (event.target !== sidebar && sidebar.style.right === '0px') {
        sidebar.style.right = '-300px';
        overlay.style.opacity = '0';
        overlay.style.visibility = 'hidden';
    }
});
document.getElementById('close-menu-btn').addEventListener('click', function (event) {
    var sidebar = document.getElementById('menu');
    var overlay = document.getElementById('overlay');

    if (sidebar.style.right === '0px') {
        sidebar.style.right = '-300px';
        overlay.style.opacity = '0';
        overlay.style.visibility = 'hidden';
      }
});
// -------------------------User Menu-----------------------------------
// Get all elements with the class "common-button"
var buttons = document.querySelectorAll('.user-menu-btn');

// Add a click event listener to each button
buttons.forEach(function(button) {
  button.addEventListener('click', function() {
    var user_menu = document.getElementById('user-menu');
    var overlay = document.getElementById('overlay');
    switch (button.getAttribute('id')) {
        case 'nav-account-btn':
            if (document.getElementById('cart-btn').classList.contains('section-btn-active'))
                document.getElementById('cart-btn').classList.remove('section-btn-active');
            if (document.getElementById('favorite-btn').classList.contains('section-btn-active'))
                document.getElementById('favorite-btn').classList.remove('section-btn-active');
            changeSectionContent('account');
            document.getElementById('account-btn').classList.add('section-btn-active');
            break;
        case 'nav-cart-btn':
            if (document.getElementById('account-btn').classList.contains('section-btn-active'))
                document.getElementById('account-btn').classList.remove('section-btn-active');
            if (document.getElementById('favorite-btn').classList.contains('section-btn-active'))
                document.getElementById('favorite-btn').classList.remove('section-btn-active');
            changeSectionContent('cart');
            document.getElementById('cart-btn').classList.add('section-btn-active');
            break;
        case 'nav-favorite-btn':
            if (document.getElementById('account-btn').classList.contains('section-btn-active'))
                document.getElementById('account-btn').classList.remove('section-btn-active');
            if (document.getElementById('cart-btn').classList.contains('section-btn-active'))
                document.getElementById('cart-btn').classList.remove('section-btn-active');
            changeSectionContent('favorite');
            document.getElementById('favorite-btn').classList.add('section-btn-active');
            break;
    }
    

    if (user_menu.style.left !== '0px') {
        user_menu.style.left = '0';
        overlay.style.opacity = '1';
        overlay.style.visibility = 'visible';
    }
  });
});
document.getElementById('overlay').addEventListener('click', function (event) {
    var user_menu = document.getElementById('user-menu');
    var overlay = document.getElementById('overlay');

    if (event.target !== user_menu && user_menu.style.left === '0px') {
        user_menu.style.left = '-500px';
        overlay.style.opacity = '0';
        overlay.style.visibility = 'hidden';
    }
});
document.getElementById('close-user-menu-btn').addEventListener('click', function (event) {
    var user_menu = document.getElementById('user-menu');
    var overlay = document.getElementById('overlay');

    if (user_menu.style.left === '0px') {
        user_menu.style.left = '-500px';
        overlay.style.opacity = '0';
        overlay.style.visibility = 'hidden';
      }
});
// -------------------user-menu-secton-content-------------------------
// Get all elements with the class "common-button"
// var buttons = document.querySelectorAll('.section-btn');

// Add a click event listener to each button
// buttons.forEach(function(button) {
//   button.addEventListener('click', function() {
//     var cart_btn = document.getElementById('cart-btn');
//     var cart = document.getElementById('cart');
//     var favorite_btn = document.getElementById('favortie-btn');
//     var favorite = document.getElementById('favorite');
//     var account_btn = document.getElementById('account-btn');
//     var account = document.getElementById('account');

//     switch (button.getAttribute('id')) {
//         case 'account-btn':
//             if (cart_btn.classList.contains('section-btn-active'))
//                 cart_btn.classList.remove('section-btn-active');
//             if (!cart.classList.contains('hidden'))
//                 cart.classList.add('hidden');
//             if (favorite_btn.classList.contains('section-btn-active'))
//                 favorite_btn.classList.remove('section-btn-active');
//             if (!favorite.classList.contains('hidden'))
//                 favorite.classList.add('hidden');
//             account_btn.classList.add('section-btn-active');
//             account.classList.remove('hidden');
//         case 'cart-btn':
//             if (account_btn.classList.contains('section-btn-active'))
//                 account.classList.remove('section-btn-active');
//             if (!account.classList.contains('hidden'))
//                 account.classList.add('hidden');
//             if (favorite_btn.classList.contains('section-btn-active'))
//                 favorite_btn.classList.remove('section-btn-active');
//             if (!favorite.classList.contains('hidden'))
//                 favorite.classList.add('hidden');
//             cart_btn.classList.add('section-btn-active');
//             cart.classList.remove('hidden');
//             break;
//         case 'favorite-btn':
//             if (cart_btn.classList.contains('section-btn-active'))
//                 cart_btn.classList.remove('section-btn-active');
//             if (!cart.classList.contains('hidden'))
//                 cart.classList.add('hidden');
//             if (account_btn.classList.contains('section-btn-active'))
//                 account_btn.classList.remove('section-btn-active');
//             if (!account.classList.contains('hidden'))
//                 account.classList.add('hidden');
//             favorite_btn.classList.add('section-btn-active');
//             favorite.classList.remove('hidden');
//             break;
//     }
//   });
// });

function changeSectionContent(sectionId) {
    var sections = ['cart', 'favorite', 'account'];
    var sections_btn = ['cart-btn', 'favorite-btn', 'account-btn'];
    
    // Hide all elements
    sections.forEach(function (el) {
        var currentSection = document.getElementById(el);
        if (currentSection) {
            currentSection.classList.add('hidden');
        }
    });
    sections_btn.forEach(function (el) {
        var currentSectioBtn = document.getElementById(el);
        if (currentSectioBtn) {
            if (currentSectioBtn.classList.contains('section-btn-active'))
                currentSectioBtn.classList.remove('section-btn-active');
        }
    });

    // Show the selected element
    var selectedSection = document.getElementById(sectionId);
    if (selectedSection) {
        event.target.classList.add('section-btn-active')
        selectedSection.classList.remove('hidden');
    }
}
// ---------------------update-order-info----------------------------
function update_order_info() {
    url = '/cart/order/info/'
    axios.get(url, {
    }).then(response => {
        document.getElementById('details-price').innerText = `${response.data.price} تومان`;
        document.getElementById('details-discount').innerText = `${response.data.discount} تومان`;
        document.getElementById('details-final-price').innerText = `${response.data.final_price} تومان`;
    }).catch(error => {
      Loger.ConnectionError();
    });
}
// ----------------------------------CART------------------------------------
function removeitemfromcart(id) {
    const delete_item_url = '/cart/item/delete/';
    csrfmiddlewaretoken = document.getElementById(`form-menu-${id}`).children.namedItem('csrfmiddlewaretoken').value;
    const fd = new FormData();
    fd.append('csrfmiddlewaretoken', csrfmiddlewaretoken)
    fd.append('uid', id)
    axios.post(delete_item_url, fd)
    .then(response => {
        update_order_info()
        if (response.data.status === 'ok') {
            document.getElementById(`menu-${id}`).remove();
            var cartList = document.getElementById('cart-user-menu-section-list')
            if (cartList.children.length === 0) {
                cartList.innerHTML = '<li id="cart-menu-empty" class="nothing">هیچ کالایی در سبد خرید شما وجود ندارد.</li>';
                document.getElementById('continue-in-cart').classList.add('disabled');
            }
            if (detail_page) {
                document.getElementById('in-cart-container').remove();
                document.getElementById('prop').insertAdjacentHTML('afterend', 
                `<div id="product-cart-stat" class="button">
                    <form id="add-to-cart">
                    <button class="add-to-order-btn" onclick="cart.add()" type="button" onclick="cart.add()">افزودن به سبد خرید</button>
                    </form>
                </div>`
                );
            }
        }
    })
    .catch(error => {
        // Handle errors
        Loger.ConnectionError();
    });
}
// ------------------------------Remobe-From-BookMark------------------------------------
function remove_book_mark(uid) {
    const url = '/favorite/bookmark/';
    const fd = new FormData();
    fd.append('csrfmiddlewaretoken', header_csrftoken);
    fd.append('uid', uid);
    axios.post(url, fd)
    .then(response => {
      if (response.data.status === 'ok') {
        if (response.data.message === 'removed') {
          var bookmark = document.getElementById('bookmark');
          if (bookmark) {
            bookmark.classList.remove('fa-solid');
            bookmark.classList.add('fa-regular');
          }
          document.getElementById(`menu-favorite-${uid}`).remove();
          if (document.getElementById('favorite-user-menu-section-list').children.length === 0) {
            document.getElementById('favorite-user-menu-section-list').innerHTML = '<li id="favorite-menu-empty" class="nothing">هیچ کالایی در علاقه مندی ها وجود ندار.</li>';
            document.getElementById('all-favorites').classList.add('disabled');
          }
        }
      }
    })
    .catch(error => {
      // Handle errors
      Loger.ConnectionError();
    });
}
// ---------Go-To-Dash-BTN-----------
function GoToDash() {
    location.href = '/dashboard/profile/';
}
// ---------------Brand-Name-Link-To-Home-Page-------------------
function BrandNameLinkToHomePage() {
    location.href = '/';
}