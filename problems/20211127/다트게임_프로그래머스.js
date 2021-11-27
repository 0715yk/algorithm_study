// 문제 이름 : 2018 카카오 블라인드 공채 (레벨 1) - 다트 게임
// 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/17682

function solution(dartResult) {
    var answer = 0;
    // 스택을 활용하는 방향으로 풀어야할듯?
    // 0-10 사이니까 dartResult를 하나하나 쪼개도 될듯 
    // >>> 여기서 오답 !! 0-10 사이라는 말이 0, 10 을 포함한다는 말이었다 <<<
    // 10을 어떻게 처리할 수 있을까
    const list = dartResult.split('');
    // 맨 앞에서부터 하나씩 pop하면서 계산
    // S 가 나오면 pass
    // D 가 나오면 앞의 수에 2승
    // T 가 나오면 앞의 수에 3승
    // 상만 없으면 매우 간단하게 여기서 나온 수들을 더하면 끝남

    const stack = [];
    const obj = {
        "S" : 1,
        "D" : 2,
        "T" : 3,
    }
    
    for (let el of list) {
        if(!obj[el]) {
            if(el === "*") {
                stack[stack.length-1] = stack[stack.length-1] * 2;
                if (stack[stack.length-2]) stack[stack.length-2] = stack[stack.length-2] * 2;
            } else if(el === "#") {
                stack[stack.length-1] = stack[stack.length-1] * -1;
            } else {
                if(el === "0" && stack[stack.length-1] === 1) {
                    stack.pop();
                    stack.push(parseInt(10));
                } else stack.push(parseInt(el));
            }
        } else {
            stack[stack.length-1] = stack[stack.length-1] ** obj[el];
        }
    }
    answer = stack.reduce((x,y) => x+y);
    
    return answer;
}