# kafka-chat

### 📤 Kafka Producer CLI: chatpro

---

## 설치 방법

### 1. 프로젝트 클론

```bash
git clonegit@github.com:wminhyuk/kafka-chatpro.git
```

### 2. 의존성 설치

```bash
pdm install
```

---

## 🚀 사용 방법

```bash
chatpro
```

### 실행 흐름:

1. Bootstrap 서버를 입력 (예시: `localhost:9092`)
2. Topic을 입력 (예시: `seochat`)
3. 메시지 입력 (`exit` 입력 시 종료)
4. 메시지는 JSON 형식으로 Kafka에 전송됨

---

## 💬 예시

```bash
chatpro 시작합니다.
Kafka Producer CLI
Bootstrap 서버를 입력하세요(예시: 127.0.0.1:9092): <aws IP>:9092
Topic을 입력하세요: seochat
Connected to 13.125.197.73:9092, publishing to topic 'seochat'
메시지를 입력하세요. 종료하려면 exit를 입력하세요.
메시지 전송 중...
▶ test
▶ 테스트
▶ 잘되네
▶ exit
✅ chatpro 종료합니다.
```

---

## 📁 디렉토리 구조

```text
.
├── pyproject.toml
├── README.md
└── src
    └── kafka_chat
        ├── __init__.py
        └── chat_pro.py
```



