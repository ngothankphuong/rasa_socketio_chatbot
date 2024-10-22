const mongoose = require('mongoose');

const massageSchema = new mongoose.Schema({
    senderID : {type:String, require: true },
    senderName : {type:String, require: true },
    receiverID : {type:String, require: true },
    message : {type:String, require: true },
    timestamp : {type:String, require:  true },
    type : { type:Number },
    deleted : {type:Boolean}

})

const message = mongoose.model('message', massageSchema);

module.exports = message;