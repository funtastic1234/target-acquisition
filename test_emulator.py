import target_acquisition.inference as inference
import target_acquisition.utils as utils

net = inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
input_URI = "rtsp://jetson_emulator:554/detectNet/road_cam/4k"
input  = utils.videoSource(input_URI, argv="")
output = utils.videoOutput("display://1", argv="")

img = input.Capture()
detections = net.Detect(img, "box")
output.SetStatus(f"Test | Network {net.GetNetworkFPS():.0f} FPS")
output.Render(img)

print(f"✅ Emulator test: detected {len(detections)} object(s)")