// 문제 이름 : 행렬 테두리 회전하기 (프로그래머스 winter dev 2021 기출문제 level 2)
// 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/77485

function solution(rows, columns, queries) {
  var answer = [];
  // 단순하게 회전 구현 + 회전 시행마다 최소값을 배열에 담아서 리턴해주는 문제라고 생각가능
  // 시간복잡도도 걸리지 않을듯
  // queries를 순회하면서 인덱스를 받아서 해당 인덱스 범위에 있는 것을 회전시켜야함(테두리만
  // 2,2 => 2,3 // 2,3 => 2,4 // 2,4 => 3,4
  // 가로가 3, 세로가 4인 직사각형
  // 3,4 => 4,4 // 4,4 => 5,4
  // 2,2 => 2,3 => 2,4 => 3,4 => 4,4 => 5,4 => 5,3 => ....3,2
  // 여기에 있는 수들을 배열에 하나하나 담고,
  // 그 배열을 한칸씩 오른쪽으로 밀어냄 (맨끝 요소를 맨앞으로)
  // 그리고 그 배열을 다시 위의 좌표를 조회하면서 갱신
  // board 만들기
  var num = 1;
  let board = [];
  for (let i = 0; i < rows; i++) {
    board.push([]);
    for (let j = 0; j < columns; j++) {
      board[i].push(num);
      num++;
    }
  }
  // queries가 최대 10,000개
  // 한번의 회전 로직에 있어서 최악의 경우 98 + 98 + 100 + 100 = 400정도(반올림해서)
  // 10,000 * (400 + 400) = 10,000 * 800 = 8,000,000 8백만 정도 Ok

  for (let q of queries) {
    // 4개의 꼭지점을 구하고 for문 으로 탐색
    // 인덱스 -1 해주면서 계산해야함
    const first = [q[0] - 1, q[1] - 1]; // 시작점
    const second = [q[0] - 1, q[3] - 1]; // 두번째 꼭지점
    const third = [q[2] - 1, q[1] - 1];
    const fourth = [q[2] - 1, q[3] - 1];

    var prev = board[first[0]][first[1]];
    var min_num = prev;

    for (let i = first[1] + 1; i <= second[1]; i++) {
      var origin = board[first[0]][i];
      if (origin < min_num) min_num = origin;
      board[first[0]][i] = prev;
      prev = origin;
    }

    for (let i = second[0] + 1; i <= fourth[0]; i++) {
      var origin = board[i][second[1]];
      if (origin < min_num) min_num = origin;
      board[i][second[1]] = prev;
      prev = origin;
    }

    for (let i = fourth[1] - 1; i >= third[1]; i--) {
      var origin = board[third[0]][i];
      if (origin < min_num) min_num = origin;
      board[third[0]][i] = prev;
      prev = origin;
    }

    for (let i = third[0] - 1; i >= first[0]; i--) {
      var origin = board[i][third[1]];
      if (origin < min_num) min_num = origin;
      board[i][third[1]] = prev;
      prev = origin;
    }

    answer.push(min_num);
  }

  return answer;
}
