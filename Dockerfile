# For more information, please refer to https://aka.ms/vscode-docker-python
FROM tiangolo/uwsgi-nginx:python3.8

LABEL Name=code6 Version=0.0.1
EXPOSE 8000

ENV LISTEN_PORT=8000
ENV USWGI_INI uswgi.ini

WORKDIR /app
ADD . /app

RUN chmod g+w /app
RUN chmod g+w /app/app.sql
# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
# RUN useradd appuser && chown -R appuser /app
# USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "aspilos.wsgi"]
