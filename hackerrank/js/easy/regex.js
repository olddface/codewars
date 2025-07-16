'use strict';
let s = "aasdea"
function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
     */
    if (s.length < 3 || /[A-Z]/.test(s)) {
        return false;
    }

    let startChar = /^[aiueo]/;
    let endChar = /[aiueo]$/;

    if (startChar.test(s) && endChar.test(s) && s[0] == s[s.length-1]){
        return true
    }
    else {
        return false
    }
    
    /*
     * Do not remove the return statement
     */
    return re;
}

console.log(regexVar());