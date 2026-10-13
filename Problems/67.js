var addBinary = function(a,b){

    let i = a.length - 1;
    let j = b.length - 1;

    let carry = 0;

    let res = "";

    while(i >= 0 || j >= 0 || carry){

        total = carry;

        if(a[i]){
            total += parseInt(a[i]);
            i--;
        }

        if(b[j]){
            total += parseInt(b[j]);
            j--;
        }

        res = String(total % 2) + res;

        carry = parseInt(total / 2);
    }

    return res;

}

console.log("Result:", addBinary("1", "111"))
