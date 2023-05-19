# API

## API란?
![](https://postfiles.pstatic.net/MjAyMTA2MTdfNTEg/MDAxNjIzODk4Mzk4MTQ3._6IQrd6Q_JSSrMNzJ-SBE7vTwX4wRhBmlfPI8ppcx_Yg.2kn2MB2Rmmm6CqLoZ0q96PzjWgmqsyuuq7fwS80GYvEg.PNG.ghdalswl77/%EB%A9%94%E3%85%91.png?type=w773)

* 프로그램들이 서로 상호작용하는 것을 도와주는 매개체
### API의 4가지 방식
 - SOAP API : 단순 객체 접근 프로토콜, 클라이언트와 서버는 XML을 사용하여 메시지를 교환
 - RPC API : 원격 프로시저 호출, 클라이언트가 서버에서 함수나 프로시저를 완료하면 서버가 출력을 클라이언트로 다시 전송한다.
 - Websocket API : JSON 객체를 사용하여 데이터를 전달, 클라이언트와 서버 간의 양방향 통신을 지원, 서버가 연결된 클라이언트에 콜백 메시지를 전송할 수 있어 REST API보다 효율적
 - REST API : 가장 많이 사용, 클라이언트가 서버에 요청을 데이터로 전송, 서버가 이 클라이언트 입력을 사용하여 내부 함수를 시작하고 출력 데이터를 다시 클라이언트에 반환
### REST API의 4가지 이점
- 통합 : 새로운 애플리케이션을 기존 소프트웨어 시스템과 통합하는데 사용, 각 기능을 처음부터 작성할 필요가 없기 때문에 개발 속도 증가, 기존 코드 활용 가능
- 혁신 : 전체 코드를 다시 작성할 필요 없이 API 수준에서 변경하여 사용 가능
- 확장 : 요구 사항을 충족할 수 있는 고유한 기회를 제공, 내부 데이터베이스에 유시한 액세스 권한을 부여 가능
- 유지 관리의 용이성 : 한 시스템의 향후 코드 변경이 다른 시스템에 영향을 미치지 않는다.
---
## 엔드포인트
![](https://blogfiles.pstatic.net/MjAyMTA2MTdfMjAy/MDAxNjIzODk4ODYyNTg3.XOuG3T6VKIDbgmnvcdHhArnhPLprsWFKn-KwxGi0AvUg.8qSDRytl2qg-YnYmBCGiPtXFi7Y2myY7A4bP2YCILbgg.PNG.ghdalswl77/image.png)
 - 서비스를 사용 가능하도록 하는 서비스에서 제공하는 커뮤니케이션 채널의 한쪽 끝
 - 요청을 받아 응답을 제공하는 서비스를 사용할 수 있는 지점을 의미

---
#### Reference
* [API란 무엇인가요?](https://aws.amazon.com/ko/what-is/api/)