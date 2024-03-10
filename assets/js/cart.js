class CartClass {
    constructor(order) {
      this.order = order;
      this.created = new Date().getTime();
      this.ChangeCountURL = '/cart/change/count/';
      this.DeleteItemURL = '/cart/delete/item/';
    }
    increase(id) {
      const increase_url = this.ChangeCountURL;
      this.csrfmiddlewaretoken = document.getElementById(`increase-${id}`).children.namedItem('csrfmiddlewaretoken').value;
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
            document.getElementById(`count-${id}`).innerText = response.data.count;
          }
        })
        .catch(error => {
          // Handle errors
          console.error('Error submitting form:', error);
        });
    }
    decrease(id) {
      const decrease_url = this.ChangeCountURL;
      this.csrfmiddlewaretoken = document.getElementById(`decrease-${id}`).children.namedItem('csrfmiddlewaretoken').value;
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
            document.getElementById(`count-${id}`).innerText = response.data.count;
          }
        })
        .catch(error => {
          // Handle errors
          console.error('Error submitting form:', error);
        });
    }
    delete(id) {
      const delete_item_url = this.DeleteItemURL;
      this.csrfmiddlewaretoken = document.getElementById(`delete-${id}`).children.namedItem('csrfmiddlewaretoken').value;
      const fd = new FormData();
      fd.append('csrfmiddlewaretoken', this.csrfmiddlewaretoken)
      fd.append('uid', id)
      axios.post(delete_item_url, fd)
      .then(response => {
          console.log(response)
          if (response.data.status === 'ok') {
            document.getElementById(`${id}`).remove();
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