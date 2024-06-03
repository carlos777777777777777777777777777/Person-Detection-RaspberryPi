import cv2
from video_capture import VideoCapture
from image_preprocessing import ImagePreprocessing
from cnn_model import CNNModel
from ml_model import MLModel


def main():
    video_capture = VideoCapture()
    image_processor = ImagePreprocessing()
    cnn_model = CNNModel()
    ml_model = MLModel()
    ml_model.load_model('path_to_pretrained_ml_model.pkl')

    while True:
        frame = video_capture.get_frame()
        if frame is None:
            break

        processed_frame = image_processor.preprocess(frame)
        cnn_prediction = cnn_model.predict(processed_frame)
        ml_prediction = ml_model.predict(processed_frame)

        print(
            f'CNN Prediction: {cnn_prediction}, ML Prediction: {ml_prediction}')

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
