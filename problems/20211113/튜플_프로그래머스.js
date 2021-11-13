// 문제 이름 : 프로그래머스 - 튜플(level2 kakao 겨울 인턴쉽 기출 문제)
// 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/64065

function solution(s) {
  var answer = [];
  // 일단 순서별로 정렬할 수 있나?
  // 양 끝에 {}을 없애고
  var lists = [];
  let els = s.slice(1, s.length - 1).split("},");
  for (let i = 0; i < els.length; i++) {
    if (els[i][0] === "{") {
      els[i] = els[i].substring(1);
    }
    if (els[i][els[i].length - 1] === "}") {
      els[i] = els[i].substring(0, els[i].length - 1);
    }
    lists.push(els[i].split(","));
  }

  lists.sort((x, y) => {
    if (x.length > y.length) return 1;
    else return -1;
  });

  for (let i = 0; i < lists.length; i++) {
    var arr = lists[i].map((el) => parseInt(el));
    answer = answer.concat(arr.filter((el) => !answer.includes(el)));
  }

  return answer;
}
