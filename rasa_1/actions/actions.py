from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from .constant import Constant
constant  = Constant()

from custom.write_file import write_file
import logging
logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

#=====================
#                   ||
#LOC                ||
#                   ||
#===================||

class actionSuMangTamNhinTrietLyGiaoDuc(Action):
    def name(self):
        return "action_thong_tin_truong"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            info_truong = constant.get_thong_tin_truong()	

            entities = tracker.latest_message.get('entities', [])
            print(f"\nEntities từ input:\n {entities}")
            
            default_response = "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."
            responses = ""

            for entity in entities:
                if entity.get('entity') == 'thong_tin_truong':
                    role_truong = entity.get('role')
                    
                    print(f"{role_truong}")
                    
                    if role_truong:
                        part_response = info_truong.get(role_truong,)
                        if part_response:
                            responses += part_response
                        else:
                            file_writer = write_file()
                            file_writer.get_ghi_log_file('action_thong_tin_dang: ' + tracker.latest_message['text'])
                            
                    else:
                        file_writer = write_file()
                        file_writer.get_ghi_log_file('action_thong_tin_dang: ' + tracker.latest_message['text'])
                    
            
            if responses:
                dispatcher.utter_message(text=responses)
            else:
                dispatcher.utter_message(text=default_response)
        except Exception as e:
            file_writer = write_file()
            file_writer.get_ghi_log_file(f"Exception in action_thong_tin_truong: {str(e)}")
            dispatcher.utter_message(text=default_response)
        return []

class ActionBanGiamHieu(Action):
    def name(self):
        return "action_ban_giam_hieu"
   
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
        # Tạo dictionary ánh xạ các role với thông điệp tương ứng
            info_ban_giam_hieu = constant.get_info_ban_giam_hieu()
                
            entities = tracker.latest_message.get('entities', [])
            print(f"\nEntities từ input:\n {entities}")
            default_response = "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."
            responses = ""
           
            for entity in entities:
                if entity.get('entity') == 'ban_giam_hieu':
                    role_ban_giam_hieu = entity.get('role')
                   
                    print(f"{role_ban_giam_hieu}")
                    
                    if role_ban_giam_hieu:
                        part_response = info_ban_giam_hieu.get(role_ban_giam_hieu)
                        if part_response:
                            responses = part_response
                        else:
                            file_writer = write_file()
                            file_writer.get_ghi_log_file('action_ban_giam_hieu: ' + tracker.latest_message['text'])
                            
                    else:
                        file_writer = write_file()
                        file_writer.get_ghi_log_file('action_ban_giam_hieu: ' + tracker.latest_message['text'])
                    
            
            if responses:
                dispatcher.utter_message(text=responses)
            else:
                dispatcher.utter_message(text=default_response)
        
        
        except Exception as e:
            file_writer = write_file()
            file_writer.get_ghi_log_file(f"Exception in action_thong_tin_dang: {str(e)}")
            dispatcher.utter_message(text=default_response)
        
        return []
       
class ActionHoiDongTruong(Action):
    def name(self):
        return "action_hoi_dong_truong"
   
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
        # Tạo dictionary ánh xạ các role với thông điệp tương ứng
            infor_hoi_dong_truong = constant.get_infor_hoi_dong_truong()

            entities = tracker.latest_message.get('entities', [])
            print(f"\nEntities từ input: \n{entities}")

            default_response = "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."
            responses = ""
           
            for entity in entities:
                if entity.get('entity') == 'hoi_dong_truong':
                    role_hoi_dong_truong = entity.get('role')
                    print(f"{role_hoi_dong_truong}")
                    
                    if role_hoi_dong_truong:
                        part_response = infor_hoi_dong_truong.get(role_hoi_dong_truong)
                        if part_response:
                            responses = part_response
                        else:
                            file_writer = write_file()
                            file_writer.get_ghi_log_file('action_thong_tin_dang: ' + tracker.latest_message['text'])
                            
                    else:
                        file_writer = write_file()
                        file_writer.get_ghi_log_file('action_thong_tin_dang: ' + tracker.latest_message['text'])
                    
            
            if responses:
                dispatcher.utter_message(text=responses)
            else:
                dispatcher.utter_message(text=default_response)
        
        except Exception as e:
            file_writer = write_file()
            file_writer.get_ghi_log_file(f"Exception in action_thong_tin_dang: {str(e)}")
            dispatcher.utter_message(text=default_response)
        
        return []

class actionThongTinDang(Action):
    def name(self):
        return "action_thong_tin_dang"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            info_dang = constant.get_infor_dang()
            entities = tracker.latest_message.get('entities', [])
            user_input = tracker.latest_message['text']
            print(f"\n Người dùng hỏi: {user_input}\nEntities từ input: {entities} ")
            
            default_response = "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."
            responses = ""
           
            for entity in entities:
                if entity.get('entity') == 'dang_bo_dang_uy':
                    role_dang = entity.get('role')
                    value_dang = entity.get('value')
                    print(f"{role_dang} ----> {value_dang}")
                    
                    if role_dang and value_dang:
                        part_response = info_dang.get(role_dang, {}).get(value_dang)
                        if part_response:
                            responses += part_response
                        else:
                            file_writer = write_file()
                            file_writer.get_ghi_log_file('action_thong_tin_dang: ' + tracker.latest_message['text'])
                            
                    else:
                        file_writer = write_file()
                        file_writer.get_ghi_log_file('action_thong_tin_dang: ' + tracker.latest_message['text'])
                    
            
            if responses:
                dispatcher.utter_message(text=responses)
            else:
                dispatcher.utter_message(text=default_response)
        
        except Exception as e:
            file_writer = write_file()
            file_writer.get_ghi_log_file(f"Exception in action_thong_tin_dang: {user_input}")
            dispatcher.utter_message(text=default_response)
        
        return []

