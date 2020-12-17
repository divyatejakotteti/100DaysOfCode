/**
Objective

In this challenge, we practice looping over the characters of string. Check out the attached tutorial for more details.

Task

Complete the vowelsAndConsonants function in the editor below. It has one parameter, a string,

, consisting of lowercase English alphabetic letters (i.e., a through z). The function must do the following:

    First, print each vowel in 

on a new line. The English vowels are a, e, i, o, and u, and each vowel must be printed in the same order as it appeared in
.
Second, print each consonant (i.e., non-vowel) in
on a new line in the same order as it appeared in

    .

Input Format

Locked stub code in the editor reads string

from stdin and passes it to the function.

Output Format

First, print each vowel in
on a new line (in the same order as they appeared in ). Second, print each consonant (i.e., non-vowel) in on a new line (in the same order as they appeared in

).

Sample Input 0

javascriptloops

Sample Output 0

a
a
i
o
o
j
v
s
c
r
p
t
l
p
s


**/
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
    const vowels = 'aeiou';
    var consonants = '';
    for (var i = 0; i < s.length; i++) {
        if (vowels.includes(s[i])) {
            console.log(s[i]);
    }
    else {
        consonants += s[i] + '\n';
    }
    }
    console.log(consonants.trim());

    }


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}