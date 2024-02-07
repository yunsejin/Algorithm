const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input.push(line);
}).on('close', function () {
    const testCases = Number(input[0]);
    for (let i = 1; i <= testCases; i++) {
        const [H, W, N] = input[i].split(' ').map((el) => Number(el));
        let floor = N % H;
        let room = Math.ceil(N / H);
        if (floor === 0) floor = H;
        console.log(floor * 100 + room);
    }
    process.exit();
});