class ActionLanhDaoDangDoanThe(Action):
    def name(self):
        return "action_lanh_dao_dang_doan_the"
   
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message['text']
        print("người dùng hỏi về lãnh đạo: " + user_input)
        # Lấy entities từ câu chat của người dùng
        entities = tracker.latest_message.get('entities', [])
        print(f"\nEntities từ input:\n {entities}")
       
       
        # Tạo dictionary ánh xạ các role với thông điệp tương ứng
        infor_department = {
            'hội đồng trường':'PGS.TS. BS. Nguyễn Minh Phương, Chủ tịch, Email: nmphuong@ctump.edu.vn',
            'đảng và các đoàn thể': "</br>PGS.TS. BS. Nguyễn Minh Phương, Bí thư Đảng ủy, Email: nmphuong@ctump.edu.vn</br>TS. BS. Trần Thanh Hùng, Chủ tịch công đoàn Trường, Email: tthung@ctump.edu.vn</br>TS. BS. Phạm Hoàng Khánh, Bí thư Đoàn TNCSHCM Trường, Email: phkhanh@ctump.edu.vn</br>PGS.TS. BS. Lê Thành Tài, Chủ tịch Hội cựu chiến binh, Email: lttai@ctump.edu.vn</br>",
            "khoa y":"Khoa Y</br>TS.BS. Lê Văn Minh, Trưởng Khoa, Email: lvminh@ctump.edu.vn</br>TS.BS. Trần Thái Thanh Tâm, Phó Trưởng Khoa, Email: ttttam@ctump.edu.vn</br>TS. BS. Nguyễn Như Nghĩa, Phó Trưởng Khoa, Email: nnnghia@ctump.edu.vn</br>",
            "khoa dược":"Khoa Dược</br>PGS.TS. DS Phạm Thành Suôl, Trưởng Khoa, Email: ptsuol@ctump.edu.vn</br>PGS.TS.DS. Đỗ Châu Minh Vĩnh Thọ, Phó Trưởng Khoa, email: dcmvtho@ctump.edu.vn</br>TS. DS Phạm Thị Tố Liên, Phó Trưởng Khoa, Email: pttlien@ctump.edu.vn</br>",
            "khoa răng hàm mặt":"Khoa Răng hàm mặt</br>PGS.TS. BS Trương Nhựt Khuê, Trưởng Khoa, Email: tnkhue@ctump.edu.vn</br>PGS.TS.BS. Lê Nguyên Lâm, Phó Trưởng Khoa, Email: lnlam@ctump.edu.vn</br>TS. BS. Đỗ Thị Thảo, Phó Trưởng Khoa, Email: dtthao@ctump.edu.vn</br>",
            "khoa y tế công cộng":"Khoa Y Tế Công Cộng</br>TS. BS. Lê Minh Hữu, Trưởng Khoa , Email: lmhuu@ctump.edu.vn</br>TS. BS. Nguyễn Tấn Đạt, Phó Trưởng Khoa, Email: ntdat@ctump.edu.vn</br>",
            "khoa điều dưỡng":"Khoa Điều dưỡng</br>TS. BS Nguyễn Hồng Phong, Trưởng Khoa , Email: nhphong@ctump.edu.vn</br>TS. ĐD. Nguyễn Thị Thanh Trúc, Phó Trưởng Khoa, Email: ntttruc@ctump.edu.vn</br>",
            "khoa kỹ thuật y học":"Khoa Kỹ thuật y học</br>TS. BS Nguyễn Hồng Phong, Trưởng Khoa , Email: nhphong@ctump.edu.vn</br>TS. ĐD. Nguyễn Thị Thanh Trúc, Phó Trưởng Khoa, Email: ntttruc@ctump.edu.vn</br>",
            "khoa học cơ bản":"Khoa học cơ bản</br>PGS.TS. Nguyễn Thị Thu Trâm, Trưởng Khoa, Email: ntttram@ctump.edu.vn</br>ThS. Nguyễn Thanh Hùng, Phó Trưởng Khoa, Email: nthung@ctump.edu.vn</br>TS. Trần Thị Hồng Lê, Phó Trưởng Khoa, Email: tthle@ctump.edu.vn</br>",
            "khoa y học cổ truyền":"Khoa Y học cổ truyền</br>TS. BS. Lê Minh Hoàng , Trưởng Khoa, Email: lmhoang@ctump.edu.vn</br>ThS. BS. Nguyễn Ngọc Chi Lan , Phó Trưởng  Khoa, Email: nnclan@ctump.edu.vn</br>",
           
            "phòng thông tin và truyền thông":"Phòng Thông tin và Truyền thông</br>ThS. Châu Minh Khoa, Trưởng Phòng, Email: cmkhoa@ctump.edu.vn</br>ThS. Trần Thị Bích Phương, Phó Trưởng Phòng, Email: ttbphuong@ctump.edu.vn</br>",
            "phòng công tác sinh viên":"Phòng Công tác sinh viên</br>ThS. Ngô Phương Thảo, Trưởng phòng, Email: npthao@ctump.edu.vn</br>ThS. Võ Văn Quyền, Phó Trưởng phòng, Email: vvquyen@ctump.edu.vn</br>",
            "phòng đảm bảo chất lượng":"Phòng đảm bảo chất lượng</br>ThS. BS. Phạm Thị Mỹ Ngọc, Trưởng Phòng, Email: ptmngoc@ctump.edu.vn</br>",
            "phòng đào tạo đại học":"Phòng Đào tạo Đại học</br>TS. BS. Phạm Kiều Anh Thơ, Trưởng phòng, Email: pkatho@ctump.edu.vn</br>TS. BS. Trần Quang Khải, Phó Trưởng phòng, Email: tqkhai@ctump.edu.vn</br>",
            "phòng đào tạo sau đại học":"Phòng Đào tạo Sau đại học</br>GS.TS. BS Võ Huỳnh Trang, Trưởng phòng, Email: vhtrang@ctump.edu.vn</br>TS. BS. Nguyễn Hồng Hà, Phó Trưởng phòng, Email: nhha@ctump.edu.vn</br>TS. DS Đặng Duy Khánh, Phó Trưởng phòng , Email: ddkhanh@ctump.edu.vn</br>",
            "phòng hành chính tổng hợp":"Phòng Hành chính tổng hợp</br>ThS. Phạm Trương Yến Nhi , Trưởng phòng, Email: ptynhi@ctump.edu.vn</br>ThS. Phạm Thị Minh, Phó Trưởng phòng, Email: ptminh@ctump.edu.vn</br>CN. Nguyễn Văn Bộ, Phó Trưởng phòng, Email: nvbo@ctump.edu.vn</br>",
            "phòng khảo thi":"Phòng Khảo thí</br>ThS. Phan Thị Tuyết Nhung, Trưởng Phòng, Email: pttnhung@ctump.edu.vn</br>Ths. DS. Lê Thị Minh Ngọc, Phó Trưởng Phòng, Email: ltmngoc@ctump.edu.vn</br>",
            "phòng khoa học công nghệ và quan hệ đối ngoại":"Phòng Khoa học công nghệ và Quan hệ đối ngoại</br>PGS. TS. DS. Nguyễn Thị Ngọc Vân, Trưởng phòng, Email:  ntnvan@ctump.edu.vn</br>PGS.TS. DS. Nguyễn Thắng, Phó Trưởng phòng, Email: nthang@ctump.edu.vn</br>TS. BS. Hoàng Minh Tú, Phó Trưởng phòng, Email: hmtu@ctump.edu.vn</br>",
            "phòng quản trị thiết bị":"Phòng Quản trị thiết bị</br>ThS. Nguyễn Văn Tám, Trưởng phòng, Email: nvtam@ctump.edu.vn</br>ThS. Huỳnh Trường Hiệp, Phó Trưởng phòng, Email: hthiep@ctump.edu.vn</br>",
            "phòng tài chính kế toán":"Phòng Tài chính kế toán</br>ThS. Võ Nhật Nhân Tuyền, Trưởng phòng, Email: vnntuyen@ctump.edu.vn</br>CN. Hứa Kim Chi, Phó Trưởng phòng, Email: hkchi@ctump.edu.vn</br>",
            "phòng tổ chức cán bộ":"Phòng Tổ chức Cán bộ</br>ThS. Trần Trương Ngọc Bích, Trưởng Phòng, Email:  ttnbich@ctump.edu.vn</br>ThS. Hà Bảo Trân, Phó Trưởng phòng, Email: hbtran@ctump.edu.vn</br>",
            "phòng thanh tra pháp chế":"Phòng Thanh tra - Pháp chế</br>TS. BS. Bùi Quang Nghĩa, Trưởng Phòng, Email: bqnghia@ctump.edu.vn</br>CN. Nguyễn Hiệp Phúc, Phó Trưởng phòng, Email: nhphuc@ctump.edu.vn</br>",
            "ban quản lý dự án":"Ban Quản lý dự án</br>KS. Nguyễn Chí Trung, Phó Trưởng Ban, Email: nctrung@ctump.edu.vn</br>",
            "trung tâm dịch vụ và đào tạo theo nhu cầu xã hội":"Trung tâm Dịch vụ và Đào tạo theo nhu cầu xã hội</br>TS. BS. Nguyễn Triều Việt, Giám đốc, Email: ntviet@ctump.edu.vn</br>TS. Phan Thị Luyện, Phó Giám đốc, Email: ptluyen@ctump.edu.vn</br>",
            "trung tâm giáo dục y học và huấn luyện kỹ năng y khoa":"Trung tâm Giáo dục y học và Huấn luyện kỹ năng y khoa</br>ThS. BS Phạm Thị Mỹ Ngọc, Trưởng Trung tâm, Email: ptmngoc@ctump.edu.vn</br>ThS. BS. Trần Xuân Quỳnh, Phó Trưởng Trung tâm, Email: txquynh@ctump.edu.vn</br>",
            "thư viện":"Thư viện</br>TS. BS. Nguyễn Thị Hải Yến, Giám đốc, Email: nthyen@ctump.edu.vn</br>TS.BS. Lê Thị Hoàng Mỹ , Phó Giám đốc, Email: lthmy@ctump.edu.vn</br>",
            "bệnh viện":"BỆNH VIỆN</br>BSCKII. Lại Văn Nông, Giám đốc, Email: lvnong@ctump.edu.vn.</br>PGS. TS.BS. Nguyễn Thành Tấn, Phó Giám đốc, Email: nttan@ctump.edu.vn</br>ThS. Nguyễn Văn Tám, Phó Giám đốc, Email: nvtam@ctump.edu.vn</br>TS. BS. Võ Phạm Minh Thư, Phó Giám đốc, Email: vpmthu@ctump.edu.vn</br>"
           


        }
       
        input_value = None
       
        for entity in entities:
            if entity.get('entity') == "department":
                input_value = entity.get('value')
                print("----"+input_value)
        if input_value in infor_department:
            response = infor_department[input_value]
        else:
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_lanh_dao_dang_doan_the: '+ tracker.latest_message['text'])
            response= "Xin lỗi, tôi không có thông tin về câu hỏi của bạn."
        dispatcher.utter_message(text=response)
        return []

