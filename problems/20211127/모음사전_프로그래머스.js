// 문제 이름 : 모음사전(레벨2 - 위클리 챌린지)
// 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/84512

function solution(word) {
    var answer = 0;
    const list = ["A","E","I","O","U"];
    // 위에 리스트를 재귀함수로 추적하면서 word와 같아지면 break거는식으로 해도될듯
    let results = "";

    const recursion = () => {
        if (results === word) return true;
        if (results.length === 5) return;
        
        for(let el of list) {
            results += el;
            answer ++;
            if (recursion()) return true;
            results = results.substring(0, results.length-1);
        }
    }
    
    recursion();
    
    return answer;
}