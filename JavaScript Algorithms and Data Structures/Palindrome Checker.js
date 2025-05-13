function palindrome(str) {
    str = str.replace(/[`~ !@#$%^&*()_|+\-=?;:'",.<>\{\}\[\]\\\/]/g, '').toLowerCase();
    
    for (let i = 0; i < str.length; i++) {
        if (myString[i] !== str[str.length - i - 1]) {
          return false;
        }
    }

    return true;
}

palindrome("racecar")