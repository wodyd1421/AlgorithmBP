function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    const numer = numer1 * denom2 + numer2 * denom1;
    const denom = denom1 * denom2;
    const getGcd = (a, b) => (a % b == 0 ? b : getGcd(b, a % b));
    const gcd = getGcd(numer, denom);
    answer = [numer/gcd, denom/gcd];
    return answer;
}