# 1. Python 기반 이미지 사용 (최신 버전 추천)
FROM python:3.11

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 프로젝트 코드 복사
COPY . .

# 5. Django 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
