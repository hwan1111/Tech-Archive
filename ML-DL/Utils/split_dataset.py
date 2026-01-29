import os
import random
import shutil

def split_dataset(image_source, label_source, train_dir, val_dir, test_dir, train_ratio=0.7, val_ratio=0.2):
    """
    데이터셋을 학습(train), 검증(val), 테스트(test) 세트로 분리하는 함수.

    Parameters:
    - image_source (str): 원본 이미지 파일들이 저장된 디렉토리 경로.
    - label_source (str): 원본 라벨 파일들이 저장된 디렉토리 경로.
    - train_dir (str): 학습 이미지 및 라벨 파일을 저장할 디렉토리 경로.
    - val_dir (str): 검증 이미지 및 라벨 파일을 저장할 디렉토리 경로.
    - test_dir (str): 테스트 이미지 및 라벨 파일을 저장할 디렉토리 경로.
    - train_ratio (float): 학습 데이터셋 비율 (기본값: 0.7).
    - val_ratio (float): 검증 데이터셋 비율 (기본값: 0.2).
    
    Returns:
    - None: 이미지와 라벨 파일이 지정된 디렉토리로 이동됨.

    Function Description:
    1. 지정된 원본 디렉토리에서 파일 리스트를 가져옵니다.
    2. 학습, 검증, 테스트 비율에 따라 데이터셋을 무작위로 분할합니다.
    3. 분할된 파일 리스트를 각각의 대상 디렉토리로 이동합니다.
    4. 이미지 파일에 맞는 라벨 파일도 함께 이동합니다.
    """

    # 이미지 소스 디렉토리에서 파일 목록 불러오기
    files = os.listdir(image_source)
    random.shuffle(files)  # 파일 리스트 무작위 셔플

    # 데이터셋 크기 계산
    train_count = int(len(files) * train_ratio)
    val_count = int(len(files) * val_ratio)
    test_count = len(files) - train_count - val_count

    # 데이터셋 분리
    train_files = files[:train_count]
    val_files = files[train_count:train_count + val_count]
    test_files = files[train_count + val_count:]

    def move_files(file_list, target_image_dir, target_label_dir):
        """
        지정된 파일 리스트를 대상 디렉토리로 이동하는 내부 함수.

        Parameters:
        - file_list (list): 이동할 파일 이름 리스트.
        - target_image_dir (str): 이미지 파일의 대상 디렉토리.
        - target_label_dir (str): 라벨 파일의 대상 디렉토리.

        Returns:
        - None: 파일이 대상 디렉토리로 이동됨.
        """
        for file in file_list:
            # 이미지 파일 이동
            shutil.move(os.path.join(image_source, file), os.path.join(target_image_dir, file))
            
            # 라벨 파일 이름 결정 (이미지 확장자를 텍스트 확장자로 변환)
            label_file = file.replace(".jpg", ".txt")  # 확장자에 따라 필요 시 수정
            
            # 라벨 파일 이동
            if os.path.exists(os.path.join(label_source, label_file)):
                shutil.move(os.path.join(label_source, label_file), os.path.join(target_label_dir, label_file))
            else:
                print(f"Label not found for {file}")  # 라벨 파일이 없는 경우 알림

    # 데이터셋 분리 후 파일 이동
    move_files(train_files, train_dir, os.path.join(train_dir, 'labels'))
    move_files(val_files, val_dir, os.path.join(val_dir, 'labels'))
    move_files(test_files, test_dir, os.path.join(test_dir, 'labels'))
