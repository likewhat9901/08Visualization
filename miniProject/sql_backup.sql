/* 공공배달앱 배달특급 가맹점 */
create table delivery_apps(
	idx number primary key,
	sigun varchar2(20) not null,
	faclt varchar2(100) not null,
	addr varchar2(200) not null,
	latitude number(20,10) not null,
	longitude number(20,10) not null
);
desc delivery_apps;

create sequence seq_delivery_apps
    /* 증가치, 시작값, 최소값을 모두 1로 지정 */
    increment by 1
    start with 1
    minvalue 1
    /* 최대값, 사이클, 캐시메모리 사용을 모두 No로 지정 */
    nomaxvalue
    nocycle
    nocache;
