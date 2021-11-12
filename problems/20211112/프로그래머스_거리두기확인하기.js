// 문제 이름 : 프로그래머스 - 거리두기 확인하기(카카오 겨울 채용연계형 인턴쉽 기출 2021 - level 2)
// 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/81302

function solution(places) {
  var answer = [];

  for (let j = 0; j < places.length; j++) {
    var l = places[j];
    for (let i = 0; i < l.length; i++) {
      l[i] += "##";
      l[i] = "##" + l[i];
    }
    places[j].push("#########");
    places[j].push("#########");
    places[j].unshift("#########");
    places[j].unshift("#########");
  }

  const direc = [
    [
      [-1, 0],
      [0, -1],
    ],
    [
      [-1, 0],
      [0, 1],
    ],
    [
      [1, 0],
      [0, 1],
    ],
    [
      [1, 0],
      [0, -1],
    ],
  ];

  for (let el of places) {
    var board = el;
    var flag = false;
    for (let i = 2; i <= 6; i++) {
      for (let j = 2; j <= 6; j++) {
        if (board[i][j] !== "P") continue;
        else {
          // case1
          for (let way of [
            [i + 1, j],
            [i, j + 1],
            [i - 1, j],
            [i, j - 1],
          ]) {
            if (board[way[0]][way[1]] === "#") continue;
            if (board[way[0]][way[1]] === "P") {
              flag = true;
              break;
            }
          }
          if (flag) break;
          // case 2
          var idx = -1;
          for (let way of [
            [i + 2, j],
            [i, j + 2],
            [i - 2, j],
            [i, j - 2],
          ]) {
            idx++;
            if (board[way[0]][way[1]] === "#") continue;
            if (board[way[0]][way[1]] === "P") {
              if (idx === 0) {
                // 아래
                if (board[way[0] - 1][way[1]] === "O") {
                  flag = true;
                  break;
                }
              } else if (idx === 1) {
                // 오른쪽
                if (board[way[0]][way[1] - 1] === "O") {
                  flag = true;
                  break;
                }
              } else if (idx === 2) {
                // 위쪽
                if (board[way[0] + 1][way[1]] === "O") {
                  flag = true;
                  break;
                }
              } else if (idx === 3) {
                // 왼쪽
                if (board[way[0]][way[1] + 1] === "O") {
                  flag = true;
                  break;
                }
              }
            }
          }
          if (flag) break;
          // case 3
          idx = -1;

          for (let way of [
            [i + 1, j + 1],
            [i + 1, j - 1],
            [i - 1, j - 1],
            [i - 1, j + 1],
          ]) {
            idx++;
            if (board[way[0]][way[1]] === "#") continue;
            if (board[way[0]][way[1]] === "P") {
              for (let dir of direc[idx]) {
                if (board[way[0] + dir[0]][way[1] + dir[1]] === "O") {
                  flag = true;
                  break;
                }
              }
              if (flag) break;
            }
          }
          if (flag) break;
        }
      }
    }
    if (flag) answer.push(0);
    else answer.push(1);
  }

  return answer;
}

// 일단 포인트는 P를 찾는 것임.
// P를 찾아서 그 P주변을 탐색=> 맨해튼 거리 2 이내에 또다른 P가 있을 경우(아마도 BFS)
// 없을 경우 => pass
// 있을 경우 => 그 P와 처음 찾은 P 사이에 X가 있는지, O가 있는지 봐야함(혹은 아무것도 없는 바로 붙은)
// 그래서 X가 제대로 있으면 => pass,
// 1) O를 사이에 두고 있다던지, P O P이렇게
// 2) P O
// X P 등 이런식으로 중간에 O이 있다던지 하면 이건 바로 규칙 위반이니까 0 break
// 3) 혹은 아무것도 없는 바로 붙은 경우
// 먼저 3번 케이스는 BFS로 거리 0인 경우임 즉, 첫시행 탐색에서 위, 오른쪽, 아래, 왼쪽에 P가 있으면
// 바로 위반임 => break
// 1번 케이스는 2번째 시행에서 각각의 위, 아래, 왼쪽, 오른쪽 끄트머리에 P가 있는 경우인데,
// 이 경우에는 첫번째 시행에서 그 사이에 O가 있었으면 break임
// 2번 케이스는 두개를 체크해야함. 체크했을 때 한쪽이라도 O면 break

// 위오른쪽아래왼쪽 체크후에 P 면 바로 break -1
// 만약에 1을 통과했으면, 각각 맨끝 요소가(위아래오른쪽왼쪽) P인지 체크후 만약에
// P인 곳이 있으면 그 바로 전요소가 X인지 체크=> 만약 X가 아니고 O 면 break -2
// 찾은 P에서 대각선 오른쪽왼쪽위아래 를 체크해서 P인지 체크 => P면 각각 그 근처에 X가 둘다 있는지체크
// 하나라도 O면 break - 3
// 1,2,3 다 통과하면 pass임

// 경계처리 #으로해서 #이면 아예 고려 x
