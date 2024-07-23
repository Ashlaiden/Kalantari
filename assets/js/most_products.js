function active_items_listener() {
    document.querySelectorAll('.item-link').forEach(function (link) {
        link.addEventListener('click', function (event) {
            if (event.target.parentElement.tagName.toLowerCase() === 'button') {
                copy_to_clipboard(this.href);
                event.preventDefault();
                event.stopPropagation();
            }
        });
    });

    // Get all the elements with the class 'product-item'
    const productItems = document.querySelectorAll('.item');

    // Add mouseover and mouseout event listeners to each product item
    productItems.forEach(item => {
        var dualimage = item.getAttribute('dual-image');

        if (dualimage && dualimage === 'true') {
            item.querySelector('.image-container').addEventListener('mouseenter', () => {

                // When the mouse is over the item, hide the cover image and show the hover image
                item.querySelector('.cover-image').style.opacity = '0';
                // item.querySelector('.cover-image').style.transform = 'rotateY(-180deg)';
                // item.querySelector('.hover-image').style.transform = 'rotateY(0deg)';
                item.querySelector('.hover-image').style.opacity = '1';
            });

            item.querySelector('.image-container').addEventListener('mouseleave', () => {
                // When the mouse is no longer over the item, show the cover image and hide the hover image
                item.querySelector('.cover-image').style.opacity = '1';
                // item.querySelector('.hover-image').style.transform = 'rotateY(-180deg)';
                // item.querySelector('.cover-image').style.transform = 'rotateY(0deg)';
                item.querySelector('.hover-image').style.opacity = '0';
            });
        }
    });
}
// ----***************-----------

document.addEventListener('DOMContentLoaded', (event) => {
    const items = Array.from(document.getElementById('carousel-container').querySelectorAll('.card'));
    items.forEach(function (item) {
        item.addEventListener('touchstart', function (event) {
            if (!event.target.parentElement.classList.contains('image-container')) {
                if (!item.classList.contains('most-product-touch-active')) {
                    event.preventDefault();
                    event.stopPropagation();
                    if (document.querySelector('.most-product-touch-active')) {
                        document.querySelector('.most-product-touch-active').classList.remove('most-product-touch-active')
                    }
                    item.classList.add('most-product-touch-active');
                    // setTimeout(() => {
                    // }, 200);
                }
            }
        });
        item.addEventListener('touchend', function (event) {
            if (item.classList.contains('most-product-touch-active')) {
                var owl = $('.owl-carousel');
                owl.trigger('stop.owl.autoplay');
                setTimeout(() => {
                    item.classList.remove('most-product-touch-active');
                    owl.trigger('play.owl.autoplay');
                }, 3000);
            }
        });
    });
    const carousel_container = document.getElementById('carousel-container');
    document.addEventListener('click', function(e) {
        if (!carousel_container.contains(e.target) && document.querySelector('.most-product-touch-active')) {
            var owl = $('.owl-carousel');
            document.querySelector('.most-product-touch-active').classList.remove('most-product-touch-active');
            owl.trigger('play.owl.autoplay');
        }
    });
    function groupItems() {
        // Destroy the existing Owl Carousel
        $('.owl-carousel').trigger('destroy.owl.carousel').removeClass('owl-carousel owl-loaded');
        $('.owl-carousel').find('.owl-stage-outer').children().unwrap();
        document.getElementById('carousel-container').remove();
        const container = document.createElement('div');
        container.className = 'carousel-container';
        container.id = 'carousel-container';
        document.getElementById('most-products').appendChild(container)


        let itemsPerGroup;
        const screenWidth = window.innerWidth;

        // if (screenWidth >= 1200) {
        //     itemsPerGroup = 6;
        // } else if (screenWidth >= 768) {
        //     itemsPerGroup = 4;
        // } else if (screenWidth >= 574) {
        //     itemsPerGroup = 2;
        // } else {
        //     itemsPerGroup = 1;
        // }

        if (screenWidth >= 1200) {
            itemsPerGroup = 6;
        } else if (screenWidth >= 768) {
            itemsPerGroup = 4;
        } else {
            itemsPerGroup = 2;
        }

        // Create groups
        // let group = document.createElement('div');
        // group.className = 'carousel-group';
        // items.forEach((item, index) => {
        //     group.appendChild(item);
        //     if ((index + 1) % itemsPerGroup === 0 || index === items.length - 1) {
        //         container.appendChild(group);
        //         group = document.createElement('div');
        //         group.className = 'carousel-group';
        //     }
        // });


        // items.length = 0;

        for (let i = 0; i < items.length; i += itemsPerGroup) {
            const group = document.createElement('div');
            group.className = 'carousel-group';
            items.slice(i, i + itemsPerGroup).forEach(item => group.appendChild(item));
            container.appendChild(group);
        }


        // Check if Owl Carousel is initialized
        // if ($('.owl-carousel').data('owlCarousel')) {
        //     // If it is, destroy it
        //     $('.owl-carousel').data('owlCarousel').destroy();
        // }

        container.classList.add('owl-carousel')

        $('.owl-carousel').owlCarousel({
            loop: true,
            margin: 0,
            nav: true,
            items: 1,
            autoplay: true,
            autoplayTimeout: 4000,
            autoplayHoverPause: true,
        })
        active_items_listener();
    }

    // Initial grouping
    groupItems();

    // Debounce function
    function debounce(func, wait) {
        let timeout;
        return function () {
            clearTimeout(timeout);
            timeout = setTimeout(func, wait);
        }
    }

    // Re-group items on window resize
    window.addEventListener('resize', debounce(groupItems, 500));
});


