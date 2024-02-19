// ----------------------------------------
class Authenticate {
    constructor(order) {
      this.order = order;
      this.created = new Date().getTime();
      this.LoginURL = location.protocol + '//' + location.hostname +'/account/login/';
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
      if (String(passwd).length <= 1){
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
        const login_url = this.LoginURL;
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
                window.location.href = location.protocol + '//' + location.hostname;
            } else {
                login_button.classList.remove('submiting')
                login_button.classList.remove('disabled')
                login_button.innerHTML = 'ورود'
            }
          })
          .catch(error => {
            // Handle errors
            console.error('Error submitting form:', error);
            login_button.classList.remove('submiting')
            login_button.classList.remove('disabled')
            login_button.innerHTML = 'ورود'
          });
      }
    }
    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}
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
    console.log('started....')
    login_button.classList.add('submiting')
    login_button.innerHTML = '<i class="fa-solid fa-spinner"></i>'
    if (authenticate.isValid()) {
        authenticate.Login();
    } else {
        console.log('failed')
        login_button.classList.remove('submiting')
        login_button.innerHTML = 'ورود'
    }
}












