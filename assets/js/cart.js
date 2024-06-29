class CartClass {
    constructor(order) {
      this.order = order;
      this.created = new Date().getTime();
      this.ChangeCountURL = '/cart/change/count/';
      this.DeleteItemURL = '/cart/item/delete/';
    }
    increase(id) {
      const increase_url = this.ChangeCountURL;
      // this.csrfmiddlewaretoken = document.getElementById(`increase-${id}`).children.namedItem('csrfmiddlewaretoken').value;
      const fd = new FormData();
      fd.append('csrfmiddlewaretoken', this.csrfmiddlewaretoken)
      fd.append('uid', id)
      fd.append('action', '+')
      axios.post(increase_url, fd)
      .then(response => {
          console.log(response)
          if (response.data.status === 'ok') {
            if (response.data.count == 1) {
              document.getElementById(`decrease-${id}`).children.namedItem('submit').classList.add('disabled');
            } else {
              document.getElementById(`decrease-${id}`).children.namedItem('submit').classList.remove('disabled');
            }
            if (response.data.max === 'true') {
              document.getElementById(`increase-${id}`).children.namedItem('submit').classList.add('disabled');
              document.getElementById(`count-section-${id}`).insertAdjacentHTML('beforeend', `<p id="max-${id}">حداکثر</p>`);
            }
            document.getElementById(`count-${id}`).innerText = response.data.count;
            update_order_info();
          }
        })
        .catch(error => {
          // Handle errors
          console.error('Error submitting form:', error);
        });
    }
    decrease(id) {
      const decrease_url = this.ChangeCountURL;
      // this.csrfmiddlewaretoken = document.getElementById(`decrease-${id}`).children.namedItem('csrfmiddlewaretoken').value;
      const fd = new FormData();
      fd.append('csrfmiddlewaretoken', this.csrfmiddlewaretoken)
      fd.append('uid', id)
      fd.append('action', '-')
      axios.post(decrease_url, fd)
      .then(response => {
          console.log(response)
          if (response.data.status === 'ok') {
            if (response.data.count == 1) {
              document.getElementById(`decrease-${id}`).children.namedItem('submit').classList.add('disabled');
            } else {
              document.getElementById(`decrease-${id}`).children.namedItem('submit').classList.remove('disabled');
            }
            if (response.data.max === 'false' && document.getElementById(`increase-${id}`).children.namedItem('submit').classList.contains('disabled')) {
              document.getElementById(`increase-${id}`).children.namedItem('submit').classList.remove('disabled');
              document.getElementById(`max-${id}`).remove();
            }
            document.getElementById(`count-${id}`).innerText = response.data.count;
            update_order_info();
          }
        })
        .catch(error => {
          // Handle errors
          console.error('Error submitting form:', error);
        });
    }
    delete(id) {
      const delete_item_url = this.DeleteItemURL;
      // this.csrfmiddlewaretoken = document.getElementById(`delete-${id}`).children.namedItem('csrfmiddlewaretoken').value;
      const fd = new FormData();
      fd.append('csrfmiddlewaretoken', this.csrfmiddlewaretoken)
      fd.append('uid', id)
      axios.post(delete_item_url, fd)
      .then(response => {
          console.log(response)
          if (response.data.status === 'ok') {
            if (document.getElementById(`cart-${id}`)) {
              document.getElementById(`cart-${id}`).remove();
              var cartSectionElement = document.getElementById('cart-items-ul');
              if (cartSectionElement.childElementCount == 0) {
                cartSectionElement.innerHTML = `<div id="empty-cart">
                <p>هیچ کالایی در سبد خرید شما وجود ندارد.</p>
                <a href="/list/man/">صفحه محصولات</a>
            </div>`
              }
            }
            if (document.getElementById(`${id}`)) {
              document.getElementById(`${id}`).remove();
            }
            if (document.getElementById(`menu-${id}`)) {
              document.getElementById(`menu-${id}`).remove();
            }
            update_order_info();
          }
        })
        .catch(error => {
          // Handle errors
          console.error('Error submitting form:', error);
        });
    }
}
// ----------------------------------------------
const cart = new CartClass('create')

function update_order_info() {
  url = '/cart/order/info/'
  axios.get(url, {
  }).then(response => {
      document.getElementById('cart-price').innerText = `${response.data.price}`;
      document.getElementById('cart-discount').innerText = `${response.data.discount}`;
      document.getElementById('cart-tax').innerText = `${response.data.tax}`;
      document.getElementById('cart-final-price').innerText = `${response.data.final_price}`;
  }).catch(error => {
    console.error('Error sending GET request:', error);
  });
}