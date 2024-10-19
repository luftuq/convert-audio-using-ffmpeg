# Use the Micromamba base image
FROM mambaorg/micromamba:latest

# Install Python and ffmpeg via Micromamba
COPY --chown=$MAMBA_USER:$MAMBA_USER .devcontainer/environment.yaml /tmp/environment.yaml
RUN micromamba install -y -n base -f /tmp/environment.yaml && \
    micromamba clean --all --yes

# Install Git
USER root
RUN apt-get update && apt-get install -y git \
    && git config --system pull.ff only
USER $MAMBA_USER
