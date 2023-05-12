import subprocess

def run_detection(source_url):
    cmd = f"python ./yolov5/detect.py --source {source_url} --weights ./best.pt"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output, error
