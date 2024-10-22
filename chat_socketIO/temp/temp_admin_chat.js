const socket = io();

////////////Khởi tạo adminID
const adminID = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-';
socket.emit('adminID', adminID);

//nhận tin nhắn realtime từ người dùng
//hiển thị chat người dùng gửi đến
socket.on('server_send_to_admin', (msg) => {

    //tạo div chứa tin nhắn
    const messContainer = document.createElement('div');
    
    console.log(msg)
})

const form = document.getElementById('form-chat');
const input_chat = document.getElementById('input-chat');

//gửi tin nhắn đến server
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const input_data = input_chat.value;
    console.log(input_data);
    if (input_data) {
        socket.emit('admin_send_to_server', {
            message: input_data
        });
        input_chat.value = '';
    }
})

/////////////CALL API LẤY DANH SÁCH NGƯỜI DÙNG
document.addEventListener('DOMContentLoaded', async function (e) {
    const response = await fetch('/api/get_user');
    const users = await response.json();
    console.log(users)
    
    const listUser = document.querySelector('.list-search-user-chat');

    users.forEach(user => {
        listUser.innerHTML += `<div class="user-chat" data-username="${user.userName}">
        <div class="user-chat-img">
            <img src="https://img.freepik.com/free-vector/blue-circle-with-white-user_78370-4707.jpg"
                alt="" />
            <div class="offline"></div>
            <div>${user.userName}</div>
        </div>

        <div class="user-chat-text">
            <p class="mt-0 mb-0"><strong>${user.userName}</strong></p>
            <small>Hi, how are you?</small>
        </div>
    </div>`
    })
});


