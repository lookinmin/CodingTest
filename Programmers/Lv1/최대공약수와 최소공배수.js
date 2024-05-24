function solution(n, m) {
    
    const gcd = (n, m) => {
        return n % m === 0 ? m : gcd(m, n % m);
    }
    
    const lcm = (n, m) => {
        let num = 1;
        while(1){
            if((num % n == 0) && (num % m == 0)){
                return num
            }
            num += 1;
        }
    }
    return [gcd(n,m), lcm(n, m)];
}