// ----------------------------------------
class Authenticate {
  constructor(order) {
    this.order = order;
    this.created = new Date().getTime();
    this.LoginURL = location.protocol + '//' + location.hostname + '/account/login/';
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
    if (String(passwd).length <= 1) {
      return false;
    } else {
      this.passwd = passwd;
      return true;
    }
  }
  isValid() {
    if (this.email && this.passwd) {
      return true;
    } else {
      return false;
    }
  }
  Login() {
    if (this.isValid()) {
      const login_url = this.LoginURL + `?next=${this.get_next()}`;
      this.csrfmiddlewaretoken = document.getElementById('login-form').children.namedItem('csrfmiddlewaretoken').value;
      const fd = new FormData();
      fd.append('csrfmiddlewaretoken', this.csrfmiddlewaretoken)
      fd.append('email', this.email)
      fd.append('passwd', this.passwd)
      axios.post(login_url, fd)
        .then(response => {
          if (response.data.status === 'ok' && response.data.code === '200') {
            login_button.classList.remove('submiting')
            login_button.classList.add('disabled')
            login_button.innerHTML = 'در حال پردازش...'
            this.to_next()
          } else {
            Loger.Failed();
            login_button.classList.remove('submiting')
            login_button.classList.remove('disabled')
            login_button.innerHTML = 'ورود'
          }
        })
        .catch(error => {
          // Handle errors
          Loger.ConnectionError();
          login_button.classList.remove('submiting')
          login_button.classList.remove('disabled')
          login_button.innerHTML = 'ورود'
        });
    }
  }
  sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  get_next() {
    try {
      const queryString = window.location.search;

      // Create a URLSearchParams address_manager
      const urlParams = new URLSearchParams(queryString);

      // Get the value of the 'next' parameter
      const nextUrl = urlParams.get('next');

      return nextUrl
    } catch (error) {
      Loger.Message('اطاعات موجود در URL معتبر نمی باشد')
      return ''
    }
  }

  to_next() {
    // Example: Redirect to the next URL if it exists
    var nextUrl = this.get_next()
    if (nextUrl != '') {
      window.location.href = nextUrl;
    } else {
      window.location.gref = '/';
    }
  }
}
// --------------------------------------------------
var authenticate = new Authenticate('create');
var login_button = document.getElementById('login');
document.getElementById('email').addEventListener('input', function () {
  var vlue = this.value;
  if (authenticate.cleaned_email(vlue)) {
    if (authenticate.isValid()) {
      login_button.classList.remove('disabled');
    } else {
      login_button.classList.add('disabled');
    }
  } else {
    login_button.classList.add('disabled');
  }
});
document.getElementById('passwd').addEventListener('input', function () {
  var vlue = this.value;
  if (authenticate.cleaned_passwd(vlue)) {
    if (authenticate.isValid()) {
      login_button.classList.remove('disabled');
    } else {
      login_button.classList.add('disabled');
    }
  } else {
    login_button.classList.add('disabled');
  }
});
// ------------------------------------------
function Login() {
  login_button.classList.add('submiting')
  login_button.innerHTML = '<i class="fa-solid fa-spinner"></i>'
  if (authenticate.isValid()) {
    authenticate.Login();
  } else {
    Loger.AddWarning('لطفا اطلاعات مورد نیاز را به طور صحیح وارد نمایید')
    login_button.classList.remove('submiting')
    login_button.innerHTML = 'ورود'
  }
}












