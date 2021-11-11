// 문제 이름 : 2019 KAKAO BLIND RECRUITMENT - 실패율(프로그래머스 level 1)
// 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42889

function solution(N, stages) {
  var answer = Array.from({ length: N }, (_, n) => n + 1);
  // 먼저 N을 바탕으로 stages를 조회하면서 실패율을 구하는건 쉽다
  // N * stages 만큼 => 500 * 200,000 = 100,000,000
  // 실패율이란건 특정 스테이지 까지 갔는데 => 성공하지 못한 사람의 비율이다
  // 한번 돌면서 1:에 1이상인수와 1인수를 담고
  // 한번 돌면서 2:에 2 이상인수와 2인수를 담고
  // [0,1,3,2,1,0,1]
  // 20만번 수행 + 500번 * 500 = 250,000 => 훨씬 적긴하다
  const cnt = Array.from({ length: N + 2 }, () => 0);

  for (let stage of stages) {
    cnt[stage]++;
  }

  const arrSum = (arr) => arr.reduce((a, b) => a + b, 0);

  var rates = {};
  for (let i = 1; i <= N; i++) {
    if (cnt[i] === 0) rates[i] = 0;
    rates[i] = cnt[i] / arrSum(cnt.slice(i));
  }

  answer.sort((x, y) => {
    if (rates[x] > rates[y]) return -1;
    else return 1;
  });

  return answer;
}
