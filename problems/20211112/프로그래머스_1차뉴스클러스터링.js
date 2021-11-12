// 문제 이름 : 프로그래머스 1차 뉴스 클러스터링(level 2 카카오 2018 블라인드 공채 기출)
// 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/17677

function solution(str1, str2) {
  var answer = 0;
  const parseToString = (str) => {
    var myRegex = /[a-zA-Z]/gi;
    var result = str.match(myRegex);
    if (result) return result.join("").toLowerCase();
    else return "";
  };

  var l1 = [];
  var l2 = [];

  for (let i = 0; i < str1.length; i++) {
    var str = parseToString(str1.substring(i, i + 2));
    if (str.length === 2) l1.push(str);
  }

  for (let i = 0; i < str2.length; i++) {
    var str = parseToString(str2.substring(i, i + 2));
    if (str.length === 2) l2.push(str);
  }

  let same = new Set(l1.filter((x) => l2.includes(x)));

  const count = (l, val) => {
    return l.filter((el) => el === val).length;
  };

  // 여기서 이 same을 가지고, 각각의 l1, l2를 탐색한다 => 그래서 숫자가 작은쪽의 카운트를 교집합 수에 더해줌
  // 둘다 1이면 1만추가하면됨
  var sameCount = 0;
  var sumCount = 0;

  for (let el of same) {
    var l1Count = count(l1, el);
    var l2Count = count(l2, el);
    if (l1Count > l2Count) {
      sameCount += l2Count;
      sumCount += l1Count;
    } else {
      sameCount += l1Count;
      sumCount += l2Count;
    }
  }

  sumCount += l1
    .filter((el) => !same.has(el))
    .concat(l2.filter((el) => !same.has(el))).length;

  if (sumCount === 0 && sameCount === 0) answer = 65536;
  else answer = Math.floor((sameCount / sumCount) * 65536);

  return answer;
}

// 처음에 str1, str2를 가지고 +,-,숫자, 공백 이런거 다 없애고 순수 알파벳만 골라내는 작업
// 2글자씩 끊어서 다중 집합의 원소로 만들기
// 둘이 겹치는게 없으면 정답은 0 / 두 다중 집합의 개수의 합  = 0
// 둘다 0이면 = 1
// 둘이 겹치는게 있으면 정답은 겹치는 부분의 개수 / 두 다중 집합의 개수의 합
// 둘이 겹치는게 있으면 => 그 겹치는 부분이 적은쪽의 개수를 선택해서 겹치는 부분의 개수에 추가해주고
// 겹치는 부분이 많은쪽의 개수는 합집합의 개수에 추가한다.
