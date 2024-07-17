

function remove_favorite(uid) {
    const url = '/favorite/bookmark/';
    const fd = new FormData();
    fd.append('csrfmiddlewaretoken', header_csrftoken);
    fd.append('uid', uid);
    axios.post(url, fd)
    .then(response => {
      if (response.data.status === 'ok') {
        if (response.data.message === 'removed') {
          var favorite_item = document.getElementById(`favorite-item-${uid}`);
          favorite_item.remove();
        }
        if (document.getElementById('favorite-items-container').children.length == 0) {
            document.getElementById('favorite-items-ul').insertAdjacentHTML('afterbegin', `<div id="empty-favorite">
            <p>هیچ کالایی در لیست سما وجود ندارد.</p>
            <a href="/list/man/">صفحه محصولات</a>
        </div>`)
        }
      }
    })
    .catch(error => {
      // Handle errors
      Loger.ConnectionError();
    });
}

function add_to_cart(id) {
    const delete_item_url = '/cart/item/add/';
    const fd = new FormData();
    fd.append('csrfmiddlewaretoken', header_csrftoken)
    fd.append('uid', id)
    axios.post(delete_item_url, fd)
    .then(response => {
        if (response.data.status === 'ok') {
            var cart_control = document.getElementById(`favorite-item-control-${id}`)
            document.getElementById(`add-to-cart-${id}`).remove();
            cart_control.insertAdjacentHTML('afterBegin', `<button id="remove-from-cart-${id}" onclick="remove_from_cart(${id})" class="remove-from-cart" type="button" name="add-to-cart">حذف از سبد خرید</button>`)
        }
    })
    .catch(error => {
        // Handle errors
        Loger.ConnectionError();
    });
}

function remove_from_cart(id) {
    const delete_item_url = '/cart/item/delete/';
    const fd = new FormData();
    fd.append('csrfmiddlewaretoken', header_csrftoken)
    fd.append('uid', id)
    axios.post(delete_item_url, fd)
    .then(response => {
        if (response.data.status === 'ok') {
            var cart_control = document.getElementById(`favorite-item-control-${id}`)
            document.getElementById(`remove-from-cart-${id}`).remove();
            cart_control.insertAdjacentHTML('afterBegin', `<button id="add-to-cart-${id}" onclick="add_to_cart(${id})" class="add-to-cart" type="button" name="add-to-cart">افزودن به سبد خرید</button>`)
        }
    })
    .catch(error => {
        // Handle errors
        Loger.ConnectionError();
    });
}

