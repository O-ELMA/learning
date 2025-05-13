function checkCashRegister(price, cash, cid) {
    let change = [];
    let sep = [];
    let needed = cash - price;
    let converter = [0.01, 0.05, 0.1, 0.25, 1, 5, 10, 20, 100];

    cid.forEach(unit => sep.push(unit[1]));

    while (needed != 0){
        let closest = converter.reduce((b,a) => b - a < 0 && needed - a >= 0 ? a : b);
        let index = converter.indexOf(closest);

        if (needed > sep.slice(0, index + 1).reduce((a,b) => a + b)){
            return {
                status: "INSUFFICIENT_FUNDS",
                change: []
            };
        } else if (needed == sep.slice(0, index + 1).reduce((a,b) => a + b)){
            return {
                status: "CLOSED",
                change: cid
            };
        }

        while(sep[index] == 0){
            closest = converter[index - 1];
            index--
        }

        const covered = Math.min(
            Math.floor(needed / closest),
            Math.floor(sep[index] / closest)
        );

        change.push(
            [cid[index][0],
            converter[index] * covered]
        );

        needed -= converter[index] * covered;
        sep[index] -= converter[index] * covered;
        needed = Math.round(needed * 100) / 100
    }

    return {
        status: 'OPEN', 
        change: change
    };
}

checkCashRegister(
    19.5,
    20,
    [
        ["PENNY", 1.01],
        ["NICKEL", 2.05],
        ["DIME", 3.1],
        ["QUARTER", 4.25],
        ["ONE", 90],
        ["FIVE", 55],
        ["TEN", 20],
        ["TWENTY", 60],
        ["ONE HUNDRED", 100]
    ]
);