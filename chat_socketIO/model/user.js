const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    userID : {type:String, require: true },
    userName : {type:String, require: true },
    status : {type:String, require: true },
    deleted : {type:Boolean, require: true}
})

const user = mongoose.model('user', userSchema);

module.exports = user;