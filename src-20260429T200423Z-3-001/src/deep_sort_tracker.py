from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def track_players(video):

    results = model.track(video, persist=True)

    # returns tracked players with IDs
    return len(results)