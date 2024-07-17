// ----------------------------------------
class Authenticate {
  constructor(order) {
    this.order = order;
    this.created = new Date().getTime();
    this.LoginURL = '/account/login/';
    this.LogoutURL = '/account/logout/';
    this.RegisterURL = {'URL': '/account/register/', 'type': '_blank'}
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
    if (String(passwd).length <= 4){
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
            Loger.Success();
            location.reload();
          }
        })
        .catch(error => {
          Loger.Failed();
          Loger.ServerError();
        });
    }
  }
  LogOut() {
    const logout_url = this.LogoutURL
    // Send the GET request with the user information in the headers
    axios.get(logout_url, {
    }).then(response => {
      if (response.data.status === 'ok' && response.data.code === '200') {
        Loger.Success();
        location.reload()
      } else {
        Loger.Failed();
      }
    }).catch(error => {
      Loger.ConnectionError();
    });
  }
}
var authenticate = new Authenticate('create');
if (document.getElementById('login-form')) {
  var form = document.getElementById('login-form').children;
  var login_button = form.namedItem('submit');
  form.namedItem('email').addEventListener('input', function () {
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
  form.namedItem('passwd').addEventListener('input', function () {
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
    if (authenticate.isValid()) {
      authenticate.Login();
    } else {
      Loger.AddError('اطلاعات وارد شده معتبر نیست')
    }
  }
  // ------------------------register-btn---------------------------
  document.getElementById('register-btn').addEventListener('click', function() {
    window.open(authenticate.RegisterURL.URL, authenticate.RegisterURL.type);
  });
}
// -------------logout--------------------
function Logout() {
  authenticate.LogOut();
}


