class actionGoiYCTDT(Action):
    def name(self):
        return "action_goi_y_CTDT"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action Gợi ý ctdt")
        response = "Tôi có thông tin chương trình đào tạo của các ngành:<br>- Y khoa,<br>- Răng hàm mặt,<br>- Y học dự phòng<br>- Y học cổ truyền<br>- Dược<br>- Điều dưỡng<br>- Y tế công cộng<br>- Kỹ thuật xét nghiệm y học<br>- Hộ sinh<br>- Kỹ thuật hình ảnh y học"

        dispatcher.utter_message(text=response)
        
        return []

class actionCTDT(Action):
    def name(self):
        return "action_CTDT_nganh"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message['entities']
        print(f"\n\nEntity từ input : {entities}")
        print("ACTION CTĐT ngành")
        infor_ctdt_hoc_phi = constant.get_hocphi_ctdt()
        role = []
        slot_ten_nganh = tracker.get_slot('CTDT_nganh')
        print(f"Slot tên ngành là : {slot_ten_nganh}")
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        response = "Bạn vui lòng nhập đầy đủ câu hỏi<br> Ví dụ:<br>- Học phí + tên ngành<br>- Chương trình đào tạo + tên ngành"
        found = False
        res_default = False
        try:
            if 'ten_nganh' in role and 'hoi_ctdt' in role:
                response = f"<br>Chương trình đào tạo của {slot_ten_nganh} : "
                print("Chương trình đào tạo của ngành là")
                # Chính Quy 
                #Trúng tuyển chính quy
                if slot_ten_nganh in infor_ctdt_hoc_phi['daihoc']['he_chinhquy']['chinhquy']:
                    print("Chương trình đào tạo chính quy")
                    response += "<br>Hệ chính quy :" 
                    response += f"<br>- Đào tạo trúng tuyển chính quy : " + infor_ctdt_hoc_phi['daihoc']['he_chinhquy']['chinhquy'][slot_ten_nganh]['ctdt'] 
                    found = True
                    res_default = True
                #đào tạo theo nhu cầu xã hội
                if slot_ten_nganh in infor_ctdt_hoc_phi['daihoc']['he_chinhquy']['nhu_cau_xh']:
                    response += "<br>- Đào tạo theo nhu cầu xã hội (theo đặt hàng ) : " + infor_ctdt_hoc_phi['daihoc']['he_chinhquy']['nhu_cau_xh'][slot_ten_nganh]['ctdt'] 
                    found = True
                    res_default = True
                #đào tạo hệ quốc tế tiếng anh
                if slot_ten_nganh in infor_ctdt_hoc_phi['daihoc']['he_chinhquy']['qte_tieng_anh']:
                    response += "<br>- Đào tạo hệ quốc tế tiếng anh : "+ infor_ctdt_hoc_phi['daihoc']['he_chinhquy']['qte_tieng_anh'][slot_ten_nganh]['ctdt'] 
                    found = True
                    res_default = True
            
                # Liên thông
                # Liên thông chính quy
                if slot_ten_nganh in infor_ctdt_hoc_phi['daihoc']['he_lienthong']['lt_chinhquy']:
                    response += "<br>Hệ liên thông : "
                    response += "<br>- Đào tạo liên thông hệ chính quy : " + infor_ctdt_hoc_phi['daihoc']['he_lienthong']['lt_chinhquy'][slot_ten_nganh]['ctdt'] 
                    found = True
                    res_default = True
                #Liên thông theo nhu cầu xã hội
                if slot_ten_nganh in infor_ctdt_hoc_phi['daihoc']['he_lienthong']['lt_nhu_cau_xh']:
                    response += "<br>- Đào tạo liên thông theo nhu cầu xã hội : " + infor_ctdt_hoc_phi['daihoc']['he_lienthong']['lt_nhu_cau_xh'][slot_ten_nganh]['ctdt'] 
                    found = True
                    res_default = True
            
                if found == False:
                    response = f"Không tìm thấy ngành bạn yêu cầu."
        except KeyError:
            response = "Bạn vui lòng nhập đầy đủ câu hỏi<br> Ví dụ:<br>- Học phí + tên ngành<br>- Chương trình đào tạo + tên ngành"

        if res_default == False:
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_CTDT_nganh: ' + tracker.latest_message['text'])
        dispatcher.utter_message(text=response)
        
        return [SlotSet("CTDT_nganh", None)]

class actionGoiYHoiVeDH_LT_SDH(Action):
    def name(self):
        return "action_goi_y_info_daihoc_lienthong_saudaihoc"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action Gợi ý hỏi về đại học, liên thông, sau đại học")
        entities = tracker.latest_message['entities']
        # print(f"\nnEntity từ input : {entities}")
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        
        response = "Tôi có thông tin tuyển sinh, học phí, chương trình đào tạo:<br>- Đại học chính quy<br>- Liên thông<br>- Sau đại học"
      
        dispatcher.utter_message(text=response)
        
        return []
    
class actionGoiYHoiVeDH_LT_SDH(Action):
    def name(self):
        return "action_goi_y_info_daihoc_lienthong_saudaihoc"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action Gợi ý hỏi về đại học, liên thông, sau đại học")
        entities = tracker.latest_message['entities']
        # print(f"\nnEntity từ input : {entities}")
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        
        response = "Tôi có thông tin tuyển sinh, học phí, chương trình đào tạo:<br>- Đại học chính quy<br>- Liên thông<br>- Sau đại học"
      
        dispatcher.utter_message(text=response)
        
        return []
    
class actionGoiYTuyenSinh(Action):
    def name(self):
        return "action_goi_y_thong_tin_tuyen_sinh"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print("action Gợi ý tuyển sinh")
        # print(f"\nnEntity từ input : {entities}")
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        if 'info' in role and 'thong_tin_tuyen_sinh' in role or 'thong_tin_tuyen_sinh' in role:
            response = "Bạn vui lòng nhập đầy đủ câu hỏi<br>Ví dụ:<br>- Tuyển sinh đại học<br>- Tuyển sinh liên thông<br>- Tuyển sinh sau đại học"
        else:
            response = f"Bạn vui lòng mô tả thêm thông tin"
        dispatcher.utter_message(text=response)
        
        return []
    
