// 문제 이름 : 프로그래머스 2021 KAKAO BLIND RECRUITMENT 메뉴 리뉴얼(level 2)
// 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/72411

function solution(orders, course) {
  var answer = [];
  const ascSort = (l) => {
    return l.sort((x, y) => {
      if (x > y) return 1;
      else return -1;
    });
  };

  for (let i = 0; i < orders.length; i++) {
    var strList = ascSort(orders[i].split(""));
    orders[i] = strList.join("");
  }
  const cntObj = {};

  var word = "";
  let results = [];

  // 여기 중간에서 글자 탐색 로직을 다시 짜야할 것 같다.
  // 재귀 함수로
  // course에서 글자 길이를 바탕으로 각각의 시행마다 재귀함수를 돌린다
  // ABCFG로 course의 2만큼의 글자를 (알파벳 순) 만들수 있는만큼의 조합을 모두 cntObj[2]에 담는다

  const recursion = (l, cnt) => {
    if (word.length === cnt) {
      if (cntObj[cnt]) {
        if (cntObj[cnt][word]) cntObj[cnt][word]++;
        else cntObj[cnt][word] = 1;
      } else {
        cntObj[cnt] = {};
        cntObj[cnt][word] = 1;
      }
      return;
    }

    for (let i = 0; i < l.length; i++) {
      word += l[i];
      recursion(l.substring(i + 1), cnt);
      word = word.substring(0, word.length - 1);
    }
  };

  for (let num of course) {
    for (let el of orders) {
      word = "";
      recursion(el, num);
    }
  }

  for (let cnt of course) {
    if (cntObj[cnt]) {
      const maxCnt = Math.max(...Object.values(cntObj[cnt]));
      if (maxCnt < 2) continue;
      answer = answer.concat(
        Object.keys(cntObj[cnt]).filter((el) => {
          if (cntObj[cnt][el] === maxCnt) return true;
          else return false;
        })
      );
    }
  }

  answer.sort((x, y) => {
    if (x > y) return 1;
    else return -1;
  });

  return answer;
}

// orders에서 course 개수별로 만들 수 있는 조합을 다은 다음에
// 각각의 영역에서 최빈 단어를 result에 넣기

// 2번 이상 나오고 && course에 그 메뉴 개수 조합이 포함돼있으면 result에 속하는 것
// 먼저, orders 안에 문자열을 알파벳 기준으로 정렬한 문자열로 파싱하고,
// 그 때부터 2중 for문으로 탐색하는데,
// 탐색할 때, 각 원소에 대해 course의 수만큼을 가지고 비교를 해야함
// 예를 들어,
// ["XYZ", "WXY", "AWX"] 이렇게 정렬된 채로 파싱했을 때

// 1) 정렬된 채로 파싱
// 이것을 2중 for문으로 탐색하면서
// "XYZ" => "WXY", "AWX"
// course [2,3,4] 먼저 2를 기준
// "XY" 를 가지고, "WXY" 안에 XY가 있으면 XY는 2개이상이므로 => result에 푸시
// 바로 break 걸어도됨 2개만 있으면 되니까
// 그리고 다음에는 3을 기준 4를 기준 (길이를 넘으면 패스)
// 그리고 다음 WXY로 넘어가서도 똑같이 뒤의 원소에 대해서 이렇게 해주면 됨.

//     for (let cnt of course) {
//         for (let i =0;i<orders.length;i++) {
//             word = orders[i];
//             for (let j =0;j<word.length;j++) {
//                 for (let k =j+1;k<word.length;k++) {
//                     var newWord = word[j] + word.substring(k,k+cnt-1);
//                     if (newWord.length === cnt) {
//                         if (cntObj[cnt]) {
//                             if (cntObj[cnt][newWord]) cntObj[cnt][newWord] ++;
//                             else cntObj[cnt][newWord] = 1;

//                         }
//                         else {
//                             cntObj[cnt] = {};
//                             cntObj[cnt][newWord] = 1;
//                         }
//                         results.push(newWord);
//                     }
//                 }
//             }
//         }
//     }
