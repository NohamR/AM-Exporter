FROM python:3.10-alpine

WORKDIR /t

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3005

RUN pip install gunicorn

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:3005", "--chdir", "/t", "app:app"]