class actionTuyenSinhTungNganh(Action):
    def name(self):
        return "action_thong_tin_tuyen_sinh_tung_nganh"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(f"\nnEntity từ input : {entities}")
        print("action Gợi ý tuyển sinh từng ngành")
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        slot_tuyensinh = tracker.get_slot('ten_nganh')
        print(f"Slot tuyển sinh là : {slot_tuyensinh}")

        tuyen_sinh_dh_chinhquy_2024 = constant.get_tuyen_sinh_dh_chinhquy_2024()
        response = "Bạn vui lòng nhập đầy đủ câu hỏi<br>Ví dụ:<br>- Tuyển sinh + tên ngành"
        
        try:
            if 'thong_tin_tuyen_sinh' in role and 'ten_nganh' in role:
                response = f"Thông tin tuyển sinh chính quy ngành {slot_tuyensinh} :<br>"
                nganh_tuyen_sinh = tuyen_sinh_dh_chinhquy_2024['đại học chính quy']['cac_nganh_tuyen_sinh']
                found = False
                for nganh, thong_tin in nganh_tuyen_sinh.items():
                    if nganh == slot_tuyensinh:
                        response += (
                            f"+ Mã xét tuyển: {thong_tin['ma_xet_tuyen']},<br>"
                            f"+ Phương thức tuyển: {thong_tin['phuong_thuc_tuyen']},<br>"
                            f"+ Tổ hợp: {thong_tin['to_hop']}<br>"
                            f"+ Xét tuyển đợt 1 (dự kiến): "
                            f"Kết quả thi THPT: {thong_tin['xet_tuyen_dot_1_du_kien']['kqua_thpt']}, "
                            f"Dự bị dân tộc: {thong_tin['xet_tuyen_dot_1_du_kien']['du_bi_dan_toc']}, "
                            f"Hợp đồng: {thong_tin['xet_tuyen_dot_1_du_kien']['hop_dong']}"
                        )
                        found = True
                        break

                if not found:
                    response = "Không tìm thấy tên ngành theo yêu cầu"
 
        except KeyError:
            response = "Bạn vui lòng nhập đầy đủ câu hỏi<br>Ví dụ:<br>- Tuyển sinh + tên ngành"
        dispatcher.utter_message(text=response)
        
        return [SlotSet("ten_nganh", None)]

class actionThanhToanHocPhi(Action):
    def name(self):
        return "action_thanh_toan_hoc_phi"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(f"\nnEntity từ input : {entities}")
        print("action thanh toán học phí")
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
     
        
        response = f"Thanh toán học phí online xem chi tiết tại đây: http://www.ctump.edu.vn/DesktopModules/NEWS/DinhKem/7991_HUONG-DAN-NOP-HP-ONLINE_moi.pdf"
       
       
        dispatcher.utter_message(text=response)
        
        return []

class actionDiemChuanTungNganh(Action):
    def name(self):
        return "action_diem_chuan_tung_nganh"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(f"\nnEntity từ input : {entities}")
        print("action điểm chuẩn từng ngành")
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        slot_tuyensinh = tracker.get_slot('ten_nganh')
        print(f"Slot tuyển sinh là : {slot_tuyensinh}")

        tuyen_sinh_dh_chinhquy_2024 = constant.get_tuyen_sinh_dh_chinhquy_2024()
       
        response = f"Thông tin điểm chuẩn của ngành {slot_tuyensinh} năm 2024 :<br>"
       
        try:
            if 'diem_tuyen_sinh_dh' in role and 'ten_nganh' in role:
                nganh_tuyen_sinh = tuyen_sinh_dh_chinhquy_2024['đại học chính quy']['cac_nganh_tuyen_sinh']
                for nganh, thong_tin in nganh_tuyen_sinh.items():
                    # print(type(nganh), type(slot_tuyensinh))
                    if nganh == slot_tuyensinh:
                        response += f"+ Mã xét tuyển: {thong_tin['ma_xet_tuyen']},<br>+ Điểm chuẩn: {thong_tin['diem_chuan']}<br>  + Phương thức tuyển: {thong_tin['phuong_thuc_tuyen']},<br>  + Tổ hợp: {thong_tin['to_hop']}<br>"   
                    # else: response = "Bạn vui lòng nhập đầy đủ câu hỏi<br>Ví dụ:<br>- Điểm chuẩn + tên ngành"  
              
        except KeyError:
            response = "Bạn vui lòng nhập đầy đủ câu hỏi<br>Ví dụ:<br>- Điểm chuẩn + tên ngành"
        dispatcher.utter_message(text=response)
        
        return [SlotSet("ten_nganh", None)]

class actionGoiYTuyenSinhDaiHoc(Action):
    def name(self):
        return "action_goi_y_tuyen_sinh_dai_hoc"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(f"\nnEntity từ input : {entities}")
        print("ACTION goi ý tuyển sinh đại học, liên thông, sau đại học")

        tuyen_sinh_dh_chinhquy_2024 = constant.get_tuyen_sinh_dh_chinhquy_2024()

        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        slot_tuyensinh = tracker.get_slot('tuyen_sinh_daihoc_chinhquy')
        print(f"Slot tuyển sinh là : {slot_tuyensinh}")
        response = "Bạn vui lòng nhập đầy đủ câu hỏi<br>Ví dụ:<br>- Tuyển sinh đại học<br>- Tuyển sinh liên thông<br>- Tuyển sinh sau đại học"
        try:
            if 'thong_tin_tuyen_sinh' in role and 'dai_hoc_chinh_quy' in role and 'quy_trinh_tuyen_sinh' not in role:
                response = f"<br>Thông tin tuyển sinh {slot_tuyensinh} gôm:<br>"
                if slot_tuyensinh in tuyen_sinh_dh_chinhquy_2024 and slot_tuyensinh == 'đại học chính quy':
                    cac_nganh_tuyen_sinh = tuyen_sinh_dh_chinhquy_2024[slot_tuyensinh]['cac_nganh_tuyen_sinh']
                    thong_tin_tuyen_sinh = tuyen_sinh_dh_chinhquy_2024[slot_tuyensinh]['thong_tin_tuyen_sinh']
                    for nganh, thong_tin in cac_nganh_tuyen_sinh.items():
                        response += f"- {nganh}<br>  + Mã xét tuyển: {thong_tin['ma_xet_tuyen']},<br>  + Phương thức tuyển: {thong_tin['phuong_thuc_tuyen']},<br>  + Tổ hợp: {thong_tin['to_hop']}<br>"
                    response += "<br>" + thong_tin_tuyen_sinh


            if 'thong_tin_tuyen_sinh' in role and 'lien_thong' in role and 'quy_trinh_tuyen_sinh' not in role:
                response = f"<br>Thông tin tuyển sinh {slot_tuyensinh} gôm:<br>"
                if slot_tuyensinh in tuyen_sinh_dh_chinhquy_2024 and slot_tuyensinh == 'liên thông chính quy':
                    trung_cap_len_dai_hoc = tuyen_sinh_dh_chinhquy_2024[slot_tuyensinh]['trung_cap_len_dai_hoc']['cac_nganh_tuyen_sinh']
                    cao_dang_len_dai_hoc = tuyen_sinh_dh_chinhquy_2024[slot_tuyensinh]['cao_dang_len_dai_hoc']['cac_nganh_tuyen_sinh']
                    thong_tin_tuyen_sinh = tuyen_sinh_dh_chinhquy_2024[slot_tuyensinh]['thong_tin_tuyen_sinh']
                    response += "***Trung cấp lên đại học***<br>" 
                    for nganh, thong_tin in trung_cap_len_dai_hoc.items():
                        response += f"- {nganh}<br>  + Mã ngành: {thong_tin['ma_nganh']}<br>  + Mã xét tuyển: {thong_tin['ma_xet_tuyen']},<br>  + Phương thức tuyển: {thong_tin['phuong_thuc_tuyen']}<br>"
                    response += "***Cao đẳng lên đại học***<br>" 
                    for nganh, thong_tin in cao_dang_len_dai_hoc.items():
                        response += f"- {nganh}<br>  + Mã ngành: {thong_tin['ma_nganh']}<br>  + Mã xét tuyển: {thong_tin['ma_xet_tuyen']},<br>  + Phương thức tuyển: {thong_tin['phuong_thuc_tuyen']}<br>"
                    response += "<br>" + thong_tin_tuyen_sinh
                    
            if 'thong_tin_tuyen_sinh' in role and 'sau_dai_hoc' in role and 'quy_trinh_tuyen_sinh' not in role:
                response = f"<br>Thông tin tuyển sinh {slot_tuyensinh} gôm:<br>"
                response += tuyen_sinh_dh_chinhquy_2024[slot_tuyensinh]
        except KeyError:
            response = "Bạn vui lòng nhập đầy đủ câu hỏi<br>Ví dụ:<br>- Tuyển sinh đại học<br>- Tuyển sinh liên thông<br>- Tuyển sinh sau đại học"
        if response == "Bạn vui lòng nhập đầy đủ câu hỏi<br>Ví dụ:<br>- Tuyển sinh đại học<br>- Tuyển sinh liên thông<br>- Tuyển sinh sau đại học":
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_goi_y_tuyen_sinh_dai_hoc: ' + tracker.latest_message['text'])
            
        dispatcher.utter_message(text=response)
        
        return  [SlotSet("tuyen_sinh_daihoc_chinhquy", None)]

