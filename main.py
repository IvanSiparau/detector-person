import argparse
from detector import process_video
from ultralytics import YOLO


def main():
    """
    Основная функция для запуска детекции людей на видео.
    """
    parser = argparse.ArgumentParser(description="Детекция людей на видео с помощью YOLO.")
    parser.add_argument('--input', '-i', type=str, required=True, help="Путь к входному видео.")
    parser.add_argument('--output', '-o', type=str, required=True, help="Путь для сохранения выходного видео.")

    args = parser.parse_args()
    detector = YOLO('yolo12m.pt', verbose=False)

    process_video(detector, args.input, args.output)

if __name__ == "__main__":
    main()