/**
 * count all letters in the string,
 * return result in such format:
 * {
 *  a: 3,
 *  b: 8,
 *  g: 10,
 *  ....,
 * }
 *
 * your solution should be case insensitive,
 * it means that letter "G" is the same as "g" and otherwise - "g" is the same as "G"
 */

//Importing the necessary modules 
const assert = require('assert');
const { isDeepStrictEqual } = require('util');

//We define the string to test and also the expected output for that string
const testString = 'Some string for TeSting purpose';

const expectedOutput = {
    s: 4,
    o: 3,
    m: 1,
    e: 3,
    ' ': 4,
    t: 3,
    r: 3,
    i: 2,
    n: 2,
    g: 2,
    f: 1,
    p: 2,
    u: 1
};

//We write our test
const testWordCounter = () => {
    assert(isDeepStrictEqual(wordCounter(testString), expectedOutput));
    console.log('Test have passed!');
};

//We finally define the word counter function
const wordCounter = (str) => {
    //Case insensitive!
    let finalStr = str.toLowerCase();

    let strArr = finalStr.split("");
    let letterCount = {}

    strArr.forEach( char => {
        letterCount[char] ??= 0
        letterCount[char] += 1 
    })

    return letterCount;
};

testWordCounter();