class actionGoiYQuyTrinhTuyenSinh(Action):
    def name(self):
        return "action_goi_y_quy_trinh_tuyen_sinh"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action Gợi ý các quy trinh")
        entities = tracker.latest_message['entities']
        # print(f"\nnEntity từ input : {entities}")
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        
        response = f"Tôi có thông tin quy trình tuyển sinh đại học, liên thông, sau đại học nè<br>Bạn vui lòng nhập đầy đủ câu hỏi<br>Ví dụ:<br>- quy trình tuyển sinh đại học<br>- quy trình tuyển sinh liên thông<br>- quy trình tuyển sinh sau đại học"
        dispatcher.utter_message(text=response)
        
        return []

class actionTuyenSinhDaiHocLienThongSauDaiHoc(Action):
    def name(self):
        return "action_quy_trinh_tuyen_sinh_dh_lt_sdh"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("ACTION tuyển sinh đại học, liên thông, sau đại học")
        entities = tracker.latest_message['entities']
        print(f"\nnEntity từ input : {entities}")

        tuyen_sinh_dh_chinhquy_2024 = constant.get_tuyen_sinh_dh_chinhquy_2024()
        # print(tuyen_sinh_dh_chinhquy_2024)
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        slot_tuyensinh = tracker.get_slot('tuyen_sinh_daihoc_chinhquy')
        print(f"Slot tuyển sinh là : {slot_tuyensinh}")
        response = "Bạn vui lòng nhập đầy đủ câu hỏi<br>Ví dụ:<br>- Quy trình tuyển sinh đại học<br>- Quy trình tuyển sinh liên thông<br>- Quy trình tuyển sinh sau đại học."
        try:
            if  'quy_trinh_tuyen_sinh' in role and 'thong_tin_tuyen_sinh' in role and 'dai_hoc_chinh_quy' in role:
                response = f"<br>Quy trình tuyển sinh {slot_tuyensinh} gôm:<br>"
                phuong_thuc_tuyen_sinh = tuyen_sinh_dh_chinhquy_2024[slot_tuyensinh]['phuong_thuc_hinh_thuc_tuyen_sinh']['phuong_thuc']
                hinh_thuc_tuyen_sinh = tuyen_sinh_dh_chinhquy_2024[slot_tuyensinh]['phuong_thuc_hinh_thuc_tuyen_sinh']['phuong_thuc']
            
                response += "- Phương thức: "+phuong_thuc_tuyen_sinh
                response += "<br>- Hình thức: "+hinh_thuc_tuyen_sinh

            if  'quy_trinh_tuyen_sinh' in role and 'thong_tin_tuyen_sinh' in role and 'lien_thong' in role:
                response = f"<br>Quy trình tuyển sinh {slot_tuyensinh} gôm:<br>"
                hinh_thuc_tuyen_sinh = tuyen_sinh_dh_chinhquy_2024[slot_tuyensinh]['hinh_thuc_tuyen_sinh']['thong_tin']
                lt_chinh_quy_trung_cap_len_dh_Y_khoa = tuyen_sinh_dh_chinhquy_2024[slot_tuyensinh]['hinh_thuc_tuyen_sinh']['lt_chinh_quy_trung_cap_len_dh_Y_khoa']
                lt_chinh_quy_trung_cap_len_dh_yhct_d_yhdp_dd_xnyh = tuyen_sinh_dh_chinhquy_2024[slot_tuyensinh]['hinh_thuc_tuyen_sinh']['lt_chinh_quy_trung_cap_len_dh_yhct_d_yhdp_dd_xnyh']
                lt_chinh_quy_cao_dang_len_dh_d_dd_xnyh = tuyen_sinh_dh_chinhquy_2024[slot_tuyensinh]['hinh_thuc_tuyen_sinh']['lt_chinh_quy_cao_dang_len_dh_d_dd_xnyh']
                response += f""+hinh_thuc_tuyen_sinh
                response += f"<br>"+lt_chinh_quy_trung_cap_len_dh_Y_khoa
                response += f"<br>"+lt_chinh_quy_trung_cap_len_dh_yhct_d_yhdp_dd_xnyh
                response += f"<br>"+lt_chinh_quy_cao_dang_len_dh_d_dd_xnyh
            if  'quy_trinh_tuyen_sinh' in role and 'thong_tin_tuyen_sinh' in role and 'sau_dai_hoc' in role:
                response = f"<br>Quy trình tuyển sinh {slot_tuyensinh} gôm:<br>"
                response += f"Sau đại học có nhiều thông tin nên bạn xem chi tiết ở đây nha: http://www.ctump.edu.vn/Default.aspx?tabid=1036"
        except KeyError:
               response = "Bạn vui lòng nhập đầy đủ câu hỏi<br>Ví dụ:<br>- Quy trình tuyển sinh đại học<br>- Quy trình tuyển sinh liên thông<br>- Quy trình tuyển sinh sau đại học."
        if response == "Bạn vui lòng nhập đầy đủ câu hỏi<br>Ví dụ:<br>- Quy trình tuyển sinh đại học<br>- Quy trình tuyển sinh liên thông<br>- Quy trình tuyển sinh sau đại học.":
                file_writer = write_file()
                file_writer.get_ghi_log_file('action_quy_trinh_tuyen_sinh_dh_lt_sdh: ' + tracker.latest_message['text'])
        dispatcher.utter_message(text=response)
        
        return  [SlotSet("tuyen_sinh_daihoc_chinhquy", None)]

class actionGoiYDoiTuong(Action):
    def name(self):
        return "action_goi_y_doi_tuong"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action Gợi ý dối tượng")
        entities = tracker.latest_message['entities']
        # print(f"\nnEntity từ input : {entities}")
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        
        response = f"Tôi có thông tin về đối tượng tuyển sinh đại học, liên thông, sau đại học"
        dispatcher.utter_message(text=response)
        
        return []

