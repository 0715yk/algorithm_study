// 퀵정렬 구현하기 (JS)
const quick_sort = (l) => {
    if (l <= 1) return l;
    else {
        const pivot = l[0];
        const ltp = [];
        const gtp = [];
        for (let i = 1; i < l.length; i++) {
            if (l[i] > pivot) {
                gtp.push(l[i]);
            } else {
                ltp.push(l[i]);
            }
        }
        const sorted_ltp = quick_sort(ltp);
        const sorted_gtp = quick_sort(gtp);
        const results = sorted_ltp.concat([pivot]).concat(sorted_gtp);
        return results;
    }
}