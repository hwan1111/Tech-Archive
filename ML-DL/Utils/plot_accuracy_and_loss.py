def plot_accuracy_and_loss(history):
    """
    모델 학습 과정에서 정확도와 손실을 시각화하는 함수.

    Parameters:
        history: keras.callbacks.History - 모델 학습 후 반환된 히스토리 객체.

    Returns:
        None
    """
    import matplotlib.pyplot as plt

    # 에포크 수
    epochs = range(1, len(history.history['accuracy']) + 1)  # 히스토리에서 에포크 범위 계산

    # 그래프 크기 설정
    plt.figure(figsize=(14, 6)) 

    # 1. 정확도 시각화
    plt.subplot(1, 2, 1)  # 1행 2열 중 첫 번째 그래프
    plt.plot(epochs, history.history['accuracy'], label='Training Accuracy', marker='o')  # 훈련 정확도
    plt.plot(epochs, history.history['val_accuracy'], label='Validation Accuracy', marker='o', linestyle='--')  # 검증 정확도
    plt.title('Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.xticks(epochs)
    plt.legend()
    plt.grid(True)

    # 2. 손실 시각화
    plt.subplot(1, 2, 2)  # 1행 2열 중 두 번째 그래프
    plt.plot(epochs, history.history['loss'], label='Training Loss', marker='o')  # 훈련 손실
    plt.plot(epochs, history.history['val_loss'], label='Validation Loss', marker='o', linestyle='--')  # 검증 손실
    plt.title('Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.xticks(epochs)
    plt.legend()
    plt.grid(True)

    # 레이아웃 정리 및 출력
    plt.tight_layout()  # 그래프 간 간격 자동 조정
    plt.show()
