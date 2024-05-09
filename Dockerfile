# Gunakan image Python versi 3.9
FROM python:3.9

# Set working directory di dalam container
WORKDIR /app

# Copy file requirements.txt ke dalam container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy seluruh isi proyek ke dalam container
COPY . .

# Command yang akan dijalankan ketika container dijalankan
CMD ["python", "etl_script.py"]