document.addEventListener("DOMContentLoaded", function() {
    var phones = document.querySelectorAll("input[type=tel]");
    
    let get_numbers_from_input = (input) => {
        return input.value.replace(/\D/g, "");
    }
    
    function correct_phone_number(event) {
        let input = event.target
        let number = get_numbers_from_input(input)
        
        let index = ["7","8","9"].indexOf(number[0]);
        let beautifulNumber = "";
        
        console.log(`${number[0]}`);
        if (index > -1) {
            // Russian
            if (number[0] == "9") number = "7" + number;
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
});