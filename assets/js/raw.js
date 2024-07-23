class LogClass {
    constructor() {
        this.checkContainer();
    }
    checkContainer() {
        if (document.getElementById('log-container')) {
            this.container = document.getElementById('log-container');
        } else {
            document.getElementsByTagName('body')[0].insertAdjacentHTML('afterbegin', `<div id="log-container"></div>`);
        }
    }

    generateUUID() {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
            var r = Math.random() * 16 | 0,
                v = c === 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
    }

    remove_log(id) {
        var data = document.getElementById(id);
        data.style.transition = 'opacity 0.7s ease';
        data.style.opacity = '0';
        setTimeout(() => {
            data.remove();
        }, 700);
    }

    remove_auto(id) {
        var data = document.getElementById(id);
        data.style.transition = 'opacity 0.7s ease';
        setTimeout(() => {
            data.style.opacity = '0';
            setTimeout(() => {
                data.remove();
            }, 800);
        }, 5000);
    }

    active_log(id) {
        // document.getElementById(id).style.transition = 'left 0.7s ease';
        document.getElementById(id).classList.add('is-on');
        this.remove_auto(id)
    }

    add_log(el) {
        el.id = this.generateUUID();
        if (this.container.children.length >= 5) {
            this.remove_log(this.container.lastElementChild.getAttribute('id'));
        }
        this.container.insertBefore(el, this.container.firstChild);
        this.active_log(el.id)
    }

    AddError(message, i = null) {
        var data = document.createElement('div');
        data.classList = 'log log-warning';
        var data_message = document.createElement('span');
        data_message.textContent = `${message}`;
        data.appendChild(data_message);
        if (i) {       
            data.insertAdjacentHTML('beforeend', `${i}`); 
        } else {
            data.insertAdjacentHTML('beforeend', `<i class="fa-solid fa-exclamation"></i>`); 
        }
        this.add_log(data);
    }

    AddWarning(message, i = null) {
        var data = document.createElement('div');
        data.classList = 'log log-error';
        var data_message = document.createElement('span');
        data_message.textContent = `${message}`;
        data.appendChild(data_message);
        if (i) {       
            data.insertAdjacentHTML('beforeend', `${i}`); 
        } else {
            data.insertAdjacentHTML('beforeend', `<i class="fa-solid fa-triangle-exclamation"></i>`); 
        }
        this.add_log(data);
    }

    AddSuccess(message, i = null) {
        var data = document.createElement('div');
        data.classList = 'log log-success';
        var data_message = document.createElement('span');
        data_message.textContent = `${message}`;
        data.appendChild(data_message);
        if (i) {       
            data.insertAdjacentHTML('beforeend', `${i}`); 
        } else {
            data.insertAdjacentHTML('beforeend', `<i class="fa-regular fa-circle-check"></i>`); 
        }
        this.add_log(data);
    }

    ConnectionError() {
        var data = document.createElement('div');
        data.classList = 'log log-error';
        var data_message = document.createElement('span');
        data_message.textContent = `خطا در برقراری ارتباط با سرور`;
        data.appendChild(data_message);
        data.insertAdjacentHTML('beforeend', `<i class="fa-solid fa-triangle-exclamation"></i>`); 
        this.add_log(data);
    }

    ServerError() {
        var data = document.createElement('div');
        data.classList = 'log log-error';
        var data_message = document.createElement('span');
        data_message.textContent = `سرور با خطا مواجه شد`;
        data.appendChild(data_message);
        data.insertAdjacentHTML('beforeend', `<i class="fa-solid fa-circle-exclamation"></i>`); 
        this.add_log(data);
    }

    Error() {
        var data = document.createElement('div');
        data.classList = 'log log-error';
        var data_message = document.createElement('span');
        data_message.textContent = `خطایی رخ داد`;
        data.appendChild(data_message);
        data.insertAdjacentHTML('beforeend', `<i class="fa-solid fa-exclamation"></i>`); 
        this.add_log(data);
    }

    Failed() {
        var data = document.createElement('div');
        data.classList = 'log log-error';
        var data_message = document.createElement('span');
        data_message.textContent = `عملیات ناموفق بود`;
        data.appendChild(data_message);
        data.insertAdjacentHTML('beforeend', `<i class="fa-solid fa-xmark"></i>`); 
        this.add_log(data);
    }

    Success() {
        var data = document.createElement('div');
        data.classList = 'log log-success';
        var data_message = document.createElement('span');
        data_message.textContent = `عملیات با موفقست انجام شد`;
        data.appendChild(data_message);
        data.insertAdjacentHTML('beforeend', `<i class="fa-regular fa-circle-check"></i>`); 
        this.add_log(data);
    }

    Message(message) {
        var data = document.createElement('div');
        data.classList = 'log log-message';
        var data_message = document.createElement('span');
        data_message.textContent = `${message}`;
        data.appendChild(data_message);
        this.add_log(data);
    }
}
// **************************
const Loger = new LogClass()
// **************************
