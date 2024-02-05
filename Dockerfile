FROM python:3.10.2-slim

RUN apt update && apt install -y --no-install-recommends \
                    default-jre \
                    git \
                    zsh \
                    curl \
                    wget \
                    fonts-powerline \
                    gnupg \
                    wkhtmltopdf \
                    gnupg2 apt-transport-https gpg \
                    && apt clean

RUN wget -q -O- https://packages.microsoft.com/keys/microsoft.asc | \
    gpg --dearmor | tee /usr/share/keyrings/microsoft.gpg > /dev/null 2>&1

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add && echo "deb [signed-by=/usr/share/keyrings/microsoft.gpg arch=amd64,armhf,arm64] https://packages.microsoft.com/ubuntu/18.04/prod bionic main" | tee /etc/apt/sources.list.d/mssql-release.list

RUN apt update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 mssql-tools unixodbc-dev && apt clean

RUN useradd -ms /bin/bash python

RUN pip install pdm

USER python

WORKDIR /home/python/app

ENV MY_PYTHON_PACKAGES=/home/python/app/__pypackages__/3.10
ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH $PATH:${MY_PYTHON_PACKAGES}/bin

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.2/zsh-in-docker.sh)" -- \
    -t https://github.com/romkatv/powerlevel10k \
    -p git \
    -p git-flow \
    -p https://github.com/zdharma-continuum/fast-syntax-highlighting \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions \
    -a 'export TERM=xterm-256color' \
    -a 'export GPG_TTY=$(tty)'

RUN echo '[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh' >> ~/.zshrc && \
    echo 'HISTFILE=/home/python/zsh/.zsh_history' >> ~/.zshrc && \
    echo 'eval "$(pdm --pep582)"' >> ~/.zshrc && \
    echo 'eval "$(pdm --pep582)"' >> ~/.bashrc


CMD [ "tail", "-f", "/dev/null" ]