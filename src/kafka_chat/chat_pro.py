#!/usr/bin/env python3
"""
Interactive Kafka Producer CLI: chatpro
"""
import sys
import json
from kafka import KafkaProducer
import time

def main():
    print("chatpro 시작합니다.")
    print("Kafka Producer CLI")
    # 입력받기
    bootstrap = input("Bootstrap 서버를 입력하세요(예시: 127.0.0.1:9092): ").strip()
    if not bootstrap:
        print("Error: Bootstrap servers required.")
        sys.exit(1)
    topic = input("Topic을 입력하세요: ").strip()
    if not topic:
        print("Error: Topic name required.")
        sys.exit(1)

    # 프로듀서 생성 (UTF-8 문자열 직렬화)
    producer = KafkaProducer(
        bootstrap_servers=bootstrap,
        value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode('utf-8')
    )

    print(f"Connected to {bootstrap}, publishing to topic '{topic}'")
    print("메시지를 입력하세요. 종료하려면 exit를 입력하세요.")
    print("메시지 전송 중...")

    # 메시지 입력 루프
    try:
        while True:
            msg = input("▶ ").strip()
            if msg.lower() == 'exit':
                break
            if msg:
                producer.send(topic, msg)
                producer.flush()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")

    # 플러시 및 종료
    try:
        producer.flush()
        producer.close()
    except Exception:
        pass

    print("✅ chatpro 종료합니다. ")

if __name__ == '__main__':
    main()
