const express = require('express');
const { Server } = require('socket.io');
// const { join }= require('node:path');
const {
    createServer
} = require('node:http');
const mongoose = require('mongoose');
const http = require('http');

const app = express();
const server = createServer(app)
const io = new Server(server, {
    connectionStateRecovery: {}
});

app.use(express.static(__dirname));

const Message = require('./model/message');
const User = require('./model/user');


//Kết nối csdl
const connectDB = async () => {
    try {
        await mongoose.connect('mongodb://127.0.0.1:27017/chat');
        console.log('Kết nối MongoDB thành công');
    } catch (err) {
        console.error('Lỗi khi kết nối cơ sở dữ liệu:', err);
    }
};
connectDB();

//HÀM GỬI TIN NHẮN ĐẾN RAG 
function sendMessageToPython(message) {
    const postData = JSON.stringify({ message });

    const options = {
        hostname: '127.0.0.1',
        port: 5000,
        path: '/chat-rag',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(postData)
        }
    };

    //nhận tin nhắn từ python rag server
    const req = http.request(options, (res) => {
        res.setEncoding('utf8');
        res.on('data', (chunk) => {
            const responseData = JSON.parse(chunk);
            rag_message = responseData.response['result'];
            console.log('phản hồi từ RAG:', responseData.response['result']);
            
            //gửi tin nhắn đến người dùng
            socket.emit('server_send_to_client', rag_message);

        });
    });

    req.on('error', (e) => {
        console.error(`Problem with request: ${e.message}`);
    });

    req.write(postData);
    req.end();
}




app.get('/', (req, res) => {
    console.log(__dirname)
    res.sendFile(__dirname + '/view/user.html');
    // res.sendFile('../index.php');
});

app.get('/admin-chat', (req, res) => {
    res.sendFile(__dirname + '/view/admin_chat.html');
})

//API lấy user
app.get('/api/get_user', async (req, res) => {
    try {
        const user_data = await User.find({ deleted: false });
        res.status(200).json(user_data);
    } catch (error) {
        // Xử lý lỗi nếu có
        console.error('Lỗi:', error);
        res.status(500).json({ success: false, error: error.message });
    }
});

app.get('/api/update_deleted_user', async (req, res) => {
    const userid = req.query.userid;
    try {
        const updatedUser =  await User.updateOne(
            { $or: { userID: userid}},
            { $set: { deleted: true } } 
        );

        if (!updatedUser) {
            return res.status(404).json({ success: false, message: 'User not found' });
        }

        return res.status(200).json({ success: true, message: 'Đã xóa user' });
    } catch (error) {
        console.error('Error:', error);
        return res.status(500).json({ success: false, error: error.message });
    }
})
app.get('/api/update_deleted_user_false', async (req, res) => {
    const userid = req.query.userid;
    try {
        const updatedUser =  await User.updateOne(
            { $or: { userID: userid}},
            { $set: { deleted: false } } 
        );

        if (!updatedUser) {
            return res.status(404).json({ success: false, message: 'User not found' });
        }

        return res.status(200).json({ success: true, message: 'Cập nhật lại trạng thái deleted user false' });
    } catch (error) {
        console.error('Error:', error);
        return res.status(500).json({ success: false, error: error.message });
    }
})

// API lấy tin nhắn của user theo id, và tin nhắn của admin gửi đến người dùng theo id
app.get('/api/get_mess_user', async (req, res) => {
    console.log('GỌI API lấy tin nhắn');
    //userid
    const userid = req.query.userid;

    const user_mess_data = await Message.find({
        $or: [{
            senderID: userid,
            deleted: false,
        }, {
            receiverID: userid,
            type: 1,
            deleted: false,
        }]
    })
    res.status(200).json(user_mess_data);
})

app.delete('/api/delete_mess', async (req, res) => {
    try {
        const userId = req.query.userid;
        if (!userId) {
            return res.status(400).json({ success: false, message: 'Cần có userID' });
        }

        // Cập nhật thuộc tính 'deleted' của người dùng thành false
        const result = await Message.updateMany(
            { $or: [{ senderID: userId},{receiverID: userId} ]},
            { $set: { deleted: true } } 
        );

        if (result.nModified === 0) {
            return res.status(404).json({ success: false, message: 'Không tìm thấy tin nhắn' });
        }

        // Phản hồi với thông báo cập nhật thành công
        res.status(200).json({ success: true, message: `Đã xóa tin nhắn người dùng` });
    } catch (error) {
        // Xử lý lỗi nếu có
        console.error('Lỗi:', error);
        res.status(500).json({ success: false, error: error.message });
    }
});


app.get('/api/latest_user_mess', async function (req, res) {
    try {
        const idAdmin ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-';
        
        const user_data = await Message.find({
            deleted: false,
            senderID: { $ne: idAdmin }
        }).sort({ timestamp: -1 });

        const uniqueSenderIDs = new Set();

        user_data.forEach(message => {
            
            if (!uniqueSenderIDs.has(message.senderID)) {
                uniqueSenderIDs.add(message);
            }
            
        });
        res.status(200).json(Array.from(uniqueSenderIDs));
    } catch (error) {
        console.error('Lỗi:', error);
        res.status(500).json({ success: false, error: error.message });
    }
});




