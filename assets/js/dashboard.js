
// ***********************Start******************************
class DashboardClass {
    constructor() {
        this.main_section = '';
        this.checking = {};
        this.checking_parent = '';
        this.checked = [];
    }

    path_reference = {
        'profile': {},
        'cart': {
            'order': {
                'addressing': {},
                'checkout': {},
                'receipt': {},
                'payment': {},
            }
        },
        'favorite': {},
    }

    // path_reference_functions = {
    //     'profile': this.default_section(),
    //     'cart': {
    //         'order': none
    //     },
    //     'favorite': this.load_base_section('favorite'),
    // }

    start() {
        var base_sec = '';
        var base_loaded = false;
        if (this.paths.length > 1) {
            for (var i = 0; i <= this.paths.length; i++) {
                var path = this.paths[i];

                if (!base_loaded) {
                    base_loaded = this.is_main_path(path)
                    if (base_loaded) {
                        base_sec = path;
                        this.main_section = path;
                        this.checking = this.path_reference[path];
                        this.checking_parent = path;
                        this.checked.push(path)
                    } else {
                        this.default_section();
                    }
                } else {
                    this.check_sub_path(path);
                    if (i == this.paths.length) {
                        this.load_path();
                    }
                }
            }
            this.paths.forEach(path => {
                if (!base_loaded) {
                    base_loaded = this.is_main_path(path)
                    if (base_loaded) {
                        base_sec = path;
                        this.main_section = path;
                        this.checking = this.path_reference[path];
                        this.checking_parent = path;
                        this.checked.add(path)
                    } else {
                        this.default_section();
                    }
                } else {
                    this.check_sub_path(path)
                }
            });
        } else if (this.paths.length == 1) {
            base_loaded = this.is_main_path(this.paths[0]);
            if (base_loaded) {
                base_sec = this.paths[0];
                this.main_section = this.paths[0];
                this.load_base_section(this.paths[0]);
            } else {
                this.default_section();
            }
        } else {
            this.default_section();
        }
    }

    default_section() {
        const newPath = '/dashboard/profile/';
        history.pushState(null, '', newPath); 
        chooseSectionBtn('profile');   
    }

    keyExists(dict, key) {
        return dict.hasOwnProperty(key);
        // Alternatively, use: return key in dict;
    }

    is_main_path(path) {
        if (this.keyExists(this.path_reference, path)) {
            this.checking = this.path_reference[path];
            this.checking_parent = path;
            this.checked.push(path)
            return true
        } else {
            return false
        }
    }

    check_sub_path(subpath) {
        if (this.keyExists(this.checking, subpath)) {
            this.chfecking = this.checking[subpath];
            this.checking_parent = subpath;
            this.checked.push(subpath)
        } else {
            this.load_path();
        }
        // sub_loaded = false;
        // switch (this.base_sec) {
        //     case 'profile':
        //         this.profile_sub_paths.forEach(path => {
        //             if (!sub_loaded) {
        //                 if (subpath == path) {

        //                 } else {
                            
        //                 }
        //             }
        //         });
        //         break;
        //     case 'cart':
        //         this.cart_sub_paths.forEach(path => {
        //             if (subpath == path) {

        //             } else {

        //             }
        //         });
        //         break;
        //     case 'favorite':
        //         this.favorite_sub_paths.forEach(path => {
        //             if (subpath == path) {

        //             } else {
                        
        //             }
        //         });
        //         break;
        // }
    }

    load_base_section(bs) {
        chooseSectionBtn(document.getElementById(`${bs}_section_btn`));
    }
    
    load_path() {
        const fstate = this.checked;
        switch (fstate[0]) {
            case 'profile':
                this.load_base_section('profile');
                break;
            case 'cart':
                switch (fstate[1]) {
                    case 'order':
                        switch (fstae[2]) {
                            case 'addressing':
                                Ordering('auto');
                                break;
                            case 'checkout':
                                Ordering('auto');
                                break;
                            case 'receipt':
                                Ordering('auto');
                                break;
                            case 'payment':
                                Ordering('auto');
                                break;
                            default:
                                Ordering('auto');
                                break;
                        }
                        break;
                    default:
                        this.load_base_section('cart');
                        break;
                }
                break;
            case 'favorite':
                this.load_base_section('favorite');
                break;
            default:
                this.load_base_section('profile');
                break;
        }
    }
}

// ***************
const dashboard = new DashboardClass()
// ***************

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
    
    const newPath = '/dashboard/cart/';
    history.pushState(null, '', newPath);    

    axios.get(cart_url).then(response => {
        LoadingLayerToggle(false);
        document.getElementById('content').innerHTML = response.data;
    }).catch(error => {
        console.log(`Error: ${error}`);
    });
}

function favoriteSection() {
    favorite_url = '/favorite/_items_list/';

    const newPath = '/dashboard/favorite/';
    history.pushState(null, '', newPath);   

    axios.get(favorite_url).then(response => {
        LoadingLayerToggle(false);
        document.getElementById('content').innerHTML = response.data;
    }).catch(error => {
        console.log(`Error: ${error}`);
    });
}












