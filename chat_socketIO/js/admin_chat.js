

const socket = io();
//Khởi tạo adminID
const adminID = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-';
socket.emit('adminID', adminID);

socket.on('server_send_to_admin', (msg) => {
    // HIỂN THỊ NGƯỜI DÙNG TRONG LIST KHI VỪA NHẬN TIN NHẮN
    const sender_div = document.querySelector(`[data-user-id="${msg.senderID}"]`);
    const userList = document.querySelector('.userList');

    // kiểm tra Id của người dùng có trên giao diện hay chưa
    if (!sender_div) {
        // hiển thị tin nhắn lên giao diện list user
        userList.insertAdjacentHTML('afterbegin',
            `<div data-user-id="${msg.senderID}">
                <div onclick="register_popup('${msg.senderID}', '${msg.senderName}')" data-user-id="${msg.senderID}" class="sidebar-name">
                    <a>
                        <img width="30" height="30" src="https://t4.ftcdn.net/jpg/02/29/75/83/360_F_229758328_7x8jwCwjtBMmC6rgFzLFhZoEpLobB6L8.jpg" />
                    <div class="chatContent">
                        <span>${msg.senderName}</span>
                        <p style="font-size: 16px;">${msg.message}</p>
                    </div>
                    <div class="status-dot '. $offline .'"><i class="fas fa-circle"></i></div>
                    </a>
                    <button id="btn-delete" class="btn btn-danger" onclick="deleteItem(event,'${msg.senderID}');">Xóa</button>
                </div>
            </div>`
        );
        try {
        $.ajax({
            type: 'GET',
            dataType: 'json',
            url: '/api/update_deleted_user_false',
            data: { userid: msg.senderID },
            success: function(response) {
                console.log(response);
            },
            error: function(err) {
                console.log(err);
            }
        });
    } catch (err) {
        console.log('Lỗi ngoài:', err);
    }
    } else {
        // người dùng đã có giao diện, chỉ thay đổi lại tin nhắn cuối
        sender_div.querySelector('p').innerHTML = msg.message;

        // di chuyển người dùng lên đầu danh sách
        sender_div.remove();
        userList.insertAdjacentHTML('afterbegin',
            `<div data-user-id="${msg.senderID}">
                <div onclick="register_popup('${msg.senderID}', '${msg.senderName}')" data-user-id="${msg.senderID}" class="sidebar-name">
                    <a>
                        <img width="30" height="30" src="https://t4.ftcdn.net/jpg/02/29/75/83/360_F_229758328_7x8jwCwjtBMmC6rgFzLFhZoEpLobB6L8.jpg" />
                    <div class="chatContent">
                        <span>${msg.senderName}</span>
                        <p style="font-size: 16px;">${msg.message}</p>
                    </div>
                    <div class="status-dot '. $offline .'"><i class="fas fa-circle"></i></div>
                    </a>
                    <button id="btn-delete" class="btn btn-danger" onclick="deleteItem(event,'${msg.senderID}');">Xóa</button>
                </div>
            </div>`
        );
    }
    
    // NẾU Ô CHAT ĐANG MỞ, HIỂN THỊ TIN NHẮN TRONG Ô CHAT
    const window_chat = document.getElementsByClassName(`mess-padding-${msg.senderID}`)[0];
    if (window_chat) {
        const newDiv = document.createElement('div');
        newDiv.innerHTML = `
        <div class="mess-user-${msg.senderID}">
            <div class="d-flex justify-content-between">
                <p class="small mb-1">${msg.senderName}</p>
                <p class="small mb-1 text-muted">${msg.timestamp}</p>
            </div>
            <div class="d-flex flex-row justify-content-start mb-1">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava5-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;">
                <div>
                    <p class="small p-2 ms-3 mb-3 rounded-3" style="background-color: #f5f6f7;">${msg.message}</p>
                </div>
            </div>
        </div>`;
        window_chat.appendChild(newDiv);
        scrollToBottom();
    }
});


    
 ///////////CALL API LẤY DANH SÁCH NGƯỜI DÙNG KHI LOAD LẠI TRANG

