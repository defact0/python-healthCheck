작업개요
----

> 운영중인 서비스에 대한 상태 체크를 하기 위하여 만들었다.  
> 상태 체크는 Port 상태를 확인한다.  
> 만일 Port 연결을 할 수 없으면 결과를 리포트하여 메일을 전달한다.


프로그램 설명
---

 - 서비스 상태 체크 (port 오픈 여부)
 - 서비스 상태가 이상 있을 경우 이메일 전송



프로그램 동작 환경
----

 - Python 3.8.7
 - markdownmail 모듈 추가필요
    ```shell
    pip install markdownmail
    ```
- config.json  
  
  - 메일 전송 및 체크 서비스 정의파일 필요


프로그램 활용법
----

> CentOS 7 환경 기준으로 설명

1. 프로그램 설치위치 `/data/healthCheck`

   ```shell
   mkdir -p /data/healthCheck
   ```

2. 환경설정파일 수정 `config.json`

   ```shell
   vi /data/healthCheck/config.json
   ```

   - config = 보내는 사람의 Gmail 계정과 앱 비밀번호 필요
   - address = 받는 사람의 메일 리스트 작성 필요(Gmail 주소 권장)
   - service = 체크할 서비스의 이름, 아이피, 포트 를 입력

3. `crontab` 유틸에 `healthCheck` 프로그램 등록

   - crontab 에 등록하기

     ```shell
     crontab -e
     ```

   - 30분 마다 프로그램 실행

     ```shell
     */30 * * * * /data/healthCheck/healthCheck.py
     ```

   - crontab 리스트 확인하기

     ```shell
     crontab -l
     ```

4. 프로그램 로그 확인하기

   ```shell
   vi /data/healthCheck/healthCheck.log
   ```

   