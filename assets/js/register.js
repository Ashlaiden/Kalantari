// ---------------jalali-date-time---------------------------
$("#birthday").persianDatepicker({
    months: ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"],
    dowTitle: ["شنبه", "یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنج شنبه", "جمعه"],
    shortDowTitle: ["ش", "ی", "د", "س", "چ", "پ", "ج"],
    showGregorianDate: !1,
    persianNumbers: !0,
    formatDate: "YYYY/MM/DD",
    selectedBefore: !1,
    startDate: null,
    endDate: "today",
    selectedDate: "1400/01/01",
    prevArrow: '\u25c4',
    nextArrow: '\u25ba',
    theme: 'default',
    alwaysShow: !1,
    selectableYears: [1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1318, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1332, 1333, 1334, 1335, 1336, 1337, 1338, 1339, 1340, 1341, 1342, 1343, 1344, 1345, 1346, 1347, 1348, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1357, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399,1400],
    selectableMonths: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    cellWidth: 40, // by px
    cellHeight: 30, // by px
    fontSize: 15, // by px                
    isRTL: !1,
    calendarPosition: {
        x: 0,
        y: 0,
    },
    onShow: function () { },
    onHide: function () { },
    onSelect: function () { },
    onRender: function () { }
});
// ------------------------------------------------------------
class Registeration {
    constructor(order) {
        this.order = order;
        this.created = new Date().getTime();
        this.options = {
            errors: {
                '0': 'Valid Password',
                '1': 'Passwords do not match',
                '2': 'Password length must be at least 8 characters',
                '3': 'Password must contain at least one number',
                '4': 'Password must contain at least one character',
                '5': 'Password must contain at least one lowercase letter',
                '6': 'Password must contain at least one uppercase letter',
                '7': 'Password must contain at least one ASCII character'
            },
            errorsType: {
                '0': true,
                '1': false,
                '2': false,
                '3': false,
                '4': false,
                '5': false,
                '6': false,
                '7': false
            }
        };
        this.minAge = 18;
    }
    cleaned_email(email) {
         // Regular expression for basic email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        // Test the email against the regular expression
        var isValid = emailRegex.test(email);
        if (isValid) {
            this.email = email;
            return true;
        } else {
            return false;
        }
    }
    cleaned_passwd(passwd) {
        const error = this.options['errors'];
        const options = this.options;
        let validation = 0;

        if (!passwd.trim() && options.errorsType['1']) {
            return { 'status': false, 'value': validation + 1, 'error': error['1'] };
        } else {
            if (String(passwd).length < 8 && options.errorsType['2']) {
                return { 'status': false, 'value': validation + 2, 'error': error['2'] };
            } else {
                let num = 0;
                let char = 0;
                let lowe = 0;
                let upper = 0;
                let asci = 0;
                let none = 0;
    
                for (let i = 0; i < String(passwd).length; i++) {
                    const currentChar = String(passwd)[i];
    
                    if (!isNaN(currentChar)) {
                        num += 1;
                    } else if (currentChar.match(/[a-zA-Z]/)) {
                        char += 1;
    
                        if (currentChar === currentChar.toLowerCase()) {
                            lowe += 1;
                        } else if (currentChar === currentChar.toUpperCase()) {
                            upper += 1;
                        }
                    } else if (currentChar.charCodeAt(0) <= 127) {
                        asci += 1;
                    } else {
                        none += 1;
                    }
                }
    
                if (num === 0 && options.errorsType['3']) {
                    return { 'status': false, 'value': validation + 3, 'error': error['3'] };
                } else if (char === 0 && options.errorsType['4']) {
                    return { 'status': false, 'value': validation + 4, 'error': error['4'] };
                } else if (lowe === 0 && options.errorsType['5']) {
                    return { 'status': false, 'value': validation + 5, 'error': error['5'] };
                } else if (upper === 0 && options.errorsType['6']) {
                    return { 'status': false, 'value': validation + 6, 'error': error['6'] };
                } else if (asci === 0 && options.errorsType['7']) {
                    return { 'status': false, 'value': validation + 7, 'error': error['7'] };
                } else {
                    this.passwd = passwd;
                    return { 'status': true, 'value': validation, 'error': error['0'] };
                }
            }
        }
    }
    confirm_passwd(confirm_passwd) {
        if (confirm_passwd === this.passwd) {
            this.confirmed_passwd = confirm_passwd;
            this.passwd_confirmed = true;
            return true;
        } else {
            this.passwd_confirmed = false;
            return false;
        }
    }
    cleaned_gender(gender) {
        if (gender === 'male') {
            this.gender = 'male';
            return true;
        } else if (gender === 'female') {
            this.gender = 'female';
            return true;
        } else if (gender === 'other') {
            this.gender = 'other';
            return true;
        } else {
            return false;
        }
    }
    cleaned_firstName(firstName) {
        // Regular expression to match only letters and spaces
        const regex = /^[A-Za-z\s]+$/;
        // Test if the name matches the regular expression
        if (regex.test(firstName)) {
            this.firstName = firstName;
            return true;
        } else {
            return false;
        }
    }
    cleaned_lastName(lastName) {
        // Regular expression to match only letters and spaces
        const regex = /^[A-Za-z\s]+$/;
        // Test if the name matches the regular expression
        if (regex.test(lastName)) {
            this.lastName = lastName;
            return true;
        } else {
            return false;
        }
    }
    cleaned_phoneNumber(phoneNumber) {
        // Remove non-digit characters
        const cleanedPhoneNumber = phoneNumber.replace(/\D/g, '');

        // Check if the cleaned phone number is numeric and has a valid length
        if (/^\d{10}$/.test(cleanedPhoneNumber)) {
            // Check for 10-digit number starting with 9
            if (cleanedPhoneNumber[0] === '9' && cleanedPhoneNumber[0] !== '0') {
                this.phoneNumber = '0' + cleanedPhoneNumber;
                return true;
            }
        } else if (/^\d{11}$/.test(cleanedPhoneNumber)) {
            // Check for 11-digit number starting with 09
            if (cleanedPhoneNumber[0] === '0' && cleanedPhoneNumber[1] === '9') {
                this.phoneNumber = cleanedPhoneNumber;
                return true;
            }
        } else {
            return false; // Invalid phone number
        }
    }
    cleaned_birthday(birthday) {
        const parsedDate = new Date(birthday);
        const minAge = this.minAge;

        if (isNaN(parsedDate.getTime())) {
            return false;
        }
        const currentYear = new Date().getFullYear();
        const minBirthYear = currentYear - minAge;
        const year = parsedDate.getFullYear();
        const month = parsedDate.getUTCMonth();
        const day = parsedDate.getDate();
        if (year > minBirthYear) {
            return false;
        }
        this.birthday = `${year}-${month}-${day}`;
        return true;
    }
    cleaned_privacy(checked) {
        if (checked) {
            this.privacy = true;
            return true;
        } else {
            this.privacy = false;
            return false;
        }
    }
    isValid() {
        let isValid = 0;
        if (!this.email) {
            isValid = 1;
        } else if (!this.passwd) {
            isValid = 2;
        } else if (!this.passwd_confirmed) {
            isValid = 3;
        } else if (!this.gender) {
            isValid = 4;
        } else if (!this.firstName) {
            isValid = 5;
        } else if (!this.lastName) {
            isValid = 6;
        } else if (!this.phoneNumber) {
            isValid = 7;
        // } else if (!this.birthday) {
        //     isValid = 8;
        } else if (!this.privacy) {
            isValid = 9;
        }
        if (isValid === 0) {
            return true;
        } else {
            return false;
        }
    }
    register() {
        const dataIsValid = this.isValid();
        if (dataIsValid) {
            let form = document.getElementById('register-form')
            const fd = new FormData();
            fd.append('csrfmiddlewaretoken', form.children.namedItem(name='csrfmiddlewaretoken').value);
            fd.append('email', this.email);
            fd.append('passwd', this.passwd);
            fd.append('confirm_passwd', this.confirmed_passwd);
            fd.append('passwd_confirmed', this.passwd_confirmed);
            fd.append('gender', this.gender);
            fd.append('first_name', this.firstName);
            fd.append('last_name', this.lastName);
            fd.append('phone_number', this.phoneNumber);
            if (this.birthday)
                fd.append('birth_date', this.birthday);
            fd.append('privacy_accepted', this.privacy);
            axios.post('/account/register/', fd)
              .then(response => {
                if (response.data.status === 'ok' && response.data.code === '200' && response.data.success) {
                    window.location.href = location.protocol + '//' + location.hostname;
                }
              })
              .catch(error => {
                // Handle errors
                Loger.ConnectionError();
              });
        } else {
            return {'status': 'failed', 'code': '400', 'error': 'data is not valid!'}
        }
    }

}
const register = new Registeration('create address_manager!');
register.cleaned_gender('man');
let register_btn = document.getElementById('register-btn');
// Add an event listener for the 'email' event
document.getElementById('email').addEventListener('input', function(event) {
    if (register.cleaned_email(this.value)) {
        if (register.isValid()) {
            register_btn.classList.remove('disabled');
        } else {
            register_btn.classList.add('disabled');
        }
    } else {
        register_btn.classList.add('disabled');
    }
});
// Add an event listener for the 'passwd' event
document.getElementById('passwd').addEventListener('input', function(event) {
    if (register.cleaned_passwd(this.value)) {
        if (register.isValid()) {
            register_btn.classList.remove('disabled');
        } else {
            register_btn.classList.add('disabled');
        }
    } else {
        register_btn.classList.add('disabled');
    }
});
// Add an event listener for the 'confirm-passwd' event
document.getElementById('confirm-passwd').addEventListener('input', function(event) {
    if (register.confirm_passwd(this.value)) {
        if (register.isValid()) {
            register_btn.classList.remove('disabled');
        } else {
            register_btn.classList.add('disabled');
        }
    } else {
        register_btn.classList.add('disabled');
    }
});
// Add an event listener for the 'gender' event
document.getElementById('gender').addEventListener('input', function(event) {
    if (register.cleaned_gender(this.value)) {
        if (register.isValid()) {
            register_btn.classList.remove('disabled');
        } else {
            register_btn.classList.add('disabled');
        }
    } else {
        register_btn.classList.remove('disabled');
    }
});
// Add an event listener for the 'first-name' event
document.getElementById('first-name').addEventListener('input', function(event) {
    if (register.cleaned_firstName(this.value)) {
        if (register.isValid()) {
            register_btn.classList.remove('disabled');
        } else {
            register_btn.classList.add('disabled');
        }
    } else {
        register_btn.classList.add('disabled');
    }
});
// Add an event listener for the 'last-name' event
document.getElementById('last-name').addEventListener('input', function(event) {
    if (register.cleaned_lastName(this.value)) {
        if (register.isValid()) {
            register_btn.classList.remove('disabled');
        } else {
            register_btn.classList.add('disabled');
        }
    } else {
        register_btn.classList.add('disabled');
    }
});
// Add an event listener for the 'phone-number' event
document.getElementById('phone-number').addEventListener('input', function(event) {
    if (register.cleaned_phoneNumber(this.value)) {
        if (register.isValid()) {
            register_btn.classList.remove('disabled');
        } else {
            register_btn.classList.add('disabled');
        }
    } else {
        register_btn.classList.add('disabled');
    }
});
// Add an event listener for the 'birthday' event
document.getElementById('birthday').addEventListener('gdate', function(event) {
    var date = new Date(this.dataset.gdate.replace(/\//g, '-'));
    if (register.cleaned_birthday(date)) {
        if (register.isValid()) {
            register_btn.classList.remove('disabled');
        } else {
            register_btn.classList.add('disabled');
        }
    } else {
        register_btn.classList.add('disabled');
    }
});
// Add an event listener for the 'input' event
document.getElementById('accept-rules').addEventListener('change', function() {
    var date = document.getElementById('birthday');
    if (register.cleaned_birthday(date.value)) {
    } else {
        register_btn.classList.add('disabled');
    }


    if (register.cleaned_privacy(this.checked)) {
        if (register.isValid()) {
            register_btn.classList.remove('disabled');
        } else {
            register_btn.classList.add('disabled');
        }
    } else {
        register_btn.classList.add('disabled');
    }
});
document.getElementById('register-btn').addEventListener('click', function () {
    if (register.isValid()) {
        register.register();
    }
});


