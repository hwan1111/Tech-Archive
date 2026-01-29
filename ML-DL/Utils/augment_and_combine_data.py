import numpy as np

def augment_and_combine_data(images, labels, augment_layer, augment_ratio=0.5):
    '''
    입력 데이터의 일부를 증강하고, 원본 데이터와 결합하여 반환.

    Parameters:
        images (numpy.ndarray or tf.Tensor): 입력 이미지 배열 또는 텐서.
        labels (numpy.ndarray or tf.Tensor): 해당하는 레이블 배열 또는 텐서.
        augment_layer (tf.keras.layers.Layer): 데이터 증강에 사용되는 TensorFlow 증강 레이어.
        augment_ratio (float, optional, default=0.5): 데이터셋 중 증강할 비율.

    Returns:
        combined_images (numpy.ndarray): 원본 이미지와 증강 이미지를 결합한 배열.
        combined_labels (numpy.ndarray): 원본 레이블과 증강 레이블을 결합한 배열.
    '''
    # 증강 데이터 생성
    num_augment = int(len(images) * augment_ratio)
    augmented_images = augment_layer(images[:num_augment], training=True)
    augmented_labels = labels[:num_augment]

    # 원본 데이터와 증강 데이터 합치기
    combined_images = np.concatenate([images, augmented_images.numpy()], axis=0)
    combined_labels = np.concatenate([labels, augmented_labels], axis=0)

    return combined_images, combined_labels