class actionDoiTuongTuyenSinh(Action):
    def name(self):
        return "action_doi_tuong_tuyen_sinh_dh_lt_sdh"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(f"\nnEntity từ input : {entities}")
        print("ACTION đối tượng tuyển sinh đại học, liên thông, sau đại học")

        tuyen_sinh_dh_chinhquy_2024 = constant.get_tuyen_sinh_dh_chinhquy_2024()
        response = "Bạn vui lòng nhập đầy đủ câu hỏi<br>Ví dụ:<br>- Đối tượng tuyển sinh đại học<br>- Đối tượng tuyển sinh liên thông<br>- Đối tượng tuyển sinh sau đại học."
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        # slot_tuyensinh = tracker.get_slot('tuyen_sinh_daihoc_chinhquy')
        # print(f"Slot tuyển sinh là : {slot_tuyensinh}")
        # response = "đói tượng tuyển."
        try:
            if  'doi_tuong_tuyen_sinh' in role and 'thong_tin_tuyen_sinh' in role and ('dai_hoc_chinh_quy' not in role or 'lien_thong' not in role or 'sau_dai_hoc' not in role):
                response = f"<br>- Đối tượng tuyển sinh đại học gôm:<br>"
                doi_tuong_tuyen_sinh_dh = tuyen_sinh_dh_chinhquy_2024['đại học chính quy']['doi_tuong_tuyen_sinh']
                vung_tuyen_sinh_dh = tuyen_sinh_dh_chinhquy_2024['đại học chính quy']['vung_tuyen_sinh']
                response += "+ Đối tượng: "+doi_tuong_tuyen_sinh_dh
                response += "<br>+ Vùng tuyển sinh: "+vung_tuyen_sinh_dh
                
                response += f"<br>- Đối tượng tuyển sinh liên thông gôm:<br>"
                doi_tuong_tuyen_sinh_lt = tuyen_sinh_dh_chinhquy_2024['liên thông chính quy']['doi_tuong_tuyen_sinh']
                tieu_chuan_tuyen_sinh_lt_chinh_tri = tuyen_sinh_dh_chinhquy_2024['liên thông chính quy']['tieu_chuan_tuyen_sinh']['chinh_tri']
                doi_tuong_tuyen_sinh_lt_van_hoa_chuyen_mon = tuyen_sinh_dh_chinhquy_2024['liên thông chính quy']['tieu_chuan_tuyen_sinh']['van_hoa_chuyen_mon']
                tieu_chuan_tuyen_sinh_lt_suc_khoe = tuyen_sinh_dh_chinhquy_2024['liên thông chính quy']['tieu_chuan_tuyen_sinh']['suc_khoe']
                response += "+ Đối tượng: "+doi_tuong_tuyen_sinh_lt
                response += "<br>+ Tiêu chuẩn chính trị: "+tieu_chuan_tuyen_sinh_lt_chinh_tri
                response += "<br>+ Tiêu chuẩn văn hóa chuyên môn: "+doi_tuong_tuyen_sinh_lt_van_hoa_chuyen_mon
                response += "<br>+ Tiêu chuẩn sức khỏe: "+tieu_chuan_tuyen_sinh_lt_suc_khoe
                
                doi_tuong_tuyen_sinh_sdh = tuyen_sinh_dh_chinhquy_2024['sau đại học chính quy']
                response += f"<br>- Đối tượng tuyển sinh sau đại học gôm:<br>"+doi_tuong_tuyen_sinh_sdh

            if  'doi_tuong_tuyen_sinh' in role and 'thong_tin_tuyen_sinh' in role and 'dai_hoc_chinh_quy' in role:
                response = f"<br>- Đối tượng tuyển sinh đại học gồm <br>"
                doi_tuong_tuyen_sinh_dh = tuyen_sinh_dh_chinhquy_2024['đại học chính quy']['doi_tuong_tuyen_sinh']
                vung_tuyen_sinh_dh = tuyen_sinh_dh_chinhquy_2024['đại học chính quy']['vung_tuyen_sinh']
                response += "+ Đối tượng: "+doi_tuong_tuyen_sinh_dh
                response += "<br>+ Vùng tuyển sinh: "+vung_tuyen_sinh_dh
            if  'doi_tuong_tuyen_sinh' in role and 'thong_tin_tuyen_sinh' in role and 'lien_thong' in role:
                response = f"<br>- Đối tượng tuyển sinh liên thông gồm:<br>"
                doi_tuong_tuyen_sinh_lt = tuyen_sinh_dh_chinhquy_2024['liên thông chính quy']['doi_tuong_tuyen_sinh']
                tieu_chuan_tuyen_sinh_lt_chinh_tri = tuyen_sinh_dh_chinhquy_2024['liên thông chính quy']['tieu_chuan_tuyen_sinh']['chinh_tri']
                doi_tuong_tuyen_sinh_lt_van_hoa_chuyen_mon = tuyen_sinh_dh_chinhquy_2024['liên thông chính quy']['tieu_chuan_tuyen_sinh']['van_hoa_chuyen_mon']
                tieu_chuan_tuyen_sinh_lt_suc_khoe = tuyen_sinh_dh_chinhquy_2024['liên thông chính quy']['tieu_chuan_tuyen_sinh']['suc_khoe']
                response += "+ Đối tượng: "+doi_tuong_tuyen_sinh_lt
                response += "<br>+ Tiêu chuẩn chính trị: "+tieu_chuan_tuyen_sinh_lt_chinh_tri
                response += "<br>+ Tiêu chuẩn văn hóa chuyên môn: "+doi_tuong_tuyen_sinh_lt_van_hoa_chuyen_mon
                response += "<br>+ Tiêu chuẩn sức khỏe: "+tieu_chuan_tuyen_sinh_lt_suc_khoe

            if  'doi_tuong_tuyen_sinh' in role and 'thong_tin_tuyen_sinh' in role and 'sau_dai_hoc' in role:
                response = f"<br>- Đối tượng tuyển sinh sau đại học gôm:<br>"+doi_tuong_tuyen_sinh_sdh
        except KeyError:
            response = "Bạn vui lòng nhập đầy đủ câu hỏi<br>Ví dụ:<br>- Đối tượng tuyển sinh đại học<br>- Đối tượng tuyển sinh liên thông<br>- Đối tượng tuyển sinh sau đại học."
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_doi_tuong_tuyen_sinh_dh_lt_sdh: ' + tracker.latest_message['text'])
        dispatcher.utter_message(text=response)
        
        return  []

class actionThongTinKyTucXa(Action):
    def name(self):
        return "action_thong_tin_ky_tuc_xa"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action thông tin ký túc xá")
        entities = tracker.latest_message['entities']
        # print(f"\nnEntity từ input : {entities}")
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        
        response = f"Tôi có thông tin về ký túc xá xem chi tiết tại đây: https://www.facebook.com/KytucxaTDHYDCT/"
        dispatcher.utter_message(text=response)
        
        return []

#=====================
#                   ||
#   PHUONG          ||
#                   ||
#=====================

class actionGoiYDiadiemkhoa(Action):
    def name(self):
        return "action_goi_y_khoa"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #lấy ra entity từ câu chat
        entities = tracker.latest_message['entities']
        print(f"\n\nEntities từ input: {entities} ")
        
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)

        #in slot
        print("Slot : ", tracker.get_slot(''))
        
        return []

class actionDiadiemkhoa(Action):
    def name(self):
        return "action_diadiem_khoa"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        list_thong_tin = constant.get_thongtin_khoa()
        
        #lấy ra entity từ câu chat
        entities = tracker.latest_message['entities']
        print(f"\n\nEntities từ input: {entities} ")
        
        response = "Vui lòng nhập đầy đủ câu hỏi: Địa điểm + tên khoa cần tìm."
        slot_tenkhoa = tracker.get_slot('ten_khoa')
        print(f"slot tên khoa khi hỏi địa điểm là {slot_tenkhoa}")
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
                               
        if 'where' in role and 'ten_khoa' in role:
            if slot_tenkhoa in list_thong_tin:
                print(123)
                response = f"Địa chỉ của {list_thong_tin[slot_tenkhoa]['Tên']:} : \n"   
                response += list_thong_tin[slot_tenkhoa]['Địa chỉ']
            else : response = "Tìm khong thấy tên khoa"
        dispatcher.utter_message(text=response)
        
        return [SlotSet("ten_khoa", None)]
    
class actionGiayxacnhan(Action):
    def name(self):
        return "action_giay_xac_nhan"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # lấy entities từ câu chat của người dùng
        entities = tracker.latest_message['entities']
        print(f"\n\nEntities từ input: {entities} ")
        
        #lấy ra slots
        giayxacnhan = tracker.get_slot('giayxacnhan')
        ask = tracker.get_slot('ask')
        print(f"Slot giayxacnhan: {giayxacnhan}")
        print(f"Slot ask: {ask}")
        
        #mảng role 
        giayxacnhan_roles = {
            'GiayVayVon': False,
            'GiayTamHoanNghiaVu': False,
            'GiamThue': False
        }

        list_thong_tin_can_biet = constant.get_thong_tin_can_biet()

        # Phân loại các role từ entities
        for entity in entities:
            if entity.get('entity') == 'giayxacnhan' and entity.get('role'):
                role = entity.get('role')
                if role in giayxacnhan_roles:
                    giayxacnhan_roles[role] = True
        print(f"Roles của giayxacnhan: {giayxacnhan_roles}")

        if giayxacnhan_roles['GiayVayVon'] or  giayxacnhan_roles['GiayTamHoanNghiaVu'] or giayxacnhan_roles['GiamThue']:
            thong_tin = list_thong_tin_can_biet['hoan_nghia_vu_vay_von_giam_thue']
            response = f"{thong_tin['mota']}"
            response += f"Yêu cầu:{thong_tin['yeucau']}"
            response += f"{thong_tin['thoigian']}"
        else:
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_the_sv: '+ tracker.latest_message['text'])
            response = "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."

        # Gửi phản hồi tới người dùng
        dispatcher.utter_message(text=response)
        return [SlotSet("ask", None) , SlotSet("giayxacnhan", None)]