// document.addEventListener('DOMContentLoaded', async function () {
//     try {
//         const response = await fetch('/api/get_user');
//         const users = await response.json();
//         // console.log(users)
//         const userList = document.querySelector('.userList');
//         console.log(users);
        
//         // Duyệt qua mảng users từ cuối lên đầu
//         for (let i = users.length - 1; i >= 0; i--) {
//             const user = users[i];

//             // const latestMessageResponse = await fetch(`/api/latest_message?userId1=${adminID}&userId2=${user.userID}`);
//             // const latestMessage = await latestMessageResponse.json();
//             userList.innerHTML +=
//             `<div data-user-id="${user.userID}">
//                 <div onclick="register_popup('${user.userID}', '${user.userName}')" class="sidebar-name">
//                     <a>
//                         <img width="30" height="30" src="https://t4.ftcdn.net/jpg/02/29/75/83/360_F_229758328_7x8jwCwjtBMmC6rgFzLFhZoEpLobB6L8.jpg" />
//                     <div class="chatContent">
//                         <span>${user.userName}</span>
//                         <p style="font-size: 16px; margin-bottom:0"></p>
//                     </div>
//                     <div class="status-dot '. $offline .'"><i class="fas fa-circle"></i></div>
//                     </a>
//                     <button id="btn-delete" class="btn btn-danger" onclick="deleteItem(event,'${user.userID}');">Xóa</button>
//                 </div>
//             </div>`;
//         }
//     } catch (error) {
//         console.log('không thấy tin nhắn mới nhất vì list user rỗng', error);
//     }
// });


document.addEventListener('DOMContentLoaded', async function () {
    try {
        const response = await fetch('/api/latest_user_mess');
        const users = await response.json();
        // console.log(users)
        const userList = document.querySelector('.userList');
        console.log(users);
        
        // Duyệt qua mảng users từ cuối lên đầu
        for (let i = 0; i <=  users.length - 1; i++) {
            const user = users[i];
            
            // const latestMessageResponse = await fetch(`/api/latest_message?userId1=${adminID}&userId2=${user.userID}`);
            // const latestMessage = await latestMessageResponse.json();
            userList.innerHTML +=
            `<div data-user-id="${user.senderID}">
                <div onclick="register_popup('${user.senderID}', '${user.senderName}')" class="sidebar-name">
                    <a>
                        <img width="30" height="30" src="https://t4.ftcdn.net/jpg/02/29/75/83/360_F_229758328_7x8jwCwjtBMmC6rgFzLFhZoEpLobB6L8.jpg" />
                    <div class="chatContent">
                        <span>${user.senderName}</span>
                        <p style="font-size: 16px; margin-bottom:0"></p>
                    </div>
                    <div class="status-dot '. $offline .'"><i class="fas fa-circle"></i></div>
                    </a>
                    <button id="btn-delete" class="btn btn-danger" onclick="deleteItem(event,'${user.senderID}');">Xóa</button>
                </div>
            </div>`;
        }
    } catch (error) {
        console.log('không thấy tin nhắn mới nhất vì list user rỗng', error);
    }
});

