// 문제 이름 : [3차] 파일명 정렬(카카오 2018 블라인드 공채 기출 - 레벨2)
// 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/17686

function solution(files) {
    var answer = [];
    // 포인트는 맨앞에 있는 문자열을 바탕으로 정렬 비교하고(1)
    // 만약 맨앞의 문자열의 우선순위가 같으면 바로 그 다음에 나오는 숫자를 바탕으로 정렬함
    // 맨앞의 문자열과 그 다음 나오는 숫자를 따로 파싱하는 작업이 필요함
    if (files.length === 1) return files;
    files.sort((x,y) => {
        var idx1 = undefined;
        var idx2 = undefined;
        var array1 = x.split('');
        var array2 = y.split('');
        array1.push('.');
        array2.push('.');
        
        for(let i=0;i<array1.length;i++) {
            if(!isNaN(parseInt(array1[i]))) {
                idx1 = i;
                break
            }
        }
        
        for(let i=0;i<array2.length;i++) {
            if(!isNaN(parseInt(array2[i]))) {
                idx2 = i;
                break
            }
        }
        
        var newArray1 = array1.slice(idx1);
        var newArray2 = array2.slice(idx2);
        
        if (x.substring(0,idx1).toLowerCase() > y.substring(0,idx2).toLowerCase()) return 1;
        else if (x.substring(0,idx1).toLowerCase() < y.substring(0,idx2).toLowerCase()) return -1;

        for(let i=0;i<newArray1.length;i++) {
            if(isNaN(parseInt(newArray1[i]))) {
                idx1 = i;
                break
            }
        }
        
        for(let i=0;i<newArray2.length;i++) {
            if(isNaN(parseInt(newArray2[i]))) {
                idx2 = i;
                break
            }
        }

        var num1 = parseInt(newArray1.slice(0, idx1).join(''));
        var num2 = parseInt(newArray2.slice(0, idx2).join(''));
        
        if (num1 >= num2) return 1;
        else if (num1 < num2) return -1;
        
    })
    
    answer = files;
    return answer;
}