import cv2
from pathlib import Path

def process_video(detector, input_path: str, output_path: str):

    """
    Обрабатывает видео: делает детекцию людей и сохраняет отрисованное видео.

    :param detector: YOLO модель.
    :param input_path: Путь к входному видеофайлу.
    :param output_path: Путь для сохранения выходного видео с отрисованными людьми.
    """

    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Файл {input_path} не найден.")
    
    cap = cv2.VideoCapture(str(input_path))

    if not cap.isOpened():
        raise IOError(f"Не удалось открыть видео {input_path}.")
    
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        
        if not ret:
            break

        results = detector(frame)[0]


        for box in results.boxes:
            cls_id = int(box.cls[0])
            if cls_id != 0:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            label = f"class_id: {cls_id}|{conf:.2f}"

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        out.write(frame)

    cap.release()
    out.release()