function deleteItem(event, userID) {
    
    // Ngăn chặn sự kiện click lan ra các phần tử cha
    event.stopPropagation();
    // Truy cập phần tử cần xóa bằng ID va an het cac tin nhan
    var itemToRemove = document.querySelector(`[data-user-id="${userID}"]`);
    itemToRemove.style.display = 'none';
    // Kiểm tra xem phần tử có tồn tại không
    if (itemToRemove) {
        // Gọi API để cập nhật thuộc tính 'deleted'
        fetch(`/api/delete_mess?userid=${userID}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Xóa phần tử khỏi DOM nếu API trả về thành công
                itemToRemove.remove();
                close_popup(userID);
                // console.log(data.message);

            } else {
                console.error(data.message);
            }
        })
        .catch(error => {
            console.error('Lỗi:', error);
        });
        location.reload();
    } else {
        console.error(`Không tìm thấy phần tử với ID: ${userID}`);
    }
    //an user khoi list user
    try {
        $.ajax({
            type: 'GET',
            dataType: 'json',
            url: '/api/update_deleted_user',
            data: { userid: userID },
            success: function(response) {
                console.log(response);
            },
            error: function(err) {
                console.log(err);
            }
        });
    } catch (err) {
        console.log('Lỗi ngoài:', err);
    }
}


//////////// START SCRIPT POPUP CHAT

//this function can remove a array element.
Array.remove = function (array, from, to) {
    var rest = array.slice((to || from) + 1 || array.length);
    array.length = from < 0 ? array.length + from : from;
    return array.push.apply(array, rest);
};

//this variable represents the total number of popups can be displayed according to the viewport width
var total_popups = 0;

//arrays of popups ids
var popups = [];

//this is used to close a popup
function close_popup(id) {
    for (var iii = 0; iii < popups.length; iii++) {
        if (id == popups[iii]) {
            Array.remove(popups, iii);
            document.getElementById(id).style.display = "none";
            calculate_popups();
            return;
        }
    }
}

//displays the popups. Displays based on the maximum number of popups that can be displayed on the current viewport width
function display_popups() {
    var right = 380;
    var iii = 0;
    for (iii; iii < total_popups; iii++) {
        if (popups[iii] != undefined) {
            var element = document.getElementById(popups[iii]);
            element.style.right = right + "px";
            right = right + 400;
            element.style.display = "flex";
            element.style.flexDirection = "column";
            element.style.justifyContent = "space-between";
        }
    }

    for (var jjj = iii; jjj < popups.length; jjj++) {
        var element = document.getElementById(popups[jjj]);
        element.style.display = "none";
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////
//lấy tin nhắn của đoạn chat theo id user
async function callAPIGetMessage(userid) {
    try {
        const response = $.ajax({
            type: 'GET',
            dataType: 'json',
            url: '/api/get_mess_user',
            data: { userid: userid },
        });
        // console.log('CALL API THÀNH CÔNG')
        return response;
    } catch (err) {
        console.log(err);
        return null;
    }
}

function scrollToBottom() {
    var messagesContainers = document.querySelectorAll('.popup-messages');
    messagesContainers.forEach(container => {
        container.scrollTop = container.scrollHeight;
    });
}

// Hàm hiển thị popup tin nhắn

async function register_popup(userid, username) {
    //hiển thị ID của popup
    // console.log(`ID popup la ${userid}`)

    // Kiểm tra nếu popup đã tồn tại trong mảng
    const existingIndex = popups.indexOf(userid);
    if (existingIndex !== -1) {

        popups.splice(existingIndex, 1);
        popups.unshift(userid);
        calculate_popups();
        return;
    }

    // tạo thẻ div chứa tin nhắn của từng user
    const popupBox = document.createElement('div');
    popupBox.classList.add('popup-box');
    popupBox.id = userid;
    var messageHTML = '';
    //gọi hàm lấy tất cả message của người dùng theo userid
    const userListMessage = await callAPIGetMessage(userid);

    // console.log(userListMessage);
    userListMessage.forEach(userMessage => {
        //tin nhắn của admin 
        if (userMessage.type == 1) {
            messageHTML += `
            <div class="mess-admin">
                <div class="d-flex justify-content-between">
                    <p class="small mb-1 text-muted">23 Jan 2:05 pm</p>
                    <p class="small mb-1">Bạn</p>
                </div>
                <div class="d-flex flex-row justify-content-end mb-4 pt-1">
                <div>
                    <p class="small p-2 me-3 mb-1 text-white rounded-3 bg-warning">${userMessage.message}</p>
                </div>
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava6-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;">
                </div>
            </div>
            `;
         

        } else {    //tin nhắn của người dùng
            messageHTML += `
                <div class="mess-user-${userMessage.senderID}">
                    <div class="d-flex justify-content-between">
                        <p class="small mb-1">${userMessage.senderName}</p>
                        <p class="small mb-1 text-muted">${userMessage.timestamp}</p>
                    </div>
                    <div class="d-flex flex-row justify-content-start mb-1">
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava5-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;">
                        <div>
                            <p class="small p-2 ms-3 mb-3 rounded-3" style="background-color: #f5f6f7;">${userMessage.message}</p>
                        </div>
                    </div>
                </div>
            `;
        }
    })

    popupBox.innerHTML = `
    <div class="popup-head">
        <div class="popup-head-left">${username}</div>
        <div class="popup-head-right"><button onclick = "close_popup('${userid}');"><i class="fa-solid fa-xmark"></i></button></div>
        <div style="clear: both"></div>
    </div>
     
    <div class="popup-messages">
        <div class="mess-padding-${userid}" style="padding:14px">
            ${messageHTML}
        </div>
    </div>

    <div class="popup-bottom">
        <form onsubmit="sendMessage(event, '${userid}', '${username}')" action="">
            <input id="input-${userid}" type="text" class="form-control input-mess">
            <button><i class="fa-solid fa-paper-plane"></i></button>
        </form>
    </div>
`;

    // thêm phần tử mới vào body
    document.body.appendChild(popupBox);

    popups.unshift(userid);
    calculate_popups();
    scrollToBottom();


    //KIỂM TRA INPUT ĐANG ĐƯỢC NHẬP
    $('#username').keyup(function (e) {
        console.log('vua nhap');
        socket.emit('alert_typing', {
            uID: adminID,
            uName: 'Admin',
            receiver: userid,
        });
    });
}

//calculate the total number of popups suitable and then populate the toatal_popups variable.
function calculate_popups() {
    var width = window.innerWidth;
    if (width < 540) {
        total_popups = 0;
    } else {
        width = width - 200;
        //320 is width of a single popup box
        total_popups = parseInt(width / 320);
    }
    display_popups();

}
//recalculate when window is loaded and also when window is resized.
window.addEventListener("resize", calculate_popups);
window.addEventListener("load", calculate_popups);


//admin gửi tin nhắn
function sendMessage(event, userID, userName) {
    event.preventDefault()
    const input = document.getElementById(`input-${userID}`);
    const message_input = input.value;
    if (message_input == '') {
        return;
    } else {
        socket.emit('admin_send_to_server', {
            uID: adminID,
            uName: 'Admin',
            receiverID: userID,
            message: message_input,
        })

        input.value = ''
    }
    const window_chat = document.getElementsByClassName(`mess-padding-${userID}`)[0];
    const new_div = document.createElement('div');
    const vietnamTime = new Date(new Date().getTime() + 7 * 60 * 60 * 1000).toISOString();
    new_div.innerHTML += `
    <div class="mess-admin">
        <div class="d-flex justify-content-between">
            <p class="small mb-1 text-muted">${vietnamTime}</p>
            <p class="small mb-1">Admin</p>
        </div>
        <div class="d-flex flex-row justify-content-end mb-1 pt-1">
        <div>
            <p class="small p-2 me-3 mb-1 text-white rounded-3 bg-warning">${message_input}</p>
        </div>
        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava6-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;">
        </div>
    </div>
    `;
    window_chat.appendChild(new_div);
    
    scrollToBottom();
    updateLatestMessage(userID, message_input);
}


//cap nhat tin nhan mới nhất vào listuser
async function updateLatestMessage(userID, message) {
    const userDivLatestMessage = document.querySelector(`div[data-user-id="${userID}"] .chatContent p`);
    if (userDivLatestMessage) {
        userDivLatestMessage.innerHTML = message;
    }
    const userDiv = document.querySelector(`div[data-user-id="${userID}"]`);
    if (userDiv) {
        const userList = document.querySelector('.userList');
        //chên phan tu con vào đâu phần tu cha
        userList.prepend(userDiv);
    }
}


/////// THÔNG BÁO ĐANG NHẬP

// var typing = false;
// var timeout = undefined;

// function tineoutFunction(){
//     typing = false;
//     socket.emit()
// }

