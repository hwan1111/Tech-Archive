import matplotlib.pyplot as plt

def plot_images(images, num_images, title_prefix=" "):
    """
    이미지들을 서브플롯으로 원하는 수만큼 시각화.

    Parameters:
        images (list of np.array): 증강된 이미지 배열의 리스트.
        num_images (int): 시각화할 이미지의 개수.
        title_prefix (str): 각 이미지 위에 표시할 제목의 접두사.

    Returns:
        None
    """
    # 요청한 이미지 수만큼 자르기
    images_to_plot = images[:num_images]

    fig, axes = plt.subplots(1, num_images, figsize=(num_images * 2, 5))  # 이미지 수에 따라 크기 조정
    for i, image in enumerate(images_to_plot):
        axes[i].imshow(image)
        axes[i].axis("off")
        axes[i].set_title(f"{title_prefix} {i+1}", fontsize=8)

    plt.tight_layout()
    plt.show()
