FROM python:3.8.3
RUN pip install pandas
RUN pip install numpy
RUN pip install sklearn
RUN pip install statsmodels==0.11.1
RUN pip install pmdarima
RUN useradd --create-home --shell /bin/bash app_user
WORKDIR /home/app_user
USER app_user
COPY . ./
CMD ["predict_drivers.py"]
ENTRYPOINT ["python"]