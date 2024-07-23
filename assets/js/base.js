

function sleep(ms) {
    const end = Date.now() + ms;
    while (Date.now() < end) continue;
}

function copy_to_clipboard(message) {
    navigator.clipboard.writeText(`${message}`).then(function() {
        Loger.AddSuccess('آدرس کالا کپس شد');
    }).catch(function(error) {
        Loger.Failed();
    });
}

