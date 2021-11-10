// 문제 이름 : 가장 먼 노드(프로그래머스 그래프 유형 level 3)
// 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/49189?language=javascript

function solution(n, edge) {
  var answer = 0;
  // 1번 노드를 기준으로함
  // 가장 멀리 떨어진 노드까지의 거리를 구하는 문제가 아닌
  // 가장 멀리 떨어진 노드까지의 거리를 갖는 노드가 몇개인지를 구하는 문제
  // vertex는 양방향을 표현하지 않고, 간선 하나만을 표현하고 있음(내가 직접 양방향 형태로 만들어줘야할듯)
  // 이건 BFS로 해야하듯
  // 먼저, vertex를 바탕으로 객체를 만들어보면
  const obj = {};
  for (let el of edge) {
    if (obj[el[0]]) {
      obj[el[0]].push(el[1]);
    } else obj[el[0]] = [el[1]];
    if (obj[el[1]]) {
      obj[el[1]].push(el[0]);
    } else obj[el[1]] = [el[0]];
  }

  // 시작점은 1번노드에서부터임
  // BFS
  const queue = [1];
  const path = {};
  var top = undefined;
  const len = Array.from({ length: n }, () => 0);
  let max_len = 0;
  len[0] = 0;
  path[1] = true;

  while (queue.length !== 0) {
    top = queue.shift();
    for (let el of obj[top]) {
      if (path[el]) continue;
      len[el - 1] = len[top - 1] + 1;
      if (max_len < len[el - 1]) {
        max_len = len[el - 1];
      }
      path[el] = true;
      queue.push(el);
    }
  }

  for (let el of len) {
    if (el === max_len) answer++;
  }

  return answer;
}