class actionTroCap(Action):
    def name(self):
        return "action_tro_cap"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #lấy ra entity từ câu chat
        entities = tracker.latest_message['entities']
        print(f"\n\nEntities từ input: {entities}")
        
        tro_cap_slot = tracker.get_slot('tro_cap')
        print(f"Slot trợ cấp: {tro_cap_slot}")
        
        list_thong_tin_can_biet = constant.get_thong_tin_can_biet()
        
        input_value = None
        
        for entity in entities:
            if entity.get('entity') == "tro_cap":
                input_value = entity.get('value')
                
        if input_value in list_thong_tin_can_biet:
            thong_tin = list_thong_tin_can_biet[input_value]
            response = f"{thong_tin['mota']}"
            response += f"Yêu cầu:{thong_tin['yeucau']}"
            response += f"{thong_tin['thoigian']}"
        else:
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_the_sv: '+ tracker.latest_message['text'])
            response= "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."
        dispatcher.utter_message(text=response)
        return []

class actionThuVien_TTHL(Action):
    def name(self):
        return "action_thuvien_tthl"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message['entities']
        print(f"Entity từ input: {entities}")
        
        list_thong_tin_can_biet = constant.get_thong_tin_can_biet()
        
        the_thu_vien_slot = tracker.get_slot('the_tv_tthl')
        print(f"Slot thẻ thư viện/TTHL: {the_thu_vien_slot}")
        
        input_value = None
        
        for entity in entities:
            if (entity.get('entity') == "the_tv_tthl"):
                input_value = entity.get('value')
                
        if input_value in list_thong_tin_can_biet:
            thong_tin = list_thong_tin_can_biet[input_value]
            response = f"{thong_tin['mota']}"
            response += f"Yêu cầu:{thong_tin['yeucau']}"
            response += f"{thong_tin['thoigian']}"
        else:
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_the_sv: '+ tracker.latest_message['text'])
            response = "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."

            
        dispatcher.utter_message(text= response)
        return []

class actionGiayCongTac(Action):
    def name(self):
        return "action_giay_cong_tac"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        list_thong_tin_can_biet = constant.get_thong_tin_can_biet()
        
        entities = tracker.latest_message['entities']
        print(f"Entity từ input: {entities}")

        slot_giay_cong_tac = tracker.get_slot('giay_cong_tac')
        print(f"Slot giay cong tac {slot_giay_cong_tac}")

        input_value = None

        for entity in entities:
            if entity.get('entity') == "giay_CT":
                input_value = entity.get('value')
                
        if input_value in list_thong_tin_can_biet:
            thong_tin = list_thong_tin_can_biet[input_value]
            response = f"{thong_tin['mota']}"
            response += f"Yêu cầu:{thong_tin['yeucau']}"
            response += f"{thong_tin['thoigian']}"
        else:
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_the_sv: '+ tracker.latest_message['text'])
            response = "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."

        dispatcher.utter_message(text=response)
        return []

class actionCapTheSinhVien(Action):
    def name(self):
        return "action_cap_the_sv"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        list_thong_tin = constant.get_thong_tin_can_biet()
        
        entities = tracker.latest_message['entities']
        print(f"\n\nEntity từ input : {entities}")
        
        input_value = None
        
        for entity in entities:
            if entity.get('entity') == "the_sv":
                input_value = entity.get('value')
                
        if input_value in list_thong_tin:
            thong_tin = list_thong_tin[input_value]
            response = f"{thong_tin['mota']}"
            response += f"Yêu cầu:{thong_tin['yeucau']}"
            response += f"{thong_tin['thoigian']}"
        else: 
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_the_sv: '+ tracker.latest_message['text'])
            response = "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."
        
        dispatcher.utter_message(text = response)
        return []
    
class actionHocBong(Action):
    def name(self):
        return "action_hoc_bong"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        list_thong_tin = constant.get_thong_tin_can_biet()
        
        entities = tracker.latest_message['entities']
        print(f"\n\nEntity từ input : {entities}")
        
        input_value = None
        
        for entity in entities:
            if entity.get('entity') == "hoc_bong":
                input_value = entity.get('value')
                
        if input_value in list_thong_tin:
            thong_tin = list_thong_tin[input_value]
            response = f"{thong_tin['mota']}"
            response += f"Yêu cầu: {thong_tin['yeucau']}"
            response += f"{thong_tin['thoigian']}"
        else: 
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_the_sv: '+ tracker.latest_message['text'])
            response = "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."
        
        dispatcher.utter_message(text = response)
        return []
    
class actionBaoLuu(Action):
    def name(self):
        return "action_baoluu_thoihoc"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        list_thong_tin = constant.get_thong_tin_can_biet()
        
        entities = tracker.latest_message['entities']
        print(f"\n\nEntity từ input : {entities}")
        
        thoihoc_slot = tracker.get_slot('baoluu_thoihoc')
        print(f"slot của baoluu_thoihoc là: {thoihoc_slot}")
        
        input_value = None
        
        for entity in entities:
            if entity.get('entity') == "baoluu_thoihoc":
                input_value = entity.get('value')
                
        if input_value in list_thong_tin:
            thong_tin = list_thong_tin[input_value]
            response = f"{thong_tin['mota']}"
            response += f"Yêu cầu: {thong_tin['yeucau']}"
            response += f"{thong_tin['thoigian']}"
        else: 
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_the_sv: '+ tracker.latest_message['text'])
            response = "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."
        
        dispatcher.utter_message(text = response)
        return []

class actionBHYT(Action):
    def name(self):
        return "action_cap_thaydoi_BHYT"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        list_thong_tin = constant.get_thong_tin_can_biet()
        
        entities = tracker.latest_message['entities']
        print(f"\n\nEntity từ input : {entities}")
        
        BHYT_slot = tracker.get_slot('the_BHYT')
        print(f"slot của the_BHYT là: {BHYT_slot}")
        
        input_value = None
        
        for entity in entities:
            if entity.get('entity') == "the_BHYT":
                input_value = 'caplai_thaydoi_BHYT'
                
        if input_value in list_thong_tin:
            thong_tin = list_thong_tin[input_value]
            response = f"{thong_tin['mota']}"
            response += f"Yêu cầu: {thong_tin['yeucau']}"
            response += f"{thong_tin['thoigian']}"
        else: 
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_the_sv: '+ tracker.latest_message['text'])
            response = "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."
        
        dispatcher.utter_message(text = response)
        return []
    
class actionTK_QLDT(Action):
    def name(self):
        return "action_caplai_tk_QLDT"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        list_thong_tin = constant.get_thong_tin_can_biet()
        
        entities = tracker.latest_message['entities']
        print(f"\n\nEntity từ input : {entities}")
        
        QLDT_slot = tracker.get_slot('taikhoan_QLDT')
        print(f"slot của the_BHYT là: {QLDT_slot}")
        
        input_value = None
        
        for entity in entities:
            if entity.get('entity') == "tk_qldt":
                input_value = 'caplai_qldt'
                
        if input_value in list_thong_tin:
            thong_tin = list_thong_tin[input_value]
            response = f"{thong_tin['mota']}"
            response += f"Yêu cầu: {thong_tin['yeucau']}"
            response += f"{thong_tin['thoigian']}"
        else: 
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_the_sv: '+ tracker.latest_message['text'])
            response = "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."
        
        dispatcher.utter_message(text = response)
        return []

