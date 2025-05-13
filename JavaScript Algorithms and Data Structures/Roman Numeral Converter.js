const arabicNums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
const romanNums = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];

function convertToRoman(num) {
    let output = '';

    arabicNums.forEach(function(arabicNum, i) {
        while (num >= arabicNum) {
            output += romanNums[i];
            num -= arabicNum;
        }
    });
    
    return output;
}

console.log(
    convertToRoman(36)
);