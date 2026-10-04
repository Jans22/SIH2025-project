import os
import sys
import time
import json
import subprocess
from pathlib import Path
from datetime import datetime

import cv2
import numpy as np

# RPi.GPIO for servo
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# ---------------- Config ----------------
USER_HOME = Path("/home/sih")
SIH_DIR = USER_HOME / "SIH"
IMG_DIR = SIH_DIR / "images"
LOG_FILE = SIH_DIR / "sih_scan_final.log"

SERVO_GPIO = 13
SERVO_FREQ = 50
SERVO_SETTLE_SEC = 1.0

# ---------------- Logging ----------------
def log(msg):
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{t}] {msg}"
    print(line)
    try:
        SIH_DIR.mkdir(parents=True, exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(line + "\n")
    except Exception:
        pass

# ---------------- Dirs ----------------
def ensure_dirs():
    SIH_DIR.mkdir(parents=True, exist_ok=True)
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    log("Ensured dirs")

# ---------------- Camera ----------------
CAM_CMD_CANDIDATES = ["libcamera-still", "rpicam-still", "raspistill"]

def find_camera_cmd():
    for c in CAM_CMD_CANDIDATES:
        if subprocess.run(["which", c], stdout=subprocess.PIPE).returncode == 0:
            return c
    return None

def take_photo(dest_path: Path, timeout=15):
    camexe = find_camera_cmd()
    if not camexe:
        log("No camera binary found.")
        return False
    cmd = [camexe, "-n", "-o", str(dest_path), "-t", "2000"]
    log(f"Capturing: {' '.join(cmd)}")
    try:
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
        if p.returncode != 0:
            log("Camera error: " + p.stderr.decode().strip())
        time.sleep(0.1)
        return dest_path.exists()
    except Exception as e:
        log("Capture exception: " + str(e))
        return False

# ---------------- Servo PWM ----------------
class ServoPWM:
    def __init__(self, gpio_pin, freq=50):
        self.gpio = gpio_pin
        self.freq = freq
        GPIO.setup(self.gpio, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio, self.freq)
        self.pwm.start(0)
        log(f"Servo PWM initialized on GPIO {self.gpio}")

    def angle_to_duty(self, angle):
        return 2.5 + (angle / 180.0) * 10.0

    def move(self, angle):
        duty = self.angle_to_duty(angle)
        self.pwm.ChangeDutyCycle(duty)
        log(f"Servo moving to {angle} (duty {duty:.2f}%)")
        time.sleep(SERVO_SETTLE_SEC)
        self.pwm.ChangeDutyCycle(0)

    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup(self.gpio)

# ---------------- Pump Controller (simulated) ----------------
class PumpController:
    def spray(self, seconds):
        log(f"[SIMULATED] Pump spraying for {seconds:.2f}s")
        time.sleep(min(seconds, 0.5))
        log("[SIMULATED] Pump off")
        return {"sprayed": True, "simulated": True, "duration": seconds}

# ---------------- Dummy Blue-index ----------------
def blue_index_process(img_path, mask_path=None, overlay_path=None):
    img = cv2.imread(str(img_path))
    if img is None:
        raise ValueError("Image not found")
    stress_percent = np.random.uniform(0, 20)
    return stress_percent, img, img

# ---------------- Main ----------------
def main():
    ensure_dirs()
    log("=== Starting SIH scan cycle ===")

    pump = PumpController()  # no arguments
    servo = ServoPWM(SERVO_GPIO)

    positions = [("left", 0), ("center", 90), ("right", 180)]
    results = {}

    for name, angle in positions:
        log(f"--- Move -> {name} ---")
        servo.move(angle)

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        local_orig = IMG_DIR / f"{name}_{ts}.jpg"

        if not take_photo(local_orig):
            log("Capture failed")
            results[name] = {"status": "capture_failed"}
            continue
        log(f"Captured {local_orig.name}")

        try:
            stress_percent, mask, overlay = blue_index_process(local_orig)
            log(f"Processed: stress={stress_percent:.2f}%")
        except Exception as e:
            log(f"Processing error: {e}")
            results[name] = {"status": "processing_failed"}
            continue

        results[name] = {"status": "ok", "stress_percent": stress_percent}

    servo.cleanup()
    log("=== SCAN CYCLE COMPLETE ===")
    print(json.dumps(results))
    return results

if __name__ == "__main__":
    main()
