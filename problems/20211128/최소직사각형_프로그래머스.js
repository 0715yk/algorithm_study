// 문제 이름 : 최소직사각형(프로그래머스 레벨1)
// 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/86491

function solution(sizes) {
  var answer = 0;
  // 50 60
  // 30 70
  // 30 60
  // 40 80
  // 이렇게 작은쪽 큰쪽을 나눠서
  // 작은쪽에서 최대값, 큰쪽의 최대값을 곱해서 구하면 끝
  const smallPart = [];
  const bigPart = [];

  for (let size of sizes) {
    bigPart.push(Math.max(...size));
    smallPart.push(Math.min(...size));
  }

  answer = Math.max(...bigPart) * Math.max(...smallPart);

  return answer;
}
