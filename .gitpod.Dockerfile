# .gitpod.Dockerfile
FROM gitpod/workspace-full

# Install additional packages for native UI development
RUN sudo apt-get update && \
    sudo apt-get install -y \
    libgtk-3-dev \
    build-essential \
    cmake \
    xvfb
