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
            location.reload();
          }
        })
        .catch(error => {
          // Handle errors
          console.error('Error submitting form:', error);
        });
    }
  }
  LogOut() {
    const logout_url = this.LogoutURL
    console.log(logout_url)
    // Send the GET request with the user information in the headers
    axios.get(logout_url, {
    }).then(response => {
      console.log('JsonData Received')
      console.log(response.data)
      console.log(response.data.code)
      if (response.data.status === 'ok' && response.data.code === '200') {
        location.reload()
      } else {
        console.log(response)
      }
    }).catch(error => {
      console.error('Error sending GET request:', error);
    });
  }
}
var authenticate = new Authenticate('create');
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
  console.log('started....')
  if (authenticate.isValid()) {
    authenticate.Login();
    console.log('success')
  } else {
    console.log('failed')
  }
  console.log('end')
}
// -------------logout--------------------
function Logout() {
  console.log('started....')
  authenticate.LogOut();
  console.log('success')
  console.log('end')
}
// ------------------------register-btn---------------------------
document.getElementById('register-btn').addEventListener('click', function() {
  window.open(authenticate.RegisterURL.URL, authenticate.RegisterURL.type);
});


















