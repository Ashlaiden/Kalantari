


// const progressBar = document.getElementById("progress-bar");
// const progressNext = document.getElementById("progress-next");
// const progressPrev = document.getElementById("progress-prev");
// const steps = document.querySelectorAll(".step");
let last_step = 1;
let active = 1;

function progress_next() {
  const steps = document.querySelectorAll(".step");
  active++;
  if (active > steps.length) {
    active = steps.length;
  }
  updateProgres();
}

function progress_perv() {
  const steps = document.querySelectorAll(".step");
  active--;
  if (active < 1) {
    active = 1;
  }
  updateProgres();
}

function updateProgres() {
  // const progressNext = document.getElementById("progress-next");
  // const progressPrev = document.getElementById("progress-prev");
  const progressBar = document.getElementById("progress-bar");
  const steps = document.querySelectorAll(".step");


  steps.forEach((step, i) => {
    step.classList.remove('pending');
  });

  if (active > last_step) {
    steps.forEach((step, i) => {
      if (i < (active - 1)) {
        step.innerHTML = `<i class="fa-solid fa-check"></i>`;
        step.classList.add('active');
      }
    });
    progressBar.style.width = ((active - 1) / (steps.length - 1)) * 100 + "%";

    steps[active - 1].classList.add('pending');
  } else {
    progressBar.style.width = ((active - 1) / (steps.length - 1)) * 100 + "%";

    steps[active - 1].classList.remove('active');
    steps[active - 1].innerHTML = active;
    steps[active - 1].classList.add('pending');

    // steps.forEach((step, i) => {
    //   if (i < )
    // });
  }


  // if (active > last_step) {
  //   start = active - 2;
  //   end = active - 1;
  //   steps[start].classList.remove('pending');
  //   sleep(200);
  //   steps[start].classList.add('active');
  //   steps[start].innerHTML = `<i class="fa-solid fa-check"></i>`;
  //   sleep(200)
  //   progressBar.style.width = ((active - 1) / (steps.length - 1)) * 100 + "%";
  //   sleep(700);
  //   steps[end].classList.add('pending');


  // steps.forEach((step, i) => {
  //   st = i + 1;
  // if (st < active) {
  //   step.classList.remove('pending')
  //   step.classList.add('active');
  //   step.innerHTML = `<i class="fa-solid fa-check"></i>`;
  // } else {
  //   step.classList.remove('pending');
  //   step.classList.remove('active');
  //   step.innerHTML = st;
  // }
  // if (st == active) {
  //   steps[i - 1].classList.remove('pending');
  //   sleep(200);
  //   steps[i - 1].classList.add('active');
  //   sleep(200)
  //   progressBar.style.width = ((active - 1) / (steps.length - 1)) * 100 + "%";
  //   sleep(700);
  //   step.classList.add('pending');
  // }

  // });
  // } else {
  //   strat = active;
  //   end = active - 1;
  //   steps[start].classList.remove('pending');
  //   sleep(200);
  //   progressBar.style.width = ((active - 1) / (steps.length - 1)) * 100 + "%";
  //   sleep(700);
  //   steps[end].classList.remove('active');
  //   steps[end].innerHTML = active;
  //   sleep(200);
  //   steps[end].classList.add('pending');
  // stl = steps.length
  // for (i = 1; i <= stl; i++) {
  //   st = stl - i;
  //   if (st > active) {
  //     steps[st].classList.remove('pending');
  //   }
  //   if (st == active) {
  //     steps[st].classList.remove('pending');
  //     sleep(200)
  //     progressBar.style.width = ((active - 1) / (steps.length - 1)) * 100 + "%";
  //     sleep(700);
  //     steps[st].classList.remove('active');
  //     steps[st].innerHTML = st;
  //     sleep(200);
  //     steps[st].classList.add('pending');
  //   }
  // }
  // steps.reverse().forEach((step, i) => {
  //   st = stl - i;

  // });
  // }

  // if (last_step < active) {

  //   setTimeout(() => {
  //     // toggle active class on list items
  //     steps.forEach((step, i) => {
  //       console.log(i)
  //       step.classList.remove("pending")
  //       if (i < (active - 1)) {
  //         step.classList.add("active");
  //         step.innerHTML = `<i class="fa-solid fa-check"></i>`
  //       } else {
  //         step.classList.remove("active");
  //         step.classList.remove("pending")
  //       }
  //     });
  //   }, 500);

  //   // set progress bar width  
  //   progressBar.style.width = 
  //     ((active - 1) / (steps.length - 1)) * 100 + "%";

  //   setTimeout(() => {
  //     // toggle active class on list items
  //     steps.forEach((step, i) => {
  //       if (i == (last_step - 2)) {
  //         step.innerHTML = `<i class="fa-solid fa-check"></i>`
  //       }
  //       if (i < (active - 1)) {
  //         step.classList.remove("pending")
  //         step.classList.add("active");
  //       } else {
  //         step.classList.remove("active");
  //         step.classList.remove("pending")
  //       }
  //       if (i == (active - 1)) {
  //         step.classList.add("pending")
  //         step.innerHTML = active
  //       }
  //     });
  //   }, 500);
  // } else if (last_step > active) {
  //   // toggle active class on list items
  //   steps.forEach((step, i) => {
  //     if (i == (last_step - 1)) {
  //       step.innerHTML = active + 1
  //     }
  //     // if (i == (last_step - 2)) {
  //     //   step.innerHTML = active
  //     // }
  //     if (i < (active - 1)) {
  //       step.classList.remove("pending")
  //       step.classList.add("active");
  //     } else {
  //       step.classList.remove("active");
  //       step.classList.remove("pending")
  //     }
  //     if (i == (active - 1)) {
  //       step.classList.add("pending")
  //       step.innerHTML = active
  //     }

  //   setTimeout(() => {
  //       // set progress bar width  
  //       progressBar.style.width = 
  //       ((active - 1) / (steps.length - 1)) * 100 + "%";
  //     });
  //   }, 500);
  // }
  // // enable disable prev and next buttons
  // if (active === 1) {
  //   progressPrev.disabled = true;
  // } else if (active === steps.length) {
  //   progressNext.disabled = true;
  // } else {
  //   progressPrev.disabled = false;
  //   progressNext.disabled = false;
  // }

  last_step = active;
}

