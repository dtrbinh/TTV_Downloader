import os
import requests
from bs4 import BeautifulSoup
import re

# MODIFY CODE BELOW FOR YOUR NEED
novel_name = 'Truyện ngắn của Nam Cao'  # name of novel for folder name
base_url = 'https://truyen.tangthuvien.vn/doc-truyen/chi-pheo/'
number_of_chapter = 12  # download from 1 to number_of_chapter chapter


# DONT MODIFY CODE BELOW IF YOU DONT KNOW WHAT YOU ARE DOING
def downloadTo(novelName, baseURL, numberOfChapter):
    # Đường dẫn đến thư mục hiện tại
    current_directory = os.getcwd()

    # Đường dẫn tới thư mục mới
    new_folder_path = os.path.join(current_directory, novelName)

    # Tạo thư mục và tất cả các thư mục con nếu chưa tồn tại
    os.makedirs(new_folder_path, exist_ok=True)

    print("Saving path: " + new_folder_path)

    for i in range(0, numberOfChapter):
        chapter = 'chuong-' + str(i + 1)
        target_url = baseURL + chapter

        # Tải trang web
        response = requests.get(target_url)
        # Phân tích cú pháp HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        # Lấy tiêu đề của trang
        title = soup.title.string
        # Lấy tất cả các thẻ div có class chứa từ 'div_name'
        div_name = "box-chap box-chap-"
        divs = soup.find_all('div', {'class': lambda x: x and div_name in x})
        # Lấy nội dung của các thẻ div
        if len(divs) == 0:
            print("Error: " + str(i + 1) + '/' + str(numberOfChapter))
            continue
        else:
            div_content = divs[0]

        # print(title)
        # print(div_content)

        # Lưu lại
        chapter_name_number = str(title).split("-")[1]
        chapter_name = clean_filename('_'.join(chapter_name_number.split(":")[1].split()))
        file_name = str(i + 1) + '_' + chapter_name + ".txt"
        file_content = div_content.text

        with open(new_folder_path + '/' + file_name, 'w', encoding="utf-8") as file:
            file.write(title + "\n")
            file.write(file_content)
            file.close()

        print("Downloaded: " + str(i + 1) + '/' + str(numberOfChapter))
        # print('File name: ' + file_name)
        # print('File content: ' + file_content)


def downloadFromIndexToIndex(novelName, baseURL, fromIndex, toIndex):
    # Đường dẫn đến thư mục hiện tại
    current_directory = os.getcwd()

    # Đường dẫn tới thư mục mới
    new_folder_path = os.path.join(current_directory, novelName)

    # Tạo thư mục và tất cả các thư mục con nếu chưa tồn tại
    os.makedirs(new_folder_path, exist_ok=True)

    print("Saving path: " + new_folder_path)

    for i in range(fromIndex, toIndex):
        chapter = 'chuong-' + str(i + 1)
        target_url = baseURL + chapter

        # Tải trang web
        response = requests.get(target_url)
        # Phân tích cú pháp HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        # Lấy tiêu đề của trang
        title = soup.title.string
        # Lấy tất cả các thẻ div có class chứa từ 'div_name'
        div_name = "box-chap box-chap-"
        divs = soup.find_all('div', {'class': lambda x: x and div_name in x})
        # Lấy nội dung của các thẻ div
        div_content = divs[0]

        # print(title)
        # print(div_content)

        # Lưu lại
        chapter_name_number = str(title).split("-")[1]
        chapter_name = clean_filename('_'.join(chapter_name_number.split(":")[1].split()))
        file_name = str(i + 1) + '_' + chapter_name + ".txt"
        file_content = div_content.text

        with open(new_folder_path + '/' + file_name, 'w', encoding="utf-8") as file:
            file.write(title + "\n")
            file.write(file_content)
            file.close()

        print("Downloaded: " + str(i + 1) + '/' + str(toIndex))
        print('File name: ' + file_name)
        # print('File content: ' + file_content)


def clean_filename(filename):
    # List các ký tự không hợp lệ trong tên file
    illegal_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    # Thay thế các ký tự không hợp lệ bằng dấu gạch chân
    clean_name = re.sub('[{}]'.format(re.escape(''.join(illegal_chars))), '', filename)
    return clean_name


downloadTo(novel_name, base_url, number_of_chapter)

# downloadFromIndexToIndex(novel_name, base_url, 5, 10)
