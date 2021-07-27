var https = require('https');

var options = {
    host: 'swapi.co',
    path: '/api/people/1/',
    headers: {
        'Accept': 'application/json'
    }
};
https.get(options, function (res) {
    var json = '';

    res.on('data', function (chunk) {
        json += chunk;
    });

    res.on('end', function () {
        if (res.statusCode === 200) {
            try {
                var data = JSON.parse(json);
                // data is available here:
                console.log(json);
            } catch (e) {
                console.log('Error parsing JSON!');
            }
        } else {
            console.log('Status:', res.statusCode);
        }
    });
}).on('error', function (err) {
    console.log('Error:', err);
});