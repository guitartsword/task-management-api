FROM python:3.12-slim-bookworm  as base

RUN pip install poetry

RUN mkdir /app
WORKDIR /app

COPY ./pyproject.toml .
COPY ./poetry.lock .
RUN poetry export --output='requirements.txt'


FROM python:3.12-slim-bookworm as final
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY --from=base /app/requirements.txt .
RUN pip install -r requirements.txt

COPY ./app .

# Using non-root user
RUN useradd -ms /bin/bash user
RUN chown -R user:user /app
USER user

# Pretty Bash :)
RUN echo 'export PS1="\[$(tput bold)\]\[\033[38;5;190m\]\u\[$(tput sgr0)\]@docker:\[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;39m\]\W\[$(tput sgr0)\]\\$\[$(tput sgr0)\] "' >> /home/user/.bashrc

CMD ["fastapi", "run", "main.py"]