io.on('connection', (socket) => {
    //CLIENT
    //nhận tin nhắn trực tiếp từ admin
    socket.on('admin_send_to_server', async (msg) => {

        const vietnamTime = new Date(new Date().getTime() + 7 * 60 * 60 * 1000).toISOString();
        var data = {
            'senderID': msg.uID,
            'senderName': msg.uName,
            'receiverID': msg.receiverID,
            'message': msg.message,
            'timestamp': vietnamTime,
            'type': 1,
            'deleted': false
        }

        //Thêm messgae vào DB
        console.log(data);
        const newMessageAdmin = new Message(data);
        try {
            await newMessageAdmin.save();
        } catch (err) {
            console.log('Loi them vao db')
        }
        
        // gửi đến người dùng
        io.emit(`${msg.receiverID}`, data);
    })

    //Nhận thông báo đang gõ tin nhắn
    socket.on('alert_typing', (alert_typing) => {
        console.log(alert_typing)
    })

    //nhận tin nhắn từ người dùng
    socket.on('client_send_to_server', async (msg) => {
        const vietnamTime = new Date(new Date().getTime() + 7 * 60 * 60 * 1000).toISOString();
        adminID = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-'
        console.log("Tin nhắn từ người dùng: " + msg.message)
        console.log("Option chat: " + msg.option_chat)

        var data = {
            'senderID': msg.uID,
            'senderName': msg.uName,
            'receiverID': adminID,
            'message': msg.message,
            'timestamp': vietnamTime,
            'deleted': false,
            'option_chat': msg.option_chat,
        }

        isbot = JSON.stringify(data.option_chat);
        // console.log(typeof (isbot));
        //gửi tin nhắn đến rasa
        if (isbot === '\"bot_ctump\"') {

            const postData = JSON.stringify({ message: msg.message });
            // Các tùy chọn cho yêu cầu HTTP
            const options = {
                hostname: '127.0.0.1', // Địa chỉ máy chủ
                port: 5005, // Cổng của Rasa webhook
                path: '/webhooks/rest/webhook',
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Content-Length': Buffer.byteLength(postData)
                }
            };

            const req = http.request(options, (res) => {
                res.setEncoding('utf8');
                res.on('data', (chunk) => {
                    try {
                        const responseData = JSON.parse(chunk);
                        // Tin nhắn phản hồi từ chatbot
                        const dataBot = {
                            message: responseData[0].text,
                        };
                        socket.emit('server_send_to_client', dataBot);
                    } catch (e) {
                        console.error('Error parsing JSON response:', e);
                        const dataBot = {
                            message: 'Xin lỗi tôi không có thông tin, bạn mô tả thông tin chi tiết hơn được không',
                        };
                        socket.emit('server_send_to_client', dataBot);
                    }
                });
            });

            req.on('error', (e) => {
                console.error(`Problem with request: ${e.message}`);
                const dataBot = {
                    message: 'Server đang bảo trì, vui lòng thử lại sau',
                };
                socket.emit('server_send_to_client', dataBot);
            });
            req.write(postData);
            req.end();
        } 

        //GỬI TIN NHẮN ĐẾN RAG
        if (msg.option_chat == 'chat_rag'){
        //     console.log('Gửi đến RAG server')
        //     console.log(msg.message)
        //     // sendMessageToPython(msg.message)

        //     const postData = JSON.stringify({'message': msg.message});

        //     const options = {
        //         hostname: '127.0.0.1',
        //         port: 5000,
        //         path: '/chat-rag',
        //         method: 'POST',
        //         headers: {
        //             'Content-Type': 'application/json',
        //             'Content-Length': Buffer.byteLength(postData)
        //         }
        //     };
        //     //nhận tin nhắn từ python rag server
        //     const req = http.request(options, (res) => {
        //         res.setEncoding('utf8');
        //         res.on('data', (chunk) => {
        //             try {
        //                 const responseData = JSON.parse(chunk);
        //                 if (responseData && responseData.response && responseData.response['result']) {
        //                     //tin nhắn nhận từ rag server
        //                     const rag_message = responseData.response['result'];
        //                     console.log('phản hồi từ RAG:', rag_message);

        //                     //chuyển mess từ rag thành json gửi về client
        //                     mess = {message : rag_message}

        //                     socket.emit('server_send_to_client', mess);
        //                 } else {
        //                     console.error('Response or result is undefined:', responseData);
        //                     socket.emit('server_send_to_client', 'Phản hồi từ server không hợp lệ');
        //                 }
        //             } catch(e){
        //                 console.error('Error parsing JSON response:', e);
        //                 socket.emit('server_send_to_client', 'Đã xảy ra lỗi, vui lòng thử lại sau.');
        //             }
        //         });
        //     });
        //     req.on('error', (e) => {
        //         console.error(`Problem with request: ${e.message}`);
        //     });
        //     req.write(postData);
        //     req.end();
        }

        //Gửi tin nhắn đên admin
        if(msg.option_chat =='admin_ctump') {            
            //thêm người dùng
            try {
                //kiểm tra người dùng tồn tại
                const getUser = await User.findOne({
                    userID: msg.uID
                });
                if (!getUser) {
                    var user = {
                        'userID': msg.uID,
                        'userName': msg.uName,
                        'lastMessage': msg.message,
                        'status': 'on',
                        'deleted': false
                    }
                    const userModel = new User(user);
                    await userModel.save();
                    console.log('Thêm người dùng thành công');
                } else {
                    //cập nhật tin nhắn cuối
                    await User.findOneAndUpdate({
                        userID: msg.uID
                    }, {
                        $set: {
                            lastMessage: msg.message
                        }
                    })
                }
            } catch (err) {
                console.log('Lỗi khi thêm user', err)
            }
            //gửi lại đoạn chat client vừa nhập
            socket.emit('server_send_to_client', msg.message);
            //gửi đoạn chat người dùng đến admin
            io.emit('server_send_to_admin', data);
            // lưu vào db
            const newMessage = new Message(data);
            try {
                await newMessage.save();
                // console.log('Đã thêm tin nhắn');
            } catch (err) {
                console.log('Lỗi khi thêm dữ liệu: ', err);
            }
        }
    });
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});