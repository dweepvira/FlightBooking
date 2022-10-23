function subs(){
    document.getElementById("subscribed").innerHTML="Thank You For Subscribing !";
}


function EnableDisableTextBox(category) {
    var selectedValue = category.options[category.selectedIndex].value;
    var txtOther = document.getElementById("txtOther");
    txtOther.disabled = selectedValue == 6 ? false : true;
    if (!txtOther.disabled) {
        txtOther.focus();
    }
}