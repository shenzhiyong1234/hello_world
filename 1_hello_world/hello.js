// var addon = require('bindings')('hello');

var addon = require('./build/Release/addon.node')

console.log(addon.test('hello world')); 

console.log('---------',addon.num('hello world')); 

