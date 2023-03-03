import os

# 띄어쓰기 제거 함수
def remove_whitespace(filename):
    return filename.replace("_", "_")
num_digits = 10
# 파일 이름 변경 함수

def rename_files(directory):
    i=0
    for filename in os.listdir(directory):
        # 띄어쓰기 제거
        
        new_filename = '{:0{}}.jpg'.format(i, num_digits)
        # 파일 이름 변경
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        i+=1
        
# 폴더 경로
directory_path ="D:/result/color"

# 파일 이름 변경 함수 호출
rename_files(directory_path)