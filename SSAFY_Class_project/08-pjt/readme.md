

## 프로젝트명

> 비동기 통신을 이용한 웹 사이트 구현

## 시행 날짜 

> 2023.11.03(금)

## 팀원

> 최성호, 김지용

## 개발도구 및 라이브러리

> VSCode, Django 4.2.6, djangorestframework, Chrome Browser

## 개발 목표 

> <li> 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web Application 제작 • AJAX 통신과 JSON 구조에 대한 이해
> <li> Many to one relationship(N:1)에 대한 이해
> <li> Many to many relationship(N:M)에 대한 이해
> <li> accounts, community, movies  각각의 앱에 비동기 통신이 필요한 부분을 axios를 이용해 구현


## 목차

> 1. 
> 2. 
> 3. 
> 4. 
> 5. 


## 프로젝트 설명


## ERD
![Alt text](image.png)


## 느낀점

> serializer로 json형식의 데이터들을 변환하면 id형식으로 반환되기 때문에 
serializer.py에서 오버라이딩을 통해 부모 클래스의 동작을 수정해 줘야한다.

> serialize에 대한 이해도는 있었지만 프로젝트를 통한 실습은 serialize이용하여 
json형태로 변환하는 방법에 있어서 더욱 확실하게 알게되었다.