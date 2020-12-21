apt-get update -y && apt-get install -y graphviz \
libsm6 libxext6 libxrender-dev xdg-utils build-essential

pip install --upgrade pip

pip install   --no-cache-dir   -r requirements.txt