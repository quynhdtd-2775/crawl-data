from bs4 import BeautifulSoup
import requests

# # URL của trang web bạn muốn lấy dữ liệu từ
# url = f"https://luanvan.moet.gov.vn/?page=1.31"

# # Gửi yêu cầu HTTP đến trang web và lấy nội dung HTML
# response = requests.get(url)
# html_content = response.text

# # Sử dụng BeautifulSoup để phân tích HTML
# soup = BeautifulSoup(html_content, "html.parser")

# # Tìm tất cả các đối tượng có class là "tdKevach"
# td_kevach_objects = soup.find_all(class_="tdKevach")

# # Lặp qua mảng các đối tượng
# for obj in td_kevach_objects:
#     # Tìm tất cả các thẻ <a> trong đối tượng hiện tại
#     a_tags = obj.find_all("a")
    
#     # Lặp qua mảng các thẻ <a>
#     for a_tag in a_tags:
#         # Tìm thẻ <b> trong thẻ <a>
#         b_tag = a_tag.find("b")
        
#         # Kiểm tra xem thẻ <b> có tồn tại không
#         if b_tag:
#             # In ra nội dung của thẻ <b>
#             print(b_tag.text)


def get_data(page_num):
    # URL của trang web với page_num được truyền vào
    url = f"https://luanvan.moet.gov.vn/?page=1.31&page_num={page_num}"
    
    # Gửi yêu cầu HTTP và lấy nội dung HTML
    response = requests.get(url)
    html_content = response.text

    # Sử dụng BeautifulSoup để phân tích HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Tìm và in ra các thông tin bạn quan tâm từ trang web này
    td_kevach_objects = soup.find_all(class_="tdKevach")

    # Lặp qua mảng các đối tượng
    for obj in td_kevach_objects:
        # Tìm tất cả các thẻ <a> trong đối tượng hiện tại
        a_tags = obj.find_all("a")
        
        # Lặp qua mảng các thẻ <a>
        for a_tag in a_tags:
            # Tìm thẻ <b> trong thẻ <a>
            b_tag = a_tag.find("b")
            
            # Kiểm tra xem thẻ <b> có tồn tại không
            if b_tag:
                # In ra nội dung của thẻ <b>
                print(b_tag.text)


# Sử dụng vòng lặp để lấy dữ liệu từ các trang từ page_num 2 đến 222
for page_num in range(2, 223):
    get_data(page_num)