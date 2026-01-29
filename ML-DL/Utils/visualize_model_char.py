import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (precision_recall_curve, roc_curve,
                                auc, classification_report,
                                confusion_matrix, f1_score)
from sklearn.preprocessing import label_binarize


def visualize_model_char(model, x_val, y_val, class_names=None):
    """
    모델의 성능을 평가하고 혼동 행렬과 다양한 지표를 시각화합니다.

    Parameters:
        model: keras.Model - 평가할 Keras 모델
        x_val: np.array - 검증 데이터 (입력)
        y_val: np.array 또는 list - 검증 데이터 (레이블)
        class_names: list - 클래스 이름 (옵션, 제공하지 않을 경우 숫자 인덱스로 표시)

    Returns:
        None
    """

    # y_val을 numpy 배열로 변환
    y_val = np.array(y_val)

    # 클래스 이름 설정
    num_classes = len(np.unique(y_val))
    if class_names is None:
        class_names = [f"Class {i}" for i in range(num_classes)]

    # 예측 수행
    predictions = model.predict(x_val)
    predicted_classes = predictions.argmax(axis=1)  # 클래스별 확률 중 가장 높은 값을 선택

    # 레이블 이진화 (ROC-AUC 및 다중 클래스 대응)
    y_val_binarized = label_binarize(y_val, classes=range(num_classes))

    # 정밀도-재현율 곡선 및 ROC 곡선 준비
    precision = {}
    recall = {}
    fpr = {}
    tpr = {}
    pr_auc = {}
    roc_auc = {}

    for i in range(num_classes):
        # 각 클래스별로 Precision-Recall 곡선 데이터 생성
        precision[i], recall[i], thresholds = precision_recall_curve(y_val_binarized[:, i], predictions[:, i])
        # 각 클래스별로 ROC 곡선 데이터 생성
        fpr[i], tpr[i], _ = roc_curve(y_val_binarized[:, i], predictions[:, i])
        # PR AUC와 ROC AUC 계산
        pr_auc[i] = auc(recall[i], precision[i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # 1. Precision-Recall Curve 서브플롯
    fig, axes = plt.subplots(2, 5, figsize=(18, 9))  # 클래스 수만큼 서브플롯 생성
    axes = axes.ravel()

    for i in range(num_classes):
        # F1-스코어 계산
        f1_scores = 2 * (precision[i] * recall[i]) / (precision[i] + recall[i] + 1e-10)  # 분모에 작은 값 추가로 NaN 방지
        max_f1_index = np.argmax(f1_scores)  # F1-스코어 최대값 위치
        max_f1 = f1_scores[max_f1_index]  # 최대 F1-스코어 값

        # PR 커브 그리기
        axes[i].plot(recall[i], precision[i], label=f'PR AUC = {pr_auc[i]:.2f}')
        axes[i].scatter(recall[i][max_f1_index], precision[i][max_f1_index], color='red', label=f'Max F1 = {max_f1:.2f}')
        axes[i].set_title(f'Precision-Recall: {class_names[i]}')
        axes[i].set_xlabel('Recall')
        axes[i].set_ylabel('Precision')
        axes[i].legend()
        axes[i].grid()

    plt.tight_layout()
    plt.show()

    # 2. ROC Curve 서브플롯
    fig, axes = plt.subplots(2, 5, figsize=(18, 9))  # 서브플롯: 클래스별로 개별 ROC 곡선 표시
    axes = axes.ravel()

    for i in range(num_classes):
        axes[i].plot(fpr[i], tpr[i], label=f'ROC AUC = {roc_auc[i]:.2f}')
        axes[i].plot([0, 1], [0, 1], 'k--')  # 무작위 예측 기준선
        axes[i].set_title(f'ROC Curve: {class_names[i]}')
        axes[i].set_xlabel('False Positive Rate')
        axes[i].set_ylabel('True Positive Rate')
        axes[i].legend()
        axes[i].grid()

    plt.tight_layout()
    plt.show()

    # 3. 혼동 행렬 시각화
    conf_matrix = confusion_matrix(y_val, predicted_classes)

    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=class_names, yticklabels=class_names)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted Labels")
    plt.ylabel("True Labels")
    plt.show()

    # 4. Classification Report
    print("\nClassification Report:")
    print(classification_report(y_val, predicted_classes, target_names=class_names))

    # 5. F1-Score 막대그래프
    f1_per_class = f1_score(y_val, predicted_classes, average=None)  # 클래스별 F1-스코어 계산

    plt.figure(figsize=(8, 6))
    plt.bar(range(num_classes), f1_per_class, tick_label=class_names)
    plt.title('F1-Score per Class')
    plt.xlabel('Class')
    plt.ylabel('F1-Score')
    plt.grid(axis='y')
    plt.show()
