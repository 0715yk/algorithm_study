// 재귀함수로 합병정렬 구현하기(JS)

const mergeSort = (l) => {
    if (l.length <= 1) return l;
    else {
        const mid = Math.floor(l.length / 2);
        const left = l.slice(0, mid);
        const right = l.slice(mid);
        const sortedLeft = mergeSort(left);
        const sortedRight = mergeSort(right);
        let result = []

        while (true) {
            if (sortedLeft[0] > sortedRight[0]) {
                result.push(sortedRight[0])
                sortedRight.shift()
            } else {
                result.push(sortedLeft[0])
                sortedLeft.shift()
            }

            if (sortedLeft.length === 0) {
                result = result.concat(sortedRight)
                break
            } else if (sortedRight.length === 0) {
                result = result.concat(sortedLeft)
                break
            }
        }
        return result;
    }
}

// 구현할 때 특이사항 
// 1) concat은 합친 배열을 리턴할뿐, 합쳐주지 않는다. 따라서 합친 것을 가져다 쓰려며 변수로 담아서 써야한다!
