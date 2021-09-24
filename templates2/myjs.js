function month_add_zero(month) {
    if (month < 10) {
        month1 = "0" + month.toString();
    }
    else {
        month1 = month.toString();
    }
    return month1;
}

function day_add_zero(day) {
    if (day < 10) {
        day1 = "0" + day.toString();
    }
    else {
        day1 = day.toString();
    }
    return day1;
}

function random_format(randomnum) {
    if (randomnum == 0) {
        randomnum1 = "0001";
    }
    else if (randomnum > 0 && randomnum <= 9) {
        randomnum1 = "000" + randomnum.toString();
    }
    else if (randomnum > 9 && randomnum <= 99) {
        randomnum1 = "00" + randomnum.toString();
    }
    else if (randomnum > 99 && randomnum <= 999) {
        randomnum1 = "0" + randomnum.toString();
    }
    return randomnum1;
}

function myCheck() {
    for (var i = 0; i < document.form1.elements.length - 1; i++) {
        if (document.form1.elements[i].value == "") {
            alert("cannot empty");
            document.form1.elements[i].focus();
            return false;
        }
    }
    return true;
}