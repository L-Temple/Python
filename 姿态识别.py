import cv2
import mediapipe as mp

# 初始化 Mediapipe Pose 模块
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# 初始化 OpenCV 的预训练 DNN 模型 (YOLO、SSD 或其他模型)
body_detector = cv2.dnn.readNetFromCaffe(
    "deploy.prototxt",  # 替换为你的 Caffe 模型配置文件路径
    "res10_300x300_ssd_iter_140000.caffemodel"  # 替换为你的模型权重文件路径
)

# 打开摄像头
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 初始化 Mediapipe 的 Pose 检测器
pose = mp_pose.Pose()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("无法读取摄像头帧")
        break

    # 转换为灰度或其他模型所需的格式
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
    body_detector.setInput(blob)
    detections = body_detector.forward()

    # 遍历所有检测到的人体
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.6:  # 置信度阈值
            box = detections[0, 0, i, 3:7] * [w, h, w, h]
            (x1, y1, x2, y2) = box.astype("int")

            # 裁剪该区域，并传入 Mediapipe Pose 检测姿态
            person_frame = frame[y1:y2, x1:x2]
            person_frame_rgb = cv2.cvtColor(person_frame, cv2.COLOR_BGR2RGB)
            results = pose.process(person_frame_rgb)

            if results.pose_landmarks:
                # 绘制人体姿态关键点到原图
                mp_drawing.draw_landmarks(
                    frame[y1:y2, x1:x2],  # 将结果绘制回原图像的检测区域
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3),
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2)
                )

    # 显示结果
    cv2.imshow("Multi-Person Pose Detection", frame)

    # 按下 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
