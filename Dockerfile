FROM python:3.6

ARG project_dir=/app/

ADD ./.config/requirements.txt $project_dir
COPY ./src $project_dir/src

WORKDIR $project_dir

RUN pip install -r requirements.txt

CMD ["python", "src/app.py"]
