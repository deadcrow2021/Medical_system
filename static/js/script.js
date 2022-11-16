document.addEventListener("DOMContentLoaded", function() {
    var phones = document.querySelectorAll("input[type=tel]");
    
    let get_numbers_from_input = (input) => {
        return input.value.replace(/\D/g, "");
    }
    
    function correct_phone_number(event) {
        let input = event.target
        let number = get_numbers_from_input(input)
        
        let index = ["4","7","8","9"].indexOf(number[0]);
        let beautifulNumber = "";
        
        if (index > -1) {
            // Russian
            if (["4", "9"].indexOf(number[0]) > -1) number = "7" + number;
            beautifulNumber = (number[0] == "8") ? "8" : "+7";
            if (number.length > 1)
                beautifulNumber += " (" + number.substr(1, 3);
            if (number.length > 4)
                beautifulNumber += ") " + number.substr(4, 3);
            if (number.length > 7)
                beautifulNumber += "-" + number.substr(7, 2);
            if (number.length > 9)
                beautifulNumber += "-" + number.substr(9, 2);
        } else if (number.length > 0) {
            // Not Russian
            beautifulNumber = "+" + number.substr(0, 15);
        }
        
        input.value = beautifulNumber;
    }
    
    for (let phone of phones) {
        phone.addEventListener("input", correct_phone_number);
    }
    
    
    var date_inputs = document.querySelectorAll('input[type=date]');
    for (let inp of date_inputs) {
        // inp.style.width = '200px';
        inp.onfocus = (e) => {
            let i = inp;
            let date = i.defaultValue;
            // console.log(`focus ${date}`);
            i.type = 'date';
            i.defaultValue = date;
        };
        inp.onblur = (e) => {
            let i = inp;
            let date = i.defaultValue;// !== '' ? i.defaultValue : "дд.мм.гггг";
            // console.log(`blur ${date}`);
            i.type = 'text';
            i.placeholder = 'дд.мм.гггг';
            i.defaultValue = date;
        };
        inp.onfocus();
        inp.onblur();
    }
    
});

