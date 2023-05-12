import subprocess

def run_detection(source_url):
    subprocess.run(['python', 'detect.py', '--source', source_url])
    output, error = process.communicate()
    return output, error
