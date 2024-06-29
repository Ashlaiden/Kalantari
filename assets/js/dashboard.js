
// ***********************Start******************************

function chooseSectionBtn(section) {
    var line = section.querySelector('.under-line');

    var data_section = section.getAttribute('data_section');

    removeActiveSection()
    LoadingLayerToggle(true)

    line.classList.add('under-line-active')

    switch (data_section) {
        case 'profile':
            break;
        case 'cart':
            cartSection();
            break;
        case 'favorite':
            favoriteSection();
            break;
    }
}
function removeActiveSection() {
    try {        
        var sections_btn = document.getElementsByClassName('section');
        for (i = 0; i <= sections_btn.length; i++) {
            var under_line = sections_btn[i].querySelector('.under-line');
            if (under_line.classList.contains('under-line-active')) {
                under_line.classList.remove('under-line-active');
            }
        }
    } catch (error) {
        // console.log(`Error ${error.message}`);
    }
}

// ------------Content-Loading-Layer-----------
function LoadingLayerToggle(stat) {
    var loadingLayer = document.getElementById('loading-layer');

    if (stat == true) {
        if (loadingLayer.classList.contains('hidden')) {
            document.getElementById('content').innerHTML = '';
            loadingLayer.classList.remove('hidden');
        }
        return true
    } else if (stat == false) {
        if (!loadingLayer.classList.contains('hidden')) {
            loadingLayer.classList.add('hidden');
        }
        return true
    } else {
        return false
    }

    // if (loadingLayer.classList.contains('hidden')) {
    //     loadingLayer.classList.remove('hidden');
    // } else {
    //     loadingLayer.classList.add('hidden');
    // }
    // var contentContainer = document.getElementById('content-container');
    
    // // Show the loading layer
    // loadingLayer.classList.remove('hidden');

    // // Simulate an AJAX request or any other async operation
    // setTimeout(function() {
    //     // Hide the loading layer
    //     loadingLayer.classList.add('hidden');
        
    //     // Update the content (for demonstration purposes)
    //     contentContainer.innerHTML = '<p>New content loaded!</p>';
    // }, 2000); // Simulate a 2-second loading time
}
// -----------------------------

// *************************************************************************

// --------------cart-------------------
function cartSection() {
    cart_url = '/cart/'


    axios.get(cart_url).then(response => {
        LoadingLayerToggle(false);
        document.getElementById('content').innerHTML = response.data;
    }).catch(error => {
        console.log(`Error: ${error}`);
    });
}

function favoriteSection() {
    favorite_url = '/favorite/_items_list/';


    axios.get(favorite_url).then(response => {
        LoadingLayerToggle(false);
        document.getElementById('content').innerHTML = response.data;
    }).catch(error => {
        console.log(`Error: ${error}`);
    });
}






// -------------------------------------------------
function ContinueCart() {
    favorite_url = '/cart/continue_ordering/';


    axios.get(favorite_url).then(response => {
        LoadingLayerToggle(false);
        document.getElementById('content').innerHTML = response.data;
    }).catch(error => {
        console.log(`Error: ${error}`);
    });
}





