import os


def create_project_structure():
    folders = [
        'src',
        'src/utils',
        'models',
        'data',
        'data/raw',
        'data/processed',
        'results',
        'results/logs',
        'results/outputs',
        'results/comparisons'
    ]

    files = [
        'README.md',
        'requirements.txt',
        'src/__init__.py',
        'src/main.py',
        'src/video_capture.py',
        'src/image_preprocessing.py',
        'src/cnn_model.py',
        'src/ml_model.py',
        'src/utils/__init__.py',
        'src/utils/logger.py',
        'src/utils/config.py'
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    for file in files:
        with open(file, 'w') as f:
            pass


if __name__ == '__main__':
    create_project_structure()
