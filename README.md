# MLops
Tutorials

# Virtual Enviorment
 - To create virtual enviorment:
   - python3.11 -m venv mlops
 - To activate virtual enviorment
   - Win: source ./mlops/Scripts/activate
   - Mac/Linux : source mlops/bin/activate

# Steps to run:
  - python model.py
  - docker build -t fastapi-gradio-app .
  - docker run -p 8000:8000 -p 7860:7860 fastapi-gradio-app


# Docker commands
  - Build docker image:
    - docker build -t fastapi-gradio-app .
  - Run container
    - docker run -p 8000:8000 -p 7860:7860 fastapi-gradio-app
  - Docker clean up
    - docker ps -a
    - docker stop <container-id>
    - docker rm <container-id>
  - Monitoring
    docker logs <container-id>
# Free port
  - netstat -ano | findstr :8000
  - taskkill /PID <PID> /F



!<table class="tfo-notebook-buttons" align="left">
  <tr><td>Hello World in MLOps </td></tr>
</table>