class actionEmailSV(Action):
    def name(self):
        return "action_caplai_email"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        list_thong_tin = constant.get_thong_tin_can_biet()
        
        entities = tracker.latest_message['entities']
        print(f"\n\nEntity từ input : {entities}")
        
        input_value = None
        
        email_sv_slot = tracker.get_slot('email_sv')
        print(f"slot của caplai_email là: {email_sv_slot}")
        
        for entity in entities:
            if entity.get('entity') == "caplai_email_sv":
                input_value = 'caplai_email'
                
        if input_value in list_thong_tin:
            thong_tin = list_thong_tin[input_value]
            response = f"{thong_tin['mota']}"
            response += f"Yêu cầu: {thong_tin['yeucau']}"
            response += f"{thong_tin['thoigian']}"
        else: 
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_the_sv: '+ tracker.latest_message['text'])
            response = "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."
        
        dispatcher.utter_message(text = response)
        return []
    
class actionBHTN(Action):
    def name(self):
        return "action_caplai_thanhphi_BHTN"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        list_thong_tin = constant.get_thong_tin_can_biet()
        
        entities = tracker.latest_message['entities']
        print(f"\n\nEntity từ input : {entities}")
        
        input_value = None
        
        caplai_thanhphi_BHTN_slot = tracker.get_slot('caplai_thanhphi_BHTN')
        print(f"slot của caplai_thanhphi_bhtn là: {caplai_thanhphi_BHTN_slot}")
        
        for entity in entities:
            if entity.get('entity') == "caplai_thanhphi_bhtn":
                input_value = 'caplai_thanhphi_BHTN'
                
        if input_value in list_thong_tin:
            thong_tin = list_thong_tin[input_value]
            response = f"{thong_tin['mota']}"
            response += f"Yêu cầu: {thong_tin['yeucau']}"
            response += f"{thong_tin['thoigian']}"
        else: 
            file_writer = write_file()
            file_writer.get_ghi_log_file('action_cap_lai_the_sv: '+ tracker.latest_message['text'])
            response = "Xin lỗi tôi không có thông tin về câu hỏi này! Vui lòng cung cấp chi tiết thông tin."
        
        dispatcher.utter_message(text = response)
        return []

class actionGoiYHocPhi(Action):
    def name(self):
        return "action_goi_y_hocphi"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("action Gợi ý học phí")
        entities = tracker.latest_message['entities']
        print(f"Entity từ input : {entities}")
        
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        response = "Tôi có thông tin học phí của các ngành:<br>- Y khoa,<br>- Răng hàm mặt,<br>- Y học dự phòng<br>- Y học cổ truyền<br>- Dược<br>- Điều dưỡng<br>- Y tế công cộng<br>- Kỹ thuật xét nghiệm y học<br>- Hộ sinh<br>- Kỹ thuật hình ảnh y học"
        print("action Gợi ý học phí")
        entities = tracker.latest_message['entities']
        print(f"Entity từ input : {entities}")
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        response = "Tôi có thông tin học phí của các ngành:<br>- Y khoa,<br>- Răng hàm mặt,<br>- Y học dự phòng<br>- Y học cổ truyền<br>- Dược<br>- Điều dưỡng<br>- Y tế công cộng<br>- Kỹ thuật xét nghiệm y học<br>- Hộ sinh<br>- Kỹ thuật hình ảnh y học"

        dispatcher.utter_message(text=response)

        return []

class actionHocPhiNganh(Action):
    def name(self):
        return "action_hocphi_nganh"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message['entities']
        print(f"\n\nEntity từ input: {entities}")
        
        print("ACTION HOI HOC PHI NGÀNH CỤ THỂ")
        
        infor_ctdt_hoc_phi = constant.get_hocphi_ctdt()
        
        slot_ten_nganh = tracker.get_slot('ten_nganh')
        print(f"Slot tên ngành là: {slot_ten_nganh}")
        
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("mảng role: ", role)
        if 'hoi_hocphi' in role:
            response = "Bạn vui lòng nhập đầy đủ câu hỏi<br> Ví dụ:<br>- Học phí + tên ngành<br>- Chương trình đào tạo + tên ngành"
        else: response  = 'TÔi không hiểu câu hỏi của bạn.'
        found = False
        
        if 'ten_nganh' in role and 'hoi_hocphi' in role:
            response = f"<br>Học phí của ngành {slot_ten_nganh} : "
            # # Chính Quy
            # # Trúng tuyển chính quy
            if slot_ten_nganh in infor_ctdt_hoc_phi['daihoc']['he_chinhquy']['chinhquy']:
                response += "<br>Hệ chính quy :" 
                response += f"<br>- Đào tạo trúng tuyển chính quy : " + infor_ctdt_hoc_phi['daihoc']['he_chinhquy']['chinhquy'][slot_ten_nganh]['hocphi'] + "/tín chỉ"
                found = True
            
            # Đào tạo theo nhu cầu xã hội
            if slot_ten_nganh in infor_ctdt_hoc_phi['daihoc']['he_chinhquy']['nhu_cau_xh']:
                response += "<br>- Đào tạo theo nhu cầu xã hội (theo đặt hàng ) : " + infor_ctdt_hoc_phi['daihoc']['he_chinhquy']['nhu_cau_xh'][slot_ten_nganh]['hocphi'] + "/tín chỉ"
                found = True
            
            # Đào tạo hệ quốc tế tiếng anh
            if slot_ten_nganh in infor_ctdt_hoc_phi['daihoc']['he_chinhquy']['qte_tieng_anh']:
                response += "<br>- Đào tạo hệ quốc tế tiếng anh : " + infor_ctdt_hoc_phi['daihoc']['he_chinhquy']['qte_tieng_anh'][slot_ten_nganh]['hocphi'] + "/tín chỉ"
                found = True
            
            # Liên thông
            # Liên thông chính quy
            if slot_ten_nganh in infor_ctdt_hoc_phi['daihoc']['he_lienthong']['lt_chinhquy']:
                response += "<br>Hệ liên thông : "
                response += "<br>- Đào tạo liên thông hệ chính quy : " + infor_ctdt_hoc_phi['daihoc']['he_lienthong']['lt_chinhquy'][slot_ten_nganh]['hocphi'] + "/tín chỉ"
                found = True

            # Liên thông theo nhu cầu xã hội
            if slot_ten_nganh in infor_ctdt_hoc_phi['daihoc']['he_lienthong']['lt_nhu_cau_xh']:
                response += "<br>- Đào tạo liên thông theo nhu cầu xã hội : " + infor_ctdt_hoc_phi['daihoc']['he_lienthong']['lt_nhu_cau_xh'][slot_ten_nganh]['hocphi'] + "/tín chỉ"
                found = True
            if not found:
                response = f"Không tìm thấy ngành {slot_ten_nganh} bạn yêu cầu."
        else :
            response = "Tôi có thông tin của các ngành như: Y khoa, răng hàm mặt, dược, ... Bạn muốn biết học phí của ngành nào."
        dispatcher.utter_message(text=response) 
        
        return [SlotSet("ten_nganh", None)]

class actionEmailKhoa(Action):
    def name(self):
        return "action_email_khoa"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message['entities']
        print(f"\n\nEntity từ input: {entities}")
        
        print("ACTION HOI EMAIL KHOA CỤ THỂ")
        
        list_email = constant.get_thongtin_khoa()
        
        slot_ten_khoa = tracker.get_slot('ten_khoa')
        print(f"slot tên của khoa là: {slot_ten_khoa}")
        
        role = []
        for entity in entities:
            if entity.get('role') not in role:
                role.append(entity.get('role'))
        print("\nMảng role: ", role)
        
        if 'email' in role:
            response = f"Bạn vui lòng nhập đầy đủ câu hỏi<br> Ví dụ:<br>- Học phí + tên ngành<br>- Chương trình đào tạo + tên ngành"
        if 'ten_khoa' in role and 'email' in role:
            response = f"Email của khoa {slot_ten_khoa}: " + list_email[slot_ten_khoa]['Email']
        else : response = "Tôi không hiểu câu hỏi của bạn."
        dispatcher.utter_message(text=response)
        return [SlotSet("ten_khoa", None)]
    
