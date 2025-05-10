import inference
import utils

# Initialize DetectNet model
net = inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

# Use virtual RTSP camera from the emulator
input_URI = "rtsp://jetson_emulator:554/detectNet/road_cam/4k"
input = utils.videoSource(input_URI, argv="")
output = utils.videoOutput("display://1", argv="")

# Capture frame and run detection
img = input.Capture()
detections = net.Detect(img, "box")

# Display results
output.SetStatus(f"Test | Network {net.GetNetworkFPS():.0f} FPS")
output.Render(img)

print(f"✅ Emulator test: detected {len(detections)} object(s)")
for d in detections:
    print(f" - {net.GetClassDesc(d.ClassID)} (Confidence: {d.Confidence:.2f})")