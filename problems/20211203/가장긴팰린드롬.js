// 문제 이름 : 프로그래머스 - 가장 긴 팰린드롬(연습문제)
// 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/12904?language=javascript

function test1(string) {
  // 팰린드롬을 판별하는 함수
  // 양옆에서 한칸씩 옮기면서 같은지 판별하면서 한번이라도 틀리면 바로 false를 리턴
  const is_palindrome = (s) => {
    var chk = true;
    for (var i = 1; i < s.length; i++) {
      if (s[i] != s[s.length - 1 - i]) {
        chk = false;
        break;
      }
    }
    return chk;
  };

  var len = string.length;
  var answer = "";
  for (var i = 0; i < len; i++) {
    for (var t = 0; t <= i; t++) {
      var word = string.slice(t, len - i + t);
      if (string[t] === string[len - i + t - 1] && is_palindrome(word)) {
        if (word.length > answer.length) answer = word;
        // 여기서 break를 하는 이유는 가장 긴 팰린드롬을 찾는 것이기에
        // 굳이 이것보다 짧은 팰린드롬을 탐색해볼 필요가 없음.
        break;
      }
    }
  }

  return answer;
}

// 문제 이해
// : 가장 긴 팰린드롬을 찾고 그 문자열을 리턴하는 것이 문제

// 문제 풀이
// : 완전 탐색으로 풀어보면 일단 팰린드롬을 판별하는 방법 자체는 쉽다 => 양옆을(0,마지막 인덱스) 기준으로
// 한칸씩 +, - 하면서 비교하다가 한번이라도 불일치하면 팰린드롬이 아니고, 끝까지 가면 팰린드롬이다.
// 1) 위의 로직으로 팰린드롬을 판별하는 함수를 만든다.
// 다음은 완전탐색할 문제의 유효범위를 탐색하는 방법이 필요하다.
// string의 요소를 for문으로 탐색하면서
// 2depth에서 그 요소를 기준으로 앞의 수를 인덱스 0부터 한칸씩 +하면서 모든 범위를 탐색해봐야한다
// 즉, "My dad is a racecar athlete" 이것을 예로 들면
// 현재 dad is a 에서 끝에 a를 탐색중일 때
// "My dad is "를 가지고
// My dad is a 에 대해서 팰린드롬 체크
// y dad is a 에 대해서 팰린드롬 체ㅡ
// " dad is a" ... 이런식으로 탐색해야 가능한 모든 범위를 탐색하는 것이다.
