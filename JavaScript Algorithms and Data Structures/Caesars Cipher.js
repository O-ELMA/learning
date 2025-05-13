function rot13(str) {
    let keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.split('');
    let values = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'.split('');
    let rot13 = {};

    keys.forEach((key, i) => rot13[key] = values[i])
    let replacer = function(match){
        return rot13[match];
    }

    return str.replace(/[A-Z]/g, replacer);
}

rot13("SERR PBQR PNZC")