// *****************************************************************************
// --------Lodaing_layer----------
function LodingLayerForCart(stat) {
  var loadingLayer = document.getElementById('cart-section-loading-layer');

  if (stat == true) {
    if (loadingLayer.classList.contains('hidden')) {
      document.getElementById('continue-ordering-content').innerHTML = '';
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
}
// ----------------------
function CartStepSection(data_tab) {
  LodingLayerForCart(true)

  switch (data_tab) {
    case 'addressing':
      last_step = 1;
      active = 1;
      updateProgres();
      Addressing();
      break;
    case 'cheack':
      last_step = 2;
      active = 2;
      updateProgres();
      CheckoutCartItems();
      break;
    case 'receipt':
      last_step = 3;
      active = 3;
      updateProgres();
      Receipt();
      break;
    case 'payment':
      last_step = 4;
      active = 4;
      updateProgres();
      break;
  }
}
// ********************************************
// -------------------------------------------------
var sec_step = 'none';
function Ordering(sec) {
  user_authenticated = false
  axios.get('/account/_authenticated/').then(response => {
    if (response.data.authenticated == 0) {
      window.location.href = '/account/login/?next=/dashboard/cart/order/';
    } else if (response.data.authenticated == 1) {
      user_authenticated = true;
    }
  }).catch(error => {
    Loger.AddError('خطایی در سرور رخ داد. در حال بارگذاری مجدد صفحه...')
    window.location.reload();
  });

  const newPath = '/dashboard/cart/order/';
  history.pushState(null, '', newPath);

  switch (sec) {
    case 'auto':
      ContinueCart();
      break;
    case 'load':
      switch (sec_step) {
        case 'OP':
          Addressing();
          break;
        case 'AD':
          Addressing();
          break;
        case 'CO':
          CheckoutCartItems();
          break;
        case 'RC':
          Receipt();
          break;
        case 'PA':
          break;
        case 'CA':
          Addressing();
          break;
          break;
        case 'ER':
          Addressing();
          break;
          break;
        default:
          Loger.Error();
          break;
      }
      break;
    default:
      Ordering('auto');
      break;
  }
}

function scroll_to_top_of_section() {
  const scroll_element = document.getElementById('section-bar-id').getBoundingClientRect().top + window.scrollY - 100;
  // scroll_element.scrollIntoView({ behavior: 'smooth', block: 'start' });
  window.scrollTo({
    top: scroll_element,
    behavior: 'smooth'
  });
}
window.onload = function () {
  scroll_to_top_of_section();
};
function ContinueCart() {
  LoadingLayerToggle(true);
  scroll_to_top_of_section();
  var continue_cart_url = '/cart/_continue_ordering/';
  axios.get(continue_cart_url).then(response => {
    LoadingLayerToggle(false);
    document.getElementById('content').innerHTML = response.data.content;
    sec_step = response.data.step;
    LodingLayerForCart(true);
    last_step = 1;
    active = 1;
    updateProgres();
    Ordering('load');
  }).catch(error => {
    sec_step = 'none';
    Loger.ConnectionError();
  });
}


function truncateString(str, num) {
  if (str.length > num) {
    return str.substring(0, num) + '...';
  } else {
    return str;
  }
}

// ------------------------------------------------
function Addressing() {
  var addressing_url = '/cart/_addressing_package/';

  const newPath = '/dashboard/cart/order/addressing/';
  history.pushState(null, '', newPath);


  axios.get(addressing_url).then(response => {
    LodingLayerForCart(false);
    document.getElementById('continue-ordering-content').innerHTML = response.data;
    addressing_input_();
  }).catch(error => {
    Loger.ConnectionError();
  });
}
let address_selected = false;
function selectRadio(radioId) {
  // var btns = document.querySelectorAll('.radio-btn')
  var options = document.querySelectorAll(`.select-address`);
  // btns.forEach((btn) => {
  //   if (btn.id == `radio-btn-${radioId}`) {
  //     btn.checked = true;
  //   } else {
  //     btn.checked = false;
  //   }
  // });
  options.forEach((opt) => {
    if (opt.id == `select-address-${radioId}`) {
      opt.querySelector(`.radio-btn`).checked = true;
      if (!opt.classList.contains('selected')) {
        opt.classList.add('selected');
      }
      if (document.getElementById('confirm-address-and-continue').classList.contains('disabled')) {
        document.getElementById('confirm-address-and-continue').classList.remove('disabled');
      }
    } else {
      opt.querySelector(`.radio-btn`).checked = false;
      if (opt.classList.contains('selected')) {
        opt.classList.remove('selected');
      }
    }
  });
}

function addressing_input_() {
  let address_title = false;
  let address_addr = false;
  document.getElementById('add-address-title').addEventListener('input', function () {
    const value = this.value;
    if (value.length >= 4) {
      address_title = true;
    } else {
      address_title = false;
    }
    if (address_title && address_addr) {
      document.getElementById('submit-add-address').classList.remove('disabled');
    } else {
      document.getElementById('submit-add-address').classList.add('disabled');
    }
  });
  document.getElementById('add-address-addr').addEventListener('input', function () {
    const value = this.value;
    if (value.length >= 15) {
      address_addr = true;
    } else {
      address_addr = false;
    }
    if (address_title && address_addr) {
      document.getElementById('submit-add-address').classList.remove('disabled');
    } else {
      document.getElementById('submit-add-address').classList.add('disabled');
    }
  });

}

let messaged = false
function add_message_to_addressing(message, cls) {
  if (messaged) {
    document.getElementById('add-address-form-message').remove();
  } else {
    messaged = true;
  }
  document.getElementById('add-address-form').insertAdjacentHTML('afterbegin', `<div id="add-address-form-message" class="${cls}">
    <section></section>
    <span id="add-address-form-message-content">${message}</span>
</div>`);
  setTimeout(() => {
    document.getElementById('add-address-form-message').remove();
    messaged = false;
  }, 10000);
}
// let edit_flag = false;
// let editing_id = 0;
// function edit_address(id) {
//   edit_flag = true;
//   editing_id = id;
//   const title = document.getElementById('add-address-title');
//   const address = document.getElementById('add-address-addr');


//   var opt = document.getElementById(`select-address-${id}`);
//   var opt_title = opt.querySelector('.address-title').textContent;
//   var opt_addr = opt.querySelector('.address').textContent;

//   title.value = opt_title;
//   address.value = opt_addr;
//   document.getElementById('submit-add-address').innerHTML = 'ثبت تغییرات';
// }
function delete_address(id) {
  var delete_url = '/cart/_addressing/_delete_address/';

  const fd = new FormData();
  fd.append('csrfmiddlewaretoken', document.getElementById('add-address-form').children.namedItem('csrfmiddlewaretoken').value);
  fd.append('id', id);

  axios.post(delete_url, fd)
    .then(response => {
      if (response.data.success == 1) {
        add_message_to_addressing('عملیات با موفقیت انجام شد.', 'message-success');
        var wbd = document.getElementById(`select-address-${id}`);
        if (wbd.querySelector('.radio-btn').checked) {
          address_selected = false;
          if (!document.getElementById('confirm-address-and-continue').classList.contains('disabled')) {
            document.getElementById('confirm-address-and-continue').classList.add('disabled');
          }
        }
        wbd.remove();
        fm = document.getElementById('choose-address-form');
        if (fm.children.length == 1) {
          document.getElementById('addresses').insertAdjacentHTML('afterbegin', `<section id="emtpy-address">هیچ ادرسی برای شما ثبت نشده است.</section>`);
        }
      } else {
        add_message_to_addressing('عملیات با خطا مواجه شد.', 'message-error');
      }
    }).catch(error => {
      Loger.ConnectionError();
    });



}
function add_address() {
  var btn = document.getElementById('submit-add-address');
  btn.style.width = '50px';
  btn.style.borderRadius = '25px';
  btn.innerHTML = `<i class="fa-solid fa-rotate"></i>`;
  btn.classList.add('disabled');


  var addressing_url = '/cart/_addressing/_add_address/';

  const title_el = document.getElementById('add-address-title');
  const title = title_el.value;
  const address_el = document.getElementById('add-address-addr');
  const address = address_el.value;

  const fd = new FormData();
  fd.append('csrfmiddlewaretoken', document.getElementById('add-address-form').children.namedItem('csrfmiddlewaretoken').value);
  fd.append('title', title);
  fd.append('address', address);
  // if (edit_flag) {
  //   fd.append('edit_flag', true);
  //   fd.append('id', editing_id);
  //   addressing_url = '/cart/_addressing/_edit_or_delete_address/';

  //   axios.post(addressing_url, fd)
  //   .then(response => {
  //     btn.style.width = '100%';
  //     btn.style.borderRadius = '10px';
  //     btn.innerHTML = `ثبت آدرس`;
  //     title_el.value = '';
  //     address_el.value = '';
  //     btn.classList.remove('disabled');
  //     if (response.data.success == 1) {
  //       add_message_to_addressing('عملیات با موفقیت انجام شد.', 'message-success');
  //       var item = response.data.content;
  //       fm = document.getElementById(`select-address-${editing_id}`);
  //       fm.querySelector('.address-title').innerHTML = item.title;
  //       fm.querySelector('.address').innerHTML = item.address;
  //     } else if (response.data.success == 0 && response.data.code == 5) {
  //       add_message_to_addressing('تعداد ادرس های ثبت شده شما به حداکثز رسیده است', 'message-error');
  //     } else if (response.data.success == 0 && response.data.code == 3) {
  //       add_message_to_addressing('این عنوان را قبلا ثبت کردهاید.', 'message-error');
  //     } else {
  //       console.log(response.data)
  //       add_message_to_addressing('عملیات با خطا مواجه شد.', 'message-error');
  //     }
  //   }).catch(error => {
  //     console.log(`Error: ${error}`)
  //   });

  // }
  axios.post(addressing_url, fd)
    .then(response => {
      btn.style.width = '100%';
      btn.style.borderRadius = '10px';
      btn.innerHTML = `ثبت آدرس`;
      btn.classList.remove('disabled');
      if (response.data.success == 1) {
        add_message_to_addressing('عملیات با موفقیت انجام شد.', 'message-success');
        var item = response.data.content;
        fm = document.getElementById('choose-address-form');
        if (fm.children.length == 1) {
          document.getElementById('emtpy-address').remove();
        }
        fm.insertAdjacentHTML('afterbegin', `<div id="select-address-${item.id}" class="select-address" onclick="selectRadio('${item.id}')">
                    <input class="radio-btn" type="radio" id="radio-btn-${item.id}" name="address" value="${item.id}">
                    <div class="name-and-date">
                        <p>${truncateString(item.title, 15)}</p>
                        <span>${item.date}</span>
                    </div>
                    <section class="address">
                        ${truncateString(item.address, 70)}
                    </section>
                    <button onclick="delete_address(${item.id})" type="button" class="delete-address"><i class="fa-solid fa-trash"></i></button>
                </div>`);
        selectRadio(item.id);
        document.getElementById('add-address-title').value = '';
        document.getElementById('add-address-addr').value = '';
      } else if (response.data.success == 0 && response.data.code == 5) {
        add_message_to_addressing('تعداد ادرس های ثبت شده شما به حداکثز رسیده است', 'message-error');
      } else if (response.data.success == 0 && response.data.code == 3) {
        add_message_to_addressing('این عنوان را قبلا ثبت کردهاید.', 'message-error');
      } else {
        add_message_to_addressing('عملیات با خطا مواجه شد.', 'message-error');
      }
    })
    .catch(error => {
      btn.style.width = '100%';
      btn.style.borderRadius = '10px';
      btn.innerHTML = `ثبت آدرس`;
      btn.classList.remove('disabled');
      Loger.ConnectionError();
    });
}
function submit_address() {
  let addr_selected = document.querySelector('.selected').querySelector('.radio-btn').value;

  const submit_address_url = '/cart/_addressing_package/';

  const fd = new FormData();
  fd.append('csrfmiddlewaretoken', document.getElementById('add-address-form').children.namedItem('csrfmiddlewaretoken').value);
  fd.append('id', addr_selected);

  axios.post(submit_address_url, fd)
    .then(response => {
      if (response.data.success == 1) {
        LodingLayerForCart(true);
        sec_step = response.data.step;
        Ordering('auto');
      } else {
        add_message_to_addressing('خطای داخلی رخ داد!', 'message-error');
      }
    }).catch(error => {
      Loger.ConnectionError();
    });
}
// ***************
function CheckoutCartItems() {
  active = 2;
  updateProgres();
  var checkout_url = '/cart/_check_cart_items/';

  const newPath = '/dashboard/cart/order/checkout/';
  history.pushState(null, '', newPath);


  axios.get(checkout_url).then(response => {
    LodingLayerForCart(false);
    document.getElementById('continue-ordering-content').innerHTML = response.data;
  }).catch(error => {
    Loger.ConnectionError();
  });
}
function submit_checkout_items() {
  const submit_checkout_url = '/cart/_check_cart_items/';

  const fd = new FormData();
  fd.append('csrfmiddlewaretoken', document.getElementById('checkout-submit-form').children.namedItem('csrfmiddlewaretoken').value);
  fd.append('accept', true);

  axios.post(submit_checkout_url, fd)
    .then(response => {
      if (response.data.success == 1) {
        LodingLayerForCart(true);
        sec_step = response.data.step;
        Ordering('auto');
      } else {
        Loger.ServerError();
      }
    }).catch(error => {
      Loger.ConnectionError();
    });
}
// ***************
function Receipt() {
  active = 3;
  updateProgres();
  var receipt_url = '/cart/_receipt/';

  const newPath = '/dashboard/cart/order/receipt/';
  history.pushState(null, '', newPath);

  axios.get(receipt_url).then(response => {
    LodingLayerForCart(false);
    document.getElementById('continue-ordering-content').innerHTML = response.data;
    // load_html2pdf();
  }).catch(error => {
    Loger.ConnectionError();
  });
}

function load_html2pdf() {
  import('html2pdf.bundle.min.js')
    .then((html2pdf) => {
      window.html2pdf = html2pdf.default;
    })
    .catch(error => {
      Loger.Failed();
      Loger.AddError('Error loading html2pdf', `<i class="fa-solid fa-triangle-exclamation"></i>`);
    });

  import('jspdf.min.js')
    .then((jspdf) => {
      window.jspdf = jspdf.default;
    })
    .catch(error => {
      Loger.Failed();
      Loger.AddError('Error loading jspdf', `<i class="fa-solid fa-triangle-exclamation"></i>`);
    });
}

function LodingLayerDuringSavePdf(stat) {
  var loadingLayer = document.getElementById('cart-section-loading-layer');

  if (stat == true) {
    if (loadingLayer.classList.contains('hidden')) {
      document.getElementById('continue-ordering-content').classList.add('hidden');
      loadingLayer.classList.remove('hidden');
    }
    return true
  } else if (stat == false) {
    if (!loadingLayer.classList.contains('hidden')) {
      loadingLayer.classList.add('hidden');
      document.getElementById('continue-ordering-content').classList.remove('hidden');
    }
    return true
  } else {
    return false
  }
}

function prev_step() {
  if (active == 1) {
    window.location.href = '/dashboard/cart/';
  }
  const prev_step_url = '/cart/_continue_ordering/';

  fd = new FormData()

  // fd.append('csrfmiddlewaretoken', document.getElementById('continue-ordering-csrf').children.namedItem('csrfmiddlewaretoken').value);

  axios.post(prev_step_url, fd)
    .then(response => {
      if (active != 1) {
        active = active - 1;
      }
      updateProgres();
      sec_step = response.data.step;
      Ordering('auto');
    }).catch(error => {
      Loger.ConnectionError();
    });
}

function save_factor(uid) {
  LodingLayerDuringSavePdf(true);
  // The ID of the element you want to save as PDF
  const element = document.getElementById('receipt-factor').cloneNode(true);
  const opt = {
    margin: 0.1,
    width: 190,
    filename: `KALANTARI-Receipt--order-${uid}.pdf`,
    image: { type: 'jpeg', quality: 1 },
    html2canvas: { scale: 5 },
    jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
  };


  // Generate the PDF
  // Use jQuery to change the font size of the element
  $(element).css("font-size", "0.5rem");

  // Then call html2pdf to generate the PDF
  html2pdf().from(element).set(opt).toPdf().get('pdf').then(function (pdf) {
    // Reset the font size back to the original after the PDF is generated
    $(element).css("font-size", "1rem");
  }).save();
  setTimeout(() => {
    LodingLayerDuringSavePdf(false);
  }, 1000);

}



