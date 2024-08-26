/**
 * This is the end page that is shown after the experiment
 */
function endPage() {
    let link = '';
    let atag = '';
     let interval;
    // the value compared below is hardcoded in the .env file produced by Copier
    // if you modify the value in the .env file or your env vars to a completion code provided by Prolific
    // a link will be presented to users that redirects to Prolific with the completion code populating
    // a query string parameter
    if (process.env.NODE_APP_completionCode !== 'ABCD1234') {
        link = 'https://app.prolific.com/submission/complete?cc=${process.env.NODE_APP_completionCode}';
        let countdown = 5;
        atag = `<a href=>Click here to redirect to Prolific.</a> You will be redirected automatically in <span id="countdown">${countdown}</span> seconds...`;
        interval = setInterval(() => {
            countdown -= 1;
            document.getElementById('countdown').innerText = countdown;
    }, 1000);

        setTimeout(() => {
            clearInterval(interval);
            window.location.href = link;
        }, 5000);
    }
    let html = `<div class="msg">Thank you for participating in our experiment.<br/>${atag}</div>`;

    document.body.innerHTML = html;
}

function waitPage() {
    document.body.innerHTML = `<div class="msg">Please wait until the data has been transferred.<br>This can take up to a minute.</div>`
}

function errorPage() {
    document.body.innerHTML = "<p>We are sorry, there has been an unexpected technical issue.<br/>Thank you for your understanding.</p><aclassName='App-link'href='https://app.prolific.co'target='_blank'rel='noopener noreferrer'>Prolific</a>"
}

export { endPage, waitPage, errorPage };
