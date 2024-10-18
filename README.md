# Wistia Parser

위스티아 폴더 URL로부터 각 영상의 URL을 파싱하여 제목과 함께 출력하는 Python 스크립트입니다.

## 의존성 설치

### Pip

```
pip install -r requirements.txt
```

### Poetry

```
poetry install
```

## 사용법

```shell
python main.py <위스티아 폴더 URL>
```

- 위스티아 폴더 URL은 `https://example.wistia.com/folders/abcdef1234` 형식으로 되어 있습니다.
- 사용 예시
  ```shell
  python main.py https://example.wistia.com/folders/abcdef1234
  ```
