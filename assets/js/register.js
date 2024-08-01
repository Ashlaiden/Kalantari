// -----------------------------------
class Register {
    constructor() {
        this.step = 1;
        this.confirm_btn_id = 'confirm';
        phone_listener();
    }
    limitDigits(id, max) {
        var el = document.getElementById(id);
        if (el.value.length > max) {
            // el.value = el.value.slice(0, max);
            el.value = el.value.replace(/(\d{11}).*/, '$1');;
            el.setSelectionRange(cursorPosition, cursorPosition);
        }
    }
    confirm_btn(active = true, id = this.confirm_btn_id) {
        const btn = document.getElementById(id);
        if (btn.classList.contains('disabled') && active == true) {
            btn.classList.remove('disabled');
        } else if (!btn.classList.contains('disabled') && active == false) {
            btn.classList.add('disabled');
        }
    }
    beDigit(id) {
        const el = document.getElementById(id)
        el.value = el.value.replace(/\D/g, '');
    }
    confirm_phone_number() {
        
    }
}
// ********************************
const register = new Register();
// ********************************

function phone_listener() {
    document.getElementById('phone').addEventListener('input', function (e) {
        const phone = document.getElementById('phone');
        if (!String(phone.value).startsWith('09') || phone.value.length < 11) {
            if (phone.classList.contains('is-valid')) {
                phone.classList.remove('is-valid')
            }
            phone.classList.add('input-error');
            if (!document.getElementById('phone-error')) {
                phone.insertAdjacentHTML('afterend', `<small id="phone-error" class="input-error-message">شماره وارد شده معتبر نمی باشد</small>`);
            }
            register.confirm_btn(false);
        } else {
            if (document.getElementById('phone-error')) {
                phone.classList.remove('input-error');
                document.getElementById('phone-error').remove();
                phone.classList.add('is-valid');
            }
            register.confirm_btn(true);
        }
    });
}







// document.getElementById('phone').addEventListener('input', function (e) {
//     const phone = document.getElementById('phone');
//     if (!String(phone.value).startsWith('09') || phone.value.length < 11) {
//         beDigit('phone');
//         if (phone.classList.contains('is-valid')) {
//             phone.classList.remove('is-valid')
//         }
//         phone.classList.add('input-error');
//         if (!document.getElementById('phone-error')) {
//             phone.insertAdjacentHTML('afterend', `<small id="phone-error" class="input-error-message">شماره وارد شده معتبر نمی باشد</small>`);
//         }
//     } else {
//         if (document.getElementById('phone-error')) {
//             phone.classList.remove('input-error');
//             document.getElementById('phone-error').remove();
//             phone.classList.add('is-valid')
//         }
//     }
// });

// function limitDigits(id, max) {
//     var el = document.getElementById(id);
//     if (el.value.length > max) {
//         // el.value = el.value.slice(0, max);
//         el.value = el.value.replace(/(\d{11}).*/, '$1');;
//         el.setSelectionRange(cursorPosition, cursorPosition);
//     }
// }
// function beDigit(id) {
//     const el = document.getElementById(id)
//     el.value = el.value.replace(/\D/g, '');
// }