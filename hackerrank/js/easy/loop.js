'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    const vowel = new Set(['a','i','u','e','o']);
    [...s].forEach( char => {
        if (vowel.has(char)){
            console.log(char)
        }
    });
    [...s].forEach( char => {
        if (!vowel.has(char)){
            console.log(char)
        }
    });
};
vowelsAndConsonants("zfdzdsZdsDaaa")

function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}