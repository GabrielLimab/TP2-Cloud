import subprocess

def make_request():
    url = "http://localhost:52022/api/recommend"
    headers = "'Content-Type: application/json'"
    data = '{"songs": ["One Dance", "Congratulations"]}'
    
    command = [
        "wget",
        "--server-response",
        "--output-document", "response.out",
        "--header", headers,
        "--post-data", data,
        url
    ]
    
    try:
        subprocess.run(command, check=True)
        print("Request completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

make_request()