// ----------------------------------------------
// let ids = [];
// let active_group = '';
// let active_index = 0;
// let time_to_apply = 8000;
// function carousel_start() {
//     let groups = document.querySelectorAll('.carousel-group');
//     groups.forEach(function(group) {
//         ids.push(group.id);
//         if (group.classList.contains('active-group')) {
//             active_group = group.id
//         }
//     });
// }
// function update_active_group_info(id) {
//     for (let i = 0; i <= ids.length; i++) {
//         if (ids[i] == id) {
//             active_index = i;
//             active_group = id;
//         }
//     }
// }
// function get_next_group() {
//     time_to_apply = 10000;
//     var next = 0;
//     for (let i = 0; i < ids.length; i++) {
//         if (ids[i] == active_group) {
//             active_index = i;
//             if (i == 0) {
//                 next = i + 1;
//             } else if (i == (ids.length - 1)) {
//                 next = 0;
//             } else {
//                 next = i + 1;
//             }
//         }
//     }
//     return next
// }
// function get_prev_group() {
//     time_to_apply = 10000;
//     var prev = 0;
//     for (let i = 0; i < ids.length; i++) {
//         if (ids[i] == active_group) {
//             active_index = i;
//             if (i == 0) {
//                 prev = (ids.length - 1);
//             } else if (i == (ids.length - 1)) {
//                 prev = 0;
//             } else {
//                 prev = i - 1;
//             }
//         }
//     }
//     return prev
// }
// function next_group() {
//     let next_index = get_next_group();
//     let active_el = document.getElementById(active_group);
//     let next_el = document.getElementById(ids[next_index]);


//     console.log('-----------------')
//     console.log(next_index);
//     console.log(active_el);
//     console.log(ids[next_index]);
//     console.log(next_el);
//     console.log('-----------------')

//     active_el.classList.add('deactiving-group');
//     next_el.classList.add('activing-group');
//     active_el.classList.remove('active-group');
//     next_el.classList.add('active-group');
//     next_el.classList.remove('activing-group');

//     update_active_group_info(next_el.id);
// }
// function prev_group() {
//     let next_index = get_prev_group();
//     let active_el = document.getElementById(active_group);
//     let next_el = document.getElementById(ids[next_index]);

//     active_el.classList.add('deactiving-group');
//     next_el.classList.add('activing-group');
//     active_el.classList.remove('active-group');
//     next_el.classList.add('active-group');
//     next_el.classList.remove('activing-group');

//     update_active_group_info(next_el.id);
// }
// function update_group() {
//     time_to_apply = 8000;
//     next_group();
// }
// // document.addEventListener('DOMContentLoaded', (event) => {
// //     setInterval(carousel_start, 1000);
// //     setInterval(update_group, time_to_apply);
// // });