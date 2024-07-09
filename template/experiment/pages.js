/**
 * This is the end page that is shown after the experiment
 */
function endPage() {
    let link = ''
    if (process.env.REACT_APP_redirect !== '') {
        link = `<a href="${process.env.REACT_APP_redirect}">Back to prolific</a>`
    }
    let html = `<div class="msg">Thank you for participating in our experiment.<br/>${link}</div>`

    document.body.innerHTML = html
}

function waitPage() {
    document.body.innerHTML = `<div class="msg">Please wait until the data has been transferred.<br>This can take up to a minute.</div>`
}

export {endPage, waitPage};