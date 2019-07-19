var compressor = require('yuicompressor');
var fs = require('fs');

compressor.compress('/home/domizzi/dev/pyincome/etc/chrome_faye/app.js', {
    //Compressor Options:
    charset: 'utf8',
    type: 'js',
    nomunge: true,
    'line-break': 80
}, function(err, data, extra) {
    //err   If compressor encounters an error, it's stderr will be here
    //data  The compressed string, you write it out where you want it
    //extra The stderr (warnings are printed here in case you want to echo them
    if (err) throw err
    fs.writeFileSync('./output.js', data)
});
