import os
import json

def save_history_to_json(history, directory, filename="history.json"):
    """
    모델 학습 히스토리를 JSON 파일로 저장하는 함수.

    Parameters:
    - history (keras.callbacks.History): model.fit()으로 반환된 학습 히스토리 객체.
    - directory (str): 히스토리를 저장할 디렉토리 경로.
    - filename (str): 저장할 파일 이름. 기본값은 'history.json'.

    Returns:
    - None
    """
    try:
        # 디렉토리가 존재하지 않으면 생성
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # 저장 경로 설정
        file_path = os.path.join(directory, filename)

        # 히스토리 객체에서 딕셔너리 추출
        history_dict = history.history

        # JSON 파일로 저장
        with open(file_path, 'w') as json_file:
            json.dump(history_dict, json_file)
        
        print(f"History successfully saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving history: {e}")
