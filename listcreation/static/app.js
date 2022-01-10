


/**
 * サーバー通信を行う.
 */
function api(url) {
    return new Promise((resolve, reject) => {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.onreadystatechange = function (e) {
            if (this.readyState === 4 && this.status === 200) {
                resolve(this.responseText);
            }
        }
        xhr.send();
    });
}


        api('/api/recommend_article').then(response => {
            let { company, inf } = JSON.parse(response);
            console.log(company);
    
    
    
            document.getElementById('company').innerHTML = `${company}`;
            document.getElementById('inf').innerHTML = `${inf}`;
        });

