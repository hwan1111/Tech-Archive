import os
from collections import Counter

def count_labels_from_txt(txt_file, dataset_root):
    """
    autosplit TXT 파일에서 레이블 총 개수와 클래스별 개수를 계산.
    
    Args:
        txt_file (str): autosplit TXT 파일 경로.
        dataset_root (str): 데이터셋의 루트 디렉토리 경로.
    
    Returns:
        tuple: 총 레이블 개수, 클래스별 개수 (Counter 객체)
    """
    total_labels = 0
    class_counts = Counter()

    if not os.path.exists(txt_file):
        print(f"TXT file {txt_file} does not exist.")
        return total_labels, class_counts

    with open(txt_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            image_path = os.path.join(dataset_root, line.strip().lstrip("./"))  # 이미지 절대 경로 변환
            label_path = image_path.replace("/camera_image/", "/labels/").replace(".jpg", ".txt")

            # 라벨 파일이 존재하면 클래스 정보 추출
            if os.path.exists(label_path):
                with open(label_path, "r") as label_file:
                    for label_line in label_file:
                        class_id = int(label_line.split()[0])  # 클래스 ID 추출
                        class_counts[class_id] += 1
                        total_labels += 1

    return total_labels, class_counts
