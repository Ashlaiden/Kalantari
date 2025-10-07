
// ***********************Start******************************
class DashboardClass {
    constructor() {
        this.main_section = '';
        this.checking = {};
        this.checking_parent = '';
        this.checked = [];
        this.pathHistory = [];
        this.pathHistory.push(this.getPreviousPagePathname());
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

    changePath(newPath) {
        this.pathHistory.push(newPath);
         
        history.pushState(null, '', newPath);
    }

    // path_reference_functions = {
    //     'profile': this.default_section(),
    //     'cart': {
    //         'order': none
    //     },
    //     'favorite': this.load_base_section('favorite'),
    // }

    getBaseURLWithRegex(url) {
        // Match the base URL using regex
        const matches = url.match(/^(https?:\/\/[^\/]+)(\/[^?#]*)?/);

        if (matches) {
            // Return the base URL without query parameters and hash
            return matches[1] + (matches[2] || '');
        }

        return '';
    }

    getPathSegments() {
        try {
            const page_url = window.location.href;
            const url = this.getBaseURLWithRegex(page_url);
            const urlObject = new URL(url);
            const pathname = urlObject.pathname;
            const pathSegments = pathname.split('/').filter(segment => segment !== '');
            const NetList = pathSegments.slice(1);
            // console.log(`NetList:    ${NetList}`);
            return NetList;
        } catch (error) {
            Loger.AddError('خطای داخلی مرورگر');
            return [];
        }
    }

    start(paths) {
        var base_sec = '';
        var base_loaded = false;
        if (paths.length > 1) {
            for (var i = 0; i <= paths.length; i++) {
                var path = paths[i];
                if (!base_loaded && path !== '') {
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
                    if (i == paths.length) {
                        this.load_path();
                    }
                }
            }
            paths.forEach(path => {
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
        } else if (paths.length == 1) {
            base_loaded = this.is_main_path(paths[0]);
            if (base_loaded) {
                base_sec = paths[0];
                this.main_section = paths[0];
                this.load_base_section(paths[0]);
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
        chooseSectionBtn(document.getElementById('profile_section_btn'));
        this.load_base_section('profile');
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

    getPreviousPagePathname() {
        // Get the referrer URL
        const referrer = document.referrer;
    
        // Check if referrer URL is available
        if (referrer) {
            // Create a new URL object using the referrer URL
            const referrerURL = new URL(referrer);
    
            // Return the pathname of the referrer URL
            return referrerURL.pathname;
        } else {
            return '';
        }
    }

    go_back() {
        if (this.pathHistory.length > 2) {
            const url = this.getPathSegments();
            this.pathHistory.pop()
            this.start(url);
        } else {
            window.location.href = this.pathHistory[0];
        }
    }
}

// ***************
const dashboard = new DashboardClass()

// document.addEventListener('DOMContentLoaded', (event) => {
//     document.addEventListener('keydown', function (event) {
//         if (event.key === 'Backspace' || event.keyCode === 8) {
//             dashboard.go_back();
//         }
//     });
//     window.addEventListener('popstate', function (event) {
//         dashboard.go_back();
//     });
// });
// ***************

function chooseSectionBtn(section) {
    var line = section.querySelector('.under-line');

    var data_section = section.getAttribute('data_section');

    removeActiveSection()
    LoadingLayerToggle(true)

    line.classList.add('under-line-active')

    switch (data_section) {
        case 'profile':
            profileSection();
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
        var sections_btn = Array.from(document.getElementsByClassName('section'));
        sections_btn.forEach(function (btn) {
            var under_line = btn.querySelector('.under-line');
            if (under_line.classList.contains('under-line-active')) {
                under_line.classList.remove('under-line-active');
            }
        });
    } catch (error) {
        Loger.AddError('خطای داخلی مرورگر');
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
    cart_url = '/cart/_cart/_component/'

    if (window.location.pathname !== '/dashboard/cart/') {
        dashboard.changePath('/dashboard/cart/')
    }

    axios.get(cart_url).then(response => {
        LoadingLayerToggle(false);
        document.getElementById('content').innerHTML = response.data;
    }).catch(error => {
        Loger.ConnectionError();
    });
}
// ----------------favorite-------------------
function favoriteSection() {
    favorite_url = '/favorite/_items_list/';

    if (window.location.pathname !== '/dashboard/favorite/') {
        dashboard.changePath('/dashboard/favorite/')
    }

    axios.get(favorite_url).then(response => {
        LoadingLayerToggle(false);
        document.getElementById('content').innerHTML = response.data;
    }).catch(error => {
        Loger.ConnectionError();
    });
}
// -----------------------profile----------------------
function profileSection() {
    favorite_url = '/account/_dashboard/_profile/';

    if (window.location.pathname !== '/dashboard/profile/') {
        dashboard.changePath('/dashboard/profile/')
    }

    axios.get(favorite_url).then(response => {
        LoadingLayerToggle(false);
        document.getElementById('content').innerHTML = response.data;
    }).catch(error => {
        Loger.ConnectionError();
    });
}
function FirstLoginTo() {
    location.href = '/account/login/?next=/dashboard/profile/';
}











